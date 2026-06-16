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
def coin_silver(n):  return rew_item("magic_coins:silver_coin", n)
def coin_gold(n):    return rew_item("magic_coins:gold_coin", n)
def coin_crystal(n): return rew_item("magic_coins:crystal_coin", n)

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

# Gruppen- und Kapitel-IDs (alle vorab -> stabile dependencies)
G0, G1, G2, G3, G4, G5 = (nid() for _ in range(6))
CH_WELCOME, CH_FARM, CH_COLONY, CH_CREATE, CH_WORLD, CH_ECON = (nid() for _ in range(6))

# Quests registrieren
reg("w_start", "w_ipn")
reg("f_ernte", "f_kueche", "f_genuss", "f_saison", "f_tiere", "f_skills", "f_angeln")
reg("c_supply", "c_builder", "c_buerger", "c_mehrere", "c_bauen")
reg("t_kinetik", "t_verarbeitung", "t_kitchen", "t_energie", "t_zug", "t_aero")
reg("w_biome", "w_netz", "w_dh")
reg("e_coins", "e_handel", "e_endgame")

# ---- chapter_groups.snbt ---------------------------------------------------
chapter_groups = {"chapter_groups": [
    {"id": G0, "title": "§e👋 Willkommen"},
    {"id": G1, "title": "§a🌱 Farmen & Leben"},
    {"id": G2, "title": "§6🏘 Bauen & Gemeinschaft"},
    {"id": G3, "title": "§b⚙ Technik & Mobilität"},
    {"id": G4, "title": "§2🌍 Welt & Vernetzung"},
    {"id": G5, "title": "§e🪙 Ziele & Wirtschaft"},
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

CHID = {"kolonien": CH_COLONY, "create": CH_CREATE, "welt": CH_WORLD, "wirtschaft": CH_ECON}

def chapter(filename, group, title, icon, quests):
    return {
        "default_hide_dependency_lines": False,
        "default_quest_shape": "",
        "filename": filename,
        "group": group,
        "icon": item(icon),
        "id": CHID[filename],
        "order_index": 0,
        "progression_mode": "flexible",
        "quest_links": [],
        "title": title,
        "quests": quests,
    }

# ---- Kapitel 2: Bauen & Gemeinschaft (MineColonies) ------------------------
colony = chapter("kolonien", G2, "🏘 Bauen & Gemeinschaft", "minecolonies:blockhuttownhall", [
    quest("c_supply", 0.0, 0.0, "Die erste Kolonie",
          ["Jede Zivilisation beginnt mit einem &6Versorgungslager&r. Platziere den",
           "&aSupply Camp&r, packe die Kiste aus und setze dein &aRathaus&r (Town Hall).",
           "",
           "&7Du darfst auf diesem Server §lbeliebig viele§r§7 Kolonien gründen!"],
          tasks=[task_item("minecolonies:supplycampdeployer"), task_item("minecolonies:blockhuttownhall")],
          rewards=[rew_item("minecolonies:blockhutbuilder"), coin_gold(2), rew_xp(20)],
          icon="minecolonies:blockhuttownhall", size=1.5, shape="hexagon"),
    quest("c_builder", 2.0, 0.0, "Der Baumeister",
          ["Ohne Baumeister wächst keine Kolonie. Platziere die &aBuilder's Hut&r,",
           "weise einen Bürger zu und gib deinen ersten Bauauftrag.",
           "",
           "&7Mit dem Bau-Werkzeug richtest du Gebäude aus und upgradest sie."],
          tasks=[task_item("minecolonies:blockhutbuilder")],
          rewards=[rew_item("minecraft:oak_log", 32), coin_gold(2), rew_xp(15)],
          deps=["c_supply"], icon="minecolonies:blockhutbuilder", size=1.25),
    quest("c_buerger", 4.0, 0.0, "Bürger & Versorgung",
          ["Eine Kolonie lebt von ihren Bewohnern. Sorge für Häuser, hol dir Bürger",
           "und versorge sie: Baue &aKüche&r und &aTaverne&r, damit gekocht und",
           "rekrutiert wird. (Verbindet sich direkt mit deiner Farm!)",
           "",
           "Hak ab, sobald Küche & Taverne stehen."],
          tasks=[task_item("minecolonies:blockhutcook"), task_item("minecolonies:blockhuttavern"), task_check()],
          rewards=[coin_gold(3), rew_xp(20)],
          deps=["c_builder"], icon="minecolonies:blockhutcook", size=1.25),
    quest("c_mehrere", 6.0, 0.0, "Mehrere Zivilisationen",
          ["Der Server erlaubt §lunbegrenzt viele Kolonien pro Spieler§r.",
           "Gründe eine &6zweite Kolonie&r an einem anderen Ort.",
           "",
           "&7Mindestabstand beachten (16 Chunks). Später verbindest du sie per Zug!"],
          tasks=[task_check()],
          rewards=[coin_gold(5), rew_xp(30)],
          deps=["c_buerger"], icon="minecolonies:clipboard", size=1.25),
    quest("c_bauen", 4.0, 1.5, "Schöner Bauen",
          ["Mit &aStructurize&r und &aDomum Ornamentum&r baust und gestaltest du frei.",
           "Dazu gibt es Möbel von Macaw's & Another Furniture.",
           "",
           "Erstelle ein eigenes Blueprint oder dekoriere ein Gebäude und hak ab."],
          tasks=[task_check()],
          rewards=[coin_silver(20), rew_xp(15)],
          deps=["c_buerger"], icon="minecraft:painting", size=1.0),
])

# ---- Kapitel 3: Technik & Mobilität (Create) -------------------------------
create_ch = chapter("create", G3, "⚙ Technik & Mobilität", "create:cogwheel", [
    quest("t_kinetik", 0.0, 0.0, "Kinetik-Grundlagen",
          ["Willkommen bei &bCreate&r. Alles beginnt mit Drehkraft: Stelle ein",
           "&aZahnrad&r, ein &aWasserrad&r und eine &aMechanische Presse&r her.",
           "",
           "&7Andesite Alloy ist deine wichtigste Grundzutat."],
          tasks=[task_item("create:cogwheel"), task_item("create:water_wheel"), task_item("create:mechanical_press")],
          rewards=[rew_item("create:andesite_alloy", 16), coin_silver(20), rew_xp(15)],
          icon="create:cogwheel", size=1.5, shape="hexagon"),
    quest("t_verarbeitung", 2.0, 0.0, "Verarbeitung & Automatik",
          ["Kombiniere &aMixer&r + &aBecken&r zum Rühren und nutze den",
           "&aMechanischen Kruster&r für automatisches Crafting.",
           "",
           "&7Damit automatisierst du fast jede Produktionskette."],
          tasks=[task_item("create:mechanical_mixer"), task_item("create:basin"), task_item("create:mechanical_crafter")],
          rewards=[coin_gold(2), rew_xp(20)],
          deps=["t_kinetik"], icon="create:mechanical_mixer", size=1.25),
    quest("t_kitchen", 4.0, -1.0, "Automatische Küche",
          ["Mit &aCreate: Central Kitchen&r verheiratest du Create und Farmer's Delight:",
           "Kochtöpfe automatisch befüllen und Gerichte am Fließband produzieren.",
           "",
           "Baue eine automatisierte Koch-Anlage und hak ab."],
          tasks=[task_check()],
          rewards=[coin_gold(2), rew_xp(15)],
          deps=["t_verarbeitung"], icon="farmersdelight:cooking_pot", size=1.0),
    quest("t_energie", 4.0, 1.0, "Energie & Addons",
          ["Strom und mehr: &aCreate New Age&r, &aDiesel Generators / TFMG&r,",
           "&aCreateaddition&r, &aCreate Factory&r u.v.m. sind dabei.",
           "",
           "Baue mit einem dieser Addons eine Energiequelle und hak ab."],
          tasks=[task_check()],
          rewards=[coin_gold(2), rew_xp(15)],
          deps=["t_verarbeitung"], icon="create:shaft", size=1.0),
    quest("t_zug", 6.0, 0.0, "Schienen & Züge",
          ["Zeit für das &bSchienennetz&r (Steam 'n' Rails). Verlege &aGleise&r,",
           "setze einen &aBahnhof&r und baue einen Zug zusammen.",
           "",
           "&7Mit dem &aSchedule&r (Fahrplan) fährt der Zug automatisch."],
          tasks=[task_item("create:track", 16), task_item("create:track_station"), task_item("create:schedule")],
          rewards=[rew_item("railways:conductor_cap"), coin_gold(4), rew_xp(25)],
          deps=["t_verarbeitung"], icon="create:track_station", size=1.5, shape="hexagon"),
    quest("t_aero", 8.0, 0.0, "In die Lüfte (Create Aeronautics)",
          ["§oBonus / Endgame.§r Mit &aCreate Aeronautics&r baust du echte",
           "&bLuftschiffe&r. (Alpha-Mod — kann zickig sein, Backups machen!)",
           "",
           "Baue eine fliegende Kontraption und hak ab."],
          tasks=[task_check()],
          rewards=[coin_crystal(1), rew_xp(40)],
          deps=["t_zug"], icon="create:goggles", size=1.25),
])

# ---- Kapitel 4: Welt & Vernetzung ------------------------------------------
world = chapter("welt", G4, "🌍 Welt & Vernetzung", "minecraft:filled_map", [
    quest("w_biome", 0.0, 0.0, "Entdecke die Welt",
          ["Die Welt ist riesig und realistisch: &aTerralith&r + &aTectonic&r zaubern",
           "epische Biome und Gebirge. Erkunde mindestens &e3 verschiedene&r Biome.",
           "",
           "&7Setze Wegpunkte in JourneyMap und hak ab, wenn du 3 Biome gesehen hast."],
          tasks=[task_check()],
          rewards=[rew_item("minecraft:map"), coin_silver(20), rew_xp(15)],
          icon="minecraft:filled_map", size=1.5, shape="hexagon"),
    quest("w_netz", 2.0, 0.0, "Das Schienennetz",
          ["Der große Traum: Zivilisationen per Zug verbinden. Verlege eine",
           "&bZugstrecke zwischen zwei Kolonien&r (Bahnhof ↔ Bahnhof).",
           "",
           "Hak ab, sobald ein Zug zwischen zwei Stationen fährt."],
          tasks=[task_check()],
          rewards=[coin_gold(5), rew_xp(30)],
          deps=["w_biome"], icon="create:track", size=1.25),
    quest("w_dh", 0.0, 1.5, "Weite Sicht (Distant Horizons)",
          ["&aDistant Horizons&r rendert das Gelände als LODs bis weit zum Horizont —",
           "perfekt für Bahnfahrten und Aussichten.",
           "",
           "&7Sichtweite/Qualität in den DH-Einstellungen justieren; Iris-Shader optional.",
           "Info gelesen? Hak ab."],
          tasks=[task_check()],
          rewards=[coin_silver(10), rew_xp(10)],
          deps=["w_biome"], icon="minecraft:spyglass", size=1.0),
])

# ---- Kapitel 5: Ziele & Wirtschaft -----------------------------------------
econ = chapter("wirtschaft", G5, "🪙 Ziele & Wirtschaft", "magic_coins:gold_coin", [
    quest("e_coins", 0.0, 0.0, "Münzwirtschaft (Magic Coins)",
          ["&eMünzen&r sind der rote Faden: Quests belohnen dich mit Silber-, Gold-",
           "und Kristallmünzen. Sammle etwas Vermögen an.",
           "",
           "Besitze gleichzeitig mindestens &e3 Goldmünzen&r."],
          tasks=[task_item("magic_coins:gold_coin", 3)],
          rewards=[coin_gold(2), rew_xp(15)],
          icon="magic_coins:gold_coin", size=1.5, shape="hexagon"),
    quest("e_handel", 2.0, 0.0, "Handel (Create: Numismatics)",
          ["&aNumismatics&r bringt physische Münzen, Bankkarten und Automaten.",
           "Baue einen &aVendor&r (Verkaufsautomat) und wickle einen Handel ab.",
           "",
           "&7Passt perfekt zum Zug-/Handelsthema zwischen den Kolonien."],
          tasks=[task_item("numismatics:vendor"), task_item("numismatics:spur", 8)],
          rewards=[coin_gold(3), rew_xp(20)],
          deps=["e_coins"], icon="numismatics:vendor", size=1.25),
    quest("e_endgame", 4.0, 0.0, "Endgame-Ziele",
          ["Der große Showdown des SMP. Erfülle die Meilensteine:",
           "&7• eine große Kolonie  • ein funktionierendes Zugnetz",
           "&7• ein Aeronautics-Luftschiff  • ein ordentliches Münzvermögen",
           "",
           "§oHook: Später kommt vielleicht ein optionaler &cKartoffelboss&r§o dazu …§r"],
          tasks=[task_check(), task_check(), task_check(), task_check()],
          rewards=[coin_crystal(3), rew_xp(60)],
          deps=["e_handel"], icon="magic_coins:crystal_coin", size=1.5, shape="gear"),
])

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
write("chapters/kolonien.snbt", colony)
write("chapters/create.snbt", create_ch)
write("chapters/welt.snbt", world)
write("chapters/wirtschaft.snbt", econ)
print("total ids used:", _counter)
