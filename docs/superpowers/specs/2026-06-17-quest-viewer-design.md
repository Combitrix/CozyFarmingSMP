# Questline Web-Viewer — Design / Spec

**Datum:** 2026-06-17
**Projekt:** Cozy Farming SMP (MC 1.21.1 / NeoForge, FTB Quests)

## Ziel

Ein statischer Web-Viewer für die FTB-Questlines des Modpacks, damit Quests
gelesen/geprüft werden können, ohne ins Spiel zu wechseln. Bildet den In-Game-
Quest-Baum nach (Knoten an x/y-Positionen + Abhängigkeitslinien).

## Quelldaten

- Pfad: `pack/config/ftbquests/quests/`
  - `data.snbt` — globale Meta (`title`, `version`, …)
  - `chapter_groups.snbt` — Gruppen (`id`, `title`)
  - `chapters/*.snbt` — je Kapitel eine Datei (aktuell nur `questline.snbt`, 153 Quests)
- Format: **SNBT** (NBT-Textform). Keine Mod-JARs vorhanden → keine echten Texturen.

### SNBT-Felder (relevant)

Kapitel-Datei (root): `filename`, `group`, `icon`, `id`, `order_index`, `title`, `quests:[…]`

Quest-Objekt:
- `id` (16-Hex String)
- `x`, `y` (Double, Baum-Position)
- `title` (String, kann Formatcodes + Emoji enthalten)
- `icon` (optional): `{ id: "namespace:item", count }`
- `shape` (optional String: `gear|circle|square|diamond|hexagon|pentagon|rsquare`; Default `circle`)
- `size` (optional Double, Default 1.0)
- `description` (optional String-Array, je Zeile; Formatcodes `&`/`§`)
- `dependencies` (optional String-Array von Quest-IDs)
- `optional` (optional Boolean)
- `hide_dependent_lines` (optional Boolean)
- `tasks:[…]`, `rewards:[…]`

Task-Typen (vorkommend): `item` (`item:{id,count}`, `count`), `checkmark`, `dimension` (`dimension`), `xp`.
Reward-Typen: `item` (`item:{id,count}`, `count`), `xp` (`xp`).
Parser muss **unbekannte Typen tolerieren** (Felder generisch durchreichen).

### SNBT-Parsing-Hinweise

- Werte-Suffixe: `d` (Double), `f` (Float), `L`/`b`/`s` (Long/Byte/Short) → numerisch parsen, Suffix entfernen.
- Strings in `"…"`, mit `\"` und `\\` Escapes.
- Verschachtelte `{…}` Objekte und `[…]` Arrays, tab-eingerückt.
- Keys sind unquoted. Booleans `true/false`.
- Robust gegen leere Arrays `[ ]` und fehlende optionale Felder.

## Architektur — statischer 2-stufiger Build

### Stufe 1: `build-viewer.py` (Python, stdlib only)
1. SNBT-Parser (eigenständig, keine Fremdlib).
2. Liest data/chapter_groups/chapters → baut Datenmodell (Schema unten).
3. **Item-Humanizer:** `namespace:item_name` → `{displayName, mod}`.
   - displayName: item-Teil, `_`→Space, Title-Case (z.B. `create:cogwheel`→`Cogwheel`,
     `minecraft:oak_log`→`Oak Log`).
   - mod: Namespace (`minecraft`,`create`,`minecolonies`,`aeronautics`,`farmersdelight`,
     `magic_coins`,`numismatics`,`supplementaries`,`ftbchunks`).
4. Schreibt `quest-viewer/data.js` mit `window.QUEST_DATA = { … };` (kein Server/CORS nötig).
5. CLI: `python build-viewer.py` (Pfade relativ zum Repo-Root).

### Stufe 2: Frontend `quest-viewer/` (HTML/CSS/JS, kein Framework)
- `index.html` lädt `style.css`, `data.js`, `app.js` (in dieser Reihenfolge).
- Öffnet per `file://` per Doppelklick.

## Datenschema (Vertrag Parser ↔ Frontend)

```js
window.QUEST_DATA = {
  meta:    { title: "Cozy Farming SMP", version: 13 },
  chapters: [
    {
      id: "4C0F000000000002",
      title: "🌾 Cozy Farming SMP",
      icon: { item:"minecraft:cake", displayName:"Cake", mod:"minecraft" } | null,
      quests: [
        {
          id: "4C0F00000000000A",
          x: 0.0, y: 0.0,
          shape: "gear",          // immer gesetzt (Default "circle")
          size: 3.0,              // immer gesetzt (Default 1.0)
          title: "Willkommen…",   // roh, inkl. Formatcodes
          optional: false,
          icon: { item, displayName, mod } | null,
          description: ["…","…"], // roh, Formatcodes erhalten
          dependencies: ["<questId>", …],
          tasks:   [ { type, item?, displayName?, mod?, count?, dimension?, raw? }, … ],
          rewards: [ { type, item?, displayName?, mod?, count?, xp?, raw? }, … ]
        }
      ]
    }
  ]
};
```

Regeln:
- Fehlende optionale Felder werden mit Defaults gefüllt (`shape`,`size`) oder als `null`/`[]`.
- `item`-Tasks/Rewards: `item`= "ns:id", plus `displayName`,`mod`,`count`.
- `xp`: `{type:"xp", xp:N}`. `dimension`: `{type:"dimension", dimension:"minecraft:overworld"}`.
- `checkmark`: `{type:"checkmark"}`.
- Unbekannte Felder eines Tasks/Rewards landen in `raw` (Objekt), damit nichts verloren geht.

## Frontend-Verhalten

**Graph-Ansicht (primär):**
- SVG. Knoten an `(x,y)` skaliert (z.B. *80px). y nach unten positiv (wie FTB).
- Abhängigkeitslinien: Linie von jeder Dependency-Quest zu ihren abhängigen Quests
  (sofern nicht `hide_dependent_lines`). Dezent grau.
- Knoten: Form je `shape` (gear/circle/square/diamond/hexagon → via CSS/SVG-Polygon,
  Fallback Kreis), Größe je `size`. Im Knoten ein Icon-Platzhalter (Mod-Farbe) + abgekürzter Titel als Tooltip.
- **Pan** (Drag auf leerem Bereich) + **Zoom** (Mausrad), Reset-Button.

**Detail-Panel (rechts, bei Klick auf Knoten):**
- Titel (Formatcodes gerendert).
- Beschreibung: jede Zeile mit gerenderten Formatcodes.
- Tasks-Liste + Rewards-Liste: Item-Name + Mod-Badge + Count; xp als „N XP"; dimension/checkmark lesbar.
- Dependencies: anklickbare Quest-Titel (springt zum Knoten).

**Minecraft-Formatcode-Renderer (`&`/`§`):**
- Farben `0-9 a-f` → feste Hex-Paletten (Standard-MC-Farben).
- `l`=bold, `o`=italic, `n`=underline, `m`=strikethrough, `r`=reset, `k`=obfuscated (als normal rendern).
- Codes in HTML-`<span>` mit Styles umsetzen; Text HTML-escapen.

**Mod-Badges (feste Farben):**
- minecraft=grau, create=bronze/orange, minecolonies=blau, aeronautics=hellblau,
  farmersdelight=grün, magic_coins/numismatics=gold, supplementaries=braun, sonst neutral.

**Suche:** Textfeld filtert Knoten nach Titel (matchende hervorheben/andere dimmen).

## Bau mit Agenten (parallel)

- **Agent 1 — Parser/Exporter:** `build-viewer.py` (SNBT-Parser + Humanizer + `data.js`-Writer).
  Liefert echtes `quest-viewer/data.js` aus den 153 Quests. Selbsttest: data.js valide, alle Quests enthalten.
- **Agent 2 — Frontend:** `index.html`,`app.js`,`style.css` gegen ein **Fixture** (kleines
  `window.QUEST_DATA` nach obigem Schema mit ~4 Quests, alle Task/Reward-Typen, Formatcodes).
  Muss mit echtem data.js ohne Änderung funktionieren.

**Integration (Hauptagent):** echten Build laufen lassen, Frontend mit echten Daten im Browser/Headless prüfen (Knotenzahl=153, keine JS-Fehler, Panel funktioniert).

## Nicht-Ziele (YAGNI)

- Keine echten Item-Texturen, kein Wiki/CDN-Fetch.
- Kein Editieren von Quests (read-only Viewer).
- Kein Live-Server (kommt evtl. später; Schema bleibt wiederverwendbar).
