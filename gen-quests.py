#!/usr/bin/env python3
"""Generiert die FTB-Quests-SNBT (Format verifiziert gegen FTB-Quests 1.21.1 + ATM-10).
EIN Quest-Baum (eine Gruppe), der sich progressiv freischaltet (Kapitel sind Seiten,
über cross-chapter dependencies verkettet). Deterministische, eindeutige 16-Hex-IDs.

Kapitel-Reihenfolge (order_index):
  0 Willkommen (ATM-Style)  1 Farmen & Leben  2 Bauen & Gemeinschaft
  3 Technik (Create, aus ATM-10 transformiert, +deutsche Beschreibungen)
  4 Aeronautics (25 Quests)  5 Welt  6 Wirtschaft  7 Endgame
"""
import os, re as _re

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "pack", "config", "ftbquests", "quests")

# ---- deterministische, eindeutige ID-Vergabe -------------------------------
_counter = 0
def nid():
    global _counter
    _counter += 1
    return format(0x4C0F0000_00000000 + _counter, "016X")

# ---- SNBT-Serialisierung ---------------------------------------------------
_FMT_CODES = set("0123456789abcdefklmnor")
class Long(int): pass
class Double(float): pass

def esc(s):
    # FTB TextComponentParser: '&'/§ leiten Formatcodes ein; '&'+Whitespace/ungültig = Fehler.
    out = []
    for i, ch in enumerate(s):
        if ch == "&":
            nxt = s[i + 1] if i + 1 < len(s) else ""
            out.append("&" if (nxt == "#" or nxt in _FMT_CODES) else "\\&")
        else:
            out.append(ch)
    return "".join(out).replace("\\", "\\\\").replace('"', '\\"')

def snbt(v, ind=0):
    t = "\t" * ind; t1 = "\t" * (ind + 1)
    if isinstance(v, bool):   return "true" if v else "false"
    if isinstance(v, Long):   return f"{int(v)}L"
    if isinstance(v, Double): return f"{float(v)}d"
    if isinstance(v, int):    return str(v)
    if isinstance(v, float):  return f"{v}d"
    if isinstance(v, str):    return f'"{esc(v)}"'
    if isinstance(v, list):
        if not v: return "[ ]"
        return "[\n" + "\n".join(t1 + snbt(x, ind + 1) for x in v) + "\n" + t + "]"
    if isinstance(v, dict):
        if not v: return "{ }"
        return "{\n" + "\n".join(t1 + f"{k}: " + snbt(val, ind + 1) for k, val in v.items()) + "\n" + t + "}"
    raise TypeError(type(v))

def item(idstr, count=1): return {"count": count, "id": idstr}
def task_item(idstr, count=1):
    d = {"id": nid(), "item": item(idstr), "type": "item"}
    if count > 1: d["count"] = Long(count)
    return d
def task_check(): return {"id": nid(), "type": "checkmark"}
def task_dim(dim="minecraft:overworld"): return {"id": nid(), "type": "dimension", "dimension": dim}
def rew_item(idstr, count=1):
    d = {"id": nid(), "item": item(idstr), "type": "item"}
    if count > 1: d["count"] = count
    return d
def rew_xp(n): return {"id": nid(), "type": "xp", "xp": n}
def coin_silver(n):  return rew_item("magic_coins:silver_coin", n)
def coin_gold(n):    return rew_item("magic_coins:gold_coin", n)
def coin_crystal(n): return rew_item("magic_coins:crystal_coin", n)

# ---- Quest-Helfer ----------------------------------------------------------
def quest(key, x, y, title, desc, tasks, rewards, deps=None, icon=None, shape=None, size=None, optional=False):
    q = {"id": QIDS[key], "x": Double(x), "y": Double(y), "title": title}
    if icon:     q["icon"] = item(icon)
    if shape:    q["shape"] = shape
    if size:     q["size"] = Double(size)
    if optional: q["optional"] = True
    if desc:     q["description"] = desc
    if deps:     q["dependencies"] = [QIDS[d] if d in QIDS else d for d in deps]  # raw-Hex erlaubt
    q["tasks"] = tasks
    q["rewards"] = rewards
    return q

QIDS = {}
def reg(*keys):
    for k in keys: QIDS[k] = nid()

# ---- IDs: EINE Gruppe + Kapitel --------------------------------------------
G = nid()  # die eine Quest-Gruppe
CH_WELCOME, CH_FARM, CH_COLONY, CH_CREATE, CH_AERO, CH_WORLD, CH_ECON, CH_ENDGAME = (nid() for _ in range(8))
ATM_CREATE_ROOT = "57A7A5C79389A96A"  # Wurzel-Quest im ATM-Create-Kapitel (für Verkettung)

reg("w_start", "w_table", "w_emi", "w_map", "w_ipn", "w_claim", "w_info")
reg("f_ernte", "f_kueche", "f_genuss", "f_saison", "f_tiere", "f_skills", "f_angeln")
reg("c_supply", "c_builder", "c_buerger", "c_mehrere", "c_bauen")
reg("cr_start", "cr_press", "cr_power", "cr_processing", "cr_belt", "cr_mixing", "cr_farm",
    "cr_autocraft", "cr_contraption", "cr_energy", "cr_kitchen", "cr_factory", "cr_treefarm",
    "cr_train", "cr_trainnet", "cr_advanced")
reg("ae_intro", "ae_wood_prop", "ae_andesite_prop", "ae_prop_bearing", "ae_burner", "ae_steam",
    "ae_envelope", "ae_envelope_shaft", "ae_big_envelope", "ae_first_flight", "ae_levitite_powder",
    "ae_levitite_bucket", "ae_levitite", "ae_pearl_levitite", "ae_smart_prop", "ae_gyro",
    "ae_first_ship", "ae_potato_cannon", "ae_steer", "ae_music", "ae_high", "ae_transport",
    "ae_passenger", "ae_armada", "ae_master")
reg("w_biome", "w_netz", "w_dh")
reg("e_coins", "e_handel", "e_endgame")
reg("x_root", "x_megacolony", "x_trainnet", "x_aerofleet", "x_factory", "x_power",
    "x_selfsufficient", "x_fortune", "x_tradeempire", "x_explorer", "x_kartoffelboss", "x_completionist")

# ---- chapter_groups.snbt: EINE Gruppe --------------------------------------
chapter_groups = {"chapter_groups": [{"id": G, "title": "§6🌾 Cozy Farming SMP"}]}

# ---- data.snbt -------------------------------------------------------------
data = {
    "default_autoclaim_rewards": "disabled", "default_consume_items": False,
    "default_quest_disable_jei": False, "default_quest_shape": "circle",
    "default_reward_team": False, "detection_delay": 20, "disable_gui": False,
    "drop_loot_crates": False, "grid_scale": Double(0.5), "lock_message": "",
    "pause_game": False, "progression_mode": "flexible", "title": "Cozy Farming SMP", "version": 13,
}

CHID = {"willkommen": CH_WELCOME, "farmen_und_leben": CH_FARM, "kolonien": CH_COLONY,
        "create": CH_CREATE, "aeronautics": CH_AERO, "welt": CH_WORLD,
        "wirtschaft": CH_ECON, "endgame": CH_ENDGAME}

def chapter(filename, title, icon, quests, order):
    return {
        "default_hide_dependency_lines": False, "default_quest_shape": "",
        "filename": filename, "group": G, "icon": item(icon), "id": CHID[filename],
        "order_index": order, "progression_mode": "flexible", "quest_links": [],
        "title": title, "quests": quests,
    }

# ---- Kapitel 0: Willkommen (ATM-Style: zentrale Wurzel + Speichen) ----------
welcome_q = [
    quest("w_start", 0.0, 0.0, "Willkommen auf dem Cozy Farming SMP!",
          ["&6Hallo und herzlich willkommen!&r Schön, dass du dabei bist.",
           "Dieses Pack dreht sich um &aFarmen&r, &6Kolonien&r, &bCreate-Technik&r,",
           "&dLuftschiffe&r und ein gemütliches Leben mit Freunden.",
           "",
           "Betritt die Welt — dann öffnet sich der Quest-Baum nach und nach.",
           "&7Die Quests führen dich Schritt für Schritt durch alle Features."],
          tasks=[task_dim("minecraft:overworld")],
          rewards=[rew_item("minecraft:bread", 4), coin_silver(10), rew_xp(10)],
          icon="minecraft:cake", size=3.0, shape="gear"),
    quest("w_table", 0.0, -2.0, "Aller Anfang",
          ["Stelle einen &aWerkbank-Tisch&r her und leg los.",
           "&7Mit EMI (rechts neben dem Inventar) siehst du jedes Rezept."],
          tasks=[task_item("minecraft:crafting_table")],
          rewards=[rew_item("minecraft:oak_log", 16), coin_silver(5)],
          deps=["w_start"], icon="minecraft:crafting_table", size=1.0),
    quest("w_emi", -2.0, -1.0, "Das Rezeptbuch (EMI)",
          ["&aEMI&r zeigt dir alle Rezepte: links wie etwas hergestellt wird,",
           "rechts wofür man es braucht. Klicke auf ein Item, um es nachzuschlagen.",
           "", "Info gelesen? Hak ab."],
          tasks=[task_check()], rewards=[coin_silver(5)],
          deps=["w_start"], icon="minecraft:knowledge_book", size=1.0),
    quest("w_map", 2.0, -1.0, "Die Karte (JourneyMap)",
          ["&aJourneyMap&r (oben rechts) zeigt deine Umgebung. Mit der Karten-Taste",
           "öffnest du die Vollkarte und setzt &eWegpunkte&r — praktisch für Kolonien!",
           "", "Info gelesen? Hak ab."],
          tasks=[task_check()], rewards=[coin_silver(5)],
          deps=["w_start"], icon="minecraft:filled_map", size=1.0),
    quest("w_ipn", -2.0, 1.0, "Inventar-Komfort (Inventory Profiles Next)",
          ["Die &dlila Pfeile&r in der Hotbar gehören zu &dInventory Profiles Next&r —",
           "dem &eHotbar-Swapping&r. Wir haben sie &cstandardmäßig ausgeblendet&r",
           "(sie waren im Weg), das &aFeature bleibt aber aktiv&r. Zurückholen:",
           "",
           "&71.&r Inventar öffnen → oben (Mitte/nahe Inventar) sind die IPN-Buttons.",
           "&72.&r Einstellungen → &eInventory Profiles Next&r (Taste &aO&r): dort",
           "   &eHotbar Swapping&r / &eShow hotbar buttons&r wieder einschalten.",
           "", "Hak ab, wenn du es gelesen hast."],
          tasks=[task_check()], rewards=[coin_silver(5)],
          deps=["w_start"], icon="minecraft:hopper", size=1.0),
    quest("w_claim", 2.0, 1.0, "Land sichern (FTB Chunks)",
          ["Mit &aFTB Chunks&r (Karten-Taste → Claim-Ansicht) schützt du Chunks vor",
           "Grief. &7Tipp: Kolonie-Chunks lädt MineColonies selbst — die musst du",
           "nicht zusätzlich force-loaden.",
           "", "Claime einen Chunk und hak ab."],
          tasks=[task_check()], rewards=[coin_silver(5)],
          deps=["w_start"], icon="ftbchunks:map", size=1.0),
    quest("w_info", 0.0, 2.0, "Gute Reise!",
          ["Viel Spaß auf dem SMP! &7Baut zusammen, handelt, verbindet eure",
           "Kolonien per Zug und erobert irgendwann den Himmel.",
           "", "&8(Diese Quest ist optional.)"],
          tasks=[task_check()], rewards=[coin_silver(5), rew_xp(5)],
          deps=["w_start"], icon="minecraft:bell", size=1.0, optional=True),
]

# ---- Kapitel 1: Farmen & Leben (gated hinter Willkommen) -------------------
farm_q = [
    quest("f_ernte", 0.0, 0.0, "Die erste Ernte",
          ["Jedes Imperium beginnt mit einem Acker. Besorge dir eine &aHacke&r,",
           "lege Felder an und ernte deine erste Frucht.",
           "", "&7HarvestCraft 2, Veggies & die Delight-Mods bringen unzählige Pflanzen!"],
          tasks=[task_item("minecraft:wheat", 8), task_item("minecraft:wooden_hoe")],
          rewards=[rew_item("farmersdelight:cabbage_seeds", 3),
                   rew_item("farmersdelight:tomato_seeds", 3), coin_silver(15), rew_xp(10)],
          deps=["w_start"], icon="minecraft:wheat", size=1.5, shape="hexagon"),
    quest("f_kueche", 2.0, 0.0, "Die Küche (Farmer's Delight)",
          ["Rohe Karotten? Nicht mit uns. Stelle &aKochtopf&r und &aSchneidebrett&r her",
           "und koche dein erstes richtiges Gericht.",
           "", "&7Der Kochtopf braucht eine Hitzequelle darunter (Lagerfeuer/Ofen)."],
          tasks=[task_item("farmersdelight:cooking_pot"), task_item("farmersdelight:cutting_board"),
                 task_item("farmersdelight:vegetable_soup")],
          rewards=[rew_item("farmersdelight:skillet"), coin_gold(1), rew_xp(15)],
          deps=["f_ernte"], icon="farmersdelight:cooking_pot", size=1.25),
    quest("f_genuss", 4.0, 0.0, "Genuss & Vielfalt",
          ["Das Pack steckt voller Lebensmittel-Mods: &aVinery&r (Wein), &aMeadow&r (Käse),",
           "&aBakery&r, &aHerbalbrews&r (Tee), &aBrewin' & Chewin'&r u.v.m.",
           "", "Stelle aus einer der Delight-/Let's-Do-Mods etwas her und hak ab."],
          tasks=[task_check()], rewards=[coin_silver(15), rew_xp(10)],
          deps=["f_kueche"], icon="minecraft:cake", size=1.0),
    quest("f_saison", 2.0, 1.5, "Die Jahreszeiten (Serene Seasons)",
          ["Pflanzen wachsen je nach &eJahreszeit&r unterschiedlich gut.",
           "Achte auf Frühling/Sommer/Herbst und plane deine Felder.",
           "", "Ernte in passender Saison und hak diese Info-Quest ab."],
          tasks=[task_check()], rewards=[coin_silver(15), rew_xp(10)],
          deps=["f_kueche"], icon="minecraft:wheat_seeds", size=1.0),
    quest("f_tiere", 0.0, 1.5, "Tiere & Zucht (Naturalist)",
          ["Eine Farm lebt von ihren Tieren. Züchte mindestens zwei Tierarten",
           "und entdecke die neuen Kreaturen von &aNaturalist&r."],
          tasks=[task_item("minecraft:wheat", 4), task_check()],
          rewards=[rew_item("minecraft:wheat", 16), coin_silver(15), rew_xp(10)],
          deps=["f_ernte"], icon="minecraft:egg", size=1.0),
    quest("f_skills", 4.0, 1.5, "Fähigkeiten (Pufferfish's Skills)",
          ["Mit &aPufferfish's Skills&r levelst du Farming, Mining, Fishing & Co.",
           "Öffne den Skill-Bildschirm und investiere deinen ersten Punkt."],
          tasks=[task_check()], rewards=[coin_gold(1), rew_xp(20)],
          deps=["f_genuss"], icon="minecraft:experience_bottle", size=1.0),
    quest("f_angeln", -2.0, 0.0, "Angeln (Aquaculture)",
          ["Am Wasser wartet eine zweite Speisekammer. Bastle eine &aAngel&r und",
           "fange ein paar Fische — mit &aAquaculture&r gibt es viele neue Arten."],
          tasks=[task_item("minecraft:fishing_rod"), task_item("minecraft:cod", 3)],
          rewards=[rew_item("farmersdelight:cooked_cod_slice", 4), coin_silver(15), rew_xp(10)],
          deps=["f_ernte"], icon="minecraft:fishing_rod", size=1.0),
]

# ---- Kapitel 2: Bauen & Gemeinschaft (gated hinter Farmen) -----------------
colony_q = [
    quest("c_supply", 0.0, 0.0, "Die erste Kolonie",
          ["Jede Zivilisation beginnt mit einem &6Versorgungslager&r. Platziere den",
           "&aSupply Camp&r, packe die Kiste aus und setze dein &aRathaus&r.",
           "", "&7Du darfst auf diesem Server §lbeliebig viele§r§7 Kolonien gründen!"],
          tasks=[task_item("minecolonies:supplycampdeployer"), task_item("minecolonies:blockhuttownhall")],
          rewards=[rew_item("minecolonies:blockhutbuilder"), coin_gold(2), rew_xp(20)],
          deps=["f_kueche"], icon="minecolonies:blockhuttownhall", size=1.5, shape="hexagon"),
    quest("c_builder", 2.0, 0.0, "Der Baumeister",
          ["Ohne Baumeister wächst keine Kolonie. Platziere die &aBuilder's Hut&r,",
           "weise einen Bürger zu und gib deinen ersten Bauauftrag."],
          tasks=[task_item("minecolonies:blockhutbuilder")],
          rewards=[rew_item("minecraft:oak_log", 32), coin_gold(2), rew_xp(15)],
          deps=["c_supply"], icon="minecolonies:blockhutbuilder", size=1.25),
    quest("c_buerger", 4.0, 0.0, "Bürger & Versorgung",
          ["Eine Kolonie lebt von ihren Bewohnern. Baue &aKüche&r und &aTaverne&r,",
           "damit gekocht und rekrutiert wird. (Verbindet sich mit deiner Farm!)"],
          tasks=[task_item("minecolonies:blockhutcook"), task_item("minecolonies:blockhuttavern"), task_check()],
          rewards=[coin_gold(3), rew_xp(20)],
          deps=["c_builder"], icon="minecolonies:blockhutcook", size=1.25),
    quest("c_mehrere", 6.0, 0.0, "Mehrere Zivilisationen",
          ["Der Server erlaubt §lunbegrenzt viele Kolonien pro Spieler§r.",
           "Gründe eine &6zweite Kolonie&r an einem anderen Ort.",
           "", "&7Mindestabstand 16 Chunks. Später verbindest du sie per Zug!"],
          tasks=[task_check()], rewards=[coin_gold(5), rew_xp(30)],
          deps=["c_buerger"], icon="minecolonies:clipboard", size=1.25),
    quest("c_bauen", 4.0, 1.5, "Schöner Bauen",
          ["Mit &aStructurize&r & &aDomum Ornamentum&r baust du frei; dazu Möbel",
           "von Macaw's & Another Furniture. Dekoriere ein Gebäude und hak ab."],
          tasks=[task_check()], rewards=[coin_silver(20), rew_xp(15)],
          deps=["c_buerger"], icon="minecraft:painting", size=1.0),
]

# ---- Kapitel 3: Technik (Create) — aufbauende KONTRAPTIONEN, nicht Einzelteile ----
# Belohnt werden die fertigen, laufenden Maschinen/Kontraptionen — nicht jedes Bauteil.
create_q = [
    quest("cr_start", 0.0, 0.0, "Die erste Maschine",
          ["&bCreate&r dreht sich um Drehkraft. Baue dein erstes &alaufendes Setup&r:",
           "ein &aWasserrad&r, das über Wellen & Zahnräder eine Maschine antreibt.",
           "", "&7Ziel ist die fertige Anlage — nicht das einzelne Zahnrad."],
          tasks=[task_item("create:water_wheel"), task_check()],
          rewards=[rew_item("create:andesite_alloy", 32), coin_gold(2), rew_xp(25)],
          deps=["c_builder"], icon="create:water_wheel", size=2.0, shape="gear"),
    quest("cr_power", -2.5, 1.5, "Mehr Schwung",
          ["Eine Maschine ist nie genug. Errichte eine &astärkere Energiequelle&r —",
           "eine &aWindmühle&r (Segel!) oder ein großes Wasserrad-Array.",
           "", "Hak ab, wenn deine Anlage spürbar mehr Stress-Kapazität hat."],
          tasks=[task_check()], rewards=[coin_gold(2), rew_xp(20)],
          deps=["cr_start"], icon="create:white_sail", size=1.25),
    quest("cr_press", 0.0, 1.5, "Pressen am Fließband",
          ["Bau eine Anlage, die &aBleche automatisch presst&r: Presse über Förderband,",
           "Material rein, fertige Sheets raus.",
           "", "&7Eine laufende Press-Straße, kein einzelnes Pressen von Hand."],
          tasks=[task_check()], rewards=[coin_gold(2), rew_xp(20)],
          deps=["cr_start"], icon="create:mechanical_press", size=1.25),
    quest("cr_processing", 0.0, 3.0, "Erz-Verarbeitung",
          ["Verdopple deine Ausbeute: baue eine &aErz-Verarbeitungs-Straße&r mit",
           "Crushing Wheels oder Mühle — Erz rein, Schrot raus, automatisch verhüttet.",
           "", "Hak ab, wenn Erz ohne Handarbeit verarbeitet wird."],
          tasks=[task_check()], rewards=[coin_gold(3), rew_xp(30)],
          deps=["cr_press"], icon="create:crushing_wheel", size=1.5, shape="hexagon"),
    quest("cr_belt", 2.5, 3.0, "Logistik mit Bändern",
          ["Items sollen sich selbst bewegen. Baue ein &aFörderband-System&r mit",
           "Trichtern/Tunneln, das Waren sortiert und transportiert.",
           "", "Eine funktionierende Sortier-/Transportlinie genügt."],
          tasks=[task_check()], rewards=[coin_gold(2), rew_xp(20)],
          deps=["cr_press"], icon="create:brass_tunnel", size=1.25),
    quest("cr_mixing", 0.0, 4.5, "Misch-Anlage",
          ["Mixer + Becken (+ Hitze) machen Legierungen & mehr in Serie. Baue eine",
           "&aautomatische Misch-Anlage&r, die z.B. Andesite Alloy am Fließband produziert."],
          tasks=[task_check()], rewards=[coin_gold(3), rew_xp(30)],
          deps=["cr_processing"], icon="create:mechanical_mixer", size=1.25),
    quest("cr_farm", 2.5, 4.5, "Automatische Farm",
          ["Schluss mit Handarbeit auf dem Acker: baue eine &aCreate-Erntemaschine&r",
           "(Mechanical Harvester/Plough auf beweglicher Kontraption), die Felder",
           "selbsttätig abfährt und erntet. &7(Perfekt mit deiner Farm-Säule!)"],
          tasks=[task_check()], rewards=[coin_gold(4), rew_xp(35)],
          deps=["cr_belt"], icon="create:mechanical_harvester", size=1.5, shape="hexagon"),
    quest("cr_contraption", -2.5, 6.0, "Die erste bewegte Kontraption",
          ["Mit Kleber, Lager & Chassis wird aus Blöcken eine &abewegliche Kontraption&r.",
           "Baue etwas, das sich dreht oder fährt — Zugbrücke, Drehturm, Aufzug …",
           "", "&7Der Moment, in dem Create wirklich magisch wird."],
          tasks=[task_check()], rewards=[coin_gold(4), rew_xp(35)],
          deps=["cr_mixing"], icon="create:mechanical_bearing", size=1.5, shape="hexagon"),
    quest("cr_autocraft", 0.0, 6.0, "Automatische Fertigung",
          ["Baue eine Anlage aus &aMechanical Crafters&r, die ein komplettes Item",
           "&avollautomatisch craftet&r — du legst die Zutaten an, der Rest passiert von selbst."],
          tasks=[task_check()], rewards=[coin_crystal(1), rew_xp(40)],
          deps=["cr_mixing"], icon="create:mechanical_crafter", size=1.25),
    quest("cr_treefarm", -2.5, 7.5, "Baumfarm",
          ["Holz für immer: baue eine &aautomatische Baumfarm&r — bewegte Kontraption",
           "mit Sägen/Bohrern, die Bäume fällt und neu pflanzt."],
          tasks=[task_check()], rewards=[coin_crystal(1), rew_xp(40)],
          deps=["cr_contraption"], icon="minecraft:oak_log", size=1.25),
    quest("cr_kitchen", 0.0, 7.5, "Automatische Küche",
          ["&aCreate: Central Kitchen&r verheiratet Create & Farmer's Delight: baue eine",
           "&aKoch-Straße&r, die Gerichte am Fließband zubereitet. Nie wieder Hunger."],
          tasks=[task_check()], rewards=[coin_crystal(1), rew_xp(40)],
          deps=["cr_autocraft"], icon="farmersdelight:cooking_pot", size=1.25),
    quest("cr_factory", 2.5, 7.5, "Fabrik-Linie",
          ["Nutze die &aFactory Gauges & Packages&r von Create 6: baue eine Linie, die",
           "ein komplexes Produkt &aauf Bestellung&r vollautomatisch herstellt und verpackt."],
          tasks=[task_check()], rewards=[coin_crystal(2), rew_xp(45)],
          deps=["cr_autocraft"], icon="create:mechanical_arm", size=1.25),
    quest("cr_energy", -4.5, 3.0, "Strom-Netz (Addons)",
          ["Bring Elektrizität ins Spiel: baue mit &aCreate New Age / Createaddition /",
           "Diesel / TFMG&r ein &aStromnetz&r, das deine Maschinen versorgt."],
          tasks=[task_check()], rewards=[coin_crystal(2), rew_xp(45)],
          deps=["cr_power"], icon="create:shaft", size=1.25),
    quest("cr_train", -4.5, 7.5, "Der erste Zug",
          ["Verlege Gleise, setze einen &aBahnhof&r und baue einen fahrenden Zug",
           "(Steam 'n' Rails). &7Bald rollt er zwischen deinen Kolonien."],
          tasks=[task_item("create:track_station"), task_check()],
          rewards=[rew_item("railways:conductor_cap"), coin_crystal(1), rew_xp(40)],
          deps=["cr_contraption"], icon="create:track_station", size=1.5, shape="hexagon"),
    quest("cr_trainnet", -4.5, 9.0, "Schienen-Netz",
          ["Mehr als eine Strecke: baue ein &aZug-Netz&r mit mehreren Stationen und",
           "&aFahrplänen&r, sodass Züge automatisch ihre Routen fahren."],
          tasks=[task_check()], rewards=[coin_crystal(2), rew_xp(45)],
          deps=["cr_train"], icon="create:schedule", size=1.25),
    quest("cr_advanced", 0.0, 10.5, "Industrie-Komplex",
          ["Führe alles zusammen: ein &agroßer, weitgehend autarker Create-Komplex&r",
           "aus Energie, Verarbeitung, Auto-Crafting, Küche und Schiene.",
           "", "&6Das Herzstück deiner Zivilisation — und Sprungbrett in die Lüfte.&r"],
          tasks=[task_check()],
          rewards=[coin_crystal(5), rew_item("create:precision_mechanism", 8), rew_xp(80)],
          deps=["cr_kitchen", "cr_factory", "cr_energy", "cr_trainnet"],
          icon="create:large_cogwheel", size=2.0, shape="gear"),
]

# ---- Kapitel 4: Aeronautics (25 Quests, gated hinter Create-Start) ---------
A = "create_aeronautics"  # nur Doku; echte ID-Namespace ist "aeronautics:"
aero_q = [
    quest("ae_intro", 0.0, 0.0, "Werde Luftfahrer",
          ["Der Himmel ruft! &bCreate Aeronautics&r lässt dich echte &dLuftschiffe&r bauen.",
           "Schnapp dir die &aAviator's Goggles&r — dein Blick für alles, was fliegt.",
           "", "&7Alpha-Mod: mach vor großen Bauten ein Backup."],
          tasks=[task_item("aeronautics:aviators_goggles")],
          rewards=[coin_gold(2), rew_xp(20)],
          deps=["cr_contraption"], icon="aeronautics:aviators_goggles", size=2.0, shape="gear"),
    quest("ae_wood_prop", 0.0, 1.5, "Der erste Propeller",
          ["Jeder Flug beginnt mit Schub. Bastle einen &aHölzernen Propeller&r —",
           "simpel, aber er dreht sich. &7Aus Holz wird Höhe."],
          tasks=[task_item("aeronautics:wooden_propeller")],
          rewards=[coin_silver(10), rew_xp(10)],
          deps=["ae_intro"], icon="aeronautics:wooden_propeller", size=1.0),
    quest("ae_andesite_prop", -1.5, 2.5, "Solider Antrieb",
          ["Der &aAndesite-Propeller&r packt mehr Schub als sein hölzerner Cousin.",
           "Mehr Drehzahl = mehr Auftrieb."],
          tasks=[task_item("aeronautics:andesite_propeller")],
          rewards=[coin_silver(15), rew_xp(10)],
          deps=["ae_wood_prop"], icon="aeronautics:andesite_propeller", size=1.0),
    quest("ae_prop_bearing", 1.5, 2.5, "Das Propellerlager",
          ["Das &aPropeller Bearing&r überträgt deine Create-Drehkraft auf den",
           "Propeller. &7Hier wird aus Zahnrädern echter Vortrieb."],
          tasks=[task_item("aeronautics:propeller_bearing")],
          rewards=[coin_silver(15), rew_xp(10)],
          deps=["ae_wood_prop"], icon="aeronautics:propeller_bearing", size=1.0),
    quest("ae_burner", 0.0, 3.0, "Heiße Luft",
          ["Der &aAdjustable Burner&r erzeugt heiße Luft — der Klassiker, um leichter",
           "als Luft zu werden. &7Heißluftballon, anyone?"],
          tasks=[task_item("aeronautics:adjustable_burner")],
          rewards=[coin_gold(1), rew_xp(15)],
          deps=["ae_prop_bearing"], icon="aeronautics:adjustable_burner", size=1.0),
    quest("ae_steam", 1.5, 4.0, "Unter Dampf",
          ["Mit dem &aSteam Vent&r nutzt du Dampfkraft für deine Flugmaschine.",
           "&7Zischt beeindruckend — und treibt an."],
          tasks=[task_item("aeronautics:steam_vent")],
          rewards=[coin_silver(15), rew_xp(10)],
          deps=["ae_burner"], icon="aeronautics:steam_vent", size=1.0),
    quest("ae_envelope", 0.0, 4.5, "Die Hülle",
          ["Eine &aEnvelope&r (Ballonhülle) hält die heiße Luft zusammen und gibt",
           "deinem Schiff Auftrieb. Gibt's in allen Farben — wähl deine Flagge!"],
          tasks=[task_item("aeronautics:white_envelope")],
          rewards=[coin_silver(15), rew_xp(10)],
          deps=["ae_burner"], icon="aeronautics:white_envelope", size=1.25),
    quest("ae_envelope_shaft", -1.5, 5.5, "Hülle trifft Technik",
          ["Der &aEnvelope Encased Shaft&r führt eine Welle sauber durch die",
           "Ballonhülle. &7Ordnung muss sein, auch in der Luft."],
          tasks=[task_item("aeronautics:white_envelope_encased_shaft")],
          rewards=[coin_silver(15), rew_xp(10)],
          deps=["ae_envelope"], icon="aeronautics:white_envelope_encased_shaft", size=1.0),
    quest("ae_big_envelope", 1.5, 5.5, "Großer Ballon",
          ["Größer fliegt besser. Sammle &e16 Envelopes&r für ein ordentliches Schiff."],
          tasks=[task_item("aeronautics:white_envelope", 16)],
          rewards=[coin_gold(1), rew_xp(15)],
          deps=["ae_envelope"], icon="aeronautics:blue_envelope", size=1.0),
    quest("ae_first_flight", 0.0, 6.0, "Der erste Auftrieb",
          ["Bau deine erste fliegende Kontraption — und sei es nur ein wackliger",
           "Heißluft-Auftrieb, der ein paar Blöcke abhebt. &7Geschichte wird geschrieben!"],
          tasks=[task_check()], rewards=[coin_gold(2), rew_xp(25)],
          deps=["ae_envelope"], icon="aeronautics:white_envelope", size=1.5, shape="hexagon"),
    quest("ae_levitite_powder", -2.5, 7.0, "Schwebe-Forschung",
          ["&aEnd Stone Powder&r ist die Basis für das schwebende Wundermaterial.",
           "&7Ein bisschen Endstein, gut zermahlen."],
          tasks=[task_item("aeronautics:end_stone_powder", 4)],
          rewards=[coin_silver(15), rew_xp(10)],
          deps=["ae_first_flight"], icon="aeronautics:end_stone_powder", size=1.0),
    quest("ae_levitite_bucket", -2.5, 8.5, "Flüssiger Auftrieb",
          ["Im &aLevitite Blend Bucket&r schwappt die Vorstufe des Schwebematerials.",
           "&7Nicht trinken."],
          tasks=[task_item("aeronautics:levitite_blend_bucket")],
          rewards=[coin_silver(15), rew_xp(10)],
          deps=["ae_levitite_powder"], icon="aeronautics:levitite_blend_bucket", size=1.0),
    quest("ae_levitite", -2.5, 10.0, "Levitite",
          ["&aLevitite&r — der Stoff, der leichter ist als der gesunde Menschenverstand",
           "es erlaubt. Damit schwebt selbst schwerer Stahl."],
          tasks=[task_item("aeronautics:levitite")],
          rewards=[coin_gold(2), rew_xp(20)],
          deps=["ae_levitite_bucket"], icon="aeronautics:levitite", size=1.25),
    quest("ae_pearl_levitite", -3.5, 11.5, "Perlglanz-Levitite",
          ["&dPearlescent Levitite&r ist die Premium-Version: mehr Auftrieb, mehr Glanz.",
           "&7Für Schiffe, die beeindrucken sollen."],
          tasks=[task_item("aeronautics:pearlescent_levitite")],
          rewards=[coin_gold(3), rew_xp(25)],
          deps=["ae_levitite"], icon="aeronautics:pearlescent_levitite", size=1.0),
    quest("ae_smart_prop", 2.0, 7.0, "Smarter Schub",
          ["Der &aSmart Propeller&r lässt sich feiner steuern — Anstellwinkel inklusive.",
           "&7Fliegen für Fortgeschrittene."],
          tasks=[task_item("aeronautics:smart_propeller")],
          rewards=[coin_gold(1), rew_xp(15)],
          deps=["ae_andesite_prop"], icon="aeronautics:smart_propeller", size=1.0),
    quest("ae_gyro", 2.0, 8.5, "Gleichgewicht",
          ["Das &aGyroscopic Propeller Bearing&r hält dein Schiff stabil in der Luft.",
           "&7Damit es nicht kippt, wenn der Kapitän niest."],
          tasks=[task_item("aeronautics:gyroscopic_propeller_bearing")],
          rewards=[coin_gold(2), rew_xp(20)],
          deps=["ae_smart_prop"], icon="aeronautics:gyroscopic_propeller_bearing", size=1.0),
    quest("ae_first_ship", 0.0, 9.0, "Dein erstes Luftschiff",
          ["Jetzt wird's ernst: baue ein richtiges, abhebendes &dLuftschiff&r mit",
           "Hülle, Antrieb und einem Platz zum Stehen.",
           "", "Hak ab, wenn dein Schiff in der Luft bleibt."],
          tasks=[task_check()], rewards=[coin_crystal(1), rew_xp(40)],
          deps=["ae_first_flight", "ae_prop_bearing"], icon="aeronautics:white_envelope",
          size=2.0, shape="gear"),
    quest("ae_potato_cannon", 2.0, 10.0, "Bordkanone (Kartoffel!)",
          ["Montiere eine &6Mounted Potato Cannon&r an dein Schiff. Verteidigung",
           "schmeckt am besten stärkehaltig. &7(Passt zum Kartoffelboss-Plan …)"],
          tasks=[task_item("aeronautics:mounted_potato_cannon")],
          rewards=[coin_gold(2), rew_xp(20)],
          deps=["ae_first_ship"], icon="aeronautics:mounted_potato_cannon", size=1.0),
    quest("ae_steer", 0.0, 10.5, "Volle Kontrolle",
          ["Setze dich ans Steuer und fliege dein Schiff kontrolliert — vor, zurück,",
           "hoch, runter. &7Mit Gyroskop bleibt alles ruhig."],
          tasks=[task_check()], rewards=[coin_gold(3), rew_xp(30)],
          deps=["ae_first_ship", "ae_gyro"], icon="aeronautics:smart_propeller", size=1.25),
    quest("ae_music", -1.5, 11.0, "Cloud Skipper",
          ["Spür die Freiheit über den Wolken. Schnapp dir die Musik-Disc",
           "&aCloud Skipper&r für die perfekte Flug-Atmosphäre."],
          tasks=[task_item("aeronautics:music_disc_cloud_skipper")],
          rewards=[coin_gold(1), rew_xp(15)],
          deps=["ae_first_ship"], icon="aeronautics:music_disc_cloud_skipper", size=1.0),
    quest("ae_high", 1.5, 12.0, "Hoch hinaus",
          ["Steig auf &eHöhe Y = 300&r oder höher. Von hier oben sieht man dank",
           "&aDistant Horizons&r die ganze Welt."],
          tasks=[task_check()], rewards=[coin_gold(3), rew_xp(30)],
          deps=["ae_steer"], icon="minecraft:spyglass", size=1.0),
    quest("ae_transport", 0.0, 12.0, "Luftfracht",
          ["Transportiere Waren per Luftschiff von einer Kolonie zur nächsten —",
           "schneller als jeder Zug über Berge. &7Logistik, aber mit Stil."],
          tasks=[task_check()], rewards=[coin_crystal(1), rew_xp(35)],
          deps=["ae_steer"], icon="minecraft:chest", size=1.25),
    quest("ae_passenger", -1.5, 12.5, "Gemeinsam abheben",
          ["Nimm einen Mitspieler an Bord und macht zusammen einen Rundflug.",
           "&7SMP-Momente, die bleiben."],
          tasks=[task_check()], rewards=[coin_gold(3), rew_xp(25)],
          deps=["ae_steer"], icon="minecraft:cake", size=1.0),
    quest("ae_armada", 0.0, 13.5, "Die kleine Flotte",
          ["Ein Schiff ist gut, drei sind eine Flotte. Baue &emehrere Luftschiffe&r",
           "und parke sie stolz über deiner Basis."],
          tasks=[task_check()], rewards=[coin_crystal(2), rew_xp(45)],
          deps=["ae_transport"], icon="aeronautics:blue_envelope", size=1.25),
    quest("ae_master", 0.0, 15.0, "Herr der Lüfte",
          ["Du hast den Himmel gezähmt: Schiffe, Steuerung, Fracht, Flotte.",
           "&6Wenige werden je so hoch hinauskommen wie du.&r"],
          tasks=[task_check()],
          rewards=[coin_crystal(4), rew_item("aeronautics:pearlescent_levitite", 4), rew_xp(60)],
          deps=["ae_armada", "ae_potato_cannon", "ae_pearl_levitite"],
          icon="aeronautics:aviators_goggles", size=2.0, shape="gear"),
]

# ---- Kapitel 5: Welt & Vernetzung (gated hinter Kolonien) ------------------
world_q = [
    quest("w_biome", 0.0, 0.0, "Entdecke die Welt",
          ["Die Welt ist riesig und realistisch: &aTerralith&r + &aTectonic&r zaubern",
           "epische Biome und Gebirge. Erkunde mindestens &e3 verschiedene&r Biome."],
          tasks=[task_check()], rewards=[rew_item("minecraft:map"), coin_silver(20), rew_xp(15)],
          deps=["cr_start"], icon="minecraft:filled_map", size=1.5, shape="hexagon"),
    quest("w_netz", 2.0, 0.0, "Das Schienennetz",
          ["Der große Traum: Zivilisationen per Zug verbinden. Verlege eine",
           "&bZugstrecke zwischen zwei Kolonien&r (Bahnhof ↔ Bahnhof)."],
          tasks=[task_check()], rewards=[coin_gold(5), rew_xp(30)],
          deps=["w_biome"], icon="create:track", size=1.25),
    quest("w_dh", 0.0, 1.5, "Weite Sicht (Distant Horizons)",
          ["&aDistant Horizons&r rendert das Gelände als LODs bis zum Horizont.",
           "&7Tipp: Für flüssiges DH empfiehlt sich der ZGC-Garbage-Collector (Java 21).",
           "Sichtweite/Qualität in den DH-Einstellungen justieren; Shader optional."],
          tasks=[task_check()], rewards=[coin_silver(10), rew_xp(10)],
          deps=["w_biome"], icon="minecraft:spyglass", size=1.0),
]

# ---- Kapitel 6: Ziele & Wirtschaft (gated hinter Welt) ---------------------
econ_q = [
    quest("e_coins", 0.0, 0.0, "Münzwirtschaft (Magic Coins)",
          ["&eMünzen&r sind der rote Faden: Quests belohnen dich mit Silber-, Gold-",
           "und Kristallmünzen. Besitze gleichzeitig mindestens &e3 Goldmünzen&r."],
          tasks=[task_item("magic_coins:gold_coin", 3)], rewards=[coin_gold(2), rew_xp(15)],
          deps=["w_biome"], icon="magic_coins:gold_coin", size=1.5, shape="hexagon"),
    quest("e_handel", 2.0, 0.0, "Handel (Create: Numismatics)",
          ["&aNumismatics&r bringt physische Münzen, Bankkarten und Automaten.",
           "Baue einen &aVendor&r und wickle einen Handel ab."],
          tasks=[task_item("numismatics:vendor"), task_item("numismatics:spur", 8)],
          rewards=[coin_gold(3), rew_xp(20)],
          deps=["e_coins"], icon="numismatics:vendor", size=1.25),
    quest("e_endgame", 4.0, 0.0, "Bereit fürs Endgame",
          ["Du hast Farm, Kolonie, Technik und Wirtschaft gemeistert.",
           "Jetzt warten im &c🏆 Endgame&r die ganz großen Ziele.",
           "", "Schließe deine erste Endgame-Quest ab!"],
          tasks=[task_check()], rewards=[coin_crystal(2), rew_xp(40)],
          deps=["e_handel"], icon="magic_coins:crystal_coin", size=1.25),
]

# ---- Kapitel 7: Endgame (gated hinter Wirtschaft + Aeronautics) ------------
endgame_q = [
    quest("x_root", 0.0, 0.0, "Der lange Weg",
          ["Du hast die Grundlagen gemeistert — jetzt beginnt das große Spiel.",
           "Hier warten die ganz großen Ziele. Werde zur &6Legende des SMP&r."],
          tasks=[task_check()], rewards=[coin_gold(5), rew_xp(30)],
          deps=["e_handel", "ae_master"], icon="minecraft:nether_star", size=2.0, shape="gear"),
    quest("x_megacolony", -3.0, -1.5, "Mega-Kolonie",
          ["Lass eine Kolonie zur Großstadt wachsen: &750+ Bürger&r und viele Gebäude."],
          tasks=[task_check()], rewards=[coin_crystal(2), rew_xp(40)],
          deps=["x_root"], icon="minecolonies:blockhuttownhall", size=1.25),
    quest("x_trainnet", -1.5, -2.5, "Schienen-Imperium",
          ["Verbinde &emindestens drei Kolonien&r zu einem Zug-Netzwerk."],
          tasks=[task_check()], rewards=[coin_crystal(2), rew_xp(40)],
          deps=["x_root"], icon="create:track_station", size=1.25),
    quest("x_aerofleet", 1.5, -2.5, "Luftschiff-Flotte",
          ["&bAeronautics&r-Meisterschaft: eine ganze Flotte großer Luftschiffe."],
          tasks=[task_check()], rewards=[coin_crystal(3), rew_xp(50)],
          deps=["x_root"], icon="aeronautics:aviators_goggles", size=1.25),
    quest("x_factory", 3.0, -1.5, "Die Großfabrik",
          ["Eine &evollautomatische Create-Fabrik&r, die ein komplexes Produkt ohne",
           "Handarbeit fertigt (Factory Gauges / Packages)."],
          tasks=[task_check()], rewards=[coin_crystal(2), rew_xp(40)],
          deps=["x_root"], icon="create:mechanical_arm", size=1.25),
    quest("x_power", 3.0, 1.5, "Energie-Imperium",
          ["Ein großes Stromnetz aus &aNew Age / Createaddition / Diesel / TFMG&r."],
          tasks=[task_check()], rewards=[coin_crystal(2), rew_xp(40)],
          deps=["x_root"], icon="create:shaft", size=1.25),
    quest("x_selfsufficient", 1.5, 2.5, "Selbstversorger",
          ["Vollautomatische Nahrung mit &aCreate: Central Kitchen&r — nie wieder Hunger."],
          tasks=[task_check()], rewards=[coin_crystal(2), rew_xp(40)],
          deps=["x_root"], icon="farmersdelight:cooking_pot", size=1.25),
    quest("x_fortune", -3.0, 1.5, "Münz-Vermögen",
          ["Besitze gleichzeitig &emindestens 5 Kristallmünzen&r — der Gipfel des Wohlstands."],
          tasks=[task_item("magic_coins:crystal_coin", 5)], rewards=[coin_crystal(3), rew_xp(40)],
          deps=["x_root"], icon="magic_coins:crystal_coin", size=1.25),
    quest("x_tradeempire", -1.5, 2.5, "Handelsimperium",
          ["Ein &aNumismatics&r-Handelsnetz mit mehreren Automaten zwischen den Kolonien."],
          tasks=[task_check()], rewards=[coin_crystal(2), rew_xp(40)],
          deps=["x_root"], icon="numismatics:vendor", size=1.25),
    quest("x_explorer", 0.0, -3.5, "Welt-Entdecker",
          ["Entdecke &e15 verschiedene Biome&r von Terralith & Tectonic."],
          tasks=[task_check()], rewards=[coin_crystal(2), rew_xp(40)],
          deps=["x_root"], icon="minecraft:filled_map", size=1.25),
    quest("x_kartoffelboss", 4.5, 0.0, "Der Kartoffelboss (geplant)",
          ["§oGeplantes Eigen-Projekt:§r ein optionaler Boss — der &6Kartoffelboss&r.",
           "Wird aktiviert, sobald die Mod fertig ist. &7Platzhalter."],
          tasks=[task_check()], rewards=[coin_crystal(1)],
          deps=["x_root"], icon="minecraft:baked_potato", size=1.0, optional=True),
    quest("x_completionist", 0.0, 4.0, "Legende des SMP",
          ["Alle großen Ziele erreicht. &6Herzlichen Glückwunsch — du bist eine Legende!&r"],
          tasks=[task_check()],
          rewards=[coin_crystal(10), rew_item("minecraft:nether_star"), rew_xp(100)],
          deps=["x_megacolony", "x_trainnet", "x_aerofleet", "x_factory", "x_power",
                "x_selfsufficient", "x_fortune", "x_tradeempire", "x_explorer"],
          icon="minecraft:nether_star", size=2.0, shape="gear"),
]


# ---- EIN Kapitel: alle Cluster versetzt zusammenführen ---------------------
def shift(qs, dx, dy):
    for q in qs:
        q["x"] = Double(float(q["x"]) + dx); q["y"] = Double(float(q["y"]) + dy)
    return qs

# Cluster-Offsets -> überschneidungsfreie Anordnung auf EINER Seite.
# Haupt-Spine vertikal: Willkommen -> Farm -> Kolonie -> (Create, großer Block) -> Welt -> Wirtschaft -> Endgame.
# Aeronautics als Seitenzweig rechts neben dem Create-Block.
all_custom = []
all_custom += shift(welcome_q, 0.0, 0.0)     # y ~ -2..2
all_custom += shift(farm_q,    0.0, 7.0)     # y ~ 7..8.5
all_custom += shift(colony_q,  0.0, 13.0)    # y ~ 13..14.5
all_custom += shift(create_q,  0.0, 18.0)    # Kontraptions-Progression: y ~ 18..28.5, x ~ -4.5..2.5
all_custom += shift(aero_q,    22.0, 19.0)   # rechts: x ~ 18.5..24, y ~ 19..34
all_custom += shift(world_q,   0.0, 42.0)    # y ~ 42..43.5
all_custom += shift(econ_q,    0.0, 48.0)    # y ~ 48..49.5
all_custom += shift(endgame_q, 0.0, 56.0)    # y ~ 52.5..60

main_chapter = {
    "default_hide_dependency_lines": False, "default_quest_shape": "",
    "filename": "questline", "group": G, "icon": item("minecraft:cake"),
    "id": CH_WELCOME, "order_index": 0, "progression_mode": "flexible",
    "quest_links": [], "title": "🌾 Cozy Farming SMP", "quests": all_custom,
}

os.makedirs(os.path.join(OUT, "chapters"), exist_ok=True)
def write(relpath, obj):
    p = os.path.join(OUT, relpath); os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f: f.write(snbt(obj) + "\n")
    print("wrote", relpath)
write("chapter_groups.snbt", chapter_groups)
write("data.snbt", data)
write("chapters/questline.snbt", main_chapter)

# alte Einzel-Kapitel entfernen (alles ist jetzt EINE Seite)
for old in ("willkommen", "farmen_und_leben", "kolonien", "create", "aeronautics", "welt", "wirtschaft", "endgame"):
    p = os.path.join(OUT, "chapters", old + ".snbt")
    if os.path.exists(p): os.remove(p); print("removed", old)

print("total ids used (generated):", _counter)
