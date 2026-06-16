#!/usr/bin/env python3
"""Generiert FTB-Quests-SNBT (Format verifiziert gegen FTB-Quests 1.21.1 + ATM-10).
Erzeugt eindeutige 16-Hex-IDs und schreibt nach pack/config/ftbquests/quests/.
Idempotent: bei jedem Lauf werden die Dateien neu erzeugt (gleiche IDs, da deterministisch)."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "pack", "config", "ftbquests", "quests")

# ---- deterministische, eindeutige ID-Vergabe -------------------------------
_counter = 0
def nid():
    global _counter
    _counter += 1
    return format(0x4C0F0000_00000000 + _counter, "016X")  # 16 Hex, kollisionsfrei

# ---- SNBT-Serialisierung ---------------------------------------------------
def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

def snbt(v, ind=0):
    t = "\t" * ind
    t1 = "\t" * (ind + 1)
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, Long):
        return f"{int(v)}L"
    if isinstance(v, Double):
        return f"{float(v)}d"
    if isinstance(v, int):
        return str(v)
    if isinstance(v, float):
        return f"{v}d"
    if isinstance(v, str):
        return f'"{esc(v)}"'
    if isinstance(v, list):
        if not v:
            return "[ ]"
        items = [t1 + snbt(x, ind + 1) for x in v]
        return "[\n" + "\n".join(items) + "\n" + t + "]"
    if isinstance(v, dict):
        if not v:
            return "{ }"
        lines = [t1 + f"{k}: " + snbt(val, ind + 1) for k, val in v.items()]
        return "{\n" + "\n".join(lines) + "\n" + t + "}"
    raise TypeError(type(v))

class Long(int): pass
class Double(float): pass

def item(idstr, count=1):
    return {"count": count, "id": idstr}

def task_item(idstr, count=1):
    d = {"id": nid(), "item": item(idstr), "type": "item"}
    if count > 1:
        d["count"] = Long(count)
    return d

def task_check():
    return {"id": nid(), "type": "checkmark"}

def task_dim(dim="minecraft:overworld"):
    return {"id": nid(), "type": "dimension", "dimension": dim}

def rew_item(idstr, count=1):
    d = {"id": nid(), "item": item(idstr), "type": "item"}
    if count > 1:
        d["count"] = count
    return d

def rew_xp(n):
    return {"id": nid(), "type": "xp", "xp": n}

# Magic-Coins-Belohnung (roter Faden)
def coin_silver(n): return rew_item("magic_coins:silver_coin", n)
def coin_gold(n):   return rew_item("magic_coins:gold_coin", n)

# ---- Quest-Helfer ----------------------------------------------------------
def quest(key, x, y, title, desc, tasks, rewards, deps=None, icon=None, shape=None, size=None):
    q = {"id": QIDS[key]}
    q["x"] = Double(x)
    q["y"] = Double(y)
    q["title"] = title
    if icon:  q["icon"] = item(icon)
    if shape: q["shape"] = shape
    if size:  q["size"] = Double(size)
    if desc:  q["description"] = desc
    if deps:  q["dependencies"] = [QIDS[d] for d in deps]
    q["tasks"] = tasks
    q["rewards"] = rewards
    return q

# Quest-Keys -> IDs vorab anlegen (für dependencies)
QIDS = {}
def reg(*keys):
    for k in keys:
        QIDS[k] = nid()

# Gruppen- und Kapitel-IDs
G0, G1 = nid(), nid()
CH_WELCOME, CH_FARM = nid(), nid()

# Quests registrieren
reg("w_start", "w_ipn")
reg("f_ernte", "f_kueche", "f_genuss", "f_saison", "f_tiere", "f_skills", "f_angeln")

# ---- chapter_groups.snbt ---------------------------------------------------
chapter_groups = {"chapter_groups": [
    {"id": G0, "title": "§e👋 Willkommen"},
    {"id": G1, "title": "§a🌱 Farmen & Leben"},
]}

# ---- data.snbt -------------------------------------------------------------
data = {
    "default_autoclaim_rewards": "disabled",
    "default_consume_items": False,
    "default_quest_disable_jei": False,
    "default_quest_shape": "circle",
    "default_reward_team": False,
    "detection_delay": 20,
    "disable_gui": False,
    "drop_loot_crates": False,
    "grid_scale": Double(0.5),
    "lock_message": "",
    "pause_game": False,
    "progression_mode": "flexible",
    "title": "Cozy Farming SMP",
    "version": 13,
}

# ---- Kapitel 0: Willkommen -------------------------------------------------
welcome = {
    "default_hide_dependency_lines": False,
    "default_quest_shape": "",
    "filename": "willkommen",
    "group": G0,
    "icon": item("ftbquests:book"),
    "id": CH_WELCOME,
    "order_index": 0,
    "progression_mode": "flexible",
    "quest_links": [],
    "title": "👋 Willkommen",
    "quests": [
        quest("w_start", 0.0, 0.0,
              "Willkommen auf dem Cozy Farming SMP!",
              ["Schön, dass du da bist! Dieses Pack dreht sich um &aFarmen&r, &6Kolonien&r,",
               "&bCreate-Technik&r und ein gemütliches Leben mit Freunden.",
               "",
               "&eRezepte:&r Drücke die Taste für &aEMI&r (rechts neben dem Inventar) —",
               "links siehst du, wie etwas hergestellt wird, rechts wofür man es braucht.",
               "&eKarte:&r &aJourneyMap&r (oben rechts) — Wegpunkte mit der Karten-Taste.",
               "",
               "Stelle einen &aWerkbank-Tisch&r her, um zu starten."],
              tasks=[task_item("minecraft:crafting_table")],
              rewards=[rew_item("minecraft:bread", 4), coin_silver(10), rew_xp(10)],
              icon="minecraft:oak_sapling", size=1.5, shape="hexagon"),
        quest("w_ipn", 2.0, 0.0,
              "Inventar-Komfort (Inventory Profiles Next)",
              ["Die &dlila Pfeile&r in der Hotbar gehören zu &dInventory Profiles Next&r (IPN) —",
               "dem &eHotbar-Swapping&r: damit schaltest du ganze Hotbar-Belegungen per",
               "Tastendruck um.",
               "",
               "Wir haben die Pfeile &cstandardmäßig ausgeblendet&r, weil sie im Weg waren —",
               "das &aFeature bleibt aber aktiv&r. So holst du es zurück:",
               "",
               "&71.&r Inventar öffnen → oben (Mitte / nahe Inventar) sind die IPN-Buttons.",
               "&72.&r Einstellungen → &eInventory Profiles Next&r (Taste &aO&r): dort",
               "   &eHotbar Swapping&r bzw. &eShow hotbar buttons&r wieder einschalten.",
               "&73.&r Die zwei Symbole oben links wurden in die Nähe des Inventars verschoben.",
               "",
               "Hak diese Quest ab, wenn du es gelesen hast."],
              tasks=[task_check()],
              rewards=[coin_silver(5)],
              deps=["w_start"],
              icon="minecraft:chest", size=1.0),
    ],
}

# ---- Kapitel 1: Farmen & Leben ---------------------------------------------
farm = {
    "default_hide_dependency_lines": False,
    "default_quest_shape": "",
    "filename": "farmen_und_leben",
    "group": G1,
    "icon": item("farmersdelight:cooking_pot"),
    "id": CH_FARM,
    "order_index": 0,
    "progression_mode": "flexible",
    "quest_links": [],
    "title": "🌱 Farmen & Leben",
    "quests": [
        quest("f_ernte", 0.0, 0.0,
              "Die erste Ernte",
              ["Jedes Imperium beginnt mit einem Acker. Besorge dir eine &aHacke&r,",
               "lege Felder an und ernte deine erste Frucht.",
               "",
               "&7Tipp: HarvestCraft 2, Veggies & die Delight-Mods bringen unzählige",
               "neue Pflanzen — schau in EMI, was alles wächst!"],
              tasks=[task_item("minecraft:wheat", 8), task_item("minecraft:wooden_hoe")],
              rewards=[rew_item("farmersdelight:cabbage_seeds", 3),
                       rew_item("farmersdelight:tomato_seeds", 3), coin_silver(15), rew_xp(10)],
              icon="minecraft:wheat", size=1.5, shape="hexagon"),
        quest("f_kueche", 2.0, 0.0,
              "Die Küche (Farmer's Delight)",
              ["Rohe Karotten? Nicht mit uns. Stelle &aKochtopf&r und &aSchneidebrett&r her",
               "und koche dein erstes richtiges Gericht.",
               "",
               "&7Der Kochtopf braucht eine Hitzequelle darunter (z.B. Lagerfeuer/Ofen)."],
              tasks=[task_item("farmersdelight:cooking_pot"),
                     task_item("farmersdelight:cutting_board"),
                     task_item("farmersdelight:vegetable_soup")],
              rewards=[rew_item("farmersdelight:skillet"), coin_gold(1), rew_xp(15)],
              deps=["f_ernte"], icon="farmersdelight:cooking_pot", size=1.25),
        quest("f_genuss", 4.0, 0.0,
              "Genuss & Vielfalt",
              ["Das Pack steckt voller Lebensmittel-Mods: &aVinery&r (Wein), &aMeadow&r (Käse),",
               "&aBakery/Confectionery&r, &aHerbalbrews&r (Tee), &aBrewin' & Chewin'&r u.v.m.",
               "",
               "Probiere mindestens eine dieser Mods aus und stelle etwas her.",
               "Hak ab, wenn du ein Produkt aus einer der Delight-/Let's-Do-Mods hast."],
              tasks=[task_check()],
              rewards=[coin_silver(15), rew_xp(10)],
              deps=["f_kueche"], icon="minecraft:cake", size=1.0),
        quest("f_saison", 2.0, 1.5,
              "Die Jahreszeiten (Serene Seasons)",
              ["Pflanzen wachsen je nach &eJahreszeit&r unterschiedlich gut.",
               "Achte auf Frühling/Sommer/Herbst und plane deine Felder.",
               "",
               "Ernte eine Feldfrucht in ihrer passenden Saison (Infos: EMI / Saisons-Kalender).",
               "Hak diese Info-Quest ab."],
              tasks=[task_check()],
              rewards=[coin_silver(15), rew_xp(10)],
              deps=["f_kueche"], icon="minecraft:wheat_seeds", size=1.0),
        quest("f_tiere", 0.0, 1.5,
              "Tiere & Zucht (Naturalist)",
              ["Eine Farm lebt von ihren Tieren. Züchte mindestens zwei Tierarten",
               "und entdecke die neuen Kreaturen von &aNaturalist&r.",
               "",
               "Sammle Weizen/Samen zum Füttern und hak ab, wenn du 2 Arten gezüchtet hast."],
              tasks=[task_item("minecraft:wheat", 4), task_check()],
              rewards=[rew_item("minecraft:wheat", 16), coin_silver(15), rew_xp(10)],
              deps=["f_ernte"], icon="minecraft:egg", size=1.0),
        quest("f_skills", 4.0, 1.5,
              "Fähigkeiten (Pufferfish's Skills)",
              ["Mit &aPufferfish's Skills&r levelst du Fähigkeiten wie Farming, Mining,",
               "Fishing und Husbandry. Öffne den Skill-Bildschirm und investiere",
               "deinen ersten Skill-Punkt.",
               "",
               "Hak ab, wenn du einen Skill freigeschaltet hast."],
              tasks=[task_check()],
              rewards=[coin_gold(1), rew_xp(20)],
              deps=["f_genuss"], icon="minecraft:experience_bottle", size=1.0),
        quest("f_angeln", -2.0, 0.0,
              "Angeln (Aquaculture)",
              ["Am Wasser wartet eine zweite Speisekammer. Bastle eine &aAngel&r und",
               "fange ein paar Fische — mit &aAquaculture&r gibt es viele neue Arten.",
               "",
               "Danach kannst du sie in der Küche zu Gerichten verarbeiten."],
              tasks=[task_item("minecraft:fishing_rod"), task_item("minecraft:cod", 3)],
              rewards=[rew_item("farmersdelight:cooked_cod_slice", 4), coin_silver(15), rew_xp(10)],
              deps=["f_ernte"], icon="minecraft:fishing_rod", size=1.0),
    ],
}

# ---- schreiben -------------------------------------------------------------
os.makedirs(os.path.join(OUT, "chapters"), exist_ok=True)
def write(relpath, obj):
    p = os.path.join(OUT, relpath)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(snbt(obj) + "\n")
    print("wrote", relpath)

write("chapter_groups.snbt", chapter_groups)
write("data.snbt", data)
write("chapters/willkommen.snbt", welcome)
write("chapters/farmen_und_leben.snbt", farm)
print("total ids used:", _counter)
