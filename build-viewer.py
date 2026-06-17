#!/usr/bin/env python3
"""Daten-Export fuer den FTB-Quests Web-Viewer.

Liest die FTB-Quests-SNBT-Dateien (data.snbt, chapter_groups.snbt, chapters/*.snbt),
parst sie mit einem eigenstaendigen SNBT-Parser (nur stdlib) und schreibt das im
Spec-Vertrag definierte Datenmodell nach quest-viewer/data.js als
`window.QUEST_DATA = {...};`.

Aufruf: python build-viewer.py  (Pfade relativ zum Skript-Verzeichnis = Repo-Root)
"""
import os
import json

ROOT = os.path.dirname(os.path.abspath(__file__))
QUESTS_DIR = os.path.join(ROOT, "pack", "config", "ftbquests", "quests")
OUT_DIR = os.path.join(ROOT, "quest-viewer")
OUT_FILE = os.path.join(OUT_DIR, "data.js")


# ===========================================================================
# SNBT-Parser (eigenstaendig, keine Fremdlibrary)
# ===========================================================================
# Unterstuetzt: verschachtelte {}/[]-Strukturen, quoted Strings mit \" und \\
# Escapes, unquoted Keys, Booleans, Zahlen mit Suffix d/f/L/b/s (Suffix wird
# entfernt und numerisch geparst), leere Arrays "[ ]" und fehlende optionale
# Felder. Tabs/Whitespace/Zeilenumbrueche sind Trenner.

class _SnbtParser:
    def __init__(self, text):
        self.s = text
        self.i = 0
        self.n = len(text)

    def parse(self):
        """Parst genau einen Top-Level-Wert (i.d.R. ein {}-Objekt)."""
        self._skip_ws()
        val = self._value()
        self._skip_ws()
        return val

    # -- Whitespace/Trenner ueberspringen ----------------------------------
    def _skip_ws(self):
        while self.i < self.n and self.s[self.i] in " \t\r\n":
            self.i += 1

    def _peek(self):
        return self.s[self.i] if self.i < self.n else ""

    # -- Dispatch nach erstem Zeichen --------------------------------------
    def _value(self):
        c = self._peek()
        if c == "{":
            return self._object()
        if c == "[":
            return self._array()
        if c == '"' or c == "'":
            return self._quoted_string(c)
        # Bareword: Zahl, Boolean oder unquoted String
        return self._bareword()

    # -- Objekt {key: value, ...} ------------------------------------------
    def _object(self):
        obj = {}
        self.i += 1  # '{'
        self._skip_ws()
        while self._peek() != "}" and self.i < self.n:
            key = self._key()
            self._skip_ws()
            if self._peek() == ":":
                self.i += 1
            self._skip_ws()
            obj[key] = self._value()
            self._skip_ws()
            # Optionales Komma als Trenner; FTB nutzt meist Zeilenumbrueche.
            if self._peek() == ",":
                self.i += 1
                self._skip_ws()
        if self._peek() == "}":
            self.i += 1
        return obj

    # -- Array [v, v, ...] (auch leer "[ ]") -------------------------------
    def _array(self):
        arr = []
        self.i += 1  # '['
        self._skip_ws()
        while self._peek() != "]" and self.i < self.n:
            arr.append(self._value())
            self._skip_ws()
            if self._peek() == ",":
                self.i += 1
                self._skip_ws()
        if self._peek() == "]":
            self.i += 1
        return arr

    # -- Key: quoted oder unquoted -----------------------------------------
    def _key(self):
        c = self._peek()
        if c == '"' or c == "'":
            return self._quoted_string(c)
        start = self.i
        while self.i < self.n and self.s[self.i] not in ":{}[], \t\r\n":
            self.i += 1
        return self.s[start:self.i]

    # -- Quoted String mit \" und \\ Escapes -------------------------------
    def _quoted_string(self, quote):
        self.i += 1  # oeffnendes Quote
        out = []
        while self.i < self.n:
            ch = self.s[self.i]
            if ch == "\\":
                # Escape-Sequenz: naechstes Zeichen woertlich uebernehmen.
                nxt = self.s[self.i + 1] if self.i + 1 < self.n else ""
                out.append(nxt)
                self.i += 2
                continue
            if ch == quote:
                self.i += 1  # schliessendes Quote
                break
            out.append(ch)
            self.i += 1
        return "".join(out)

    # -- Bareword: Zahl/Boolean/unquoted String ----------------------------
    def _bareword(self):
        start = self.i
        while self.i < self.n and self.s[self.i] not in ":{}[], \t\r\n":
            self.i += 1
        token = self.s[start:self.i]
        return _coerce_scalar(token)


def _coerce_scalar(token):
    """Wandelt ein Bareword in Bool/Zahl/String um.

    Zahlen-Suffixe d/f/L/b/s werden entfernt und numerisch geparst.
    """
    if token == "true":
        return True
    if token == "false":
        return False

    # Zahl mit optionalem Typ-Suffix (d/f/L/b/s, gross/klein).
    body = token
    suffix = ""
    if body and body[-1] in "dDfFlLbBsS":
        suffix = body[-1]
        body = body[:-1]

    num = _try_number(body)
    if num is not None:
        # f/d -> float, sonst je nach Inhalt int/float.
        if suffix in ("f", "F", "d", "D"):
            return float(num)
        return num

    # Kein Suffix angenommen: ganzen Token nochmal als Zahl versuchen.
    num = _try_number(token)
    if num is not None:
        return num

    # Fallback: unquoted String.
    return token


def _try_number(text):
    """Versucht int dann float; gibt None bei Misserfolg."""
    if text == "" or text == "-" or text == "+":
        return None
    try:
        return int(text)
    except ValueError:
        pass
    try:
        return float(text)
    except ValueError:
        return None


def parse_snbt(text):
    return _SnbtParser(text).parse()


def read_snbt(path):
    with open(path, "r", encoding="utf-8") as f:
        return parse_snbt(f.read())


# ===========================================================================
# Item-Humanizer
# ===========================================================================
# "namespace:item_name" -> {item, displayName, mod}
# displayName = item-Teil, "_" -> Leerzeichen, Title-Case.
# mod = namespace.

def humanize_item(item_id):
    if not item_id or not isinstance(item_id, str):
        return None
    if ":" in item_id:
        mod, name = item_id.split(":", 1)
    else:
        mod, name = "minecraft", item_id
    display = name.replace("_", " ").strip()
    # Title-Case je Wort (z.B. "oak log" -> "Oak Log").
    display = " ".join(w[:1].upper() + w[1:] for w in display.split(" ") if w != "") or name
    return {"item": item_id, "displayName": display, "mod": mod}


def humanize_icon(icon):
    """Kapitel-/Quest-Icon: nimmt {id, count} oder reinen String und humanisiert.

    Gibt {item, displayName, mod} oder None zurueck.
    """
    if icon is None:
        return None
    item_id = None
    if isinstance(icon, dict):
        item_id = icon.get("id")
    elif isinstance(icon, str):
        item_id = icon
    if not item_id:
        return None
    return humanize_item(item_id)


# ===========================================================================
# Task-/Reward-Mapping
# ===========================================================================
# Bekannte Felder werden auf das Schema gemappt; alle uebrigen Felder landen
# in `raw`, damit nichts verloren geht (auch bei unbekannten Typen).

# Felder, die wir bereits explizit auf das Schema mappen und daher NICHT
# zusaetzlich in `raw` doppeln muessen.
_KNOWN_ENTRY_FIELDS = {"type", "item", "count", "xp", "dimension"}


def _item_id_of(entry):
    """Holt die Item-ID aus einem item-Feld (Objekt {id,count} oder String)."""
    item = entry.get("item")
    if isinstance(item, dict):
        return item.get("id")
    if isinstance(item, str):
        return item
    return None


def map_entry(entry):
    """Mappt einen Task oder Reward auf das Spec-Schema."""
    if not isinstance(entry, dict):
        return {"type": "unknown", "raw": {"value": entry}}

    etype = entry.get("type", "unknown")
    out = {"type": etype}

    if etype == "item":
        item_id = _item_id_of(entry)
        hum = humanize_item(item_id)
        if hum:
            out["item"] = hum["item"]
            out["displayName"] = hum["displayName"]
            out["mod"] = hum["mod"]
        # count: explizites count-Feld (FTB) hat Vorrang, sonst aus item-Objekt.
        if "count" in entry:
            out["count"] = entry["count"]
        elif isinstance(entry.get("item"), dict) and "count" in entry["item"]:
            out["count"] = entry["item"]["count"]
        else:
            out["count"] = 1
    elif etype == "xp":
        out["xp"] = entry.get("xp")
    elif etype == "dimension":
        out["dimension"] = entry.get("dimension")
    elif etype == "checkmark":
        pass  # nur der Typ ist relevant
    # andere/unbekannte Typen: nur Typ + raw (siehe unten)

    # Unbekannte/zusaetzliche Felder durchreichen (ohne id; id ist intern).
    raw = {}
    for k, v in entry.items():
        if k in _KNOWN_ENTRY_FIELDS or k == "id":
            continue
        raw[k] = v
    # Bei unbekanntem Typ auch die schon bekannten Item/Count-Felder sichern,
    # damit das Frontend zur Not etwas anzeigen kann.
    if out["type"] not in ("item", "xp", "dimension", "checkmark"):
        for k in ("item", "count", "xp", "dimension"):
            if k in entry:
                raw.setdefault(k, entry[k])
    if raw:
        out["raw"] = raw
    return out


# ===========================================================================
# Quest-/Kapitel-Mapping
# ===========================================================================

def map_quest(q):
    """Mappt ein Quest-Objekt auf das Spec-Schema mit Defaults."""
    # shape: leerer String oder fehlend -> Default "circle".
    shape = q.get("shape")
    if not shape:
        shape = "circle"

    # size: fehlend -> Default 1.0.
    size = q.get("size")
    size = float(size) if size is not None else 1.0

    x = q.get("x", 0.0)
    y = q.get("y", 0.0)

    description = q.get("description")
    if not isinstance(description, list):
        description = []

    dependencies = q.get("dependencies")
    if not isinstance(dependencies, list):
        dependencies = []

    tasks = q.get("tasks") if isinstance(q.get("tasks"), list) else []
    rewards = q.get("rewards") if isinstance(q.get("rewards"), list) else []

    mapped = {
        "id": q.get("id"),
        "x": float(x),
        "y": float(y),
        "shape": shape,
        "size": size,
        "title": q.get("title", ""),
        "optional": bool(q.get("optional", False)),
        "icon": humanize_icon(q.get("icon")),
        "description": description,
        "dependencies": dependencies,
        "tasks": [map_entry(t) for t in tasks],
        "rewards": [map_entry(r) for r in rewards],
    }
    # hide_dependent_lines nur durchreichen, wenn gesetzt (Frontend nutzt es).
    if "hide_dependent_lines" in q:
        mapped["hide_dependent_lines"] = bool(q["hide_dependent_lines"])
    return mapped


def map_chapter(ch):
    quests = ch.get("quests") if isinstance(ch.get("quests"), list) else []
    return {
        "id": ch.get("id"),
        "title": ch.get("title", ""),
        "icon": humanize_icon(ch.get("icon")),
        "quests": [map_quest(q) for q in quests],
    }


# ===========================================================================
# Build
# ===========================================================================

def build():
    # 1) globale Meta aus data.snbt
    data = read_snbt(os.path.join(QUESTS_DIR, "data.snbt"))
    meta = {
        "title": data.get("title", "Quests"),
        "version": data.get("version", 0),
    }

    # 2) Kapitel-Gruppen (aktuell nur fuer Reihenfolge/Info vorhanden,
    #    das Schema sammelt Kapitel flach unter "chapters").
    groups_path = os.path.join(QUESTS_DIR, "chapter_groups.snbt")
    if os.path.exists(groups_path):
        read_snbt(groups_path)  # geparst zur Validierung; aktuell ungenutzt

    # 3) alle Kapitel-Dateien (sortiert: erst nach order_index, dann Name)
    chapters_dir = os.path.join(QUESTS_DIR, "chapters")
    files = sorted(f for f in os.listdir(chapters_dir) if f.endswith(".snbt"))

    parsed_chapters = []
    for fname in files:
        ch = read_snbt(os.path.join(chapters_dir, fname))
        ch["__order"] = ch.get("order_index", 0)
        parsed_chapters.append(ch)
    parsed_chapters.sort(key=lambda c: (c.get("__order", 0)))

    chapters = [map_chapter(ch) for ch in parsed_chapters]

    return {"meta": meta, "chapters": chapters}


def write_data_js(data):
    os.makedirs(OUT_DIR, exist_ok=True)
    payload = json.dumps(data, ensure_ascii=False, indent=2)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write("window.QUEST_DATA = " + payload + ";\n")


def main():
    data = build()
    write_data_js(data)
    total_quests = sum(len(c["quests"]) for c in data["chapters"])
    print("Geschrieben: %s" % OUT_FILE)
    print("Kapitel: %d" % len(data["chapters"]))
    print("Quests gesamt: %d" % total_quests)


if __name__ == "__main__":
    main()
