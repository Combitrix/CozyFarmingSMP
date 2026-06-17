/* Cozy Farming SMP — Quest Viewer frontend (vanilla JS, no build, file:// safe). */
(function () {
  "use strict";

  // ---------------------------------------------------------------------------
  // Constants
  // ---------------------------------------------------------------------------
  var GRID = 80; // px per quest-grid unit
  var SVG_NS = "http://www.w3.org/2000/svg";

  // Standard Minecraft colour palette (codes 0-9, a-f).
  var MC_COLORS = {
    "0": "#000000", "1": "#0000AA", "2": "#00AA00", "3": "#00AAAA",
    "4": "#AA0000", "5": "#AA00AA", "6": "#FFAA00", "7": "#AAAAAA",
    "8": "#555555", "9": "#5555FF", "a": "#55FF55", "b": "#55FFFF",
    "c": "#FF5555", "d": "#FF55FF", "e": "#FFFF55", "f": "#FFFFFF"
  };

  // Mod badge colours (fixed). Returns {bg, fg}.
  var MOD_COLORS = {
    minecraft:      { bg: "#7d7d7d", fg: "#ffffff" },
    create:         { bg: "#b5651d", fg: "#ffffff" },
    minecolonies:   { bg: "#2b5fb0", fg: "#ffffff" },
    aeronautics:    { bg: "#6fc3ff", fg: "#0a2030" },
    farmersdelight: { bg: "#3f9b46", fg: "#ffffff" },
    magic_coins:    { bg: "#d4af37", fg: "#2b2200" },
    numismatics:    { bg: "#d4af37", fg: "#2b2200" },
    supplementaries:{ bg: "#7a5230", fg: "#ffffff" },
    ftbchunks:      { bg: "#4a7a4a", fg: "#ffffff" }
  };
  function modColor(mod) {
    if (mod && MOD_COLORS.hasOwnProperty(mod)) return MOD_COLORS[mod];
    return { bg: "#555a66", fg: "#e8e8e8" }; // neutral fallback
  }

  // ---------------------------------------------------------------------------
  // HTML escaping
  // ---------------------------------------------------------------------------
  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  // ---------------------------------------------------------------------------
  // Minecraft formatcode renderer. Handles & and §.
  // Always HTML-escapes text before wrapping in spans.
  // Returns an HTML string.
  // ---------------------------------------------------------------------------
  function renderFormat(raw) {
    if (raw === null || raw === undefined) return "";
    var text = String(raw);
    var out = "";
    // current style state
    var state = { color: null, bold: false, italic: false, underline: false, strike: false };
    var open = false; // whether a span is currently open

    function styleString() {
      var parts = [];
      if (state.color) parts.push("color:" + state.color);
      if (state.bold) parts.push("font-weight:bold");
      if (state.italic) parts.push("font-style:italic");
      var deco = [];
      if (state.underline) deco.push("underline");
      if (state.strike) deco.push("line-through");
      if (deco.length) parts.push("text-decoration:" + deco.join(" "));
      return parts.join(";");
    }
    function closeSpan() {
      if (open) { out += "</span>"; open = false; }
    }
    function openSpan() {
      closeSpan();
      var s = styleString();
      if (s) { out += '<span style="' + s + '">'; open = true; }
    }
    function reset() {
      state = { color: null, bold: false, italic: false, underline: false, strike: false };
    }

    var i = 0;
    var pendingText = "";
    function flushText() {
      if (pendingText.length) {
        out += escapeHtml(pendingText);
        pendingText = "";
      }
    }

    while (i < text.length) {
      var ch = text.charAt(i);
      if ((ch === "&" || ch === "§") && i + 1 < text.length) {
        var code = text.charAt(i + 1).toLowerCase();
        var isControl = MC_COLORS.hasOwnProperty(code) ||
          code === "l" || code === "o" || code === "n" ||
          code === "m" || code === "r" || code === "k";
        if (isControl) {
          flushText();
          if (MC_COLORS.hasOwnProperty(code)) {
            // colour resets formatting in MC, then sets colour
            reset();
            state.color = MC_COLORS[code];
          } else if (code === "l") { state.bold = true; }
          else if (code === "o") { state.italic = true; }
          else if (code === "n") { state.underline = true; }
          else if (code === "m") { state.strike = true; }
          else if (code === "r") { reset(); }
          else if (code === "k") { /* obfuscated -> render as normal, no change */ }
          openSpan();
          i += 2;
          continue;
        }
      }
      pendingText += ch;
      i += 1;
    }
    flushText();
    closeSpan();
    return out;
  }

  // Plain-text version (strip formatcodes) for search / tooltips / node labels.
  function stripFormat(raw) {
    if (raw === null || raw === undefined) return "";
    return String(raw).replace(/[&§][0-9a-fk-orK-OR]/g, "");
  }

  // ---------------------------------------------------------------------------
  // Geometry: compute node positions and dependency lines from a chapter.
  // Exported for node tests.
  // ---------------------------------------------------------------------------
  function computeNodes(chapter) {
    var quests = (chapter && chapter.quests) || [];
    return quests.map(function (q) {
      var size = (typeof q.size === "number" && q.size > 0) ? q.size : 1.0;
      return {
        id: q.id,
        cx: (q.x || 0) * GRID,
        cy: (q.y || 0) * GRID, // y positive downwards (FTB convention)
        r: 18 * size,
        shape: q.shape || "circle",
        quest: q
      };
    });
  }

  function computeLines(chapter) {
    var nodes = computeNodes(chapter);
    var byId = {};
    nodes.forEach(function (n) { byId[n.id] = n; });
    var lines = [];
    nodes.forEach(function (n) {
      var deps = n.quest.dependencies || [];
      // hide_dependent_lines on the dependency quest hides lines drawn to it.
      deps.forEach(function (depId) {
        var dep = byId[depId];
        if (!dep) return;
        if (dep.quest && dep.quest.hide_dependent_lines) return;
        lines.push({ from: depId, to: n.id, x1: dep.cx, y1: dep.cy, x2: n.cx, y2: n.cy });
      });
    });
    return lines;
  }

  // SVG polygon points for a given shape, centred at (cx, cy) with radius r.
  function shapePoints(shape, cx, cy, r) {
    function poly(n, rot) {
      var pts = [];
      for (var k = 0; k < n; k++) {
        var a = rot + (k * 2 * Math.PI / n);
        pts.push((cx + r * Math.cos(a)).toFixed(2) + "," + (cy + r * Math.sin(a)).toFixed(2));
      }
      return pts.join(" ");
    }
    switch (shape) {
      case "square":
      case "rsquare":
        return poly(4, Math.PI / 4);
      case "diamond":
        return poly(4, -Math.PI / 2);
      case "pentagon":
        return poly(5, -Math.PI / 2);
      case "hexagon":
        return poly(6, 0);
      case "gear":
        return poly(8, 0); // octagon approximation for gear
      default:
        return null; // circle handled separately
    }
  }

  // ---------------------------------------------------------------------------
  // Browser-only rendering. Guarded so node tests can require this file.
  // ---------------------------------------------------------------------------
  function initBrowser() {
    var DATA = window.QUEST_DATA;
    if (!DATA || !DATA.chapters || !DATA.chapters.length) {
      document.getElementById("graph-wrap").innerHTML =
        '<p style="padding:20px;color:#c66">Keine Quest-Daten gefunden (window.QUEST_DATA).</p>';
      return;
    }

    // Header / meta
    var meta = DATA.meta || {};
    document.getElementById("pack-title").textContent = meta.title || "Quest Viewer";
    document.getElementById("pack-version").textContent =
      (meta.version !== undefined && meta.version !== null) ? ("v" + meta.version) : "";

    var svg = document.getElementById("graph");
    var gRoot = document.getElementById("graph-root");
    var tabsEl = document.getElementById("chapter-tabs");
    var searchEl = document.getElementById("search");
    var panelEl = document.getElementById("detail-panel");

    var view = { x: 0, y: 0, scale: 1 };
    var activeChapterIndex = 0;
    var nodeEls = {}; // id -> { group, quest }

    // ---- Chapter tabs ----
    DATA.chapters.forEach(function (ch, idx) {
      var btn = document.createElement("button");
      btn.className = "chapter-tab" + (idx === 0 ? " active" : "");
      btn.innerHTML = renderFormat(ch.title || ("Kapitel " + (idx + 1)));
      btn.addEventListener("click", function () {
        activeChapterIndex = idx;
        Array.prototype.forEach.call(tabsEl.children, function (c, ci) {
          c.classList.toggle("active", ci === idx);
        });
        searchEl.value = "";
        renderChapter();
        resetView();
      });
      tabsEl.appendChild(btn);
    });

    // ---- Render a chapter into the SVG ----
    function renderChapter() {
      while (gRoot.firstChild) gRoot.removeChild(gRoot.firstChild);
      nodeEls = {};
      var chapter = DATA.chapters[activeChapterIndex];
      var lines = computeLines(chapter);
      var nodes = computeNodes(chapter);

      // Lines layer first (under nodes)
      var linesLayer = document.createElementNS(SVG_NS, "g");
      linesLayer.setAttribute("class", "lines-layer");
      lines.forEach(function (ln) {
        var l = document.createElementNS(SVG_NS, "line");
        l.setAttribute("x1", ln.x1); l.setAttribute("y1", ln.y1);
        l.setAttribute("x2", ln.x2); l.setAttribute("y2", ln.y2);
        l.setAttribute("class", "dep-line");
        linesLayer.appendChild(l);
      });
      gRoot.appendChild(linesLayer);

      // Nodes layer
      nodes.forEach(function (n) {
        var q = n.quest;
        var g = document.createElementNS(SVG_NS, "g");
        g.setAttribute("class", "quest-node" + (q.optional ? " optional" : ""));
        g.setAttribute("transform", "translate(0,0)");
        g.style.cursor = "pointer";

        var mc = modColor(q.icon && q.icon.mod);
        var pts = shapePoints(n.shape, n.cx, n.cy, n.r);
        var shapeEl;
        if (pts) {
          shapeEl = document.createElementNS(SVG_NS, "polygon");
          shapeEl.setAttribute("points", pts);
        } else {
          shapeEl = document.createElementNS(SVG_NS, "circle");
          shapeEl.setAttribute("cx", n.cx);
          shapeEl.setAttribute("cy", n.cy);
          shapeEl.setAttribute("r", n.r);
        }
        shapeEl.setAttribute("class", "node-shape");
        shapeEl.setAttribute("fill", mc.bg);
        g.appendChild(shapeEl);

        // Icon placeholder: first letter of displayName, mod-coloured text.
        var label = document.createElementNS(SVG_NS, "text");
        label.setAttribute("x", n.cx);
        label.setAttribute("y", n.cy);
        label.setAttribute("class", "node-glyph");
        label.setAttribute("fill", mc.fg);
        label.setAttribute("text-anchor", "middle");
        label.setAttribute("dominant-baseline", "central");
        label.style.fontSize = Math.max(10, n.r * 0.8) + "px";
        var glyph = q.icon && q.icon.displayName ? q.icon.displayName.charAt(0).toUpperCase()
          : stripFormat(q.title).charAt(0).toUpperCase() || "?";
        label.textContent = glyph;
        g.appendChild(label);

        // Tooltip via <title>
        var titleEl = document.createElementNS(SVG_NS, "title");
        titleEl.textContent = stripFormat(q.title);
        g.appendChild(titleEl);

        g.addEventListener("click", function (e) {
          e.stopPropagation();
          selectQuest(q.id);
        });

        gRoot.appendChild(g);
        nodeEls[q.id] = { group: g, node: n, quest: q };
      });

      applyTransform();
    }

    // ---- Detail panel ----
    function selectQuest(id) {
      var entry = nodeEls[id];
      if (!entry) return;
      var q = entry.quest;

      // highlight selected node
      Object.keys(nodeEls).forEach(function (k) {
        nodeEls[k].group.classList.toggle("selected", k === id);
      });

      var html = "";
      html += '<h2 class="quest-title">' + renderFormat(q.title) + "</h2>";
      if (q.optional) html += '<div class="optional-badge">optional</div>';

      // Description
      var desc = q.description || [];
      if (desc.length) {
        html += '<div class="quest-desc">';
        desc.forEach(function (line) {
          html += '<p class="desc-line">' + (line === "" ? "&nbsp;" : renderFormat(line)) + "</p>";
        });
        html += "</div>";
      }

      // Tasks
      html += '<h3 class="section-head">Aufgaben</h3>';
      html += renderEntryList(q.tasks || [], "Keine Aufgaben.");

      // Rewards
      html += '<h3 class="section-head">Belohnungen</h3>';
      html += renderEntryList(q.rewards || [], "Keine Belohnungen.");

      // Dependencies
      var deps = q.dependencies || [];
      if (deps.length) {
        html += '<h3 class="section-head">Voraussetzungen</h3>';
        html += '<ul class="dep-list">';
        deps.forEach(function (depId) {
          var depEntry = nodeEls[depId];
          var depTitle = depEntry ? stripFormat(depEntry.quest.title) : ("Quest " + depId);
          html += '<li><a href="#" class="dep-link" data-dep="' + escapeHtml(depId) + '">' +
            (depEntry ? renderFormat(depEntry.quest.title) : escapeHtml(depTitle)) + "</a></li>";
        });
        html += "</ul>";
      }

      panelEl.innerHTML = html;
      panelEl.classList.add("active");

      // wire dependency links
      Array.prototype.forEach.call(panelEl.querySelectorAll(".dep-link"), function (a) {
        a.addEventListener("click", function (e) {
          e.preventDefault();
          var dep = a.getAttribute("data-dep");
          if (nodeEls[dep]) { centerOnQuest(dep); selectQuest(dep); }
        });
      });
    }

    function renderEntryList(entries, emptyMsg) {
      if (!entries.length) return '<p class="empty">' + escapeHtml(emptyMsg) + "</p>";
      var html = '<ul class="entry-list">';
      entries.forEach(function (e) {
        html += "<li>" + renderEntry(e) + "</li>";
      });
      html += "</ul>";
      return html;
    }

    function renderEntry(e) {
      var type = e.type || "unknown";
      if (type === "item") {
        var mc = modColor(e.mod);
        var name = e.displayName || e.item || "Item";
        var badge = '<span class="mod-badge" style="background:' + mc.bg + ";color:" + mc.fg +
          '">' + escapeHtml(e.mod || "?") + "</span>";
        var count = (e.count && e.count > 1) ? ' <span class="count">×' + escapeHtml(e.count) + "</span>" : "";
        return badge + " " + escapeHtml(name) + count;
      }
      if (type === "xp") {
        return '<span class="xp-tag">' + escapeHtml(e.xp != null ? e.xp : 0) + " XP</span>";
      }
      if (type === "dimension") {
        return '<span class="dim-tag">Dimension: ' + escapeHtml(prettyDimension(e.dimension)) + "</span>";
      }
      if (type === "checkmark") {
        return '<span class="check-tag">✓ Manuell bestätigen</span>';
      }
      // unknown type — show generically
      return '<span class="unknown-tag">' + escapeHtml(type) + "</span>";
    }

    function prettyDimension(dim) {
      if (!dim) return "?";
      var name = String(dim).split(":").pop().replace(/_/g, " ");
      return name.replace(/\b\w/g, function (c) { return c.toUpperCase(); });
    }

    // ---- Pan / Zoom ----
    function applyTransform() {
      gRoot.setAttribute("transform",
        "translate(" + view.x + "," + view.y + ") scale(" + view.scale + ")");
    }

    function centerOnQuest(id) {
      var entry = nodeEls[id];
      if (!entry) return;
      var rect = svg.getBoundingClientRect();
      view.x = rect.width / 2 - entry.node.cx * view.scale;
      view.y = rect.height / 2 - entry.node.cy * view.scale;
      applyTransform();
    }

    function resetView() {
      // Fit content: compute bounds of nodes.
      var chapter = DATA.chapters[activeChapterIndex];
      var nodes = computeNodes(chapter);
      var rect = svg.getBoundingClientRect();
      if (!nodes.length) { view = { x: rect.width / 2, y: rect.height / 2, scale: 1 }; applyTransform(); return; }
      var minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
      nodes.forEach(function (n) {
        minX = Math.min(minX, n.cx - n.r); maxX = Math.max(maxX, n.cx + n.r);
        minY = Math.min(minY, n.cy - n.r); maxY = Math.max(maxY, n.cy + n.r);
      });
      var w = maxX - minX || 1, h = maxY - minY || 1;
      var pad = 60;
      var scale = Math.min((rect.width - pad) / w, (rect.height - pad) / h, 1.5);
      if (!isFinite(scale) || scale <= 0) scale = 1;
      view.scale = scale;
      view.x = rect.width / 2 - (minX + w / 2) * scale;
      view.y = rect.height / 2 - (minY + h / 2) * scale;
      applyTransform();
    }

    // Drag to pan
    var dragging = false, dragStart = null;
    svg.addEventListener("mousedown", function (e) {
      dragging = true;
      dragStart = { x: e.clientX, y: e.clientY, vx: view.x, vy: view.y };
      svg.classList.add("dragging");
    });
    window.addEventListener("mousemove", function (e) {
      if (!dragging) return;
      view.x = dragStart.vx + (e.clientX - dragStart.x);
      view.y = dragStart.vy + (e.clientY - dragStart.y);
      applyTransform();
    });
    window.addEventListener("mouseup", function () {
      dragging = false;
      svg.classList.remove("dragging");
    });

    // Wheel to zoom (centred on cursor)
    svg.addEventListener("wheel", function (e) {
      e.preventDefault();
      var rect = svg.getBoundingClientRect();
      var mx = e.clientX - rect.left, my = e.clientY - rect.top;
      var factor = e.deltaY < 0 ? 1.1 : 1 / 1.1;
      var newScale = Math.max(0.15, Math.min(4, view.scale * factor));
      // keep point under cursor stable
      var wx = (mx - view.x) / view.scale;
      var wy = (my - view.y) / view.scale;
      view.scale = newScale;
      view.x = mx - wx * view.scale;
      view.y = my - wy * view.scale;
      applyTransform();
    }, { passive: false });

    // Click empty area deselects
    svg.addEventListener("click", function () {
      Object.keys(nodeEls).forEach(function (k) {
        nodeEls[k].group.classList.remove("selected");
      });
    });

    document.getElementById("reset-btn").addEventListener("click", resetView);

    // ---- Search ----
    searchEl.addEventListener("input", function () {
      var q = stripFormat(searchEl.value).trim().toLowerCase();
      var any = q.length > 0;
      Object.keys(nodeEls).forEach(function (k) {
        var entry = nodeEls[k];
        var title = stripFormat(entry.quest.title).toLowerCase();
        var match = !any || title.indexOf(q) !== -1;
        entry.group.classList.toggle("dimmed", any && !match);
        entry.group.classList.toggle("hit", any && match);
      });
    });

    // initial render
    renderChapter();
    resetView();
  }

  // ---------------------------------------------------------------------------
  // Exports for node-based unit tests; init in browser.
  // ---------------------------------------------------------------------------
  var api = {
    renderFormat: renderFormat,
    stripFormat: stripFormat,
    escapeHtml: escapeHtml,
    computeNodes: computeNodes,
    computeLines: computeLines,
    shapePoints: shapePoints,
    modColor: modColor,
    GRID: GRID
  };

  if (typeof module !== "undefined" && module.exports) {
    module.exports = api;
  }
  if (typeof document !== "undefined") {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", initBrowser);
    } else {
      initBrowser();
    }
  }
})();
