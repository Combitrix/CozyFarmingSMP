#!/usr/bin/env python3
"""Generiert den großen Farming-Skilltree für Pufferfish's Skills.
Viele kleine Knoten (kleine % je Skill) auf radialen Ästen.
Schreibt definitions.json, skills.json, connections.json, experience.json.
category.json bleibt unverändert (starting_points)."""
import os, json, math

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "pack", "config", "puffish_skills", "categories", "farming")

# (def_id, Titel, Attribut, Wert/Knoten, Operation, Anzahl Knoten, Icon, Effekt-Text)
# Nur bewährte 1.21-Attribute (generic./player.-Form wie in der Pufferfish-Doku).
BRANCHES = [
    ("bspd",   "Grüner Daumen",      "player.block_break_speed",        0.03, "multiply_base", 12, "minecraft:iron_hoe",          "+3% Ernte-/Abbau-Tempo"),
    ("meff",   "Geübte Hände",       "player.mining_efficiency",        0.20, "addition",      10, "minecraft:diamond_hoe",       "+0,2 Abbau-Effizienz"),
    ("mspd",   "Flinke Füße",        "generic.movement_speed",          0.02, "multiply_base", 10, "minecraft:leather_boots",     "+2% Lauftempo"),
    ("brange", "Weite Arme",         "player.block_interaction_range",  0.15, "addition",       8, "minecraft:bamboo",            "+0,15 Block-Reichweite"),
    ("erange", "Tierflüsterer",      "player.entity_interaction_range", 0.15, "addition",       8, "minecraft:lead",              "+0,15 Tier-Reichweite"),
    ("hp",     "Konstitution",       "generic.max_health",              1,    "addition",      12, "minecraft:golden_carrot",     "+0,5 Herz"),
    ("armor",  "Robuste Kleidung",   "generic.armor",                   0.5,  "addition",      10, "minecraft:iron_chestplate",   "+0,5 Rüstung"),
    ("absorp", "Zähe Ausdauer",      "generic.max_absorption",          1,    "addition",       8, "minecraft:golden_apple",      "+0,5 Extra-Absorption"),
    ("luck",   "Glückspilz",         "generic.luck",                    0.5,  "addition",       8, "minecraft:rabbit_foot",       "+0,5 Glück"),
    ("subm",   "Reisbauer",          "player.submerged_mining_speed",   0.30, "addition",       6, "minecraft:kelp",              "+0,3 Abbau-Tempo unter Wasser"),
    ("sneak",  "Leise Schritte",     "player.sneaking_speed",           0.04, "multiply_base",  6, "minecraft:moss_block",        "+4% Schleich-Tempo"),
    ("kb",     "Standfest",          "generic.knockback_resistance",    0.04, "addition",       6, "minecraft:shield",            "+4% Rückstoß-Resistenz"),
    ("atkdmg", "Wehrhafter Bauer",   "generic.attack_damage",           0.25, "addition",       8, "minecraft:iron_sword",        "+0,25 Angriffsschaden"),
    ("atkspd", "Schnelle Sense",     "generic.attack_speed",            0.04, "multiply_base",  6, "minecraft:golden_sword",      "+4% Angriffs-Tempo"),
]

# ---- definitions.json ------------------------------------------------------
definitions = {
    "root_farm": {
        "title": "Bauernhof",
        "description": "§7Der Einstieg ins Farmer-Leben. Verdiene Skill-Punkte durchs §aErnten von Feldfrüchten§7.",
        "icon": {"type": "item", "data": {"item": "minecraft:wheat"}},
        "rewards": [],
    }
}
for did, title, attr, val, op, _n, icon, eff in BRANCHES:
    definitions[did] = {
        "title": title,
        "description": "§a" + eff + " §7je Stufe.",
        "icon": {"type": "item", "data": {"item": icon}},
        "rewards": [
            {"type": "puffish_skills:attribute",
             "data": {"attribute": attr, "value": val, "operation": op}}
        ],
    }

# ---- skills.json + connections.json (radiale Äste) -------------------------
skills = {"root": {"x": 0, "y": 0, "definition": "root_farm", "root": True}}
connections = []
n = len(BRANCHES)
BASE_R, STEP = 64, 30
for i, (did, *_rest) in enumerate(BRANCHES):
    count = BRANCHES[i][5]
    ang = math.radians(i * (360.0 / n))
    prev = "root"
    for j in range(count):
        r = BASE_R + j * STEP
        sid = f"{did}{j+1}"
        skills[sid] = {
            "x": round(r * math.cos(ang)),
            "y": round(r * math.sin(ang)),
            "definition": did,
        }
        connections.append([prev, sid])
        prev = sid

# ---- experience.json (XP durchs Ernten vieler Feldfrüchte) -----------------
CROPS = [("wheat", 5), ("carrots", 5), ("potatoes", 5), ("beetroots", 5),
         ("nether_wart", 5), ("melon", 8), ("pumpkin", 8), ("sweet_berry_bush", 4),
         ("cocoa", 5), ("torchflower_crop", 8), ("pitcher_crop", 8)]
experience = {
    "level_limit": 60,
    "experience_per_level": {"type": "expression", "data": {"expression": "level * 50 + 80"}},
    "sources": [{
        "type": "puffish_skills:break_block",
        "data": {
            "variables": {c: {"operations": [{"type": "get_broken_block_state"},
                                             {"type": "puffish_skills:test", "data": {"block": c}}]}
                          for c, _ in CROPS},
            "experience": [{"condition": c, "expression": str(xp)} for c, xp in CROPS],
        },
    }],
}

def w(name, obj):
    json.dump(obj, open(os.path.join(OUT, name), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("wrote", name)

w("definitions.json", definitions)
w("skills.json", skills)
w("connections.json", connections)
w("experience.json", experience)
print(f"Äste: {n} | Skills: {len(skills)} | Verbindungen: {len(connections)}")
