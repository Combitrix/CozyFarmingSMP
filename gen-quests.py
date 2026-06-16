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
welcome = chapter("willkommen", "👋 Willkommen", "minecraft:cherry_sapling", [
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
], order=0)

# ---- Kapitel 1: Farmen & Leben (gated hinter Willkommen) -------------------
farm = chapter("farmen_und_leben", "🌱 Farmen & Leben", "farmersdelight:cooking_pot", [
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
], order=1)

# ---- Kapitel 2: Bauen & Gemeinschaft (gated hinter Farmen) -----------------
colony = chapter("kolonien", "🏘 Bauen & Gemeinschaft", "minecolonies:blockhuttownhall", [
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
], order=2)

# ---- Kapitel 4: Aeronautics (25 Quests, gated hinter Create-Start) ---------
A = "create_aeronautics"  # nur Doku; echte ID-Namespace ist "aeronautics:"
aero = chapter("aeronautics", "🎈 Aeronautics — Erobere den Himmel", "aeronautics:aviators_goggles", [
    quest("ae_intro", 0.0, 0.0, "Werde Luftfahrer",
          ["Der Himmel ruft! &bCreate Aeronautics&r lässt dich echte &dLuftschiffe&r bauen.",
           "Schnapp dir die &aAviator's Goggles&r — dein Blick für alles, was fliegt.",
           "", "&7Alpha-Mod: mach vor großen Bauten ein Backup."],
          tasks=[task_item("aeronautics:aviators_goggles")],
          rewards=[coin_gold(2), rew_xp(20)],
          deps=[ATM_CREATE_ROOT], icon="aeronautics:aviators_goggles", size=2.0, shape="gear"),
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
], order=4)

# ---- Kapitel 5: Welt & Vernetzung (gated hinter Kolonien) ------------------
world = chapter("welt", "🌍 Welt & Vernetzung", "minecraft:filled_map", [
    quest("w_biome", 0.0, 0.0, "Entdecke die Welt",
          ["Die Welt ist riesig und realistisch: &aTerralith&r + &aTectonic&r zaubern",
           "epische Biome und Gebirge. Erkunde mindestens &e3 verschiedene&r Biome."],
          tasks=[task_check()], rewards=[rew_item("minecraft:map"), coin_silver(20), rew_xp(15)],
          deps=["c_builder"], icon="minecraft:filled_map", size=1.5, shape="hexagon"),
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
], order=5)

# ---- Kapitel 6: Ziele & Wirtschaft (gated hinter Welt) ---------------------
econ = chapter("wirtschaft", "🪙 Ziele & Wirtschaft", "magic_coins:gold_coin", [
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
], order=6)

# ---- Kapitel 7: Endgame (gated hinter Wirtschaft + Aeronautics) ------------
endgame = chapter("endgame", "🏆 Endgame", "minecraft:nether_star", [
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
], order=7)

# ============================================================================
# Create-Kapitel aus ATM-10 transformieren + deutsche Titel/Beschreibungen
# ============================================================================
def hum(item_id):
    return item_id.split(":", 1)[1].replace("_", " ").title()

# (Titel, [Beschreibungszeilen]) je Primär-Task-Item. Fallback: hum() + generischer Flavor.
CREATE_FLAVOR = {
 "minecraft:andesite": ("Andesit — der Anfang von allem",
    ["&bCreate&r liebt Andesit. Grab eine ordentliche Menge ab —",
     "daraus wird gleich die wichtigste Zutat überhaupt."]),
 "create:andesite_alloy": ("Andesite Alloy",
    ["Die &aAndesit-Legierung&r ist das Brot-und-Butter-Material von Create.",
     "&7Ohne sie läuft hier gar nichts. Stell einen Vorrat her!"]),
 "create:cogwheel": ("Das Zahnrad",
    ["Das &aZahnrad&r überträgt Drehkraft. Der Herzschlag jeder Maschine.",
     "&7Zwei davon nebeneinander? Vorsicht — die mögen sich nicht."]),
 "create:large_cogwheel": ("Großes Zahnrad",
    ["Mit dem &agroßen Zahnrad&r änderst du Drehzahl und Richtung.",
     "&7Übersetzung gefällig?"]),
 "create:shaft": ("Die Welle",
    ["Die &aWelle&r leitet Rotation von A nach B. Unscheinbar, unverzichtbar."]),
 "create:water_wheel": ("Wasserrad",
    ["Das &aWasserrad&r macht aus fließendem Wasser saubere, kostenlose Drehkraft.",
     "&7Die gemütlichste Energiequelle überhaupt."]),
 "create:large_water_wheel": ("Großes Wasserrad",
    ["Mehr Wasser, mehr Power. Das &agroße Wasserrad&r liefert ordentlich Schwung."]),
 "create:windmill_bearing": ("Windmühlen-Lager",
    ["Bau dir eine &aWindmühle&r — Segel dran, und der Wind erledigt den Rest."]),
 "create:white_sail": ("Segel",
    ["&aSegel&r fangen den Wind für deine Windmühle. Je mehr, desto mehr Drehkraft."]),
 "create:mechanical_press": ("Mechanische Presse",
    ["Die &aPresse&r plättet, prägt und presst. Bleche, Pflaster, Münzrohlinge …",
     "&7Das nützlichste *Klonk* im Spiel."]),
 "create:mechanical_mixer": ("Mechanischer Mixer",
    ["Der &aMixer&r rührt über einem Becken alles zusammen — Legierungen, Teige, Tränke."]),
 "create:basin": ("Das Becken",
    ["Das &aBecken&r sammelt Zutaten für Mixer und Presse. Die kleine Küche der Maschinen."]),
 "create:mechanical_crafter": ("Mechanischer Kruster",
    ["Mehrere &aKruster&r craften ganze Rezepte automatisch. Endlich Schluss mit Handarbeit!"]),
 "create:mechanical_arm": ("Mechanischer Arm",
    ["Der &aArm&r sortiert und befüllt punktgenau. Dein fleißigster Mitarbeiter."]),
 "create:mechanical_bearing": ("Mechanisches Lager",
    ["Mit dem &aLager&r drehst und bewegst du ganze Bauwerke — willkommen bei Kontraptionen!"]),
 "create:andesite_casing": ("Andesite Casing",
    ["Das &aAndesit-Gehäuse&r ummantelt Wellen und Maschinen. Hübsch und praktisch."]),
 "create:copper_casing": ("Copper Casing",
    ["Das &aKupfer-Gehäuse&r ist die Stufe für alles rund um Flüssigkeiten."]),
 "create:brass_casing": ("Brass Casing",
    ["Das &aMessing-Gehäuse&r markiert die Mittelstufe — jetzt wird's clever."]),
 "create:railway_casing": ("Railway Casing",
    ["Das &aSchienen-Gehäuse&r ist die Basis für Züge, Bahnhöfe und Schienenfahrzeuge."]),
 "create:fluid_tank": ("Flüssigkeitstank",
    ["Der &aTank&r lagert Lava, Wasser, Honig & Co. Stapelbar zu riesigen Reservoirs."]),
 "create:fluid_pipe": ("Flüssigkeitsrohr",
    ["&aRohre&r pumpen Flüssigkeiten dorthin, wo du sie brauchst. Mit Pumpe, versteht sich."]),
 "create:portable_fluid_interface": ("Portable Fluid Interface",
    ["Tankt fahrende Kontraptionen automatisch ab oder auf. Praktisch für Züge & Schiffe."]),
 "create:nozzle": ("Düse",
    ["Die &aDüse&r verteilt den Effekt eines Encased Fan im Umkreis. Wind in alle Richtungen."]),
 "create:chute": ("Schacht",
    ["Der &aSchacht&r lässt Items vertikal rieseln — die Schwerkraft arbeitet für dich."]),
 "create:belt_connector": ("Förderband",
    ["Zwei Wellen, ein &aRiemen&r dazwischen — fertig ist das Fließband. Klassiker."]),
 "create:depot": ("Ablage",
    ["Das &aDepot&r hält ein einzelnes Item für die Bearbeitung bereit. Mini-Werkbank."]),
 "create:andesite_funnel": ("Andesite Funnel",
    ["Der &aTrichter&r zieht Items ein oder gibt sie aus. Andesit = die Einsteigerklasse."]),
 "create:brass_funnel": ("Brass Funnel",
    ["Der &aMessing-Trichter&r kann filtern — nur genau das durchlassen, was du willst."]),
 "create:andesite_tunnel": ("Andesite Tunnel",
    ["Der &aTunnel&r verteilt Items auf Förderbändern sauber weiter."]),
 "create:brass_tunnel": ("Brass Tunnel",
    ["Der &aMessing-Tunnel&r verteilt und sortiert über mehrere Bänder. Logistik-Magie."]),
 "create:encased_chain_drive": ("Kettenantrieb",
    ["Der &aKettenantrieb&r verteilt Drehkraft elegant um Ecken und über Strecken."]),
 "create:adjustable_chain_gearshift": ("Regelbares Kettengetriebe",
    ["Damit steuerst du die Drehzahl per Redstone. Tempo nach Bedarf."]),
 "create:gantry_shaft": ("Portal-Welle",
    ["&aGantry&r-Aufbauten bewegen Kontraptionen kontrolliert hin und her. Schiebetüren, Aufzüge …"]),
 "create:piston_extension_pole": ("Kolben-Verlängerung",
    ["Verlängert den mechanischen Kolben — schiebe Dinge richtig weit."]),
 "create:radial_chassis": ("Radial-Chassis",
    ["Das &aChassis&r hält große Kontraptionen zusammen, wenn sie sich drehen."]),
 "create:empty_blaze_burner": ("Leerer Blaze Burner",
    ["Erst leer, dann mit einem Blaze gefüttert: der &aBlaze Burner&r ist deine Heizung",
     "für Mixer und Presse. &7Hunger auf Kuchen?"]),
 "create:blaze_cake": ("Blaze-Kuchen",
    ["Ein &aBlaze Cake&r macht den Blaze Burner so richtig heiß — für die harten Rezepte.",
     "&7Backen für Fortgeschrittene."]),
 "create:precision_mechanism": ("Präzisionsmechanismus",
    ["Das &aPräzisionsmechanismus&r ist das Herz fortgeschrittener Geräte. Fummelig, aber lohnend."]),
 "create:brass_ingot": ("Messing",
    ["&aMessing&r aus Kupfer und Zink schaltet die Mittelstufe von Create frei."]),
 "create:copper_valve_handle": ("Ventilgriff",
    ["Mit dem &aVentilgriff&r gibst du von Hand exakte Drehimpulse. Feinjustage für Bastler."]),
 "create:super_glue": ("Superkleber",
    ["&aSuperkleber&r verbindet Blöcke zu einer Kontraption. Alles, was zusammenklebt, fliegt zusammen."]),
 "create:schematic_table": ("Schematik-Tisch",
    ["Am &aSchematik-Tisch&r lädst du Baupläne — kopiere ganze Bauwerke."]),
 "create:schematicannon": ("Schematik-Kanone",
    ["Die &aSchematik-Kanone&r baut gespeicherte Schematics automatisch auf. Faulheit, aber effizient."]),
 "create:track": ("Gleise",
    ["&aGleise&r sind die Adern deines Imperiums. Hier rollen bald die Züge zwischen den Kolonien."]),
 "create:track_station": ("Bahnhof",
    ["Am &aBahnhof&r baust du Züge zusammen, gibst Fahrpläne und steigst ein. Alles einsteigen!"]),
 "create:nixie_tube": ("Nixie-Röhre",
    ["&aNixie-Röhren&r zeigen Zahlen und Signale schön stilvoll an. Retro-Chic."]),
 "minecraft:water_bucket": ("Ein Eimer Wasser",
    ["Wasser treibt Räder an und kühlt Rezepte. Hol einen &aEimer&r voll."]),
 "minecraft:bucket": ("Der Eimer",
    ["Ein simpler &aEimer&r — Anfang jeder Flüssigkeits-Logistik."]),
 "minecraft:gold_ingot": ("Gold",
    ["&aGold&r brauchst du für feinere Mechanik und glänzende Bauteile."]),
 "minecraft:iron_ingot": ("Eisen",
    ["&aEisen&r — das Rückgrat jeder Maschine. Davon nie genug."]),
 "minecraft:iron_ore": ("Eisenerz",
    ["Grab &aEisenerz&r ab — Create verdoppelt deine Ausbeute später spielend."]),
 "minecraft:diamond_ore": ("Diamanterz",
    ["&bDiamanten&r für die harten Werkzeuge und edlen Rezepte. Tief graben lohnt sich."]),
 "minecraft:copper_block": ("Kupferblock",
    ["&aKupfer&r ist überall in Create — Gehäuse, Bleche, Rohre. Hamstern!"]),
 "minecraft:glowstone_dust": ("Glowstone-Staub",
    ["&eGlowstone&r leuchtet und beschleunigt manche Create-Rezepte."]),
 "minecraft:slime_ball": ("Schleimball",
    ["&aSchleim&r macht Dinge klebrig und beweglich — Kolben, Bänder, mehr."]),
 "minecraft:honey_bottle": ("Honig",
    ["Süßer &eHonig&r — Zutat und Flüssigkeit zugleich. Bienenfleißig sammeln."]),
 "minecraft:minecart": ("Lore",
    ["Die gute alte &aLore&r — Create macht daraus rollende Wunderwerke."]),
 "minecraft:lever": ("Hebel",
    ["Ein &aHebel&r schaltet, was geschaltet werden muss. Redstone-Grundlage."]),
 "minecraft:clock": ("Uhr",
    ["Eine &aUhr&r für Zeitgefühl und manche Mechaniken."]),
 "minecraft:repeater": ("Redstone-Verstärker",
    ["Der &aRepeater&r verlängert und verzögert Redstone-Signale. Timing ist alles."]),
 "minecraft:oak_sapling": ("Setzling",
    ["Ein &aSetzling&r — Holz wächst nach, Create automatisiert die Ernte."]),
 "minecraft:wheat_seeds": ("Saatgut",
    ["&aSaatgut&r für automatische Farmen à la Create."]),
 "minecraft:dirt": ("Erde",
    ["Schlichte &aErde&r — Baustoff und Ackerland. Manchmal braucht's einfach Dreck."]),
 "minecraft:snowball": ("Schneeball",
    ["&aSchneebälle&r — Create macht daraus Eis, Kühlung und mehr."]),
 "minecraft:cornflower": ("Kornblume",
    ["Eine &9Kornblume&r — blaue Farbe und ein hübscher Tupfer im Feld."]),
 "minecraft:andesite_block": ("Andesit-Block", ["Mehr Andesit, mehr Möglichkeiten."]),
}

def transform_atm_create():
    src = open(os.path.join(ROOT, "vendor", "atm_create.snbt"), encoding="utf-8").read()

    # 1) Fremd-Items -> Pack-Items
    src = src.replace('id: "alltheores:brass_ingot"', 'id: "create:brass_ingot"')
    src = src.replace('id: "the_bumblezone:honey_bucket"', 'id: "minecraft:honey_bottle"')
    filt_map = [("mechanical_piston", "create:mechanical_piston"), ("cogwheel", "create:cogwheel"),
                ("water_wheel", "create:water_wheel"), ("seats", "create:blue_seat"),
                ("postboxes", "create:blue_postbox"), ("packages", "create:cardboard_package_12x12"),
                ("table_cloths", "create:andesite_table_cloth")]
    def repl_filter(mobj):
        inner = mobj.group(0)
        for needle, repl in filt_map:
            if needle in inner: return '{ count: 1, id: "%s" }' % repl
        return '{ count: 1, id: "create:cogwheel" }'
    src = _re.sub(r'\{ components: \{ "ftbfiltersystem:filter":.*?id: "ftbfiltersystem:smart_filter" \}',
                  repl_filter, src)

    # 2) Header: Gruppe -> G, Titel, ATM-Bilder raus
    src = _re.sub(r'group: "[0-9A-F]{16}"', 'group: "%s"' % G, src, count=1)
    src = _re.sub(r'\n\timages: \[.*?\n\t\]', '', src, count=1, flags=_re.S)
    if "\n\ttitle:" not in src:
        src = src.replace('\tfilename: "create"\n',
                          '\tfilename: "create"\n\ttitle: "%s"\n\torder_index: 3\n' % esc("⚙ Technik & Mobilität"),
                          1)

    # 3) Pro Quest: primäres Task-Item bestimmen -> deutscher Titel + Beschreibung injizieren
    #    (Quest-IDs stehen auf 3-Tab-Ebene; Task-/Reward-IDs tiefer.)
    blocks = []
    j = src.index("quests: [") + len("quests: [")
    d = 0; collect = False; buf = ""; start = 0
    for k in range(j, len(src)):
        ch = src[k]
        if ch == "{":
            d += 1
            if d == 1: collect = True; buf = "{"; start = k; continue
        elif ch == "}":
            d -= 1
            if d == 0 and collect:
                buf += "}"; blocks.append((start, k + 1, buf)); collect = False; buf = ""; continue
        if collect: buf += ch

    def primary_item(block):
        ti = block.find("tasks:"); ri = block.find("rewards:")
        seg = block[ti: ri if 0 <= ri and ri > ti else len(block)] if ti >= 0 else block
        mm = _re.search(r'id: "([a-z0-9_]+:[a-z0-9_/]+)"', seg)
        return mm.group(1) if mm else None

    roots = {"57A7A5C79389A96A", "1B182A30604655E2"}  # ATM-Wurzeln -> hinter c_builder gaten
    c_builder = QIDS["c_builder"]
    edits = []  # (insert_pos, text)  -- von hinten einfügen
    for s0, s1, block in blocks:
        qid_m = _re.search(r'\bid: "([0-9A-F]{16})"', block)
        if not qid_m: continue
        qid = qid_m.group(1)
        it = primary_item(block)
        if it and it in CREATE_FLAVOR:
            title, lines = CREATE_FLAVOR[it]
        elif it:
            title = hum(it)
            lines = ["Beschaffe &a%s&r — ein weiterer Baustein auf deinem Create-Weg." % title,
                     "&7(In EMI siehst du, wie es hergestellt wird.)"]
        else:
            title = "Create-Aufgabe"
            lines = ["Erfülle diese Aufgabe und bring dein Create-Imperium voran."]
        # Einfügetext nach der Quest-id-Zeile "\n\t\t\tid: \"<qid>\"\n"
        id_line = '\n\t\t\tid: "%s"' % qid
        pos = src.find(id_line, s0, s1)
        if pos < 0: continue
        insert_at = pos + len(id_line)
        inj = ""
        if qid in roots:
            inj += '\n\t\t\tdependencies: ["%s"]' % c_builder
        inj += '\n\t\t\ttitle: "%s"' % esc(title)
        inj += '\n\t\t\tdescription: [\n' + "\n".join('\t\t\t\t"%s"' % esc(L) for L in lines) + '\n\t\t\t]'
        edits.append((insert_at, inj))
    for pos, text in sorted(edits, reverse=True):
        src = src[:pos] + text + src[pos:]

    with open(os.path.join(OUT, "chapters", "create.snbt"), "w", encoding="utf-8") as f:
        f.write(src)
    foreign = _re.findall(r'id: "(ftbfiltersystem|alltheores|the_bumblezone):', src)
    ids = _re.findall(r'\bid: "([0-9A-F]{16})"', src)
    descs = src.count("\n\t\t\tdescription: [")
    print(f"wrote chapters/create.snbt (ATM): ids={len(ids)} descriptions={descs} foreign={foreign}")
    return ids

# ---- schreiben -------------------------------------------------------------
os.makedirs(os.path.join(OUT, "chapters"), exist_ok=True)
def write(relpath, obj):
    p = os.path.join(OUT, relpath); os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f: f.write(snbt(obj) + "\n")
    print("wrote", relpath)

write("chapter_groups.snbt", chapter_groups)
write("data.snbt", data)
write("chapters/willkommen.snbt", welcome)
write("chapters/farmen_und_leben.snbt", farm)
write("chapters/kolonien.snbt", colony)
write("chapters/aeronautics.snbt", aero)
write("chapters/welt.snbt", world)
write("chapters/wirtschaft.snbt", econ)
write("chapters/endgame.snbt", endgame)
transform_atm_create()
print("total ids used (generated):", _counter)
