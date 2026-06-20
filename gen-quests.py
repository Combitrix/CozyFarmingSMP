#!/usr/bin/env python3
"""Generiert die FTB-Quests-SNBT (Format verifiziert gegen FTB-Quests 1.21.1).
EIN Quest-Baum auf EINER Seite (chapters/questline.snbt), progressiv verkettet.

Regeln:
- KEINE einfachen Checkmarks als Fortschritt. Checkmark nur für reine INFO-Quests — ohne Belohnung.
- Alle Fortschritts-Quests sind Item-Tasks (werden automatisch erfasst, sobald man die Items hat).
- Endgame = viele sehr große, automatisierbare Massenziele (consume_items -> Abgabe per Quest-GUI).
"""
import os

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
def task_item(idstr, count=1, consume=False):
    d = {"id": nid(), "item": item(idstr), "type": "item"}
    if count > 1: d["count"] = Long(count)
    if consume: d["consume_items"] = True   # Massenziele: Abgabe per Quest-GUI (automatisierbar)
    return d
def task_check(): return {"id": nid(), "type": "checkmark"}   # NUR Info-Quests, ohne Belohnung
def task_dim(dim="minecraft:overworld"): return {"id": nid(), "type": "dimension", "dimension": dim}
def rew_item(idstr, count=1):
    d = {"id": nid(), "item": item(idstr), "type": "item"}
    if count > 1: d["count"] = count
    return d
def rew_xp(n): return {"id": nid(), "type": "xp", "xp": n}
# Coin-System (Magic Coins / Numismatics) entfernt -> Belohnungen jetzt als XP.
def coin_silver(n):  return rew_xp(n)
def coin_gold(n):    return rew_xp(n * 8)
def coin_crystal(n): return rew_xp(n * 20)

# ---- Quest-Helfer ----------------------------------------------------------
def quest(key, x, y, title, desc, tasks, rewards, deps=None, icon=None, shape=None, size=None, optional=False):
    q = {"id": QIDS[key], "x": Double(x), "y": Double(y), "title": title}
    if icon:     q["icon"] = item(icon)
    if shape:    q["shape"] = shape
    if size:     q["size"] = Double(size)
    if optional: q["optional"] = True
    if desc:     q["description"] = desc
    if deps:     q["dependencies"] = [QIDS[d] if d in QIDS else d for d in deps]
    q["tasks"] = tasks
    q["rewards"] = rewards
    return q

# INFO-Quest (erklärend): Checkmark, KEINE Belohnung.
def info(key, x, y, title, desc, deps=None, icon=None, size=1.0, optional=False):
    return quest(key, x, y, title, desc, tasks=[task_check()], rewards=[],
                 deps=deps, icon=icon, size=size, optional=optional)

QIDS = {}
def reg(*keys):
    for k in keys: QIDS[k] = nid()

# ---- IDs -------------------------------------------------------------------
G = nid()                 # die eine Quest-Gruppe
CH_MAIN = nid()           # das eine Kapitel

reg("w_start", "w_table", "w_emi", "w_map", "w_ipn", "w_claim", "w_info")
reg("f_ernte", "f_kueche", "f_genuss", "f_saison", "f_tiere", "f_angeln")
reg("c_supply", "c_builder", "c_buerger", "c_mehrere", "c_bauen")
reg("z_garden", "z_sugar", "z_pumpkin", "z_berries", "z_rice", "z_soil", "z_tomato", "z_salad",
    "z_pasta", "z_stew", "z_drinks", "z_cocoa", "z_pumpkinfeast", "z_dairy", "z_wool", "z_honey",
    "z_venison", "z_duck", "z_roast", "z_fish", "z_grill", "z_cannery", "z_harvester", "z_soup")
reg("ae_mass_envelope", "ae_mass_propeller", "ae_mass_pearl")
reg("cr_start", "cr_press", "cr_power", "cr_processing", "cr_belt", "cr_storage", "cr_mixing", "cr_farm",
    "cr_autocraft", "cr_contraption", "cr_energy", "cr_kitchen", "cr_factory", "cr_treefarm",
    "cr_train", "cr_trainnet", "cr_advanced")
reg("ae_intro", "ae_wood_prop", "ae_andesite_prop", "ae_prop_bearing", "ae_burner", "ae_steam",
    "ae_envelope", "ae_envelope_shaft", "ae_big_envelope", "ae_first_flight", "ae_levitite_powder",
    "ae_levitite_bucket", "ae_levitite", "ae_pearl_levitite", "ae_smart_prop", "ae_gyro",
    "ae_first_ship", "ae_potato_cannon", "ae_steer", "ae_music", "ae_high", "ae_transport",
    "ae_passenger", "ae_armada", "ae_master")
reg("w_biome", "w_dh")
reg("e_coins", "e_handel", "e_endgame")
reg("x_root", "x_andesite", "x_brass", "x_iron", "x_copper", "x_precision", "x_logs",
    "x_food", "x_levitite", "x_kartoffel", "x_coins", "x_diamonds", "x_completionist")

chapter_groups = {"chapter_groups": [{"id": G, "title": "§6🌾 Cozy Farming SMP"}]}

data = {
    "default_autoclaim_rewards": "disabled", "default_consume_items": False,
    "default_quest_disable_jei": False, "default_quest_shape": "circle",
    "default_reward_team": False, "detection_delay": 20, "disable_gui": False,
    "drop_loot_crates": False, "grid_scale": Double(0.5), "lock_message": "",
    "pause_game": False, "progression_mode": "flexible", "title": "Cozy Farming SMP", "version": 13,
}

# ============================================================================
# Cluster (jeweils Liste von Quests; Offsets werden später addiert)
# ============================================================================

# ---- Willkommen (ATM-Style: Wurzel + Info-Speichen) ------------------------
welcome_q = [
    quest("w_start", 0.0, 0.0, "Willkommen auf dem Cozy Farming SMP!",
          ["&6Hallo und herzlich willkommen!&r Schön, dass du dabei bist.",
           "Dieses Pack dreht sich um &aFarmen&r, &6Kolonien&r, &bCreate-Technik&r,",
           "&dLuftschiffe&r und ein gemütliches Leben mit Freunden.",
           "",
           "Betritt die Welt — dann baut sich der Quest-Baum nach und nach auf."],
          tasks=[task_dim("minecraft:overworld")],
          rewards=[rew_item("minecraft:bread", 4), coin_silver(10), rew_xp(10)],
          icon="minecraft:cake", size=3.0, shape="gear"),
    quest("w_table", 0.0, -2.0, "Aller Anfang",
          ["Stelle einen &aWerkbank-Tisch&r her und leg los."],
          tasks=[task_item("minecraft:crafting_table")],
          rewards=[rew_item("minecraft:oak_log", 16), coin_silver(5)],
          deps=["w_start"], icon="minecraft:crafting_table", size=1.0),
    info("w_emi", -2.0, -1.0, "Das Rezeptbuch (EMI)",
         ["&aEMI&r zeigt dir alle Rezepte: links wie etwas hergestellt wird,",
          "rechts wofür man es braucht. Klicke ein Item, um es nachzuschlagen.",
          "", "&8(Info-Quest — nur zum Lesen.)"],
         deps=["w_start"], icon="minecraft:knowledge_book"),
    info("w_map", 2.0, -1.0, "Die Karte (JourneyMap)",
         ["&aJourneyMap&r (oben rechts): Karten-Taste öffnet die Vollkarte,",
          "dort setzt du &eWegpunkte&r — praktisch für deine Kolonien.",
          "", "&8(Info-Quest.)"],
         deps=["w_start"], icon="minecraft:filled_map"),
    info("w_ipn", -2.0, 1.0, "Inventar-Komfort (Inventory Profiles Next)",
         ["Die &dlila Pfeile&r in der Hotbar gehören zu &dInventory Profiles Next&r —",
          "dem &eHotbar-Swapping&r. Wir haben sie &cstandardmäßig ausgeblendet&r,",
          "das &aFeature bleibt aber aktiv&r. Zurückholen:",
          "&71.&r Inventar öffnen → oben die IPN-Buttons.",
          "&72.&r Einstellungen → &eInventory Profiles Next&r (Taste &aO&r):",
          "   &eHotbar Swapping&r / &eShow hotbar buttons&r wieder einschalten.",
          "", "&8(Info-Quest.)"],
         deps=["w_start"], icon="minecraft:hopper"),
    info("w_claim", 2.0, 1.0, "Land sichern (FTB Chunks)",
         ["Mit &aFTB Chunks&r (Karten-Taste → Claim-Ansicht) schützt du Chunks.",
          "&7Kolonie-Chunks lädt MineColonies selbst — nicht zusätzlich force-loaden.",
          "", "&8(Info-Quest.)"],
         deps=["w_start"], icon="ftbchunks:map"),
    info("w_info", 0.0, 2.0, "Gute Reise!",
         ["Viel Spaß auf dem SMP! Baut zusammen, handelt, verbindet eure Kolonien",
          "per Zug und erobert irgendwann den Himmel.", "", "&8(Optional.)"],
         deps=["w_start"], icon="minecraft:bell", optional=True),
]

# ---- Farmen & Leben --------------------------------------------------------
farm_q = [
    quest("f_ernte", 0.0, 0.0, "Die erste Ernte",
          ["Jedes Imperium beginnt mit einem Acker. Besorge dir eine &aHacke&r",
           "und ernte deine erste Frucht."],
          tasks=[task_item("minecraft:wheat", 8), task_item("minecraft:wooden_hoe")],
          rewards=[rew_item("farmersdelight:cabbage_seeds", 3),
                   rew_item("farmersdelight:tomato_seeds", 3), coin_silver(15), rew_xp(10)],
          deps=["w_start"], icon="minecraft:wheat", size=1.5, shape="hexagon"),
    quest("f_kueche", 2.0, 0.0, "Die Küche (Farmer's Delight)",
          ["Stelle &aKochtopf&r und &aSchneidebrett&r her und koche dein erstes Gericht.",
           "&7Der Kochtopf braucht eine Hitzequelle darunter."],
          tasks=[task_item("farmersdelight:cooking_pot"), task_item("farmersdelight:cutting_board"),
                 task_item("farmersdelight:vegetable_soup")],
          rewards=[rew_item("farmersdelight:skillet"), coin_gold(1), rew_xp(15)],
          deps=["f_ernte"], icon="farmersdelight:cooking_pot", size=1.25),
    quest("f_genuss", 4.0, 0.0, "Genuss & Vielfalt",
          ["Das Pack steckt voller Lebensmittel-Mods (Vinery, Meadow, Bakery, Let's Do …).",
           "Stelle ein feines Gericht her — z.B. eine &aApfeltorte&r."],
          tasks=[task_item("farmersdelight:apple_pie")],
          rewards=[coin_silver(15), rew_xp(10)],
          deps=["f_kueche"], icon="minecraft:cake", size=1.0),
    info("f_saison", 2.0, 1.5, "Die Jahreszeiten (Serene Seasons)",
         ["Pflanzen wachsen je nach &eJahreszeit&r unterschiedlich gut.",
          "Achte auf Frühling/Sommer/Herbst und plane deine Felder.", "", "&8(Info-Quest.)"],
         deps=["f_kueche"], icon="minecraft:wheat_seeds"),
    quest("f_tiere", 0.0, 1.5, "Tiere & Zucht (Naturalist)",
          ["Eine Farm lebt von ihren Tieren. Halte Tiere und sammle ihre Erzeugnisse",
           "(Leder, Eier) — &aNaturalist&r bringt dazu viele neue Kreaturen."],
          tasks=[task_item("minecraft:leather", 8), task_item("minecraft:egg", 8)],
          rewards=[rew_item("minecraft:wheat", 16), coin_silver(15), rew_xp(10)],
          deps=["f_ernte"], icon="minecraft:egg", size=1.0),
    quest("f_angeln", -2.0, 0.0, "Angeln (Aquaculture)",
          ["Am Wasser wartet eine zweite Speisekammer. Bastle eine &aAngel&r",
           "und fange ein paar Fische."],
          tasks=[task_item("minecraft:fishing_rod"), task_item("minecraft:cod", 3)],
          rewards=[rew_item("farmersdelight:cooked_cod_slice", 4), coin_silver(15), rew_xp(10)],
          deps=["f_ernte"], icon="minecraft:fishing_rod", size=1.0),
]

# ---- Bauen & Gemeinschaft (MineColonies) -----------------------------------
colony_q = [
    quest("c_supply", 0.0, 0.0, "Die erste Kolonie",
          ["Platziere den &aSupply Camp&r, packe die Kiste aus und setze dein &aRathaus&r.",
           "&7Du darfst beliebig viele Kolonien gründen!"],
          tasks=[task_item("minecolonies:supplycampdeployer"), task_item("minecolonies:blockhuttownhall")],
          rewards=[rew_item("minecolonies:blockhutbuilder"), coin_gold(2), rew_xp(20)],
          deps=["w_start"], icon="minecolonies:blockhuttownhall", size=1.5, shape="hexagon"),
    quest("c_builder", 2.0, 0.0, "Der Baumeister",
          ["Platziere die &aBuilder's Hut&r, weise einen Bürger zu und gib einen Bauauftrag."],
          tasks=[task_item("minecolonies:blockhutbuilder")],
          rewards=[rew_item("minecraft:oak_log", 32), coin_gold(2), rew_xp(15)],
          deps=["c_supply"], icon="minecolonies:blockhutbuilder", size=1.25),
    quest("c_buerger", 4.0, 0.0, "Bürger & Versorgung",
          ["Baue &aKüche&r und &aTaverne&r, damit gekocht und rekrutiert wird.",
           "&7(Verbindet sich direkt mit deiner Farm!)"],
          tasks=[task_item("minecolonies:blockhutcook"), task_item("minecolonies:blockhuttavern")],
          rewards=[coin_gold(3), rew_xp(20)],
          deps=["c_builder"], icon="minecolonies:blockhutcook", size=1.25),
    quest("c_mehrere", 6.0, 0.0, "Mehrere Zivilisationen",
          ["Der Server erlaubt §lunbegrenzt viele Kolonien§r. Stelle ein zweites",
           "&aRathaus&r her und gründe eine weitere Kolonie (16 Chunks Abstand)."],
          tasks=[task_item("minecolonies:blockhuttownhall")],
          rewards=[coin_gold(5), rew_xp(30)],
          deps=["c_buerger"], icon="minecolonies:clipboard", size=1.25),
    quest("c_bauen", 4.0, 1.5, "Schöner Bauen",
          ["Mit &aStructurize&r & &aDomum Ornamentum&r baust du frei; dazu Möbel.",
           "Beschaffe ein paar &aGemälde&r zum Dekorieren."],
          tasks=[task_item("minecraft:painting", 4)],
          rewards=[coin_silver(20), rew_xp(15)],
          deps=["c_buerger"], icon="minecraft:painting", size=1.0),
]

# ---- Cozy / Sunlit Valley: Garten, Küche, Tiere (Stardew-Feeling) ----------
cozy_q = [
    quest("z_garden", 0.0, 0.0, "Der Gemüsegarten",
          ["Ein bunter Selbstversorger-Garten wie in Sunlit Valley. Ernte &e64 Karotten&r",
           "für die Vorratskammer. &7(HarvestCraft & Veggies bringen noch viel mehr!)"],
          tasks=[task_item("minecraft:carrot", 64)],
          rewards=[rew_item("minecraft:bone_meal", 16), coin_silver(15), rew_xp(10)],
          deps=["f_ernte"], icon="minecraft:carrot", size=1.5, shape="hexagon"),
    quest("z_sugar", 2.0, 0.0, "Süße Felder",
          ["Zuckerrohr ist die Grundzutat für Kuchen, Marmelade und Wein. Sammle &e96&r."],
          tasks=[task_item("minecraft:sugar_cane", 96)],
          rewards=[coin_silver(10), rew_xp(10)], deps=["z_garden"], icon="minecraft:sugar_cane"),
    quest("z_pumpkin", 4.0, 0.0, "Kürbiszeit",
          ["Herbststimmung: ziehe ein Kürbisbeet hoch und ernte &e16 Kürbisse&r."],
          tasks=[task_item("minecraft:pumpkin", 16)],
          rewards=[coin_silver(10), rew_xp(10)], deps=["z_garden"], icon="minecraft:pumpkin"),
    quest("z_berries", -2.0, 0.0, "Beeren für die Speisekammer",
          ["Wildernte am Wegesrand: sammle &e32 Süße Beeren&r."],
          tasks=[task_item("minecraft:sweet_berries", 32)],
          rewards=[coin_silver(10), rew_xp(10)], deps=["z_garden"], icon="minecraft:sweet_berries"),
    quest("z_rice", -2.0, 1.5, "Reisterrassen",
          ["Reis wächst am Wasser. Lege ein bewässertes Feld an und ernte",
           "&e48 Reis-Rispen&r."],
          tasks=[task_item("farmersdelight:rice_panicle", 48)],
          rewards=[coin_silver(15), rew_xp(10)], deps=["z_garden"], icon="farmersdelight:rice_panicle"),
    quest("z_soil", 0.0, 1.5, "Reicher Boden",
          ["Das zentrale Cozy-Farming-Upgrade: stelle &aOrganischen Kompost&r her und",
           "veredle deinen Acker zu &e16 Reicher Erde&r (schnelleres Wachstum, kein Bewässern)."],
          tasks=[task_item("farmersdelight:rich_soil", 16)],
          rewards=[rew_item("farmersdelight:rich_soil", 16), coin_gold(1), rew_xp(15)],
          deps=["z_garden"], icon="farmersdelight:rich_soil"),
    quest("z_honey", -4.0, 1.5, "Honig vom eigenen Bienenstock",
          ["Bienen sind ein cozy Klassiker — und bestäuben deine Felder. Ernte",
           "&e8 Honigflaschen&r."],
          tasks=[task_item("minecraft:honey_bottle", 8)],
          rewards=[coin_silver(15), rew_xp(10)], deps=["z_garden"], icon="minecraft:honey_bottle"),
    quest("z_drinks", 2.0, 1.5, "Hofladen-Getränke",
          ["Presse &e4 Apfelmost&r für den Marktstand. &7(Auch Melonensaft & Co. lohnen sich.)"],
          tasks=[task_item("farmersdelight:apple_cider", 4)],
          rewards=[coin_silver(15), rew_xp(10)], deps=["z_sugar"], icon="farmersdelight:apple_cider"),
    quest("z_pumpkinfeast", 4.0, 1.5, "Erntedank-Bankett",
          ["Krönung der Herbst-Linie: fülle und backe einen &aGefüllten Kürbis&r."],
          tasks=[task_item("farmersdelight:stuffed_pumpkin", 1)],
          rewards=[coin_gold(1), rew_xp(15)], deps=["z_pumpkin"], icon="farmersdelight:stuffed_pumpkin"),
    quest("z_fish", -4.0, 3.0, "Der Dorfteich (Aquaculture)",
          ["Bastle ein &aFiletmesser&r und filetiere deine Fänge zu Filets."],
          tasks=[task_item("aquaculture:iron_fillet_knife", 1)],
          rewards=[coin_silver(10), rew_xp(10)], deps=["z_garden"], icon="aquaculture:iron_fillet_knife"),
    quest("z_tomato", 0.0, 3.0, "Tomatensauce einkochen",
          ["Verarbeite deine Tomaten weiter: koche &e8 Gläser Tomatensauce&r — Basis",
           "für die Pasta-Linie."],
          tasks=[task_item("farmersdelight:tomato_sauce", 8)],
          rewards=[coin_silver(15), rew_xp(10)], deps=["z_soil"], icon="farmersdelight:tomato_sauce", size=1.25),
    quest("z_salad", 2.0, 3.0, "Frischer Salat vom Beet",
          ["Hacke dein Gemüse am Schneidebrett und richte &e4 Bunte Salate&r an."],
          tasks=[task_item("farmersdelight:mixed_salad", 4)],
          rewards=[coin_silver(15), rew_xp(10)], deps=["z_tomato"], icon="farmersdelight:mixed_salad"),
    quest("z_pasta", -2.0, 3.0, "Pasta-Abend",
          ["Mehrstufiges Rezept: Nudelteig → rohe Pasta → &e4 Pasta mit Hackbällchen&r.",
           "Gemütliches Dinner!"],
          tasks=[task_item("farmersdelight:pasta_with_meatballs", 4)],
          rewards=[coin_gold(1), rew_xp(15)], deps=["z_tomato"], icon="farmersdelight:pasta_with_meatballs"),
    quest("z_stew", 4.0, 3.0, "Eintopf-Küche",
          ["Comfort Food: koche einen &aRindereintopf&r (auch Hühnersuppe & Fischeintopf",
           "lohnen sich)."],
          tasks=[task_item("farmersdelight:beef_stew", 1)],
          rewards=[coin_silver(15), rew_xp(10)], deps=["z_tomato"], icon="farmersdelight:beef_stew"),
    quest("z_grill", -4.0, 4.5, "Fisch vom Grill",
          ["Brate &e4 gegrillte Lachse&r über dem Lagerfeuer."],
          tasks=[task_item("farmersdelight:grilled_salmon", 4)],
          rewards=[coin_silver(15), rew_xp(10)], deps=["z_fish"], icon="farmersdelight:grilled_salmon"),
    quest("z_cocoa", 2.0, 4.5, "Eine Kanne heißer Kakao",
          ["Reine Wohlfühl-Quest: braue &e4 Tassen heißen Kakao&r für kalte Winterabende."],
          tasks=[task_item("farmersdelight:hot_cocoa", 4)],
          rewards=[coin_silver(15), rew_xp(10)], deps=["z_drinks"], icon="farmersdelight:hot_cocoa"),
    quest("z_dairy", -2.0, 4.5, "Die kleine Molkerei",
          ["Halte Kühe und melke &e8 Flaschen Milch&r — Basis für Käse, Butter, Desserts.",
           "&7(Brücke zu Let's Do: Meadow.)"],
          tasks=[task_item("farmersdelight:milk_bottle", 8)],
          rewards=[coin_silver(15), rew_xp(10)], deps=["z_garden"], icon="farmersdelight:milk_bottle"),
    quest("z_wool", -4.0, 6.0, "Wollige Mitbewohner",
          ["Züchte eine Schafherde und schere &e24 Wolle&r für gemütliche Deko."],
          tasks=[task_item("minecraft:white_wool", 24)],
          rewards=[coin_silver(15), rew_xp(10)], deps=["z_dairy"], icon="minecraft:white_wool"),
    quest("z_venison", -2.0, 6.0, "Wild aus dem Wald (Naturalist)",
          ["Beziehe von Naturalist-Hirschen &e6 Wildbret&r für die Küche."],
          tasks=[task_item("naturalist:venison", 6)],
          rewards=[coin_silver(15), rew_xp(10)], deps=["z_dairy"], icon="naturalist:venison"),
    quest("z_duck", 0.0, 6.0, "Ententeich",
          ["Niedlicher Teich-Vibe: sammle &e8 Enteneier&r von Naturalist-Enten."],
          tasks=[task_item("naturalist:duck_egg", 8)],
          rewards=[coin_silver(15), rew_xp(10)], deps=["z_dairy"], icon="naturalist:duck_egg"),
    quest("z_roast", 2.0, 6.0, "Sonntagsbraten",
          ["Festmahl: brate ein ganzes &aHähnchen am Spieß&r."],
          tasks=[task_item("farmersdelight:roast_chicken", 1)],
          rewards=[coin_gold(1), rew_xp(20)], deps=["z_duck"], icon="farmersdelight:roast_chicken", size=1.25),
    # --- Cozy-Automation (Create-Verzahnung, große Mengen, consume) ---
    quest("z_harvester", -2.0, 7.5, "Große Erntemaschine",
          ["Lass Create für dich ackern: liefere &e1.000 Weizen&r von einer",
           "automatischen Farm. &7(Mechanical Harvester + Reicher Boden.)"],
          tasks=[task_item("minecraft:wheat", 1000, consume=True)],
          rewards=[coin_gold(3), rew_xp(35)], deps=["z_soil", "cr_farm"],
          icon="create:mechanical_harvester", size=1.25),
    quest("z_cannery", 0.0, 7.5, "Konservenfabrik",
          ["Cozy trifft Industrie: produziere &e256 Tomatensauce&r vollautomatisch",
           "(Auto-Crafting + Central Kitchen)."],
          tasks=[task_item("farmersdelight:tomato_sauce", 256, consume=True)],
          rewards=[coin_gold(3), rew_xp(35)], deps=["z_tomato", "cr_autocraft"],
          icon="farmersdelight:tomato_sauce", size=1.25),
    quest("z_soup", 2.0, 7.5, "Suppenküche fürs Dorf",
          ["Speise das ganze Dorf: liefere &e32 Nudelsuppen&r aus der Großküche."],
          tasks=[task_item("farmersdelight:noodle_soup", 32, consume=True)],
          rewards=[coin_gold(2), rew_xp(30)], deps=["z_stew"], icon="farmersdelight:noodle_soup"),
]

# ---- Technik (Create): aufbauende KONTRAPTIONEN, per Schlüssel-Maschine erfasst ----
create_q = [
    quest("cr_start", 0.0, 0.0, "Die erste Maschine",
          ["&bCreate&r dreht sich um Drehkraft. Baue ein &aWasserrad&r, das über",
           "Wellen & Zahnräder Maschinen antreibt. &7(2 Wasserräder = solides Setup.)"],
          tasks=[task_item("create:water_wheel", 2)],
          rewards=[rew_item("create:andesite_alloy", 32), coin_gold(2), rew_xp(25)],
          deps=["c_builder"], icon="create:water_wheel", size=2.0, shape="gear"),
    quest("cr_power", -2.5, 1.5, "Mehr Schwung",
          ["Eine stärkere Energiequelle muss her: baue eine &aWindmühle&r",
           "(Lager + Segel) für ordentlich Stress-Kapazität."],
          tasks=[task_item("create:windmill_bearing"), task_item("create:white_sail", 8)],
          rewards=[coin_gold(2), rew_xp(20)],
          deps=["cr_start"], icon="create:white_sail", size=1.25),
    quest("cr_press", 0.0, 1.5, "Pressen am Fließband",
          ["Die &aMechanische Presse&r plättet, prägt und presst. Bau eine Press-Straße."],
          tasks=[task_item("create:mechanical_press")],
          rewards=[coin_gold(2), rew_xp(20)],
          deps=["cr_start"], icon="create:mechanical_press", size=1.25),
    quest("cr_processing", 0.0, 3.0, "Erz-Verarbeitung",
          ["Verdopple deine Ausbeute: &aCrushing Wheels&r zermahlen Erz automatisch.",
           "&7(Kommen immer im Paar.)"],
          tasks=[task_item("create:crushing_wheel", 2)],
          rewards=[coin_gold(3), rew_xp(30)],
          deps=["cr_press"], icon="create:crushing_wheel", size=1.5, shape="hexagon"),
    quest("cr_belt", 2.5, 3.0, "Logistik mit Bändern",
          ["Items bewegen sich selbst: &aFörderbänder&r + &aMessing-Tunnel&r sortieren",
           "und transportieren deine Waren."],
          tasks=[task_item("create:belt_connector", 4), task_item("create:brass_tunnel")],
          rewards=[coin_gold(2), rew_xp(20)],
          deps=["cr_press"], icon="create:brass_tunnel", size=1.25),
    quest("cr_storage", 4.5, 3.0, "Das Lager",
          ["Ordnung muss sein: baue ein zentrales &aWarenlager&r aus &aItem Vaults&r.",
           "Per Trichter/Förderband befüllt, gibt dir eines deiner Maschinen-Outputs sauber",
           "sortiert wieder aus — das Herz jeder Create-Basis.",
           "", "&7Tipp: Vaults lassen sich zu riesigen Lagerblöcken zusammenbauen."],
          tasks=[task_item("create:item_vault", 4)],
          rewards=[coin_gold(1), rew_xp(20)],
          deps=["cr_belt"], icon="create:item_vault", size=1.25),
    quest("cr_mixing", 0.0, 4.5, "Misch-Anlage",
          ["&aMixer&r + &aBecken&r mischen Legierungen in Serie — z.B. Andesite Alloy",
           "am Fließband."],
          tasks=[task_item("create:mechanical_mixer"), task_item("create:basin")],
          rewards=[coin_gold(3), rew_xp(30)],
          deps=["cr_processing"], icon="create:mechanical_mixer", size=1.25),
    quest("cr_farm", 2.5, 4.5, "Automatische Farm",
          ["Schluss mit Handarbeit: der &aMechanical Harvester&r erntet deine Felder",
           "selbsttätig. &7(Perfekt mit deiner Farm-Säule!)"],
          tasks=[task_item("create:mechanical_harvester")],
          rewards=[coin_gold(4), rew_xp(35)],
          deps=["cr_belt"], icon="create:mechanical_harvester", size=1.5, shape="hexagon"),
    quest("cr_contraption", -2.5, 6.0, "Die erste bewegte Kontraption",
          ["Mit &aKleber&r & &aLager&r wird aus Blöcken eine bewegliche Kontraption —",
           "Zugbrücke, Drehturm, Aufzug … &7Hier wird Create magisch."],
          tasks=[task_item("create:mechanical_bearing"), task_item("create:super_glue")],
          rewards=[coin_gold(4), rew_xp(35)],
          deps=["cr_mixing"], icon="create:mechanical_bearing", size=1.5, shape="hexagon"),
    quest("cr_autocraft", 0.0, 6.0, "Automatische Fertigung",
          ["Baue eine Anlage aus &aMechanical Crafters&r, die ein Item vollautomatisch",
           "fertigt. &7(8 Crafter sind ein guter Start.)"],
          tasks=[task_item("create:mechanical_crafter", 8)],
          rewards=[coin_crystal(1), rew_xp(40)],
          deps=["cr_mixing"], icon="create:mechanical_crafter", size=1.25),
    quest("cr_treefarm", -2.5, 7.5, "Baumfarm",
          ["Holz für immer: baue eine &aautomatische Baumfarm&r.",
           "&7Liefere &e1.000 Holz&r ab — das schafft nur Automatisierung."],
          tasks=[task_item("minecraft:oak_log", 1000)],
          rewards=[coin_crystal(1), rew_xp(40)],
          deps=["cr_contraption"], icon="minecraft:oak_log", size=1.25),
    quest("cr_kitchen", 0.0, 7.5, "Automatische Küche",
          ["&aCreate: Central Kitchen&r kocht am Fließband. Produziere &e128 Reis&r",
           "vollautomatisch."],
          tasks=[task_item("farmersdelight:cooked_rice", 128)],
          rewards=[coin_crystal(1), rew_xp(40)],
          deps=["cr_autocraft"], icon="farmersdelight:cooking_pot", size=1.25),
    quest("cr_factory", 2.5, 7.5, "Fabrik-Linie",
          ["Nutze &aMechanical Arms&r & die Factory-/Package-Features von Create 6 für",
           "eine Produktionslinie auf Bestellung."],
          tasks=[task_item("create:mechanical_arm", 2)],
          rewards=[coin_crystal(2), rew_xp(45)],
          deps=["cr_autocraft"], icon="create:mechanical_arm", size=1.25),
    quest("cr_energy", -4.5, 3.0, "Strom-Netz (Createaddition)",
          ["Bring Elektrizität ins Spiel: ein &aAlternator&r erzeugt FE aus Drehkraft,",
           "ein &aCapacitor&r speichert sie. Baue dein erstes Stromnetz."],
          tasks=[task_item("createaddition:alternator"), task_item("createaddition:capacitor")],
          rewards=[coin_crystal(2), rew_xp(45)],
          deps=["cr_power"], icon="createaddition:alternator", size=1.25),
    quest("cr_train", -4.5, 7.5, "Der erste Zug",
          ["Verlege Gleise, setze einen &aBahnhof&r und baue einen fahrenden Zug",
           "(Steam 'n' Rails)."],
          tasks=[task_item("create:track_station"), task_item("create:track", 32)],
          rewards=[rew_item("railways:conductor_cap"), coin_crystal(1), rew_xp(40)],
          deps=["cr_contraption"], icon="create:track_station", size=1.5, shape="hexagon"),
    quest("cr_trainnet", -4.5, 9.0, "Schienen-Netz",
          ["Baue ein &aZug-Netz&r mit mehreren Bahnhöfen und &aFahrplänen&r,",
           "sodass Züge automatisch fahren. &7(3 Stationen + Fahrplan.)"],
          tasks=[task_item("create:track_station", 3), task_item("create:schedule")],
          rewards=[coin_crystal(2), rew_xp(45)],
          deps=["cr_train"], icon="create:schedule", size=1.25),
    quest("cr_advanced", 0.0, 10.5, "Industrie-Komplex",
          ["Führe alles zusammen. Als Nachweis deines Maschinenparks: fertige",
           "&e256 Precision Mechanisms&r — Herzstück fortgeschrittener Geräte.",
           "", "&6Das Sprungbrett in die Lüfte und ins Endgame.&r"],
          tasks=[task_item("create:precision_mechanism", 256)],
          rewards=[coin_crystal(5), rew_item("create:precision_mechanism", 16), rew_xp(80)],
          deps=["cr_kitchen", "cr_factory", "cr_energy", "cr_trainnet"],
          icon="create:large_cogwheel", size=2.0, shape="gear"),
]

# ---- Aeronautics (Material-/Bau-Ziele, automatisch erfasst) ----------------
aero_q = [
    quest("ae_intro", 0.0, 0.0, "Werde Luftfahrer",
          ["Der Himmel ruft! &bCreate Aeronautics&r lässt dich echte &dLuftschiffe&r bauen.",
           "Schnapp dir die &aAviator's Goggles&r. &7(Alpha-Mod: Backups!)"],
          tasks=[task_item("aeronautics:aviators_goggles")],
          rewards=[coin_gold(2), rew_xp(20)],
          deps=["cr_contraption"], icon="aeronautics:aviators_goggles", size=2.0, shape="gear"),
    quest("ae_wood_prop", 0.0, 1.5, "Der erste Propeller",
          ["Jeder Flug beginnt mit Schub. Bastle einen &aHölzernen Propeller&r."],
          tasks=[task_item("aeronautics:wooden_propeller")],
          rewards=[coin_silver(10), rew_xp(10)],
          deps=["ae_intro"], icon="aeronautics:wooden_propeller"),
    quest("ae_andesite_prop", -1.5, 2.5, "Solider Antrieb",
          ["Der &aAndesite-Propeller&r packt mehr Schub. Mehr Drehzahl = mehr Auftrieb."],
          tasks=[task_item("aeronautics:andesite_propeller")],
          rewards=[coin_silver(15), rew_xp(10)],
          deps=["ae_wood_prop"], icon="aeronautics:andesite_propeller"),
    quest("ae_prop_bearing", 1.5, 2.5, "Das Propellerlager",
          ["Das &aPropeller Bearing&r überträgt Create-Drehkraft auf den Propeller."],
          tasks=[task_item("aeronautics:propeller_bearing")],
          rewards=[coin_silver(15), rew_xp(10)],
          deps=["ae_wood_prop"], icon="aeronautics:propeller_bearing"),
    quest("ae_burner", 0.0, 3.0, "Heiße Luft",
          ["Der &aAdjustable Burner&r erzeugt heiße Luft — leichter als Luft werden!"],
          tasks=[task_item("aeronautics:adjustable_burner")],
          rewards=[coin_gold(1), rew_xp(15)],
          deps=["ae_prop_bearing"], icon="aeronautics:adjustable_burner"),
    quest("ae_steam", 1.5, 4.0, "Unter Dampf",
          ["Mit dem &aSteam Vent&r nutzt du Dampfkraft für deine Flugmaschine."],
          tasks=[task_item("aeronautics:steam_vent")],
          rewards=[coin_silver(15), rew_xp(10)],
          deps=["ae_burner"], icon="aeronautics:steam_vent"),
    quest("ae_envelope", 0.0, 4.5, "Die Hülle",
          ["Eine &aEnvelope&r (Ballonhülle) gibt Auftrieb. Gibt's in allen Farben!"],
          tasks=[task_item("aeronautics:white_envelope")],
          rewards=[coin_silver(15), rew_xp(10)],
          deps=["ae_burner"], icon="aeronautics:white_envelope", size=1.25),
    quest("ae_envelope_shaft", -1.5, 5.5, "Hülle trifft Technik",
          ["Der &aEnvelope Encased Shaft&r führt eine Welle sauber durch die Hülle."],
          tasks=[task_item("aeronautics:white_envelope_encased_shaft")],
          rewards=[coin_silver(15), rew_xp(10)],
          deps=["ae_envelope"], icon="aeronautics:white_envelope_encased_shaft"),
    quest("ae_big_envelope", 1.5, 5.5, "Großer Ballon",
          ["Größer fliegt besser. Sammle &e16 Envelopes&r für ein ordentliches Schiff."],
          tasks=[task_item("aeronautics:white_envelope", 16)],
          rewards=[coin_gold(1), rew_xp(15)],
          deps=["ae_envelope"], icon="aeronautics:blue_envelope"),
    quest("ae_first_flight", 0.0, 6.0, "Der erste Auftrieb",
          ["Stelle die Bauteile für deinen ersten Heißluft-Auftrieb zusammen:",
           "Hülle + Brenner. &7Dann ab in die Luft!"],
          tasks=[task_item("aeronautics:white_envelope", 4), task_item("aeronautics:adjustable_burner")],
          rewards=[coin_gold(2), rew_xp(25)],
          deps=["ae_envelope"], icon="aeronautics:white_envelope", size=1.5, shape="hexagon"),
    quest("ae_levitite_powder", -2.5, 7.0, "Schwebe-Forschung",
          ["&aEnd Stone Powder&r ist die Basis des schwebenden Wundermaterials."],
          tasks=[task_item("aeronautics:end_stone_powder", 4)],
          rewards=[coin_silver(15), rew_xp(10)],
          deps=["ae_first_flight"], icon="aeronautics:end_stone_powder"),
    quest("ae_levitite_bucket", -2.5, 8.5, "Flüssiger Auftrieb",
          ["Im &aLevitite Blend Bucket&r schwappt die Vorstufe. &7Nicht trinken."],
          tasks=[task_item("aeronautics:levitite_blend_bucket")],
          rewards=[coin_silver(15), rew_xp(10)],
          deps=["ae_levitite_powder"], icon="aeronautics:levitite_blend_bucket"),
    quest("ae_levitite", -2.5, 10.0, "Levitite",
          ["&aLevitite&r — leichter als der gesunde Menschenverstand erlaubt.",
           "Damit schwebt selbst schwerer Stahl."],
          tasks=[task_item("aeronautics:levitite", 8)],
          rewards=[coin_gold(2), rew_xp(20)],
          deps=["ae_levitite_bucket"], icon="aeronautics:levitite", size=1.25),
    quest("ae_pearl_levitite", -3.5, 11.5, "Perlglanz-Levitite",
          ["&dPearlescent Levitite&r: mehr Auftrieb, mehr Glanz — für Schiffe mit Stil."],
          tasks=[task_item("aeronautics:pearlescent_levitite", 4)],
          rewards=[coin_gold(3), rew_xp(25)],
          deps=["ae_levitite"], icon="aeronautics:pearlescent_levitite"),
    quest("ae_smart_prop", 2.0, 7.0, "Smarter Schub",
          ["Der &aSmart Propeller&r lässt sich fein steuern — Anstellwinkel inklusive."],
          tasks=[task_item("aeronautics:smart_propeller")],
          rewards=[coin_gold(1), rew_xp(15)],
          deps=["ae_andesite_prop"], icon="aeronautics:smart_propeller"),
    quest("ae_gyro", 2.0, 8.5, "Gleichgewicht",
          ["Das &aGyroscopic Propeller Bearing&r hält dein Schiff stabil in der Luft."],
          tasks=[task_item("aeronautics:gyroscopic_propeller_bearing")],
          rewards=[coin_gold(2), rew_xp(20)],
          deps=["ae_smart_prop"], icon="aeronautics:gyroscopic_propeller_bearing"),
    quest("ae_first_ship", 0.0, 9.0, "Dein erstes Luftschiff",
          ["Zeit für ein echtes Schiff! Beschaffe die Kernteile — Lager + reichlich Hülle —",
           "und bau dein erstes abhebendes &dLuftschiff&r."],
          tasks=[task_item("aeronautics:propeller_bearing", 2), task_item("aeronautics:white_envelope", 8)],
          rewards=[coin_crystal(1), rew_xp(40)],
          deps=["ae_first_flight", "ae_prop_bearing"], icon="aeronautics:white_envelope",
          size=2.0, shape="gear"),
    quest("ae_potato_cannon", 2.0, 10.0, "Bordkanone (Kartoffel!)",
          ["Montiere eine &6Mounted Potato Cannon&r. Verteidigung schmeckt stärkehaltig.",
           "&7(Passt zum Kartoffelboss-Plan …)"],
          tasks=[task_item("aeronautics:mounted_potato_cannon")],
          rewards=[coin_gold(2), rew_xp(20)],
          deps=["ae_first_ship"], icon="aeronautics:mounted_potato_cannon"),
    quest("ae_steer", 0.0, 10.5, "Volle Kontrolle",
          ["Für ruhiges, präzises Fliegen: &aSmart Propeller&r + &aGyroskop&r ans Schiff."],
          tasks=[task_item("aeronautics:smart_propeller", 2),
                 task_item("aeronautics:gyroscopic_propeller_bearing")],
          rewards=[coin_gold(3), rew_xp(30)],
          deps=["ae_first_ship", "ae_gyro"], icon="aeronautics:smart_propeller", size=1.25),
    quest("ae_music", -1.5, 11.0, "Cloud Skipper",
          ["Spür die Freiheit über den Wolken: die Musik-Disc &aCloud Skipper&r."],
          tasks=[task_item("aeronautics:music_disc_cloud_skipper")],
          rewards=[coin_gold(1), rew_xp(15)],
          deps=["ae_first_ship"], icon="aeronautics:music_disc_cloud_skipper"),
    quest("ae_high", 1.5, 12.0, "Hoch hinaus",
          ["Für große Höhe braucht's viel Auftrieb: beschaffe reichlich",
           "&dPearlescent Levitite&r und steig auf."],
          tasks=[task_item("aeronautics:pearlescent_levitite", 8)],
          rewards=[coin_gold(3), rew_xp(30)],
          deps=["ae_steer"], icon="minecraft:spyglass"),
    quest("ae_transport", 0.0, 12.0, "Luftfracht",
          ["Rüste ein Frachtschiff aus — viel Hülle für viel Last.",
           "&7Schneller als jeder Zug über Berge."],
          tasks=[task_item("aeronautics:white_envelope", 32)],
          rewards=[coin_crystal(1), rew_xp(35)],
          deps=["ae_steer"], icon="minecraft:chest", size=1.25),
    quest("ae_passenger", -1.5, 12.5, "Gemeinsam abheben",
          ["Bau Sitzplätze ein und nimm Mitspieler an Bord. &7SMP-Momente!"],
          tasks=[task_item("create:blue_seat", 2)],
          rewards=[coin_gold(3), rew_xp(25)],
          deps=["ae_steer"], icon="create:blue_seat"),
    quest("ae_armada", 0.0, 13.5, "Die kleine Flotte",
          ["Ein Schiff ist gut, drei sind eine Flotte. Beschaffe Material für mehrere",
           "Schiffe: &e8 Lager + 48 Hüllen&r."],
          tasks=[task_item("aeronautics:propeller_bearing", 8), task_item("aeronautics:white_envelope", 48)],
          rewards=[coin_crystal(2), rew_xp(45)],
          deps=["ae_transport"], icon="aeronautics:blue_envelope", size=1.25),
    quest("ae_master", 0.0, 15.0, "Herr der Lüfte",
          ["Du hast den Himmel gezähmt. Als Krönung: ein Schatz an &dPearlescent",
           "Levitite&r und &aSmart Propellers&r für die ultimative Flotte."],
          tasks=[task_item("aeronautics:pearlescent_levitite", 32),
                 task_item("aeronautics:smart_propeller", 16)],
          rewards=[coin_crystal(4), rew_item("aeronautics:pearlescent_levitite", 8), rew_xp(60)],
          deps=["ae_armada", "ae_potato_cannon", "ae_pearl_levitite"],
          icon="aeronautics:aviators_goggles", size=2.0, shape="gear"),
    # --- Aeronautics-Massenproduktion (automatisierbar, consume) ---
    quest("ae_mass_envelope", -2.0, 16.5, "Hüllen-Manufaktur",
          ["Eine Werft braucht Stoff ohne Ende: fertige &e10.000 Envelopes&r",
           "vollautomatisch."],
          tasks=[task_item("aeronautics:white_envelope", 10000, consume=True)],
          rewards=[coin_crystal(8), rew_xp(80)],
          deps=["ae_master"], icon="aeronautics:white_envelope", size=1.25),
    quest("ae_mass_propeller", 0.0, 16.5, "Propeller-Fließband",
          ["Schub für eine ganze Armada: produziere &e2.000 Smart Propellers&r."],
          tasks=[task_item("aeronautics:smart_propeller", 2000, consume=True)],
          rewards=[coin_crystal(10), rew_xp(90)],
          deps=["ae_master"], icon="aeronautics:smart_propeller", size=1.25),
    quest("ae_mass_pearl", 2.0, 16.5, "Levitite-Großwerk",
          ["Auftrieb im Industriemaßstab: stelle &e2.000 Pearlescent Levitite&r her."],
          tasks=[task_item("aeronautics:pearlescent_levitite", 2000, consume=True)],
          rewards=[coin_crystal(12), rew_xp(100)],
          deps=["ae_master"], icon="aeronautics:pearlescent_levitite", size=1.25),
]

# ---- Welt: nur Info (keine Belohnung) --------------------------------------
world_q = [
    info("w_biome", 0.0, 0.0, "Die große Welt (Terralith + Tectonic)",
         ["Die Welt ist riesig und realistisch: epische Biome und Gebirge.",
          "Erkunde sie, setze Wegpunkte und finde schöne Kolonie-Plätze.",
          "", "&8(Info-Quest.)"],
         deps=["w_start"], icon="minecraft:filled_map", size=1.5),
    info("w_dh", 0.0, 1.5, "Weite Sicht (Distant Horizons)",
         ["&aDistant Horizons&r rendert das Gelände als LODs bis zum Horizont.",
          "&7Tipp: Für flüssiges DH den ZGC-GC nutzen (Java 21); Chunky kann LOD-Löcher",
          "verursachen — dann DHs Distant-Generator nutzen oder DH-CPU-Threads erhöhen.",
          "", "&8(Info-Quest.)"],
         deps=["w_biome"], icon="minecraft:spyglass"),
]

# ---- Ziele & Wirtschaft ----------------------------------------------------
econ_q = [
    quest("e_coins", 0.0, 0.0, "Handel mit Dorfbewohnern",
          ["&eSmaragde&r sind die Währung des Dorfs. Handle mit Villagern und",
           "besitze mindestens &e16 Smaragde&r.",
           "&7Mit Easy Villagers & Trade Cycling baust du dir Handelshallen."],
          tasks=[task_item("minecraft:emerald", 16)],
          rewards=[rew_xp(15)],
          deps=["w_biome"], icon="minecraft:emerald", size=1.5, shape="hexagon"),
    quest("e_handel", 2.0, 0.0, "Der Marktplatz",
          ["Baue dir eine Handelshalle. Sammle &e3 Smaragdblöcke&r aus dem Handel."],
          tasks=[task_item("minecraft:emerald_block", 3)],
          rewards=[rew_xp(20)],
          deps=["e_coins"], icon="minecraft:emerald_block", size=1.25),
    quest("e_endgame", 4.0, 0.0, "Reich werden",
          ["Wohlstand will erarbeitet sein. Häufe &e8 Smaragdblöcke&r an —",
           "und mach dich bereit fürs &cEndgame&r."],
          tasks=[task_item("minecraft:emerald_block", 8)],
          rewards=[rew_xp(40)],
          deps=["e_handel"], icon="minecraft:emerald_block", size=1.25),
]

# ---- Endgame: große, automatisierbare Massenziele (consume) ----------------
endgame_q = [
    quest("x_root", 0.0, 0.0, "Tor zum Endgame",
          ["Du hast Farm, Kolonie, Maschinen, Schiene und Himmel gemeistert.",
           "Jetzt zählt nur noch &cMassenproduktion&r. Zur Einstimmung: liefere",
           "&e64 Precision Mechanisms&r ab.",
           "", "&7Alle Endgame-Ziele gibst du im Quest-Buch ab (Rechtsklick) —",
           "&7produziere sie also vollautomatisch."],
          tasks=[task_item("create:precision_mechanism", 64, consume=True)],
          rewards=[coin_crystal(5), rew_xp(50)],
          deps=["e_endgame", "ae_master", "cr_advanced"],
          icon="create:precision_mechanism", size=2.0, shape="gear"),
    quest("x_andesite", -3.5, -2.0, "Andesit-Industrie",
          ["Das Fundament von Create im großen Stil: liefere &e50.000 Andesite Alloy&r."],
          tasks=[task_item("create:andesite_alloy", 50000, consume=True)],
          rewards=[coin_crystal(10), rew_xp(80)],
          deps=["x_root"], icon="create:andesite_alloy", size=1.25),
    quest("x_brass", -1.8, -3.0, "Messing-Werk",
          ["Messing ist die Mittelstufe — also brauchst du davon &eviel&r:",
           "liefere &e20.000 Messing-Barren&r."],
          tasks=[task_item("create:brass_ingot", 20000, consume=True)],
          rewards=[coin_crystal(10), rew_xp(80)],
          deps=["x_root"], icon="create:brass_ingot", size=1.25),
    quest("x_iron", 1.8, -3.0, "Eisen-Imperium",
          ["Eisen ist das Rückgrat jeder Maschine. Liefere &e50.000 Eisenbarren&r —",
           "Erz-Verarbeitung sei Dank."],
          tasks=[task_item("minecraft:iron_ingot", 50000, consume=True)],
          rewards=[coin_crystal(10), rew_xp(80)],
          deps=["x_root"], icon="minecraft:iron_ingot", size=1.25),
    quest("x_copper", 3.5, -2.0, "Kupfer-Flut",
          ["Create läuft auf Kupfer. Liefere &e30.000 Kupferbarren&r."],
          tasks=[task_item("minecraft:copper_ingot", 30000, consume=True)],
          rewards=[coin_crystal(8), rew_xp(70)],
          deps=["x_root"], icon="minecraft:copper_ingot", size=1.25),
    quest("x_precision", 0.0, -3.8, "Präzisions-Massenfertigung",
          ["Die Königsdisziplin der Automatisierung: fertige &e10.000 Precision",
           "Mechanisms&r vollautomatisch. &7Mechanical Crafters glühen lassen!"],
          tasks=[task_item("create:precision_mechanism", 10000, consume=True)],
          rewards=[rew_item("minecraft:diamond_block", 4), rew_xp(120)],
          deps=["x_root"], icon="create:precision_mechanism", size=1.75, shape="gear"),
    quest("x_logs", -3.5, 2.0, "Endlos-Holz",
          ["Deine Baumfarm läuft heiß: liefere &e50.000 Holz&r."],
          tasks=[task_item("minecraft:oak_log", 50000, consume=True)],
          rewards=[coin_crystal(8), rew_xp(70)],
          deps=["x_root"], icon="minecraft:oak_log", size=1.25),
    quest("x_food", -1.8, 3.0, "Großküche",
          ["Niemand hungert mehr: liefere &e10.000 gekochten Reis&r aus der",
           "Central Kitchen."],
          tasks=[task_item("farmersdelight:cooked_rice", 10000, consume=True)],
          rewards=[coin_crystal(8), rew_xp(70)],
          deps=["x_root"], icon="farmersdelight:cooked_rice", size=1.25),
    quest("x_levitite", 1.8, 3.0, "Schwebe-Manufaktur",
          ["Halte deine Luftflotte am Schweben: produziere &e5.000 Levitite&r."],
          tasks=[task_item("aeronautics:levitite", 5000, consume=True)],
          rewards=[coin_crystal(12), rew_xp(90)],
          deps=["x_root"], icon="aeronautics:levitite", size=1.25),
    quest("x_kartoffel", 3.5, 2.0, "Kartoffel-Armee",
          ["§oFür den künftigen &6Kartoffelboss&r§o:§r züchte eine Armee an —",
           "liefere &e50.000 Kartoffeln&r."],
          tasks=[task_item("minecraft:potato", 50000, consume=True)],
          rewards=[coin_crystal(8), rew_xp(70)],
          deps=["x_root"], icon="minecraft:baked_potato", size=1.25),
    quest("x_diamonds", 0.0, 3.8, "Diamant-Mine",
          ["Reichtum aus der Tiefe (oder per Create-Steinfarm): liefere &e10.000 Diamanten&r."],
          tasks=[task_item("minecraft:diamond", 10000, consume=True)],
          rewards=[coin_crystal(12), rew_xp(90)],
          deps=["x_root"], icon="minecraft:diamond", size=1.25),
    quest("x_coins", -5.0, 0.0, "Smaragd-Magnat",
          ["Schwimme im Reichtum: besitze &e64 Smaragdblöcke&r gleichzeitig."],
          tasks=[task_item("minecraft:emerald_block", 64)],
          rewards=[rew_item("minecraft:diamond_block", 8), rew_xp(80)],
          deps=["x_root"], icon="minecraft:emerald_block", size=1.25),
    quest("x_completionist", 0.0, 6.0, "Legende des SMP",
          ["Du hast die größten Automatisierungs-Ziele erreicht. Niemand auf dem",
           "Server kommt dir gleich.",
           "", "&6Herzlichen Glückwunsch — du bist eine wahre Legende!&r"],
          tasks=[task_item("create:precision_mechanism", 1)],
          rewards=[rew_item("minecraft:nether_star", 4), rew_item("minecraft:diamond_block", 16), rew_xp(200)],
          deps=["x_andesite", "x_brass", "x_iron", "x_copper", "x_precision", "x_logs",
                "x_food", "x_levitite", "x_kartoffel", "x_diamonds", "x_coins"],
          icon="minecraft:nether_star", size=2.5, shape="gear"),
]

# ---- MineColonies-Questline (groß; aus den echten Hütten-Blöcken erzeugt) ---
MC_NAME = {
 "warehouse":"Lagerhaus","deliveryman":"Bote","lumberjack":"Holzfäller","miner":"Bergmann",
 "fisherman":"Fischer","stonemason":"Steinmetz","sawmill":"Sägewerk","smeltery":"Schmelze",
 "stonesmeltery":"Steinschmelze","farmer":"Bauernhof","field":"Feld","kitchen":"Küche",
 "baker":"Bäckerei","cowboy":"Rinderfarm","shepherd":"Schäferei","swineherder":"Schweinefarm",
 "chickenherder":"Hühnerfarm","rabbithutch":"Kaninchenstall","beekeeper":"Imkerei",
 "plantation":"Plantage","plantationfield":"Plantagen-Feld","florist":"Blumenladen",
 "composter":"Komposter","blacksmith":"Schmied","mechanic":"Mechaniker","dyer":"Färberei",
 "fletcher":"Bogner","glassblower":"Glasbläser","crusher":"Brecher","sifter":"Siebanlage",
 "concretemixer":"Betonmischer","university":"Universität","library":"Bibliothek","school":"Schule",
 "hospital":"Krankenhaus","graveyard":"Friedhof","guardtower":"Wachturm","archery":"Schießstand",
 "barracks":"Kaserne","combatacademy":"Kampfakademie","gatehouse":"Torhaus","enchanter":"Verzauberer",
 "alchemist":"Alchemist","mysticalsite":"Mystischer Ort","netherworker":"Nether-Arbeiter",
 "stable":"Stall","citizen":"Wohnhaus",
}
MC_CATS = [
 ("Logistik & Lager",      ["warehouse","deliveryman"]),
 ("Rohstoffe",             ["lumberjack","miner","fisherman","stonemason","sawmill","smeltery","stonesmeltery"]),
 ("Nahrung & Tiere",       ["farmer","field","kitchen","baker","cowboy","shepherd","swineherder",
                            "chickenherder","rabbithutch","beekeeper","plantation","plantationfield",
                            "florist","composter"]),
 ("Handwerk",              ["blacksmith","mechanic","dyer","fletcher","glassblower","crusher","sifter","concretemixer"]),
 ("Wissen & Gesundheit",   ["university","library","school","hospital","graveyard"]),
 ("Verteidigung",          ["guardtower","archery","barracks","combatacademy","gatehouse"]),
 ("Mystik & Spezial",      ["enchanter","alchemist","mysticalsite","netherworker","stable","citizen"]),
]
reg("mc_hub")
for _cat, _huts in MC_CATS:
    for _h in _huts: reg("mc_" + _h)

mc_q = [
    quest("mc_hub", 9.0, -2.0, "Eine wachsende Kolonie",
          ["Deine Kolonie soll zur Großstadt werden! Schalte nach und nach alle",
           "&aMineColonies-Hütten&r frei — Logistik, Rohstoffe, Nahrung, Handwerk,",
           "Wissen, Verteidigung und Mystik. &7Jede Hütte = ein Bauauftrag für den Baumeister."],
          tasks=[task_item("minecolonies:blockhutwarehouse")],
          rewards=[coin_gold(2), rew_xp(25)],
          deps=["c_buerger"], icon="minecolonies:blockhutwarehouse", size=2.0, shape="gear"),
]
for _ci, (_cat, _huts) in enumerate(MC_CATS):
    _x = float(_ci * 3)
    _prev = "mc_hub"
    for _j, _h in enumerate(_huts):
        _last = (_j == len(_huts) - 1)
        mc_q.append(quest(
            "mc_" + _h, _x, float((_j + 1) * 1.5), MC_NAME[_h] + (f"  §8({_cat})" if _j == 0 else ""),
            [f"Errichte die &a{MC_NAME[_h]}&r in einer deiner Kolonien (Bauauftrag beim Baumeister).",
             f"&7Kategorie: {_cat}."],
            tasks=[task_item("minecolonies:blockhut" + _h)],
            rewards=[(coin_gold(1) if (_j >= 3 or _last) else coin_silver(10)), rew_xp(12)],
            deps=[_prev],
            icon="minecolonies:blockhut" + _h,
            shape=("hexagon" if _j == 0 else None), size=(1.25 if _j == 0 else None)))
        _prev = "mc_" + _h

# ============================================================================
# Zusammenführen: alle Cluster RADIAL um die zentrale Willkommens-Quest
# ============================================================================
def shift(qs, dx, dy):
    for q in qs:
        q["x"] = Double(float(q["x"]) + dx); q["y"] = Double(float(q["y"]) + dy)
    return qs

all_quests = []
all_quests += shift(welcome_q, 0.0,  0.0)    # ZENTRUM
all_quests += shift(farm_q,    0.0, -5.0)    # NORD: Farm
all_quests += shift(cozy_q,    0.0, -16.0)   # NORD: Cozy/Sunlit (über der Farm)
all_quests += shift(colony_q,  8.0,  0.0)    # OST: Kolonie-Grundlagen
all_quests += shift(mc_q,      8.0,  3.0)    # OST: große MineColonies-Questline
all_quests += shift(create_q,  0.0,  5.0)    # SÜD: Create-Kontraptionen
all_quests += shift(aero_q,   -1.0, 18.0)    # SÜD (unter Create): Aeronautics
all_quests += shift(world_q,  -8.0,  0.0)    # WEST: Welt
all_quests += shift(econ_q,   -8.0,  3.0)    # WEST: Wirtschaft
all_quests += shift(endgame_q,-15.0, 7.0)    # WEST-SÜD: Endgame

main_chapter = {
    "default_hide_dependency_lines": False, "default_quest_shape": "",
    "filename": "questline", "group": G, "icon": item("minecraft:cake"),
    "id": CH_MAIN, "order_index": 0, "progression_mode": "flexible",
    # Quests sind VERSTECKT, bis ihre Voraussetzung ABGESCHLOSSEN ist (nicht nur gelockt;
    # _visible würde kaskadierend alles aufdecken, _complete zeigt nur die nächste Stufe):
    "hide_quest_until_deps_complete": True,
    "quest_links": [], "title": "🌾 Cozy Farming SMP", "quests": all_quests,
}

os.makedirs(os.path.join(OUT, "chapters"), exist_ok=True)
def write(relpath, obj):
    p = os.path.join(OUT, relpath); os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f: f.write(snbt(obj) + "\n")
    print("wrote", relpath)

write("chapter_groups.snbt", chapter_groups)
write("data.snbt", data)
write("chapters/questline.snbt", main_chapter)

for old in ("willkommen", "farmen_und_leben", "kolonien", "create", "aeronautics", "welt", "wirtschaft", "endgame"):
    p = os.path.join(OUT, "chapters", old + ".snbt")
    if os.path.exists(p): os.remove(p); print("removed", old)

print("quests:", len(all_quests), "| ids used:", _counter)
