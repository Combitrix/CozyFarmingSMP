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
_FMT_CODES = set("0123456789abcdefklmnor")  # gültige FTB-&-Codes (Color4I / TextComponentParser)

def esc(s):
    # FTB TextComponentParser: '&' (und §) leiten einen Formatcode ein. '&'+Whitespace oder '&'+
    # unbekanntes Zeichen ist ein Fehler. Literale '&' (z.B. "Farmen & Leben") als '\&' escapen.
    out = []
    for i, ch in enumerate(s):
        if ch == "&":
            nxt = s[i + 1] if i + 1 < len(s) else ""
            out.append("&" if (nxt == "#" or nxt in _FMT_CODES) else "\\&")
        else:
            out.append(ch)
    # erst unsere/echte Backslashes verdoppeln (SNBT), dann Quotes escapen
    return "".join(out).replace("\\", "\\\\").replace('"', '\\"')

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
def quest(key, x, y, title, desc, tasks, rewards, deps=None, icon=None, shape=None, size=None, optional=False):
    q = {"id": QIDS[key]}
    q["x"] = Double(x)
    q["y"] = Double(y)
    q["title"] = title
    if icon:     q["icon"] = item(icon)
    if shape:    q["shape"] = shape
    if size:     q["size"] = Double(size)
    if optional: q["optional"] = True
    if desc:     q["description"] = desc
    if deps:     q["dependencies"] = [QIDS[d] for d in deps]
    q["tasks"] = tasks
    q["rewards"] = rewards
    return q

# Quest-Keys -> IDs vorab anlegen (für dependencies)
QIDS = {}
def reg(*keys):
    for k in keys:
        QIDS[k] = nid()

# Gruppen- und Kapitel-IDs (alle vorab -> stabile dependencies)
G0, G1, G2, G3, G4, G5, G6 = (nid() for _ in range(7))
CH_WELCOME, CH_FARM, CH_COLONY, CH_CREATE, CH_WORLD, CH_ECON, CH_ENDGAME = (nid() for _ in range(7))

# Quests registrieren
reg("w_start", "w_ipn")
reg("f_ernte", "f_kueche", "f_genuss", "f_saison", "f_tiere", "f_skills", "f_angeln")
reg("c_supply", "c_builder", "c_buerger", "c_mehrere", "c_bauen")
reg("w_biome", "w_netz", "w_dh")
reg("e_coins", "e_handel", "e_endgame")
reg("x_root", "x_megacolony", "x_trainnet", "x_aerofleet", "x_factory", "x_power",
    "x_selfsufficient", "x_fortune", "x_tradeempire", "x_explorer", "x_kartoffelboss", "x_completionist")

# ---- chapter_groups.snbt ---------------------------------------------------
chapter_groups = {"chapter_groups": [
    {"id": G0, "title": "§e👋 Willkommen"},
    {"id": G1, "title": "§a🌱 Farmen & Leben"},
    {"id": G2, "title": "§6🏘 Bauen & Gemeinschaft"},
    {"id": G3, "title": "§b⚙ Technik & Mobilität"},
    {"id": G4, "title": "§2🌍 Welt & Vernetzung"},
    {"id": G5, "title": "§e🪙 Ziele & Wirtschaft"},
    {"id": G6, "title": "§c🏆 Endgame"},
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

CHID = {"kolonien": CH_COLONY, "create": CH_CREATE, "welt": CH_WORLD,
        "wirtschaft": CH_ECON, "endgame": CH_ENDGAME}

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
# Wird unten aus dem ATM-10-Create-Kapitel transformiert (siehe transform_atm_create()).

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

# ---- Kapitel 7: Endgame (G6) -----------------------------------------------
def m(*lines): return list(lines)
endgame = chapter("endgame", G6, "🏆 Endgame", "magic_coins:crystal_coin", [
    quest("x_root", 0.0, 0.0, "Der lange Weg",
          ["Du hast die Grundlagen gemeistert — jetzt beginnt das große Spiel.",
           "Hier warten die ganz großen Ziele für dich und deine Mitspieler.",
           "",
           "Schließe ein paar Endgame-Ziele ab und werde zur Legende des SMP."],
          tasks=[task_check()], rewards=[coin_gold(5), rew_xp(30)],
          icon="minecraft:nether_star", size=2.0, shape="gear"),
    quest("x_megacolony", -3.0, -1.5, "Mega-Kolonie",
          ["Lass eine deiner Kolonien zur echten Großstadt wachsen:",
           "&750+ Bürger&r und mehrere voll ausgebaute Gebäude.",
           "", "Hak ab, wenn deine Kolonie 50 Bürger erreicht."],
          tasks=[task_check()], rewards=[coin_crystal(2), rew_xp(40)],
          deps=["x_root"], icon="minecolonies:blockhuttownhall", size=1.25),
    quest("x_trainnet", -1.5, -2.5, "Schienen-Imperium",
          ["Verbinde &emindestens drei Kolonien&r zu einem funktionierenden",
           "Zug-Netzwerk mit Fahrplänen und mehreren Linien.",
           "", "Hak ab, wenn 3 Stationen per Zug verbunden sind."],
          tasks=[task_check()], rewards=[coin_crystal(2), rew_xp(40)],
          deps=["x_root"], icon="create:track_station", size=1.25),
    quest("x_aerofleet", 1.5, -2.5, "Luftschiff-Flotte",
          ["&bCreate Aeronautics&r-Meisterschaft: baue ein großes, steuerbares",
           "Luftschiff (oder gleich mehrere).",
           "", "&7Alpha-Mod — vorher Backup! Hak ab, wenn dein Schiff fliegt."],
          tasks=[task_check()], rewards=[coin_crystal(3), rew_xp(50)],
          deps=["x_root"], icon="create:goggles", size=1.25),
    quest("x_factory", 3.0, -1.5, "Die Großfabrik",
          ["Baue eine &evollautomatische Create-Fabrik&r, die ein komplexes",
           "Endprodukt ohne Handarbeit fertigt (z.B. via Factory Gauges / Packages).",
           "", "Hak ab, wenn die Linie autark läuft."],
          tasks=[task_check()], rewards=[coin_crystal(2), rew_xp(40)],
          deps=["x_root"], icon="create:mechanical_arm", size=1.25),
    quest("x_power", 3.0, 1.5, "Energie-Imperium",
          ["Errichte ein großes Stromnetz mit den Energie-Addons",
           "(&aNew Age / Createaddition / Diesel / TFMG&r) und versorge deine Basis.",
           "", "Hak ab, wenn deine Maschinen aus einem Netz laufen."],
          tasks=[task_check()], rewards=[coin_crystal(2), rew_xp(40)],
          deps=["x_root"], icon="create:shaft", size=1.25),
    quest("x_selfsufficient", 1.5, 2.5, "Selbstversorger",
          ["Vollautomatische Nahrung: &aCreate: Central Kitchen&r kocht deine",
           "Gerichte am Fließband — nie wieder Hunger.",
           "", "Hak ab, wenn Essen automatisch produziert wird."],
          tasks=[task_check()], rewards=[coin_crystal(2), rew_xp(40)],
          deps=["x_root"], icon="farmersdelight:cooking_pot", size=1.25),
    quest("x_fortune", -3.0, 1.5, "Münz-Vermögen",
          ["Häufe ein echtes Vermögen an: besitze gleichzeitig",
           "&emindestens 5 Kristallmünzen&r.",
           "", "&7Der Gipfel des Münz-Wohlstands."],
          tasks=[task_item("magic_coins:crystal_coin", 5)], rewards=[coin_crystal(3), rew_xp(40)],
          deps=["x_root"], icon="magic_coins:crystal_coin", size=1.25),
    quest("x_tradeempire", -1.5, 2.5, "Handelsimperium",
          ["Baue ein &aNumismatics&r-Handelsnetz mit mehreren Automaten und",
           "Bankkarten zwischen den Kolonien auf.",
           "", "Hak ab, wenn mehrere Vendor laufen."],
          tasks=[task_check()], rewards=[coin_crystal(2), rew_xp(40)],
          deps=["x_root"], icon="numismatics:vendor", size=1.25),
    quest("x_explorer", 0.0, -3.5, "Welt-Entdecker",
          ["Bereise die riesige Welt: entdecke &e15 verschiedene Biome&r",
           "von Terralith & Tectonic.",
           "", "Hak ab, wenn du 15 Biome gesehen hast."],
          tasks=[task_check()], rewards=[coin_crystal(2), rew_xp(40)],
          deps=["x_root"], icon="minecraft:filled_map", size=1.25),
    quest("x_kartoffelboss", 4.5, 0.0, "Der Kartoffelboss (geplant)",
          ["§oGeplantes Eigen-Projekt:§r ein optionaler Boss-Kampf — der",
           "&6Kartoffelboss&r. Diese Quest wird aktiviert, sobald die Mod fertig ist.",
           "", "&7Platzhalter — noch nichts zu tun."],
          tasks=[task_check()], rewards=[coin_crystal(1)],
          deps=["x_root"], icon="minecraft:baked_potato", size=1.0, optional=True),
    quest("x_completionist", 0.0, 4.0, "Legende des SMP",
          ["Du hast es geschafft: alle großen Ziele erreicht. Vollende die",
           "wichtigsten Endgame-Quests und sichere dir den Titel.",
           "", "&6Herzlichen Glückwunsch — du bist eine Legende!"],
          tasks=[task_check()],
          rewards=[coin_crystal(10), rew_item("minecraft:nether_star"), rew_xp(100)],
          deps=["x_megacolony", "x_trainnet", "x_aerofleet", "x_factory", "x_power",
                "x_selfsufficient", "x_fortune", "x_tradeempire", "x_explorer"],
          icon="minecraft:nether_star", size=2.0, shape="gear"),
])

# ---- ATM-10 Create-Kapitel transformieren ----------------------------------
# Quelle: AllTheMods/ATM-10 (config/ftbquests/quests/chapters/create.snbt), 206 Quests.
# Anpassung an dieses Pack: Gruppe -> G3, Fremd-Items -> Pack-Äquivalente, ATM-Bilder entfernt.
import re as _re
def transform_atm_create():
    src = open(os.path.join(ROOT, "vendor", "atm_create.snbt"), encoding="utf-8").read()

    # 1) Fremd-Item-Referenzen auf vorhandene Pack-Items mappen
    src = src.replace('id: "alltheores:brass_ingot"', 'id: "create:brass_ingot"')
    src = src.replace('id: "the_bumblezone:honey_bucket"', 'id: "minecraft:honey_bottle"')
    # 1b) ftbfiltersystem:smart_filter (Task-Items) -> konkretes Create-Item je nach Filterinhalt
    filt_map = [
        ("mechanical_piston", "create:mechanical_piston"),
        ("cogwheel",          "create:cogwheel"),
        ("water_wheel",       "create:water_wheel"),
        ("seats",             "create:blue_seat"),
        ("postboxes",         "create:blue_postbox"),
        ("packages",          "create:cardboard_package_12x12"),
        ("table_cloths",      "create:andesite_table_cloth"),
    ]
    def repl_filter(mobj):
        inner = mobj.group(0)
        for needle, repl in filt_map:
            if needle in inner:
                return '{ count: 1, id: "%s" }' % repl
        return '{ count: 1, id: "create:cogwheel" }'  # Fallback
    src = _re.sub(r'\{ components: \{ "ftbfiltersystem:filter":.*?id: "ftbfiltersystem:smart_filter" \}',
                  repl_filter, src)

    # 2) Kapitel-Header: Gruppe auf G3, Titel ergänzen, ATM-Bilder entfernen
    src = _re.sub(r'group: "[0-9A-F]{16}"', 'group: "%s"' % G3, src, count=1)
    src = _re.sub(r'\n\timages: \[.*?\n\t\]', '', src, count=1, flags=_re.S)  # images-Block raus
    if "\n\ttitle:" not in src:
        title_line = '\tfilename: "create"\n\ttitle: "%s"\n' % esc("⚙ Technik & Mobilität (Create)")
        src = src.replace('\tfilename: "create"\n', title_line, 1)

    p = os.path.join(OUT, "chapters", "create.snbt")
    with open(p, "w", encoding="utf-8") as f:
        f.write(src)
    # Rückgabe: Liste aller IDs (für Kollisionsprüfung) + Restcheck Fremd-Namespaces
    foreign = _re.findall(r'id: "(ftbfiltersystem|alltheores|the_bumblezone):', src)
    ids = _re.findall(r'\bid: "([0-9A-F]{16})"', src)
    print("wrote chapters/create.snbt (ATM, transformiert) ids:", len(ids), "foreign-left:", foreign)
    return ids

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
write("chapters/welt.snbt", world)
write("chapters/wirtschaft.snbt", econ)
write("chapters/endgame.snbt", endgame)
atm_ids = transform_atm_create()
print("total ids used (generated):", _counter)
