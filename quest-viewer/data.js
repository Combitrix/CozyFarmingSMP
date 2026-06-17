window.QUEST_DATA = {
  "meta": {
    "title": "Cozy Farming SMP",
    "version": 13
  },
  "chapters": [
    {
      "id": "4C0F000000000002",
      "title": "🌾 Cozy Farming SMP",
      "icon": {
        "item": "minecraft:cake",
        "displayName": "Cake",
        "mod": "minecraft"
      },
      "quests": [
        {
          "id": "4C0F00000000000A",
          "x": 0.0,
          "y": 0.0,
          "shape": "gear",
          "size": 3.0,
          "title": "Willkommen auf dem Cozy Farming SMP!",
          "optional": false,
          "icon": {
            "item": "minecraft:cake",
            "displayName": "Cake",
            "mod": "minecraft"
          },
          "description": [
            "&6Hallo und herzlich willkommen!&r Schön, dass du dabei bist.",
            "Dieses Pack dreht sich um &aFarmen&r, &6Kolonien&r, &bCreate-Technik&r,",
            "&dLuftschiffe&r und ein gemütliches Leben mit Freunden.",
            "",
            "Betritt die Welt — dann öffnet sich der Quest-Baum nach und nach.",
            "&7Die Quests führen dich Schritt für Schritt durch alle Features."
          ],
          "dependencies": [],
          "tasks": [
            {
              "type": "dimension",
              "dimension": "minecraft:overworld"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:bread",
              "displayName": "Bread",
              "mod": "minecraft",
              "count": 4
            },
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 10
            },
            {
              "type": "xp",
              "xp": 10
            }
          ]
        },
        {
          "id": "4C0F00000000000B",
          "x": 0.0,
          "y": -2.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Aller Anfang",
          "optional": false,
          "icon": {
            "item": "minecraft:crafting_table",
            "displayName": "Crafting Table",
            "mod": "minecraft"
          },
          "description": [
            "Stelle einen &aWerkbank-Tisch&r her und leg los.",
            "&7Mit EMI (rechts neben dem Inventar) siehst du jedes Rezept."
          ],
          "dependencies": [
            "4C0F00000000000A"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "minecraft:crafting_table",
              "displayName": "Crafting Table",
              "mod": "minecraft",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:oak_log",
              "displayName": "Oak Log",
              "mod": "minecraft",
              "count": 16
            },
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 5
            }
          ]
        },
        {
          "id": "4C0F00000000000C",
          "x": -2.0,
          "y": -1.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Das Rezeptbuch (EMI)",
          "optional": false,
          "icon": {
            "item": "minecraft:knowledge_book",
            "displayName": "Knowledge Book",
            "mod": "minecraft"
          },
          "description": [
            "&aEMI&r zeigt dir alle Rezepte: links wie etwas hergestellt wird,",
            "rechts wofür man es braucht. Klicke auf ein Item, um es nachzuschlagen.",
            "",
            "Info gelesen? Hak ab."
          ],
          "dependencies": [
            "4C0F00000000000A"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 5
            }
          ]
        },
        {
          "id": "4C0F00000000000D",
          "x": 2.0,
          "y": -1.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Die Karte (JourneyMap)",
          "optional": false,
          "icon": {
            "item": "minecraft:filled_map",
            "displayName": "Filled Map",
            "mod": "minecraft"
          },
          "description": [
            "&aJourneyMap&r (oben rechts) zeigt deine Umgebung. Mit der Karten-Taste",
            "öffnest du die Vollkarte und setzt &eWegpunkte&r — praktisch für Kolonien!",
            "",
            "Info gelesen? Hak ab."
          ],
          "dependencies": [
            "4C0F00000000000A"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 5
            }
          ]
        },
        {
          "id": "4C0F00000000000E",
          "x": -2.0,
          "y": 1.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Inventar-Komfort (Inventory Profiles Next)",
          "optional": false,
          "icon": {
            "item": "minecraft:hopper",
            "displayName": "Hopper",
            "mod": "minecraft"
          },
          "description": [
            "Die &dlila Pfeile&r in der Hotbar gehören zu &dInventory Profiles Next&r —",
            "dem &eHotbar-Swapping&r. Wir haben sie &cstandardmäßig ausgeblendet&r",
            "(sie waren im Weg), das &aFeature bleibt aber aktiv&r. Zurückholen:",
            "",
            "&71.&r Inventar öffnen → oben (Mitte/nahe Inventar) sind die IPN-Buttons.",
            "&72.&r Einstellungen → &eInventory Profiles Next&r (Taste &aO&r): dort",
            "   &eHotbar Swapping&r / &eShow hotbar buttons&r wieder einschalten.",
            "",
            "Hak ab, wenn du es gelesen hast."
          ],
          "dependencies": [
            "4C0F00000000000A"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 5
            }
          ]
        },
        {
          "id": "4C0F00000000000F",
          "x": 2.0,
          "y": 1.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Land sichern (FTB Chunks)",
          "optional": false,
          "icon": {
            "item": "ftbchunks:map",
            "displayName": "Map",
            "mod": "ftbchunks"
          },
          "description": [
            "Mit &aFTB Chunks&r (Karten-Taste → Claim-Ansicht) schützt du Chunks vor",
            "Grief. &7Tipp: Kolonie-Chunks lädt MineColonies selbst — die musst du",
            "nicht zusätzlich force-loaden.",
            "",
            "Claime einen Chunk und hak ab."
          ],
          "dependencies": [
            "4C0F00000000000A"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 5
            }
          ]
        },
        {
          "id": "4C0F000000000010",
          "x": 0.0,
          "y": 2.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Gute Reise!",
          "optional": true,
          "icon": {
            "item": "minecraft:bell",
            "displayName": "Bell",
            "mod": "minecraft"
          },
          "description": [
            "Viel Spaß auf dem SMP! &7Baut zusammen, handelt, verbindet eure",
            "Kolonien per Zug und erobert irgendwann den Himmel.",
            "",
            "&8(Diese Quest ist optional.)"
          ],
          "dependencies": [
            "4C0F00000000000A"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 5
            },
            {
              "type": "xp",
              "xp": 5
            }
          ]
        },
        {
          "id": "4C0F000000000011",
          "x": 0.0,
          "y": 7.0,
          "shape": "hexagon",
          "size": 1.5,
          "title": "Die erste Ernte",
          "optional": false,
          "icon": {
            "item": "minecraft:wheat",
            "displayName": "Wheat",
            "mod": "minecraft"
          },
          "description": [
            "Jedes Imperium beginnt mit einem Acker. Besorge dir eine &aHacke&r,",
            "lege Felder an und ernte deine erste Frucht.",
            "",
            "&7HarvestCraft 2, Veggies \\& die Delight-Mods bringen unzählige Pflanzen!"
          ],
          "dependencies": [
            "4C0F00000000000A"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "minecraft:wheat",
              "displayName": "Wheat",
              "mod": "minecraft",
              "count": 8
            },
            {
              "type": "item",
              "item": "minecraft:wooden_hoe",
              "displayName": "Wooden Hoe",
              "mod": "minecraft",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "farmersdelight:cabbage_seeds",
              "displayName": "Cabbage Seeds",
              "mod": "farmersdelight",
              "count": 3
            },
            {
              "type": "item",
              "item": "farmersdelight:tomato_seeds",
              "displayName": "Tomato Seeds",
              "mod": "farmersdelight",
              "count": 3
            },
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 15
            },
            {
              "type": "xp",
              "xp": 10
            }
          ]
        },
        {
          "id": "4C0F000000000012",
          "x": 2.0,
          "y": 7.0,
          "shape": "circle",
          "size": 1.25,
          "title": "Die Küche (Farmer's Delight)",
          "optional": false,
          "icon": {
            "item": "farmersdelight:cooking_pot",
            "displayName": "Cooking Pot",
            "mod": "farmersdelight"
          },
          "description": [
            "Rohe Karotten? Nicht mit uns. Stelle &aKochtopf&r und &aSchneidebrett&r her",
            "und koche dein erstes richtiges Gericht.",
            "",
            "&7Der Kochtopf braucht eine Hitzequelle darunter (Lagerfeuer/Ofen)."
          ],
          "dependencies": [
            "4C0F000000000011"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "farmersdelight:cooking_pot",
              "displayName": "Cooking Pot",
              "mod": "farmersdelight",
              "count": 1
            },
            {
              "type": "item",
              "item": "farmersdelight:cutting_board",
              "displayName": "Cutting Board",
              "mod": "farmersdelight",
              "count": 1
            },
            {
              "type": "item",
              "item": "farmersdelight:vegetable_soup",
              "displayName": "Vegetable Soup",
              "mod": "farmersdelight",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "farmersdelight:skillet",
              "displayName": "Skillet",
              "mod": "farmersdelight",
              "count": 1
            },
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 1
            },
            {
              "type": "xp",
              "xp": 15
            }
          ]
        },
        {
          "id": "4C0F000000000013",
          "x": 4.0,
          "y": 7.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Genuss \\& Vielfalt",
          "optional": false,
          "icon": {
            "item": "minecraft:cake",
            "displayName": "Cake",
            "mod": "minecraft"
          },
          "description": [
            "Das Pack steckt voller Lebensmittel-Mods: &aVinery&r (Wein), &aMeadow&r (Käse),",
            "&aBakery&r, &aHerbalbrews&r (Tee), &aBrewin' \\& Chewin'&r u.v.m.",
            "",
            "Stelle aus einer der Delight-/Let's-Do-Mods etwas her und hak ab."
          ],
          "dependencies": [
            "4C0F000000000012"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 15
            },
            {
              "type": "xp",
              "xp": 10
            }
          ]
        },
        {
          "id": "4C0F000000000014",
          "x": 2.0,
          "y": 8.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Die Jahreszeiten (Serene Seasons)",
          "optional": false,
          "icon": {
            "item": "minecraft:wheat_seeds",
            "displayName": "Wheat Seeds",
            "mod": "minecraft"
          },
          "description": [
            "Pflanzen wachsen je nach &eJahreszeit&r unterschiedlich gut.",
            "Achte auf Frühling/Sommer/Herbst und plane deine Felder.",
            "",
            "Ernte in passender Saison und hak diese Info-Quest ab."
          ],
          "dependencies": [
            "4C0F000000000012"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 15
            },
            {
              "type": "xp",
              "xp": 10
            }
          ]
        },
        {
          "id": "4C0F000000000015",
          "x": 0.0,
          "y": 8.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Tiere \\& Zucht (Naturalist)",
          "optional": false,
          "icon": {
            "item": "minecraft:egg",
            "displayName": "Egg",
            "mod": "minecraft"
          },
          "description": [
            "Eine Farm lebt von ihren Tieren. Züchte mindestens zwei Tierarten",
            "und entdecke die neuen Kreaturen von &aNaturalist&r."
          ],
          "dependencies": [
            "4C0F000000000011"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "minecraft:wheat",
              "displayName": "Wheat",
              "mod": "minecraft",
              "count": 4
            },
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:wheat",
              "displayName": "Wheat",
              "mod": "minecraft",
              "count": 16
            },
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 15
            },
            {
              "type": "xp",
              "xp": 10
            }
          ]
        },
        {
          "id": "4C0F000000000016",
          "x": 4.0,
          "y": 8.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Fähigkeiten (Pufferfish's Skills)",
          "optional": false,
          "icon": {
            "item": "minecraft:experience_bottle",
            "displayName": "Experience Bottle",
            "mod": "minecraft"
          },
          "description": [
            "Mit &aPufferfish's Skills&r levelst du Farming, Mining, Fishing \\& Co.",
            "Öffne den Skill-Bildschirm und investiere deinen ersten Punkt."
          ],
          "dependencies": [
            "4C0F000000000013"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 1
            },
            {
              "type": "xp",
              "xp": 20
            }
          ]
        },
        {
          "id": "4C0F000000000017",
          "x": -2.0,
          "y": 7.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Angeln (Aquaculture)",
          "optional": false,
          "icon": {
            "item": "minecraft:fishing_rod",
            "displayName": "Fishing Rod",
            "mod": "minecraft"
          },
          "description": [
            "Am Wasser wartet eine zweite Speisekammer. Bastle eine &aAngel&r und",
            "fange ein paar Fische — mit &aAquaculture&r gibt es viele neue Arten."
          ],
          "dependencies": [
            "4C0F000000000011"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "minecraft:fishing_rod",
              "displayName": "Fishing Rod",
              "mod": "minecraft",
              "count": 1
            },
            {
              "type": "item",
              "item": "minecraft:cod",
              "displayName": "Cod",
              "mod": "minecraft",
              "count": 3
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "farmersdelight:cooked_cod_slice",
              "displayName": "Cooked Cod Slice",
              "mod": "farmersdelight",
              "count": 4
            },
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 15
            },
            {
              "type": "xp",
              "xp": 10
            }
          ]
        },
        {
          "id": "4C0F000000000018",
          "x": 0.0,
          "y": 13.0,
          "shape": "hexagon",
          "size": 1.5,
          "title": "Die erste Kolonie",
          "optional": false,
          "icon": {
            "item": "minecolonies:blockhuttownhall",
            "displayName": "Blockhuttownhall",
            "mod": "minecolonies"
          },
          "description": [
            "Jede Zivilisation beginnt mit einem &6Versorgungslager&r. Platziere den",
            "&aSupply Camp&r, packe die Kiste aus und setze dein &aRathaus&r.",
            "",
            "&7Du darfst auf diesem Server §lbeliebig viele§r§7 Kolonien gründen!"
          ],
          "dependencies": [
            "4C0F000000000012"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "minecolonies:supplycampdeployer",
              "displayName": "Supplycampdeployer",
              "mod": "minecolonies",
              "count": 1
            },
            {
              "type": "item",
              "item": "minecolonies:blockhuttownhall",
              "displayName": "Blockhuttownhall",
              "mod": "minecolonies",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecolonies:blockhutbuilder",
              "displayName": "Blockhutbuilder",
              "mod": "minecolonies",
              "count": 1
            },
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 2
            },
            {
              "type": "xp",
              "xp": 20
            }
          ]
        },
        {
          "id": "4C0F000000000019",
          "x": 2.0,
          "y": 13.0,
          "shape": "circle",
          "size": 1.25,
          "title": "Der Baumeister",
          "optional": false,
          "icon": {
            "item": "minecolonies:blockhutbuilder",
            "displayName": "Blockhutbuilder",
            "mod": "minecolonies"
          },
          "description": [
            "Ohne Baumeister wächst keine Kolonie. Platziere die &aBuilder's Hut&r,",
            "weise einen Bürger zu und gib deinen ersten Bauauftrag."
          ],
          "dependencies": [
            "4C0F000000000018"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "minecolonies:blockhutbuilder",
              "displayName": "Blockhutbuilder",
              "mod": "minecolonies",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:oak_log",
              "displayName": "Oak Log",
              "mod": "minecraft",
              "count": 32
            },
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 2
            },
            {
              "type": "xp",
              "xp": 15
            }
          ]
        },
        {
          "id": "4C0F00000000001A",
          "x": 4.0,
          "y": 13.0,
          "shape": "circle",
          "size": 1.25,
          "title": "Bürger \\& Versorgung",
          "optional": false,
          "icon": {
            "item": "minecolonies:blockhutcook",
            "displayName": "Blockhutcook",
            "mod": "minecolonies"
          },
          "description": [
            "Eine Kolonie lebt von ihren Bewohnern. Baue &aKüche&r und &aTaverne&r,",
            "damit gekocht und rekrutiert wird. (Verbindet sich mit deiner Farm!)"
          ],
          "dependencies": [
            "4C0F000000000019"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "minecolonies:blockhutcook",
              "displayName": "Blockhutcook",
              "mod": "minecolonies",
              "count": 1
            },
            {
              "type": "item",
              "item": "minecolonies:blockhuttavern",
              "displayName": "Blockhuttavern",
              "mod": "minecolonies",
              "count": 1
            },
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 3
            },
            {
              "type": "xp",
              "xp": 20
            }
          ]
        },
        {
          "id": "4C0F00000000001B",
          "x": 6.0,
          "y": 13.0,
          "shape": "circle",
          "size": 1.25,
          "title": "Mehrere Zivilisationen",
          "optional": false,
          "icon": {
            "item": "minecolonies:clipboard",
            "displayName": "Clipboard",
            "mod": "minecolonies"
          },
          "description": [
            "Der Server erlaubt §lunbegrenzt viele Kolonien pro Spieler§r.",
            "Gründe eine &6zweite Kolonie&r an einem anderen Ort.",
            "",
            "&7Mindestabstand 16 Chunks. Später verbindest du sie per Zug!"
          ],
          "dependencies": [
            "4C0F00000000001A"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 5
            },
            {
              "type": "xp",
              "xp": 30
            }
          ]
        },
        {
          "id": "4C0F00000000001C",
          "x": 4.0,
          "y": 14.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Schöner Bauen",
          "optional": false,
          "icon": {
            "item": "minecraft:painting",
            "displayName": "Painting",
            "mod": "minecraft"
          },
          "description": [
            "Mit &aStructurize&r \\& &aDomum Ornamentum&r baust du frei; dazu Möbel",
            "von Macaw's \\& Another Furniture. Dekoriere ein Gebäude und hak ab."
          ],
          "dependencies": [
            "4C0F00000000001A"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 20
            },
            {
              "type": "xp",
              "xp": 15
            }
          ]
        },
        {
          "id": "4C0F00000000001D",
          "x": 22.0,
          "y": 19.0,
          "shape": "gear",
          "size": 2.0,
          "title": "Werde Luftfahrer",
          "optional": false,
          "icon": {
            "item": "aeronautics:aviators_goggles",
            "displayName": "Aviators Goggles",
            "mod": "aeronautics"
          },
          "description": [
            "Der Himmel ruft! &bCreate Aeronautics&r lässt dich echte &dLuftschiffe&r bauen.",
            "Schnapp dir die &aAviator's Goggles&r — dein Blick für alles, was fliegt.",
            "",
            "&7Alpha-Mod: mach vor großen Bauten ein Backup."
          ],
          "dependencies": [
            "57A7A5C79389A96A"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "aeronautics:aviators_goggles",
              "displayName": "Aviators Goggles",
              "mod": "aeronautics",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 2
            },
            {
              "type": "xp",
              "xp": 20
            }
          ]
        },
        {
          "id": "4C0F00000000001E",
          "x": 22.0,
          "y": 20.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Der erste Propeller",
          "optional": false,
          "icon": {
            "item": "aeronautics:wooden_propeller",
            "displayName": "Wooden Propeller",
            "mod": "aeronautics"
          },
          "description": [
            "Jeder Flug beginnt mit Schub. Bastle einen &aHölzernen Propeller&r —",
            "simpel, aber er dreht sich. &7Aus Holz wird Höhe."
          ],
          "dependencies": [
            "4C0F00000000001D"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "aeronautics:wooden_propeller",
              "displayName": "Wooden Propeller",
              "mod": "aeronautics",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 10
            },
            {
              "type": "xp",
              "xp": 10
            }
          ]
        },
        {
          "id": "4C0F00000000001F",
          "x": 20.5,
          "y": 21.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Solider Antrieb",
          "optional": false,
          "icon": {
            "item": "aeronautics:andesite_propeller",
            "displayName": "Andesite Propeller",
            "mod": "aeronautics"
          },
          "description": [
            "Der &aAndesite-Propeller&r packt mehr Schub als sein hölzerner Cousin.",
            "Mehr Drehzahl = mehr Auftrieb."
          ],
          "dependencies": [
            "4C0F00000000001E"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "aeronautics:andesite_propeller",
              "displayName": "Andesite Propeller",
              "mod": "aeronautics",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 15
            },
            {
              "type": "xp",
              "xp": 10
            }
          ]
        },
        {
          "id": "4C0F000000000020",
          "x": 23.5,
          "y": 21.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Das Propellerlager",
          "optional": false,
          "icon": {
            "item": "aeronautics:propeller_bearing",
            "displayName": "Propeller Bearing",
            "mod": "aeronautics"
          },
          "description": [
            "Das &aPropeller Bearing&r überträgt deine Create-Drehkraft auf den",
            "Propeller. &7Hier wird aus Zahnrädern echter Vortrieb."
          ],
          "dependencies": [
            "4C0F00000000001E"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "aeronautics:propeller_bearing",
              "displayName": "Propeller Bearing",
              "mod": "aeronautics",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 15
            },
            {
              "type": "xp",
              "xp": 10
            }
          ]
        },
        {
          "id": "4C0F000000000021",
          "x": 22.0,
          "y": 22.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Heiße Luft",
          "optional": false,
          "icon": {
            "item": "aeronautics:adjustable_burner",
            "displayName": "Adjustable Burner",
            "mod": "aeronautics"
          },
          "description": [
            "Der &aAdjustable Burner&r erzeugt heiße Luft — der Klassiker, um leichter",
            "als Luft zu werden. &7Heißluftballon, anyone?"
          ],
          "dependencies": [
            "4C0F000000000020"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "aeronautics:adjustable_burner",
              "displayName": "Adjustable Burner",
              "mod": "aeronautics",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 1
            },
            {
              "type": "xp",
              "xp": 15
            }
          ]
        },
        {
          "id": "4C0F000000000022",
          "x": 23.5,
          "y": 23.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Unter Dampf",
          "optional": false,
          "icon": {
            "item": "aeronautics:steam_vent",
            "displayName": "Steam Vent",
            "mod": "aeronautics"
          },
          "description": [
            "Mit dem &aSteam Vent&r nutzt du Dampfkraft für deine Flugmaschine.",
            "&7Zischt beeindruckend — und treibt an."
          ],
          "dependencies": [
            "4C0F000000000021"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "aeronautics:steam_vent",
              "displayName": "Steam Vent",
              "mod": "aeronautics",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 15
            },
            {
              "type": "xp",
              "xp": 10
            }
          ]
        },
        {
          "id": "4C0F000000000023",
          "x": 22.0,
          "y": 23.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Die Hülle",
          "optional": false,
          "icon": {
            "item": "aeronautics:white_envelope",
            "displayName": "White Envelope",
            "mod": "aeronautics"
          },
          "description": [
            "Eine &aEnvelope&r (Ballonhülle) hält die heiße Luft zusammen und gibt",
            "deinem Schiff Auftrieb. Gibt's in allen Farben — wähl deine Flagge!"
          ],
          "dependencies": [
            "4C0F000000000021"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "aeronautics:white_envelope",
              "displayName": "White Envelope",
              "mod": "aeronautics",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 15
            },
            {
              "type": "xp",
              "xp": 10
            }
          ]
        },
        {
          "id": "4C0F000000000024",
          "x": 20.5,
          "y": 24.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Hülle trifft Technik",
          "optional": false,
          "icon": {
            "item": "aeronautics:white_envelope_encased_shaft",
            "displayName": "White Envelope Encased Shaft",
            "mod": "aeronautics"
          },
          "description": [
            "Der &aEnvelope Encased Shaft&r führt eine Welle sauber durch die",
            "Ballonhülle. &7Ordnung muss sein, auch in der Luft."
          ],
          "dependencies": [
            "4C0F000000000023"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "aeronautics:white_envelope_encased_shaft",
              "displayName": "White Envelope Encased Shaft",
              "mod": "aeronautics",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 15
            },
            {
              "type": "xp",
              "xp": 10
            }
          ]
        },
        {
          "id": "4C0F000000000025",
          "x": 23.5,
          "y": 24.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Großer Ballon",
          "optional": false,
          "icon": {
            "item": "aeronautics:blue_envelope",
            "displayName": "Blue Envelope",
            "mod": "aeronautics"
          },
          "description": [
            "Größer fliegt besser. Sammle &e16 Envelopes&r für ein ordentliches Schiff."
          ],
          "dependencies": [
            "4C0F000000000023"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "aeronautics:white_envelope",
              "displayName": "White Envelope",
              "mod": "aeronautics",
              "count": 16
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 1
            },
            {
              "type": "xp",
              "xp": 15
            }
          ]
        },
        {
          "id": "4C0F000000000026",
          "x": 22.0,
          "y": 25.0,
          "shape": "hexagon",
          "size": 1.5,
          "title": "Der erste Auftrieb",
          "optional": false,
          "icon": {
            "item": "aeronautics:white_envelope",
            "displayName": "White Envelope",
            "mod": "aeronautics"
          },
          "description": [
            "Bau deine erste fliegende Kontraption — und sei es nur ein wackliger",
            "Heißluft-Auftrieb, der ein paar Blöcke abhebt. &7Geschichte wird geschrieben!"
          ],
          "dependencies": [
            "4C0F000000000023"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 2
            },
            {
              "type": "xp",
              "xp": 25
            }
          ]
        },
        {
          "id": "4C0F000000000027",
          "x": 19.5,
          "y": 26.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Schwebe-Forschung",
          "optional": false,
          "icon": {
            "item": "aeronautics:end_stone_powder",
            "displayName": "End Stone Powder",
            "mod": "aeronautics"
          },
          "description": [
            "&aEnd Stone Powder&r ist die Basis für das schwebende Wundermaterial.",
            "&7Ein bisschen Endstein, gut zermahlen."
          ],
          "dependencies": [
            "4C0F000000000026"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "aeronautics:end_stone_powder",
              "displayName": "End Stone Powder",
              "mod": "aeronautics",
              "count": 4
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 15
            },
            {
              "type": "xp",
              "xp": 10
            }
          ]
        },
        {
          "id": "4C0F000000000028",
          "x": 19.5,
          "y": 27.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Flüssiger Auftrieb",
          "optional": false,
          "icon": {
            "item": "aeronautics:levitite_blend_bucket",
            "displayName": "Levitite Blend Bucket",
            "mod": "aeronautics"
          },
          "description": [
            "Im &aLevitite Blend Bucket&r schwappt die Vorstufe des Schwebematerials.",
            "&7Nicht trinken."
          ],
          "dependencies": [
            "4C0F000000000027"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "aeronautics:levitite_blend_bucket",
              "displayName": "Levitite Blend Bucket",
              "mod": "aeronautics",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 15
            },
            {
              "type": "xp",
              "xp": 10
            }
          ]
        },
        {
          "id": "4C0F000000000029",
          "x": 19.5,
          "y": 29.0,
          "shape": "circle",
          "size": 1.25,
          "title": "Levitite",
          "optional": false,
          "icon": {
            "item": "aeronautics:levitite",
            "displayName": "Levitite",
            "mod": "aeronautics"
          },
          "description": [
            "&aLevitite&r — der Stoff, der leichter ist als der gesunde Menschenverstand",
            "es erlaubt. Damit schwebt selbst schwerer Stahl."
          ],
          "dependencies": [
            "4C0F000000000028"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "aeronautics:levitite",
              "displayName": "Levitite",
              "mod": "aeronautics",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 2
            },
            {
              "type": "xp",
              "xp": 20
            }
          ]
        },
        {
          "id": "4C0F00000000002A",
          "x": 18.5,
          "y": 30.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Perlglanz-Levitite",
          "optional": false,
          "icon": {
            "item": "aeronautics:pearlescent_levitite",
            "displayName": "Pearlescent Levitite",
            "mod": "aeronautics"
          },
          "description": [
            "&dPearlescent Levitite&r ist die Premium-Version: mehr Auftrieb, mehr Glanz.",
            "&7Für Schiffe, die beeindrucken sollen."
          ],
          "dependencies": [
            "4C0F000000000029"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "aeronautics:pearlescent_levitite",
              "displayName": "Pearlescent Levitite",
              "mod": "aeronautics",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 3
            },
            {
              "type": "xp",
              "xp": 25
            }
          ]
        },
        {
          "id": "4C0F00000000002B",
          "x": 24.0,
          "y": 26.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Smarter Schub",
          "optional": false,
          "icon": {
            "item": "aeronautics:smart_propeller",
            "displayName": "Smart Propeller",
            "mod": "aeronautics"
          },
          "description": [
            "Der &aSmart Propeller&r lässt sich feiner steuern — Anstellwinkel inklusive.",
            "&7Fliegen für Fortgeschrittene."
          ],
          "dependencies": [
            "4C0F00000000001F"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "aeronautics:smart_propeller",
              "displayName": "Smart Propeller",
              "mod": "aeronautics",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 1
            },
            {
              "type": "xp",
              "xp": 15
            }
          ]
        },
        {
          "id": "4C0F00000000002C",
          "x": 24.0,
          "y": 27.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Gleichgewicht",
          "optional": false,
          "icon": {
            "item": "aeronautics:gyroscopic_propeller_bearing",
            "displayName": "Gyroscopic Propeller Bearing",
            "mod": "aeronautics"
          },
          "description": [
            "Das &aGyroscopic Propeller Bearing&r hält dein Schiff stabil in der Luft.",
            "&7Damit es nicht kippt, wenn der Kapitän niest."
          ],
          "dependencies": [
            "4C0F00000000002B"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "aeronautics:gyroscopic_propeller_bearing",
              "displayName": "Gyroscopic Propeller Bearing",
              "mod": "aeronautics",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 2
            },
            {
              "type": "xp",
              "xp": 20
            }
          ]
        },
        {
          "id": "4C0F00000000002D",
          "x": 22.0,
          "y": 28.0,
          "shape": "gear",
          "size": 2.0,
          "title": "Dein erstes Luftschiff",
          "optional": false,
          "icon": {
            "item": "aeronautics:white_envelope",
            "displayName": "White Envelope",
            "mod": "aeronautics"
          },
          "description": [
            "Jetzt wird's ernst: baue ein richtiges, abhebendes &dLuftschiff&r mit",
            "Hülle, Antrieb und einem Platz zum Stehen.",
            "",
            "Hak ab, wenn dein Schiff in der Luft bleibt."
          ],
          "dependencies": [
            "4C0F000000000026",
            "4C0F000000000020"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:crystal_coin",
              "displayName": "Crystal Coin",
              "mod": "magic_coins",
              "count": 1
            },
            {
              "type": "xp",
              "xp": 40
            }
          ]
        },
        {
          "id": "4C0F00000000002E",
          "x": 24.0,
          "y": 29.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Bordkanone (Kartoffel!)",
          "optional": false,
          "icon": {
            "item": "aeronautics:mounted_potato_cannon",
            "displayName": "Mounted Potato Cannon",
            "mod": "aeronautics"
          },
          "description": [
            "Montiere eine &6Mounted Potato Cannon&r an dein Schiff. Verteidigung",
            "schmeckt am besten stärkehaltig. &7(Passt zum Kartoffelboss-Plan …)"
          ],
          "dependencies": [
            "4C0F00000000002D"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "aeronautics:mounted_potato_cannon",
              "displayName": "Mounted Potato Cannon",
              "mod": "aeronautics",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 2
            },
            {
              "type": "xp",
              "xp": 20
            }
          ]
        },
        {
          "id": "4C0F00000000002F",
          "x": 22.0,
          "y": 29.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Volle Kontrolle",
          "optional": false,
          "icon": {
            "item": "aeronautics:smart_propeller",
            "displayName": "Smart Propeller",
            "mod": "aeronautics"
          },
          "description": [
            "Setze dich ans Steuer und fliege dein Schiff kontrolliert — vor, zurück,",
            "hoch, runter. &7Mit Gyroskop bleibt alles ruhig."
          ],
          "dependencies": [
            "4C0F00000000002D",
            "4C0F00000000002C"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 3
            },
            {
              "type": "xp",
              "xp": 30
            }
          ]
        },
        {
          "id": "4C0F000000000030",
          "x": 20.5,
          "y": 30.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Cloud Skipper",
          "optional": false,
          "icon": {
            "item": "aeronautics:music_disc_cloud_skipper",
            "displayName": "Music Disc Cloud Skipper",
            "mod": "aeronautics"
          },
          "description": [
            "Spür die Freiheit über den Wolken. Schnapp dir die Musik-Disc",
            "&aCloud Skipper&r für die perfekte Flug-Atmosphäre."
          ],
          "dependencies": [
            "4C0F00000000002D"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "aeronautics:music_disc_cloud_skipper",
              "displayName": "Music Disc Cloud Skipper",
              "mod": "aeronautics",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 1
            },
            {
              "type": "xp",
              "xp": 15
            }
          ]
        },
        {
          "id": "4C0F000000000031",
          "x": 23.5,
          "y": 31.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Hoch hinaus",
          "optional": false,
          "icon": {
            "item": "minecraft:spyglass",
            "displayName": "Spyglass",
            "mod": "minecraft"
          },
          "description": [
            "Steig auf &eHöhe Y = 300&r oder höher. Von hier oben sieht man dank",
            "&aDistant Horizons&r die ganze Welt."
          ],
          "dependencies": [
            "4C0F00000000002F"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 3
            },
            {
              "type": "xp",
              "xp": 30
            }
          ]
        },
        {
          "id": "4C0F000000000032",
          "x": 22.0,
          "y": 31.0,
          "shape": "circle",
          "size": 1.25,
          "title": "Luftfracht",
          "optional": false,
          "icon": {
            "item": "minecraft:chest",
            "displayName": "Chest",
            "mod": "minecraft"
          },
          "description": [
            "Transportiere Waren per Luftschiff von einer Kolonie zur nächsten —",
            "schneller als jeder Zug über Berge. &7Logistik, aber mit Stil."
          ],
          "dependencies": [
            "4C0F00000000002F"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:crystal_coin",
              "displayName": "Crystal Coin",
              "mod": "magic_coins",
              "count": 1
            },
            {
              "type": "xp",
              "xp": 35
            }
          ]
        },
        {
          "id": "4C0F000000000033",
          "x": 20.5,
          "y": 31.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Gemeinsam abheben",
          "optional": false,
          "icon": {
            "item": "minecraft:cake",
            "displayName": "Cake",
            "mod": "minecraft"
          },
          "description": [
            "Nimm einen Mitspieler an Bord und macht zusammen einen Rundflug.",
            "&7SMP-Momente, die bleiben."
          ],
          "dependencies": [
            "4C0F00000000002F"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 3
            },
            {
              "type": "xp",
              "xp": 25
            }
          ]
        },
        {
          "id": "4C0F000000000034",
          "x": 22.0,
          "y": 32.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Die kleine Flotte",
          "optional": false,
          "icon": {
            "item": "aeronautics:blue_envelope",
            "displayName": "Blue Envelope",
            "mod": "aeronautics"
          },
          "description": [
            "Ein Schiff ist gut, drei sind eine Flotte. Baue &emehrere Luftschiffe&r",
            "und parke sie stolz über deiner Basis."
          ],
          "dependencies": [
            "4C0F000000000032"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:crystal_coin",
              "displayName": "Crystal Coin",
              "mod": "magic_coins",
              "count": 2
            },
            {
              "type": "xp",
              "xp": 45
            }
          ]
        },
        {
          "id": "4C0F000000000035",
          "x": 22.0,
          "y": 34.0,
          "shape": "gear",
          "size": 2.0,
          "title": "Herr der Lüfte",
          "optional": false,
          "icon": {
            "item": "aeronautics:aviators_goggles",
            "displayName": "Aviators Goggles",
            "mod": "aeronautics"
          },
          "description": [
            "Du hast den Himmel gezähmt: Schiffe, Steuerung, Fracht, Flotte.",
            "&6Wenige werden je so hoch hinauskommen wie du.&r"
          ],
          "dependencies": [
            "4C0F000000000034",
            "4C0F00000000002E",
            "4C0F00000000002A"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:crystal_coin",
              "displayName": "Crystal Coin",
              "mod": "magic_coins",
              "count": 4
            },
            {
              "type": "item",
              "item": "aeronautics:pearlescent_levitite",
              "displayName": "Pearlescent Levitite",
              "mod": "aeronautics",
              "count": 4
            },
            {
              "type": "xp",
              "xp": 60
            }
          ]
        },
        {
          "id": "4C0F000000000036",
          "x": 0.0,
          "y": 42.0,
          "shape": "hexagon",
          "size": 1.5,
          "title": "Entdecke die Welt",
          "optional": false,
          "icon": {
            "item": "minecraft:filled_map",
            "displayName": "Filled Map",
            "mod": "minecraft"
          },
          "description": [
            "Die Welt ist riesig und realistisch: &aTerralith&r + &aTectonic&r zaubern",
            "epische Biome und Gebirge. Erkunde mindestens &e3 verschiedene&r Biome."
          ],
          "dependencies": [
            "57A7A5C79389A96A"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:map",
              "displayName": "Map",
              "mod": "minecraft",
              "count": 1
            },
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 20
            },
            {
              "type": "xp",
              "xp": 15
            }
          ]
        },
        {
          "id": "4C0F000000000037",
          "x": 2.0,
          "y": 42.0,
          "shape": "circle",
          "size": 1.25,
          "title": "Das Schienennetz",
          "optional": false,
          "icon": {
            "item": "create:track",
            "displayName": "Track",
            "mod": "create"
          },
          "description": [
            "Der große Traum: Zivilisationen per Zug verbinden. Verlege eine",
            "&bZugstrecke zwischen zwei Kolonien&r (Bahnhof ↔ Bahnhof)."
          ],
          "dependencies": [
            "4C0F000000000036"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 5
            },
            {
              "type": "xp",
              "xp": 30
            }
          ]
        },
        {
          "id": "4C0F000000000038",
          "x": 0.0,
          "y": 43.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Weite Sicht (Distant Horizons)",
          "optional": false,
          "icon": {
            "item": "minecraft:spyglass",
            "displayName": "Spyglass",
            "mod": "minecraft"
          },
          "description": [
            "&aDistant Horizons&r rendert das Gelände als LODs bis zum Horizont.",
            "&7Tipp: Für flüssiges DH empfiehlt sich der ZGC-Garbage-Collector (Java 21).",
            "Sichtweite/Qualität in den DH-Einstellungen justieren; Shader optional."
          ],
          "dependencies": [
            "4C0F000000000036"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:silver_coin",
              "displayName": "Silver Coin",
              "mod": "magic_coins",
              "count": 10
            },
            {
              "type": "xp",
              "xp": 10
            }
          ]
        },
        {
          "id": "4C0F000000000039",
          "x": 0.0,
          "y": 48.0,
          "shape": "hexagon",
          "size": 1.5,
          "title": "Münzwirtschaft (Magic Coins)",
          "optional": false,
          "icon": {
            "item": "magic_coins:gold_coin",
            "displayName": "Gold Coin",
            "mod": "magic_coins"
          },
          "description": [
            "&eMünzen&r sind der rote Faden: Quests belohnen dich mit Silber-, Gold-",
            "und Kristallmünzen. Besitze gleichzeitig mindestens &e3 Goldmünzen&r."
          ],
          "dependencies": [
            "4C0F000000000036"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 3
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 2
            },
            {
              "type": "xp",
              "xp": 15
            }
          ]
        },
        {
          "id": "4C0F00000000003A",
          "x": 2.0,
          "y": 48.0,
          "shape": "circle",
          "size": 1.25,
          "title": "Handel (Create: Numismatics)",
          "optional": false,
          "icon": {
            "item": "numismatics:vendor",
            "displayName": "Vendor",
            "mod": "numismatics"
          },
          "description": [
            "&aNumismatics&r bringt physische Münzen, Bankkarten und Automaten.",
            "Baue einen &aVendor&r und wickle einen Handel ab."
          ],
          "dependencies": [
            "4C0F000000000039"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "numismatics:vendor",
              "displayName": "Vendor",
              "mod": "numismatics",
              "count": 1
            },
            {
              "type": "item",
              "item": "numismatics:spur",
              "displayName": "Spur",
              "mod": "numismatics",
              "count": 8
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 3
            },
            {
              "type": "xp",
              "xp": 20
            }
          ]
        },
        {
          "id": "4C0F00000000003B",
          "x": 4.0,
          "y": 48.0,
          "shape": "circle",
          "size": 1.25,
          "title": "Bereit fürs Endgame",
          "optional": false,
          "icon": {
            "item": "magic_coins:crystal_coin",
            "displayName": "Crystal Coin",
            "mod": "magic_coins"
          },
          "description": [
            "Du hast Farm, Kolonie, Technik und Wirtschaft gemeistert.",
            "Jetzt warten im &c🏆 Endgame&r die ganz großen Ziele.",
            "",
            "Schließe deine erste Endgame-Quest ab!"
          ],
          "dependencies": [
            "4C0F00000000003A"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:crystal_coin",
              "displayName": "Crystal Coin",
              "mod": "magic_coins",
              "count": 2
            },
            {
              "type": "xp",
              "xp": 40
            }
          ]
        },
        {
          "id": "4C0F00000000003C",
          "x": 0.0,
          "y": 56.0,
          "shape": "gear",
          "size": 2.0,
          "title": "Der lange Weg",
          "optional": false,
          "icon": {
            "item": "minecraft:nether_star",
            "displayName": "Nether Star",
            "mod": "minecraft"
          },
          "description": [
            "Du hast die Grundlagen gemeistert — jetzt beginnt das große Spiel.",
            "Hier warten die ganz großen Ziele. Werde zur &6Legende des SMP&r."
          ],
          "dependencies": [
            "4C0F00000000003A",
            "4C0F000000000035"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:gold_coin",
              "displayName": "Gold Coin",
              "mod": "magic_coins",
              "count": 5
            },
            {
              "type": "xp",
              "xp": 30
            }
          ]
        },
        {
          "id": "4C0F00000000003D",
          "x": -3.0,
          "y": 54.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Mega-Kolonie",
          "optional": false,
          "icon": {
            "item": "minecolonies:blockhuttownhall",
            "displayName": "Blockhuttownhall",
            "mod": "minecolonies"
          },
          "description": [
            "Lass eine Kolonie zur Großstadt wachsen: &750+ Bürger&r und viele Gebäude."
          ],
          "dependencies": [
            "4C0F00000000003C"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:crystal_coin",
              "displayName": "Crystal Coin",
              "mod": "magic_coins",
              "count": 2
            },
            {
              "type": "xp",
              "xp": 40
            }
          ]
        },
        {
          "id": "4C0F00000000003E",
          "x": -1.5,
          "y": 53.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Schienen-Imperium",
          "optional": false,
          "icon": {
            "item": "create:track_station",
            "displayName": "Track Station",
            "mod": "create"
          },
          "description": [
            "Verbinde &emindestens drei Kolonien&r zu einem Zug-Netzwerk."
          ],
          "dependencies": [
            "4C0F00000000003C"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:crystal_coin",
              "displayName": "Crystal Coin",
              "mod": "magic_coins",
              "count": 2
            },
            {
              "type": "xp",
              "xp": 40
            }
          ]
        },
        {
          "id": "4C0F00000000003F",
          "x": 1.5,
          "y": 53.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Luftschiff-Flotte",
          "optional": false,
          "icon": {
            "item": "aeronautics:aviators_goggles",
            "displayName": "Aviators Goggles",
            "mod": "aeronautics"
          },
          "description": [
            "&bAeronautics&r-Meisterschaft: eine ganze Flotte großer Luftschiffe."
          ],
          "dependencies": [
            "4C0F00000000003C"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:crystal_coin",
              "displayName": "Crystal Coin",
              "mod": "magic_coins",
              "count": 3
            },
            {
              "type": "xp",
              "xp": 50
            }
          ]
        },
        {
          "id": "4C0F000000000040",
          "x": 3.0,
          "y": 54.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Die Großfabrik",
          "optional": false,
          "icon": {
            "item": "create:mechanical_arm",
            "displayName": "Mechanical Arm",
            "mod": "create"
          },
          "description": [
            "Eine &evollautomatische Create-Fabrik&r, die ein komplexes Produkt ohne",
            "Handarbeit fertigt (Factory Gauges / Packages)."
          ],
          "dependencies": [
            "4C0F00000000003C"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:crystal_coin",
              "displayName": "Crystal Coin",
              "mod": "magic_coins",
              "count": 2
            },
            {
              "type": "xp",
              "xp": 40
            }
          ]
        },
        {
          "id": "4C0F000000000041",
          "x": 3.0,
          "y": 57.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Energie-Imperium",
          "optional": false,
          "icon": {
            "item": "create:shaft",
            "displayName": "Shaft",
            "mod": "create"
          },
          "description": [
            "Ein großes Stromnetz aus &aNew Age / Createaddition / Diesel / TFMG&r."
          ],
          "dependencies": [
            "4C0F00000000003C"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:crystal_coin",
              "displayName": "Crystal Coin",
              "mod": "magic_coins",
              "count": 2
            },
            {
              "type": "xp",
              "xp": 40
            }
          ]
        },
        {
          "id": "4C0F000000000042",
          "x": 1.5,
          "y": 58.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Selbstversorger",
          "optional": false,
          "icon": {
            "item": "farmersdelight:cooking_pot",
            "displayName": "Cooking Pot",
            "mod": "farmersdelight"
          },
          "description": [
            "Vollautomatische Nahrung mit &aCreate: Central Kitchen&r — nie wieder Hunger."
          ],
          "dependencies": [
            "4C0F00000000003C"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:crystal_coin",
              "displayName": "Crystal Coin",
              "mod": "magic_coins",
              "count": 2
            },
            {
              "type": "xp",
              "xp": 40
            }
          ]
        },
        {
          "id": "4C0F000000000043",
          "x": -3.0,
          "y": 57.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Münz-Vermögen",
          "optional": false,
          "icon": {
            "item": "magic_coins:crystal_coin",
            "displayName": "Crystal Coin",
            "mod": "magic_coins"
          },
          "description": [
            "Besitze gleichzeitig &emindestens 5 Kristallmünzen&r — der Gipfel des Wohlstands."
          ],
          "dependencies": [
            "4C0F00000000003C"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "magic_coins:crystal_coin",
              "displayName": "Crystal Coin",
              "mod": "magic_coins",
              "count": 5
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:crystal_coin",
              "displayName": "Crystal Coin",
              "mod": "magic_coins",
              "count": 3
            },
            {
              "type": "xp",
              "xp": 40
            }
          ]
        },
        {
          "id": "4C0F000000000044",
          "x": -1.5,
          "y": 58.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Handelsimperium",
          "optional": false,
          "icon": {
            "item": "numismatics:vendor",
            "displayName": "Vendor",
            "mod": "numismatics"
          },
          "description": [
            "Ein &aNumismatics&r-Handelsnetz mit mehreren Automaten zwischen den Kolonien."
          ],
          "dependencies": [
            "4C0F00000000003C"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:crystal_coin",
              "displayName": "Crystal Coin",
              "mod": "magic_coins",
              "count": 2
            },
            {
              "type": "xp",
              "xp": 40
            }
          ]
        },
        {
          "id": "4C0F000000000045",
          "x": 0.0,
          "y": 52.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Welt-Entdecker",
          "optional": false,
          "icon": {
            "item": "minecraft:filled_map",
            "displayName": "Filled Map",
            "mod": "minecraft"
          },
          "description": [
            "Entdecke &e15 verschiedene Biome&r von Terralith \\& Tectonic."
          ],
          "dependencies": [
            "4C0F00000000003C"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:crystal_coin",
              "displayName": "Crystal Coin",
              "mod": "magic_coins",
              "count": 2
            },
            {
              "type": "xp",
              "xp": 40
            }
          ]
        },
        {
          "id": "4C0F000000000046",
          "x": 4.5,
          "y": 56.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Der Kartoffelboss (geplant)",
          "optional": true,
          "icon": {
            "item": "minecraft:baked_potato",
            "displayName": "Baked Potato",
            "mod": "minecraft"
          },
          "description": [
            "§oGeplantes Eigen-Projekt:§r ein optionaler Boss — der &6Kartoffelboss&r.",
            "Wird aktiviert, sobald die Mod fertig ist. &7Platzhalter."
          ],
          "dependencies": [
            "4C0F00000000003C"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:crystal_coin",
              "displayName": "Crystal Coin",
              "mod": "magic_coins",
              "count": 1
            }
          ]
        },
        {
          "id": "4C0F000000000047",
          "x": 0.0,
          "y": 60.0,
          "shape": "gear",
          "size": 2.0,
          "title": "Legende des SMP",
          "optional": false,
          "icon": {
            "item": "minecraft:nether_star",
            "displayName": "Nether Star",
            "mod": "minecraft"
          },
          "description": [
            "Alle großen Ziele erreicht. &6Herzlichen Glückwunsch — du bist eine Legende!&r"
          ],
          "dependencies": [
            "4C0F00000000003D",
            "4C0F00000000003E",
            "4C0F00000000003F",
            "4C0F000000000040",
            "4C0F000000000041",
            "4C0F000000000042",
            "4C0F000000000043",
            "4C0F000000000044",
            "4C0F000000000045"
          ],
          "tasks": [
            {
              "type": "checkmark"
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "magic_coins:crystal_coin",
              "displayName": "Crystal Coin",
              "mod": "magic_coins",
              "count": 10
            },
            {
              "type": "item",
              "item": "minecraft:nether_star",
              "displayName": "Nether Star",
              "mod": "minecraft",
              "count": 1
            },
            {
              "type": "xp",
              "xp": 100
            }
          ]
        },
        {
          "id": "57A7A5C79389A96A",
          "x": -1.0,
          "y": 27.0,
          "shape": "gear",
          "size": 3.0,
          "title": "Andesit — der Anfang von allem",
          "optional": false,
          "icon": {
            "item": "create:large_cogwheel",
            "displayName": "Large Cogwheel",
            "mod": "create"
          },
          "description": [
            "&bCreate&r liebt Andesit. Grab eine ordentliche Menge ab —",
            "daraus wird gleich die wichtigste Zutat überhaupt."
          ],
          "dependencies": [
            "4C0F000000000019"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "minecraft:andesite",
              "displayName": "Andesite",
              "mod": "minecraft",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:andesite",
              "displayName": "Andesite",
              "mod": "minecraft",
              "count": 16
            }
          ]
        },
        {
          "id": "0F16498769DFB3B0",
          "x": 1.5,
          "y": 27.0,
          "shape": "circle",
          "size": 1.75,
          "title": "Andesite Alloy",
          "optional": false,
          "icon": null,
          "description": [
            "Die &aAndesit-Legierung&r ist das Brot-und-Butter-Material von Create.",
            "&7Ohne sie läuft hier gar nichts. Stell einen Vorrat her!"
          ],
          "dependencies": [
            "57A7A5C79389A96A"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:andesite_alloy",
              "displayName": "Andesite Alloy",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:andesite_alloy",
              "displayName": "Andesite Alloy",
              "mod": "create",
              "count": 8
            }
          ]
        },
        {
          "id": "5B36DE3826F26963",
          "x": 3.0,
          "y": 25.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Die Welle",
          "optional": false,
          "icon": null,
          "description": [
            "Die &aWelle&r leitet Rotation von A nach B. Unscheinbar, unverzichtbar."
          ],
          "dependencies": [
            "0F16498769DFB3B0"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:shaft",
              "displayName": "Shaft",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:shaft",
              "displayName": "Shaft",
              "mod": "create",
              "count": 8
            }
          ]
        },
        {
          "id": "1E9B2D814F50A265",
          "x": 2.0,
          "y": 29.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Encased Fan",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aEncased Fan&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "3AF2BC9A0E298882"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:encased_fan",
              "displayName": "Encased Fan",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:nozzle",
              "displayName": "Nozzle",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "minecraft:lava_bucket",
              "displayName": "Lava Bucket",
              "mod": "minecraft",
              "count": 1
            },
            {
              "type": "item",
              "item": "minecraft:soul_campfire",
              "displayName": "Soul Campfire",
              "mod": "minecraft",
              "count": 1
            }
          ]
        },
        {
          "id": "4285510271B5223D",
          "x": 3.0,
          "y": 23.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Gearbox",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aGearbox&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "5B36DE3826F26963"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:gearbox",
              "displayName": "Gearbox",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:shaft",
              "displayName": "Shaft",
              "mod": "create",
              "count": 4
            },
            {
              "type": "item",
              "item": "create:vertical_gearbox",
              "displayName": "Vertical Gearbox",
              "mod": "create",
              "count": 1
            }
          ]
        },
        {
          "id": "2BB3DB19D5EFC7E2",
          "x": 3.0,
          "y": 21.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Clutch",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aClutch&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "5B36DE3826F26963"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:clutch",
              "displayName": "Clutch",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:lever",
              "displayName": "Lever",
              "mod": "minecraft",
              "count": 1
            },
            {
              "type": "item",
              "item": "minecraft:redstone",
              "displayName": "Redstone",
              "mod": "minecraft",
              "count": 12
            }
          ]
        },
        {
          "id": "67A46ED73E488CEE",
          "x": 2.0,
          "y": 23.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Gearshift",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aGearshift&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "5B36DE3826F26963"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:gearshift",
              "displayName": "Gearshift",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:shaft",
              "displayName": "Shaft",
              "mod": "create",
              "count": 3
            },
            {
              "type": "item",
              "item": "minecraft:lever",
              "displayName": "Lever",
              "mod": "minecraft",
              "count": 1
            }
          ]
        },
        {
          "id": "7F8E50FA436DB4E6",
          "x": 4.0,
          "y": 23.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Kettenantrieb",
          "optional": false,
          "icon": null,
          "description": [
            "Der &aKettenantrieb&r verteilt Drehkraft elegant um Ecken und über Strecken."
          ],
          "dependencies": [
            "5B36DE3826F26963"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:encased_chain_drive",
              "displayName": "Encased Chain Drive",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:encased_chain_drive",
              "displayName": "Encased Chain Drive",
              "mod": "create",
              "count": 4
            }
          ]
        },
        {
          "id": "54EC1C7FC1DA9107",
          "x": 4.0,
          "y": 22.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Regelbares Kettengetriebe",
          "optional": false,
          "icon": null,
          "description": [
            "Damit steuerst du die Drehzahl per Redstone. Tempo nach Bedarf."
          ],
          "dependencies": [
            "7F8E50FA436DB4E6"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:adjustable_chain_gearshift",
              "displayName": "Adjustable Chain Gearshift",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:adjustable_chain_gearshift",
              "displayName": "Adjustable Chain Gearshift",
              "mod": "create",
              "count": 2
            },
            {
              "type": "item",
              "item": "minecraft:repeater",
              "displayName": "Repeater",
              "mod": "minecraft",
              "count": 1
            },
            {
              "type": "item",
              "item": "minecraft:redstone",
              "displayName": "Redstone",
              "mod": "minecraft",
              "count": 3
            }
          ]
        },
        {
          "id": "2D41B04C75FA02BC",
          "x": 3.0,
          "y": 27.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Mechanische Presse",
          "optional": false,
          "icon": null,
          "description": [
            "Die &aPresse&r plättet, prägt und presst. Bleche, Pflaster, Münzrohlinge …",
            "&7Das nützlichste *Klonk* im Spiel."
          ],
          "dependencies": [
            "3AF2BC9A0E298882"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:mechanical_press",
              "displayName": "Mechanical Press",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:iron_ingot",
              "displayName": "Iron Ingot",
              "mod": "minecraft",
              "count": 9
            },
            {
              "type": "item",
              "item": "minecraft:gold_ingot",
              "displayName": "Gold Ingot",
              "mod": "minecraft",
              "count": 1
            }
          ]
        },
        {
          "id": "5DC892BA79EB52EC",
          "x": 4.0,
          "y": 27.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Mechanischer Mixer",
          "optional": false,
          "icon": null,
          "description": [
            "Der &aMixer&r rührt über einem Becken alles zusammen — Legierungen, Teige, Tränke."
          ],
          "dependencies": [
            "3AF2BC9A0E298882"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:mechanical_mixer",
              "displayName": "Mechanical Mixer",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:glowstone_dust",
              "displayName": "Glowstone Dust",
              "mod": "minecraft",
              "count": 5
            },
            {
              "type": "item",
              "item": "minecraft:redstone",
              "displayName": "Redstone",
              "mod": "minecraft",
              "count": 5
            },
            {
              "type": "item",
              "item": "minecraft:nether_wart",
              "displayName": "Nether Wart",
              "mod": "minecraft",
              "count": 5
            }
          ]
        },
        {
          "id": "75CBB5BD8C1DFEA1",
          "x": -3.5,
          "y": 25.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Das Becken",
          "optional": false,
          "icon": null,
          "description": [
            "Das &aBecken&r sammelt Zutaten für Mixer und Presse. Die kleine Küche der Maschinen."
          ],
          "dependencies": [
            "483892F0A0F75B97",
            "13AEBC331F29BC3D"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:basin",
              "displayName": "Basin",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:basin",
              "displayName": "Basin",
              "mod": "create",
              "count": 1
            }
          ]
        },
        {
          "id": "1B182A30604655E2",
          "x": 4.0,
          "y": 29.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Blaze Burner",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aBlaze Burner&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "4C0F000000000019"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:blaze_burner",
              "displayName": "Blaze Burner",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:empty_blaze_burner",
              "displayName": "Empty Blaze Burner",
              "mod": "create",
              "count": 3
            },
            {
              "type": "item",
              "item": "minecraft:coal_block",
              "displayName": "Coal Block",
              "mod": "minecraft",
              "count": 4
            }
          ]
        },
        {
          "id": "45EC31812FB9934D",
          "x": -4.5,
          "y": 32.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Mechanical Piston",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aMechanical Piston&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "47897D827C50629D",
            "69EE22CB4FF1E591"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:mechanical_piston",
              "displayName": "Mechanical Piston",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:piston_extension_pole",
              "displayName": "Piston Extension Pole",
              "mod": "create",
              "count": 5
            },
            {
              "type": "item",
              "item": "minecraft:slime_ball",
              "displayName": "Slime Ball",
              "mod": "minecraft",
              "count": 3
            }
          ]
        },
        {
          "id": "29917E6196649F5D",
          "x": 5.0,
          "y": 26.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Speedometer",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aSpeedometer&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "3C892B33758B7BA6",
            "3AF2BC9A0E298882"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:speedometer",
              "displayName": "Speedometer",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:shaft",
              "displayName": "Shaft",
              "mod": "create",
              "count": 8
            }
          ]
        },
        {
          "id": "48BE7DAC5082044D",
          "x": 6.0,
          "y": 25.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Stressometer",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aStressometer&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "3C892B33758B7BA6",
            "3AF2BC9A0E298882"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:stressometer",
              "displayName": "Stressometer",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:shaft",
              "displayName": "Shaft",
              "mod": "create",
              "count": 8
            }
          ]
        },
        {
          "id": "09936F8FCEA72C5C",
          "x": -6.5,
          "y": 32.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Cart Assembler",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aCart Assembler&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "69EE22CB4FF1E591"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:cart_assembler",
              "displayName": "Cart Assembler",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:minecart",
              "displayName": "Minecart",
              "mod": "minecraft",
              "count": 2
            },
            {
              "type": "item",
              "item": "minecraft:lever",
              "displayName": "Lever",
              "mod": "minecraft",
              "count": 1
            },
            {
              "type": "item",
              "item": "minecraft:slime_ball",
              "displayName": "Slime Ball",
              "mod": "minecraft",
              "count": 3
            }
          ]
        },
        {
          "id": "51EA6B1452883AB2",
          "x": -6.0,
          "y": 31.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Linear Chassis",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aLinear Chassis&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "69EE22CB4FF1E591"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:linear_chassis",
              "displayName": "Linear Chassis",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:slime_ball",
              "displayName": "Slime Ball",
              "mod": "minecraft",
              "count": 3
            }
          ]
        },
        {
          "id": "459BA85E48B343AE",
          "x": -5.0,
          "y": 31.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Radial-Chassis",
          "optional": false,
          "icon": null,
          "description": [
            "Das &aChassis&r hält große Kontraptionen zusammen, wenn sie sich drehen."
          ],
          "dependencies": [
            "69EE22CB4FF1E591"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:radial_chassis",
              "displayName": "Radial Chassis",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:radial_chassis",
              "displayName": "Radial Chassis",
              "mod": "create",
              "count": 3
            },
            {
              "type": "item",
              "item": "minecraft:slime_ball",
              "displayName": "Slime Ball",
              "mod": "minecraft",
              "count": 3
            }
          ]
        },
        {
          "id": "76CBFA38D021AC95",
          "x": 6.75,
          "y": 21.75,
          "shape": "circle",
          "size": 1.25,
          "title": "Windmühlen-Lager",
          "optional": false,
          "icon": null,
          "description": [
            "Bau dir eine &aWindmühle&r — Segel dran, und der Wind erledigt den Rest."
          ],
          "dependencies": [
            "6893D537716AA748"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:windmill_bearing",
              "displayName": "Windmill Bearing",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:white_sail",
              "displayName": "White Sail",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:white_sail",
              "displayName": "White Sail",
              "mod": "create",
              "count": 8
            },
            {
              "type": "item",
              "item": "create:super_glue",
              "displayName": "Super Glue",
              "mod": "create",
              "count": 1
            }
          ]
        },
        {
          "id": "3029E1E133B91ED8",
          "x": -5.75,
          "y": 33.25,
          "shape": "circle",
          "size": 1.25,
          "title": "Mechanical Drill",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aMechanical Drill&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "69EE22CB4FF1E591"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:mechanical_drill",
              "displayName": "Mechanical Drill",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:iron_ore",
              "displayName": "Iron Ore",
              "mod": "minecraft",
              "count": 8
            },
            {
              "type": "item",
              "item": "minecraft:stone",
              "displayName": "Stone",
              "mod": "minecraft",
              "count": 10
            }
          ]
        },
        {
          "id": "72DCE154E1714890",
          "x": -5.75,
          "y": 34.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Mechanical Saw",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aMechanical Saw&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "69EE22CB4FF1E591"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:mechanical_saw",
              "displayName": "Mechanical Saw",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:oak_sapling",
              "displayName": "Oak Sapling",
              "mod": "minecraft",
              "count": 6
            },
            {
              "type": "item",
              "item": "minecraft:stone",
              "displayName": "Stone",
              "mod": "minecraft",
              "count": 10
            },
            {
              "type": "item",
              "item": "minecraft:deepslate",
              "displayName": "Deepslate",
              "mod": "minecraft",
              "count": 10
            }
          ]
        },
        {
          "id": "3314FBC4FEAE1D08",
          "x": 4.5,
          "y": 28.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Deployer",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aDeployer&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "3AF2BC9A0E298882"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:deployer",
              "displayName": "Deployer",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:andesite_alloy",
              "displayName": "Andesite Alloy",
              "mod": "create",
              "count": 3
            },
            {
              "type": "item",
              "item": "minecraft:copper_ingot",
              "displayName": "Copper Ingot",
              "mod": "minecraft",
              "count": 3
            },
            {
              "type": "item",
              "item": "create:brass_ingot",
              "displayName": "Brass Ingot",
              "mod": "create",
              "count": 3
            },
            {
              "type": "item",
              "item": "minecraft:stripped_oak_log",
              "displayName": "Stripped Oak Log",
              "mod": "minecraft",
              "count": 9
            }
          ]
        },
        {
          "id": "4C31649D721F76B5",
          "x": -7.0,
          "y": 34.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Mechanical Harvester",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aMechanical Harvester&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "69EE22CB4FF1E591"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:mechanical_harvester",
              "displayName": "Mechanical Harvester",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:wheat_seeds",
              "displayName": "Wheat Seeds",
              "mod": "minecraft",
              "count": 8
            },
            {
              "type": "item",
              "item": "minecraft:carrot",
              "displayName": "Carrot",
              "mod": "minecraft",
              "count": 8
            },
            {
              "type": "item",
              "item": "minecraft:potato",
              "displayName": "Potato",
              "mod": "minecraft",
              "count": 8
            }
          ]
        },
        {
          "id": "0759CA52EECF3B49",
          "x": -7.0,
          "y": 33.25,
          "shape": "circle",
          "size": 1.25,
          "title": "Mechanical Plough",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aMechanical Plough&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "69EE22CB4FF1E591"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:mechanical_plough",
              "displayName": "Mechanical Plough",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:dirt",
              "displayName": "Dirt",
              "mod": "minecraft",
              "count": 10
            },
            {
              "type": "item",
              "item": "supplementaries:bamboo_spikes",
              "displayName": "Bamboo Spikes",
              "mod": "supplementaries",
              "count": 4
            }
          ]
        },
        {
          "id": "3F663416E824720C",
          "x": -4.5,
          "y": 28.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Copper Casing",
          "optional": false,
          "icon": null,
          "description": [
            "Das &aKupfer-Gehäuse&r ist die Stufe für alles rund um Flüssigkeiten."
          ],
          "dependencies": [
            "7242F591DA474B37"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:copper_casing",
              "displayName": "Copper Casing",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:copper_casing",
              "displayName": "Copper Casing",
              "mod": "create",
              "count": 4
            }
          ]
        },
        {
          "id": "3F2C1A81C17D2D67",
          "x": 5.0,
          "y": 31.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Mechanischer Arm",
          "optional": false,
          "icon": null,
          "description": [
            "Der &aArm&r sortiert und befüllt punktgenau. Dein fleißigster Mitarbeiter."
          ],
          "dependencies": [
            "1712C3B3CF158843",
            "3C99017FD32B6DE2"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:mechanical_arm",
              "displayName": "Mechanical Arm",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:mechanical_arm",
              "displayName": "Mechanical Arm",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:depot",
              "displayName": "Depot",
              "mod": "create",
              "count": 3
            }
          ]
        },
        {
          "id": "47A6769B6BF1A46D",
          "x": -2.5,
          "y": 23.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Andesite Funnel",
          "optional": false,
          "icon": null,
          "description": [
            "Der &aTrichter&r zieht Items ein oder gibt sie aus. Andesit = die Einsteigerklasse."
          ],
          "dependencies": [
            "13AEBC331F29BC3D"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:andesite_funnel",
              "displayName": "Andesite Funnel",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:andesite_funnel",
              "displayName": "Andesite Funnel",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "minecraft:chest",
              "displayName": "Chest",
              "mod": "minecraft",
              "count": 1
            }
          ]
        },
        {
          "id": "495B0CC178B4CFA9",
          "x": 0.5,
          "y": 23.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Brass Funnel",
          "optional": false,
          "icon": null,
          "description": [
            "Der &aMessing-Trichter&r kann filtern — nur genau das durchlassen, was du willst."
          ],
          "dependencies": [
            "13AEBC331F29BC3D"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:brass_funnel",
              "displayName": "Brass Funnel",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:brass_funnel",
              "displayName": "Brass Funnel",
              "mod": "create",
              "count": 3
            },
            {
              "type": "item",
              "item": "create:belt_connector",
              "displayName": "Belt Connector",
              "mod": "create",
              "count": 5
            }
          ]
        },
        {
          "id": "7C8CDD259495A31A",
          "x": -3.0,
          "y": 22.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Andesite Tunnel",
          "optional": false,
          "icon": null,
          "description": [
            "Der &aTunnel&r verteilt Items auf Förderbändern sauber weiter."
          ],
          "dependencies": [
            "13AEBC331F29BC3D"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:andesite_tunnel",
              "displayName": "Andesite Tunnel",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:andesite_tunnel",
              "displayName": "Andesite Tunnel",
              "mod": "create",
              "count": 2
            },
            {
              "type": "item",
              "item": "create:belt_connector",
              "displayName": "Belt Connector",
              "mod": "create",
              "count": 4
            }
          ]
        },
        {
          "id": "78656C89EEE80DB5",
          "x": 1.0,
          "y": 22.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Brass Tunnel",
          "optional": false,
          "icon": null,
          "description": [
            "Der &aMessing-Tunnel&r verteilt und sortiert über mehrere Bänder. Logistik-Magie."
          ],
          "dependencies": [
            "13AEBC331F29BC3D"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:brass_tunnel",
              "displayName": "Brass Tunnel",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:brass_tunnel",
              "displayName": "Brass Tunnel",
              "mod": "create",
              "count": 3
            },
            {
              "type": "item",
              "item": "create:belt_connector",
              "displayName": "Belt Connector",
              "mod": "create",
              "count": 9
            }
          ]
        },
        {
          "id": "3D2A03EB2B91E9C1",
          "x": 0.0,
          "y": 22.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Schacht",
          "optional": false,
          "icon": null,
          "description": [
            "Der &aSchacht&r lässt Items vertikal rieseln — die Schwerkraft arbeitet für dich."
          ],
          "dependencies": [
            "13AEBC331F29BC3D"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:chute",
              "displayName": "Chute",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:chute",
              "displayName": "Chute",
              "mod": "create",
              "count": 4
            }
          ]
        },
        {
          "id": "4C77ABCD41383F32",
          "x": -6.5,
          "y": 28.5,
          "shape": "circle",
          "size": 0.8,
          "title": "Blaze-Kuchen",
          "optional": false,
          "icon": null,
          "description": [
            "Ein &aBlaze Cake&r macht den Blaze Burner so richtig heiß — für die harten Rezepte.",
            "&7Backen für Fortgeschrittene."
          ],
          "dependencies": [
            "1C2309DB4B890E71"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:blaze_cake",
              "displayName": "Blaze Cake",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:blaze_cake",
              "displayName": "Blaze Cake",
              "mod": "create",
              "count": 3
            }
          ]
        },
        {
          "id": "4194397DFD0199C2",
          "x": 6.0,
          "y": 30.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Mechanischer Kruster",
          "optional": false,
          "icon": null,
          "description": [
            "Mehrere &aKruster&r craften ganze Rezepte automatisch. Endlich Schluss mit Handarbeit!"
          ],
          "dependencies": [
            "3C99017FD32B6DE2"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:mechanical_crafter",
              "displayName": "Mechanical Crafter",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:mechanical_crafter",
              "displayName": "Mechanical Crafter",
              "mod": "create",
              "count": 3
            }
          ]
        },
        {
          "id": "75B14A09FE39EDDA",
          "x": -4.5,
          "y": 33.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Gantry Carriage",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aGantry Carriage&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "69EE22CB4FF1E591"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:gantry_carriage",
              "displayName": "Gantry Carriage",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:gantry_shaft",
              "displayName": "Gantry Shaft",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:gantry_shaft",
              "displayName": "Gantry Shaft",
              "mod": "create",
              "count": 8
            },
            {
              "type": "item",
              "item": "minecraft:slime_ball",
              "displayName": "Slime Ball",
              "mod": "minecraft",
              "count": 3
            }
          ]
        },
        {
          "id": "7EEEEDD5FF31ACD3",
          "x": 0.5,
          "y": 21.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Smart Chute",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aSmart Chute&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "3D2A03EB2B91E9C1"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:smart_chute",
              "displayName": "Smart Chute",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:chute",
              "displayName": "Chute",
              "mod": "create",
              "count": 7
            },
            {
              "type": "item",
              "item": "create:belt_connector",
              "displayName": "Belt Connector",
              "mod": "create",
              "count": 7
            }
          ]
        },
        {
          "id": "0CF69DBA9573A7B3",
          "x": -1.5,
          "y": 31.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Schematik-Tisch",
          "optional": false,
          "icon": null,
          "description": [
            "Am &aSchematik-Tisch&r lädst du Baupläne — kopiere ganze Bauwerke."
          ],
          "dependencies": [
            "57A7A5C79389A96A"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:schematic_table",
              "displayName": "Schematic Table",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": []
        },
        {
          "id": "7D67058592EE5958",
          "x": -0.5,
          "y": 31.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Schematik-Kanone",
          "optional": false,
          "icon": null,
          "description": [
            "Die &aSchematik-Kanone&r baut gespeicherte Schematics automatisch auf. Faulheit, aber effizient."
          ],
          "dependencies": [
            "0CF69DBA9573A7B3"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:schematicannon",
              "displayName": "Schematicannon",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": []
        },
        {
          "id": "24E658BA47367A44",
          "x": -3.5,
          "y": 33.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Rope Pulley",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aRope Pulley&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "69EE22CB4FF1E591"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:rope_pulley",
              "displayName": "Rope Pulley",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:andesite_casing",
              "displayName": "Andesite Casing",
              "mod": "create",
              "count": 8
            },
            {
              "type": "item",
              "item": "minecraft:slime_ball",
              "displayName": "Slime Ball",
              "mod": "minecraft",
              "count": 3
            }
          ]
        },
        {
          "id": "1C2309DB4B890E71",
          "x": -5.5,
          "y": 28.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Spout",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aSpout&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "3F663416E824720C"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:spout",
              "displayName": "Spout",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:bucket",
              "displayName": "Bucket",
              "mod": "minecraft",
              "count": 3
            },
            {
              "type": "item",
              "item": "minecraft:glass_bottle",
              "displayName": "Glass Bottle",
              "mod": "minecraft",
              "count": 3
            },
            {
              "type": "item",
              "item": "create:blaze_cake_base",
              "displayName": "Blaze Cake Base",
              "mod": "create",
              "count": 1
            }
          ]
        },
        {
          "id": "77382D4114E901CB",
          "x": -5.5,
          "y": 29.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Hose Pulley",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aHose Pulley&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "3F663416E824720C"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:hose_pulley",
              "displayName": "Hose Pulley",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:water_bucket",
              "displayName": "Water Bucket",
              "mod": "minecraft",
              "count": 2
            },
            {
              "type": "item",
              "item": "create:mechanical_pump",
              "displayName": "Mechanical Pump",
              "mod": "create",
              "count": 1
            }
          ]
        },
        {
          "id": "47897D827C50629D",
          "x": -3.5,
          "y": 32.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Kolben-Verlängerung",
          "optional": false,
          "icon": null,
          "description": [
            "Verlängert den mechanischen Kolben — schiebe Dinge richtig weit."
          ],
          "dependencies": [
            "0F16498769DFB3B0"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:piston_extension_pole",
              "displayName": "Piston Extension Pole",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:piston_extension_pole",
              "displayName": "Piston Extension Pole",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:andesite_casing",
              "displayName": "Andesite Casing",
              "mod": "create",
              "count": 3
            },
            {
              "type": "item",
              "item": "minecraft:slime_ball",
              "displayName": "Slime Ball",
              "mod": "minecraft",
              "count": 3
            }
          ]
        },
        {
          "id": "71B1B53A03A16296",
          "x": -3.5,
          "y": 29.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Portable Fluid Interface",
          "optional": false,
          "icon": null,
          "description": [
            "Tankt fahrende Kontraptionen automatisch ab oder auf. Praktisch für Züge \\& Schiffe."
          ],
          "dependencies": [
            "3F663416E824720C",
            "69EE22CB4FF1E591"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:portable_fluid_interface",
              "displayName": "Portable Fluid Interface",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:portable_fluid_interface",
              "displayName": "Portable Fluid Interface",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:fluid_tank",
              "displayName": "Fluid Tank",
              "mod": "create",
              "count": 1
            }
          ]
        },
        {
          "id": "13AEBC331F29BC3D",
          "x": -1.0,
          "y": 24.0,
          "shape": "circle",
          "size": 1.75,
          "title": "Förderband",
          "optional": false,
          "icon": null,
          "description": [
            "Zwei Wellen, ein &aRiemen&r dazwischen — fertig ist das Fließband. Klassiker."
          ],
          "dependencies": [
            "57A7A5C79389A96A"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:belt_connector",
              "displayName": "Belt Connector",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:belt_connector",
              "displayName": "Belt Connector",
              "mod": "create",
              "count": 16
            }
          ]
        },
        {
          "id": "6893D537716AA748",
          "x": 4.0,
          "y": 24.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Das Zahnrad",
          "optional": false,
          "icon": null,
          "description": [
            "Das &aZahnrad&r überträgt Drehkraft. Der Herzschlag jeder Maschine.",
            "&7Zwei davon nebeneinander? Vorsicht — die mögen sich nicht."
          ],
          "dependencies": [
            "5B36DE3826F26963"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:cogwheel",
              "displayName": "Cogwheel",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:cogwheel",
              "displayName": "Cogwheel",
              "mod": "create",
              "count": 5
            },
            {
              "type": "item",
              "item": "create:shaft",
              "displayName": "Shaft",
              "mod": "create",
              "count": 10
            }
          ]
        },
        {
          "id": "3C892B33758B7BA6",
          "x": 5.0,
          "y": 25.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Großes Zahnrad",
          "optional": false,
          "icon": null,
          "description": [
            "Mit dem &agroßen Zahnrad&r änderst du Drehzahl und Richtung.",
            "&7Übersetzung gefällig?"
          ],
          "dependencies": [
            "6893D537716AA748"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:large_cogwheel",
              "displayName": "Large Cogwheel",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:cogwheel",
              "displayName": "Cogwheel",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:large_cogwheel",
              "displayName": "Large Cogwheel",
              "mod": "create",
              "count": 3
            },
            {
              "type": "item",
              "item": "create:cogwheel",
              "displayName": "Cogwheel",
              "mod": "create",
              "count": 6
            }
          ]
        },
        {
          "id": "3AF2BC9A0E298882",
          "x": 3.0,
          "y": 28.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Andesite Casing",
          "optional": false,
          "icon": null,
          "description": [
            "Das &aAndesit-Gehäuse&r ummantelt Wellen und Maschinen. Hübsch und praktisch."
          ],
          "dependencies": [
            "0F16498769DFB3B0"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:andesite_casing",
              "displayName": "Andesite Casing",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:andesite_casing",
              "displayName": "Andesite Casing",
              "mod": "create",
              "count": 4
            }
          ]
        },
        {
          "id": "5DD6631F5996BA71",
          "x": 5.5,
          "y": 21.75,
          "shape": "circle",
          "size": 1.25,
          "title": "Wasserrad",
          "optional": false,
          "icon": null,
          "description": [
            "Das &aWasserrad&r macht aus fließendem Wasser saubere, kostenlose Drehkraft.",
            "&7Die gemütlichste Energiequelle überhaupt."
          ],
          "dependencies": [
            "6893D537716AA748"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:water_wheel",
              "displayName": "Water Wheel",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:water_bucket",
              "displayName": "Water Bucket",
              "mod": "minecraft",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:water_wheel",
              "displayName": "Water Wheel",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:large_water_wheel",
              "displayName": "Large Water Wheel",
              "mod": "create",
              "count": 1
            }
          ]
        },
        {
          "id": "3697AAF8F281B247",
          "x": 6.75,
          "y": 23.0,
          "shape": "circle",
          "size": 1.25,
          "title": "Steam Engine",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aSteam Engine&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "6893D537716AA748"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:steam_engine",
              "displayName": "Steam Engine",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:fluid_tank",
              "displayName": "Fluid Tank",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:shaft",
              "displayName": "Shaft",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:fluid_tank",
              "displayName": "Fluid Tank",
              "mod": "create",
              "count": 4
            },
            {
              "type": "item",
              "item": "create:mechanical_pump",
              "displayName": "Mechanical Pump",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:fluid_pipe",
              "displayName": "Fluid Pipe",
              "mod": "create",
              "count": 4
            }
          ]
        },
        {
          "id": "72C7698072BF0F1D",
          "x": 5.5,
          "y": 23.0,
          "shape": "circle",
          "size": 1.25,
          "title": "Hand Crank",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aHand Crank&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "6893D537716AA748"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:hand_crank",
              "displayName": "Hand Crank",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:cogwheel",
              "displayName": "Cogwheel",
              "mod": "create",
              "count": 1
            }
          ]
        },
        {
          "id": "2AEA51044AD44BE8",
          "x": -2.0,
          "y": 22.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Ablage",
          "optional": false,
          "icon": null,
          "description": [
            "Das &aDepot&r hält ein einzelnes Item für die Bearbeitung bereit. Mini-Werkbank."
          ],
          "dependencies": [
            "13AEBC331F29BC3D"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:depot",
              "displayName": "Depot",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:depot",
              "displayName": "Depot",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:belt_connector",
              "displayName": "Belt Connector",
              "mod": "create",
              "count": 4
            }
          ]
        },
        {
          "id": "476C7317510198D9",
          "x": -2.5,
          "y": 21.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Weighted Ejector",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aWeighted Ejector&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "2AEA51044AD44BE8"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:weighted_ejector",
              "displayName": "Weighted Ejector",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:snowball",
              "displayName": "Snowball",
              "mod": "minecraft",
              "count": 8
            },
            {
              "type": "item",
              "item": "minecraft:slime_ball",
              "displayName": "Slime Ball",
              "mod": "minecraft",
              "count": 8
            },
            {
              "type": "item",
              "item": "minecraft:fire_charge",
              "displayName": "Fire Charge",
              "mod": "minecraft",
              "count": 8
            }
          ]
        },
        {
          "id": "483892F0A0F75B97",
          "x": -4.5,
          "y": 25.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Flüssigkeitsrohr",
          "optional": false,
          "icon": null,
          "description": [
            "&aRohre&r pumpen Flüssigkeiten dorthin, wo du sie brauchst. Mit Pumpe, versteht sich."
          ],
          "dependencies": [
            "7242F591DA474B37"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:fluid_pipe",
              "displayName": "Fluid Pipe",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:fluid_pipe",
              "displayName": "Fluid Pipe",
              "mod": "create",
              "count": 10
            }
          ]
        },
        {
          "id": "7242F591DA474B37",
          "x": -3.5,
          "y": 27.0,
          "shape": "circle",
          "size": 1.75,
          "title": "Copper Ingot",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aCopper Ingot&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "57A7A5C79389A96A"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "minecraft:copper_ingot",
              "displayName": "Copper Ingot",
              "mod": "minecraft",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:copper_block",
              "displayName": "Copper Block",
              "mod": "minecraft",
              "count": 1
            }
          ]
        },
        {
          "id": "3F02EF19112D23BE",
          "x": 3.0,
          "y": 30.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Crushing Wheel",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aCrushing Wheel&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "3AF2BC9A0E298882"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:crushing_wheel",
              "displayName": "Crushing Wheel",
              "mod": "create",
              "count": 2
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:diamond_ore",
              "displayName": "Diamond Ore",
              "mod": "minecraft",
              "count": 8
            },
            {
              "type": "item",
              "item": "minecraft:iron_horse_armor",
              "displayName": "Iron Horse Armor",
              "mod": "minecraft",
              "count": 1
            }
          ]
        },
        {
          "id": "64FF7118E29931C0",
          "x": 1.5,
          "y": 28.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Millstone",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aMillstone&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "3AF2BC9A0E298882"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:millstone",
              "displayName": "Millstone",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:cornflower",
              "displayName": "Cornflower",
              "mod": "minecraft",
              "count": 5
            },
            {
              "type": "item",
              "item": "minecraft:poppy",
              "displayName": "Poppy",
              "mod": "minecraft",
              "count": 5
            },
            {
              "type": "item",
              "item": "minecraft:dandelion",
              "displayName": "Dandelion",
              "mod": "minecraft",
              "count": 5
            },
            {
              "type": "item",
              "item": "minecraft:netherrack",
              "displayName": "Netherrack",
              "mod": "minecraft",
              "count": 5
            }
          ]
        },
        {
          "id": "133CA315A1443A49",
          "x": -4.5,
          "y": 24.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Mechanical Pump",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aMechanical Pump&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "483892F0A0F75B97"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:mechanical_pump",
              "displayName": "Mechanical Pump",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:fluid_pipe",
              "displayName": "Fluid Pipe",
              "mod": "create",
              "count": 8
            }
          ]
        },
        {
          "id": "127F9EAC7C305BF5",
          "x": -0.25,
          "y": 29.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Wrench",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aWrench&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "57A7A5C79389A96A"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:wrench",
              "displayName": "Wrench",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:gold_ingot",
              "displayName": "Gold Ingot",
              "mod": "minecraft",
              "count": 5
            },
            {
              "type": "item",
              "item": "create:cogwheel",
              "displayName": "Cogwheel",
              "mod": "create",
              "count": 5
            }
          ]
        },
        {
          "id": "38CB5044AB3F859B",
          "x": -1.75,
          "y": 29.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Superkleber",
          "optional": false,
          "icon": null,
          "description": [
            "&aSuperkleber&r verbindet Blöcke zu einer Kontraption. Alles, was zusammenklebt, fliegt zusammen."
          ],
          "dependencies": [
            "57A7A5C79389A96A"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:super_glue",
              "displayName": "Super Glue",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:super_glue",
              "displayName": "Super Glue",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "minecraft:slime_ball",
              "displayName": "Slime Ball",
              "mod": "minecraft",
              "count": 8
            }
          ]
        },
        {
          "id": "72537968598AB884",
          "x": -1.0,
          "y": 30.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Goggles",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aGoggles&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "57A7A5C79389A96A"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:goggles",
              "displayName": "Goggles",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:gold_ingot",
              "displayName": "Gold Ingot",
              "mod": "minecraft",
              "count": 5
            },
            {
              "type": "item",
              "item": "create:speedometer",
              "displayName": "Speedometer",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:stressometer",
              "displayName": "Stressometer",
              "mod": "create",
              "count": 1
            }
          ]
        },
        {
          "id": "69EE22CB4FF1E591",
          "x": -3.5,
          "y": 31.0,
          "shape": "circle",
          "size": 1.75,
          "title": "Superkleber",
          "optional": false,
          "icon": null,
          "description": [
            "&aSuperkleber&r verbindet Blöcke zu einer Kontraption. Alles, was zusammenklebt, fliegt zusammen."
          ],
          "dependencies": [
            "3AF2BC9A0E298882",
            "38CB5044AB3F859B"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:super_glue",
              "displayName": "Super Glue",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:andesite_casing",
              "displayName": "Andesite Casing",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:andesite_casing",
              "displayName": "Andesite Casing",
              "mod": "create",
              "count": 5
            },
            {
              "type": "item",
              "item": "create:cogwheel",
              "displayName": "Cogwheel",
              "mod": "create",
              "count": 3
            }
          ],
          "hide_dependent_lines": true
        },
        {
          "id": "087F6C09CB5B2D1A",
          "x": -5.5,
          "y": 25.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Smart Fluid Pipe",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aSmart Fluid Pipe&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "483892F0A0F75B97"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:smart_fluid_pipe",
              "displayName": "Smart Fluid Pipe",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:fluid_tank",
              "displayName": "Fluid Tank",
              "mod": "create",
              "count": 2
            }
          ]
        },
        {
          "id": "50DBB87E53017E60",
          "x": -5.5,
          "y": 26.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Fluid Valve",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aFluid Valve&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "483892F0A0F75B97"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:fluid_valve",
              "displayName": "Fluid Valve",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:copper_valve_handle",
              "displayName": "Copper Valve Handle",
              "mod": "create",
              "count": 1
            }
          ]
        },
        {
          "id": "3C99017FD32B6DE2",
          "x": 5.5,
          "y": 29.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Brass Casing",
          "optional": false,
          "icon": null,
          "description": [
            "Das &aMessing-Gehäuse&r markiert die Mittelstufe — jetzt wird's clever."
          ],
          "dependencies": [
            "5DC892BA79EB52EC",
            "1B182A30604655E2"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:brass_casing",
              "displayName": "Brass Casing",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:brass_ingot",
              "displayName": "Brass Ingot",
              "mod": "create",
              "count": 5
            }
          ]
        },
        {
          "id": "1712C3B3CF158843",
          "x": 4.0,
          "y": 30.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Präzisionsmechanismus",
          "optional": false,
          "icon": null,
          "description": [
            "Das &aPräzisionsmechanismus&r ist das Herz fortgeschrittener Geräte. Fummelig, aber lohnend."
          ],
          "dependencies": [
            "3314FBC4FEAE1D08"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:precision_mechanism",
              "displayName": "Precision Mechanism",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:precision_mechanism",
              "displayName": "Precision Mechanism",
              "mod": "create",
              "count": 3
            }
          ]
        },
        {
          "id": "1BA11428DF7541AD",
          "x": 2.0,
          "y": 22.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Sequenced Gearshift",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aSequenced Gearshift&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "67A46ED73E488CEE"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:sequenced_gearshift",
              "displayName": "Sequenced Gearshift",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:brass_casing",
              "displayName": "Brass Casing",
              "mod": "create",
              "count": 3
            },
            {
              "type": "item",
              "item": "minecraft:lever",
              "displayName": "Lever",
              "mod": "minecraft",
              "count": 1
            }
          ]
        },
        {
          "id": "4EE10B8E194F5CA9",
          "x": 6.0,
          "y": 32.0,
          "shape": "circle",
          "size": 1.25,
          "title": "Railway Casing",
          "optional": false,
          "icon": null,
          "description": [
            "Das &aSchienen-Gehäuse&r ist die Basis für Züge, Bahnhöfe und Schienenfahrzeuge."
          ],
          "dependencies": [
            "3C99017FD32B6DE2"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:railway_casing",
              "displayName": "Railway Casing",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:railway_casing",
              "displayName": "Railway Casing",
              "mod": "create",
              "count": 4
            }
          ]
        },
        {
          "id": "09E34E1F9C751458",
          "x": 3.0,
          "y": 22.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Vertical Gearbox",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aVertical Gearbox&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "5B36DE3826F26963"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:vertical_gearbox",
              "displayName": "Vertical Gearbox",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:shaft",
              "displayName": "Shaft",
              "mod": "create",
              "count": 4
            },
            {
              "type": "item",
              "item": "create:gearbox",
              "displayName": "Gearbox",
              "mod": "create",
              "count": 1
            }
          ]
        },
        {
          "id": "3A4C62865C7CC862",
          "x": -5.0,
          "y": 27.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Flüssigkeitstank",
          "optional": false,
          "icon": null,
          "description": [
            "Der &aTank&r lagert Lava, Wasser, Honig \\& Co. Stapelbar zu riesigen Reservoirs."
          ],
          "dependencies": [
            "7242F591DA474B37"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:fluid_tank",
              "displayName": "Fluid Tank",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:fluid_tank",
              "displayName": "Fluid Tank",
              "mod": "create",
              "count": 2
            }
          ]
        },
        {
          "id": "39A7619B4C5592BE",
          "x": -4.5,
          "y": 29.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Item Drain",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aItem Drain&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "3F663416E824720C"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:item_drain",
              "displayName": "Item Drain",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:honey_bottle",
              "displayName": "Honey Bottle",
              "mod": "minecraft",
              "count": 3
            },
            {
              "type": "item",
              "item": "create:fluid_tank",
              "displayName": "Fluid Tank",
              "mod": "create",
              "count": 1
            }
          ]
        },
        {
          "id": "078C5B50CDC174CB",
          "x": -5.5,
          "y": 32.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Mechanisches Lager",
          "optional": false,
          "icon": null,
          "description": [
            "Mit dem &aLager&r drehst und bewegst du ganze Bauwerke — willkommen bei Kontraptionen!"
          ],
          "dependencies": [
            "69EE22CB4FF1E591"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:mechanical_bearing",
              "displayName": "Mechanical Bearing",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:mechanical_bearing",
              "displayName": "Mechanical Bearing",
              "mod": "create",
              "count": 3
            },
            {
              "type": "item",
              "item": "create:shaft",
              "displayName": "Shaft",
              "mod": "create",
              "count": 3
            },
            {
              "type": "item",
              "item": "minecraft:slime_ball",
              "displayName": "Slime Ball",
              "mod": "minecraft",
              "count": 3
            }
          ]
        },
        {
          "id": "18914FDF9CF9EEA8",
          "x": -4.5,
          "y": 34.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Clockwork Bearing",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aClockwork Bearing&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "69EE22CB4FF1E591"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:clockwork_bearing",
              "displayName": "Clockwork Bearing",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:clock",
              "displayName": "Clock",
              "mod": "minecraft",
              "count": 1
            },
            {
              "type": "item",
              "item": "minecraft:slime_ball",
              "displayName": "Slime Ball",
              "mod": "minecraft",
              "count": 3
            }
          ]
        },
        {
          "id": "5979DE0E2BA3DAE5",
          "x": 5.0,
          "y": 32.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Gleise",
          "optional": false,
          "icon": null,
          "description": [
            "&aGleise&r sind die Adern deines Imperiums. Hier rollen bald die Züge zwischen den Kolonien."
          ],
          "dependencies": [
            "3314FBC4FEAE1D08"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:track",
              "displayName": "Track",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:track",
              "displayName": "Track",
              "mod": "create",
              "count": 32
            }
          ]
        },
        {
          "id": "77BE3D9D274F72F1",
          "x": 7.0,
          "y": 32.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Bahnhof",
          "optional": false,
          "icon": null,
          "description": [
            "Am &aBahnhof&r baust du Züge zusammen, gibst Fahrpläne und steigst ein. Alles einsteigen!"
          ],
          "dependencies": [
            "4EE10B8E194F5CA9",
            "5979DE0E2BA3DAE5"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:track_station",
              "displayName": "Track Station",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:track_station",
              "displayName": "Track Station",
              "mod": "create",
              "count": 2
            },
            {
              "type": "item",
              "item": "create:track",
              "displayName": "Track",
              "mod": "create",
              "count": 8
            }
          ]
        },
        {
          "id": "3FBCBBEBB78B83FC",
          "x": 6.0,
          "y": 34.0,
          "shape": "circle",
          "size": 1.5,
          "title": "Controls",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aControls&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "5979DE0E2BA3DAE5",
            "77BE3D9D274F72F1"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:controls",
              "displayName": "Controls",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:super_glue",
              "displayName": "Super Glue",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:railway_casing",
              "displayName": "Railway Casing",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:railway_casing",
              "displayName": "Railway Casing",
              "mod": "create",
              "count": 8
            },
            {
              "type": "item",
              "item": "create:controls",
              "displayName": "Controls",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:flywheel",
              "displayName": "Flywheel",
              "mod": "create",
              "count": 1
            }
          ]
        },
        {
          "id": "30AC43222FF9B18A",
          "x": 7.0,
          "y": 35.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Track Signal",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aTrack Signal&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "3FBCBBEBB78B83FC"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:track_signal",
              "displayName": "Track Signal",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:nixie_tube",
              "displayName": "Nixie Tube",
              "mod": "create",
              "count": 4
            },
            {
              "type": "item",
              "item": "create:red_seat",
              "displayName": "Red Seat",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "minecraft:lead",
              "displayName": "Lead",
              "mod": "minecraft",
              "count": 1
            }
          ]
        },
        {
          "id": "5134C81D96C55375",
          "x": 5.0,
          "y": 35.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Track Observer",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aTrack Observer&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "3FBCBBEBB78B83FC"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:track_observer",
              "displayName": "Track Observer",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:repeater",
              "displayName": "Repeater",
              "mod": "minecraft",
              "count": 3
            },
            {
              "type": "item",
              "item": "minecraft:redstone",
              "displayName": "Redstone",
              "mod": "minecraft",
              "count": 12
            }
          ]
        },
        {
          "id": "2D96965317D3CFEC",
          "x": 6.0,
          "y": 35.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Schedule",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aSchedule&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "3FBCBBEBB78B83FC"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:schedule",
              "displayName": "Schedule",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:blue_seat",
              "displayName": "Blue Seat",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "minecraft:lead",
              "displayName": "Lead",
              "mod": "minecraft",
              "count": 3
            },
            {
              "type": "item",
              "item": "create:schedule",
              "displayName": "Schedule",
              "mod": "create",
              "count": 3
            }
          ]
        },
        {
          "id": "7F0F7111552F95A9",
          "x": 7.5,
          "y": 34.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Controls",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aControls&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "3FBCBBEBB78B83FC"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:controls",
              "displayName": "Controls",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:track_station",
              "displayName": "Track Station",
              "mod": "create",
              "count": 1
            }
          ]
        },
        {
          "id": "12274935C3D20C74",
          "x": 4.5,
          "y": 34.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Superkleber",
          "optional": false,
          "icon": null,
          "description": [
            "&aSuperkleber&r verbindet Blöcke zu einer Kontraption. Alles, was zusammenklebt, fliegt zusammen."
          ],
          "dependencies": [
            "3FBCBBEBB78B83FC"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:super_glue",
              "displayName": "Super Glue",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:train_door",
              "displayName": "Train Door",
              "mod": "create",
              "count": 2
            },
            {
              "type": "item",
              "item": "create:train_trapdoor",
              "displayName": "Train Trapdoor",
              "mod": "create",
              "count": 4
            },
            {
              "type": "item",
              "item": "create:flywheel",
              "displayName": "Flywheel",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:cogwheel",
              "displayName": "Cogwheel",
              "mod": "create",
              "count": 8
            },
            {
              "type": "item",
              "item": "create:large_cogwheel",
              "displayName": "Large Cogwheel",
              "mod": "create",
              "count": 4
            }
          ]
        },
        {
          "id": "2C2958E38293717E",
          "x": -1.0,
          "y": 21.0,
          "shape": "circle",
          "size": 1.25,
          "title": "Cardboard",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aCardboard&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "13AEBC331F29BC3D"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:cardboard",
              "displayName": "Cardboard",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:cardboard",
              "displayName": "Cardboard",
              "mod": "create",
              "count": 6
            }
          ]
        },
        {
          "id": "737DC37E4310090C",
          "x": 0.0,
          "y": 19.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Chain Conveyor",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aChain Conveyor&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "16B0C1F7B951C19D"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:chain_conveyor",
              "displayName": "Chain Conveyor",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:chain_conveyor",
              "displayName": "Chain Conveyor",
              "mod": "create",
              "count": 2
            },
            {
              "type": "item",
              "item": "minecraft:chain",
              "displayName": "Chain",
              "mod": "minecraft",
              "count": 4
            }
          ]
        },
        {
          "id": "3B3B38B17CF5D81C",
          "x": 1.0,
          "y": 19.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Package Frogport",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aPackage Frogport&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "737DC37E4310090C"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:package_frogport",
              "displayName": "Package Frogport",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:package_frogport",
              "displayName": "Package Frogport",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:cardboard_package_10x8",
              "displayName": "Cardboard Package 10x8",
              "mod": "create",
              "count": 1
            }
          ]
        },
        {
          "id": "57A18F2E51952EB8",
          "x": 1.0,
          "y": 20.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Blue Postbox",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aBlue Postbox&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "16B0C1F7B951C19D"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:blue_postbox",
              "displayName": "Blue Postbox",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:railway_casing",
              "displayName": "Railway Casing",
              "mod": "create",
              "count": 3
            },
            {
              "type": "item",
              "item": "create:track_station",
              "displayName": "Track Station",
              "mod": "create",
              "count": 1
            }
          ]
        },
        {
          "id": "6353A39CBEE599A0",
          "x": -2.0,
          "y": 19.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Stock Link",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aStock Link&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "16B0C1F7B951C19D"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:stock_link",
              "displayName": "Stock Link",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:stock_link",
              "displayName": "Stock Link",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:packager",
              "displayName": "Packager",
              "mod": "create",
              "count": 2
            },
            {
              "type": "item",
              "item": "create:item_vault",
              "displayName": "Item Vault",
              "mod": "create",
              "count": 2
            }
          ]
        },
        {
          "id": "754B8F1FBCD983C5",
          "x": -3.0,
          "y": 19.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Stock Ticker",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aStock Ticker&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "6353A39CBEE599A0"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:stock_ticker",
              "displayName": "Stock Ticker",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:stock_ticker",
              "displayName": "Stock Ticker",
              "mod": "create",
              "count": 2
            },
            {
              "type": "item",
              "item": "create:item_vault",
              "displayName": "Item Vault",
              "mod": "create",
              "count": 6
            },
            {
              "type": "item",
              "item": "create:brass_funnel",
              "displayName": "Brass Funnel",
              "mod": "create",
              "count": 2
            }
          ]
        },
        {
          "id": "672F9CF5B0E626F1",
          "x": -1.0,
          "y": 19.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Packager",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aPackager&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "2C2958E38293717E"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:packager",
              "displayName": "Packager",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:packager",
              "displayName": "Packager",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:repackager",
              "displayName": "Repackager",
              "mod": "create",
              "count": 1
            }
          ]
        },
        {
          "id": "16B0C1F7B951C19D",
          "x": -1.0,
          "y": 18.5,
          "shape": "circle",
          "size": 1.25,
          "title": "Cardboard Package 12X12",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aCardboard Package 12X12&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "672F9CF5B0E626F1"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:cardboard_package_12x12",
              "displayName": "Cardboard Package 12x12",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:cardboard_package_10x12",
              "displayName": "Cardboard Package 10x12",
              "mod": "create",
              "count": 1
            }
          ]
        },
        {
          "id": "0A4962728C98DAD9",
          "x": -1.0,
          "y": 22.5,
          "shape": "circle",
          "size": 1.0,
          "title": "Item Vault",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aItem Vault&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "13AEBC331F29BC3D"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:item_vault",
              "displayName": "Item Vault",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:item_vault",
              "displayName": "Item Vault",
              "mod": "create",
              "count": 3
            }
          ]
        },
        {
          "id": "64860340A5BEBAB9",
          "x": -3.0,
          "y": 20.0,
          "shape": "circle",
          "size": 1.0,
          "title": "Andesite Table Cloth",
          "optional": false,
          "icon": null,
          "description": [
            "Beschaffe &aAndesite Table Cloth&r — ein weiterer Baustein auf deinem Create-Weg.",
            "&7(In EMI siehst du, wie es hergestellt wird.)"
          ],
          "dependencies": [
            "6353A39CBEE599A0",
            "754B8F1FBCD983C5"
          ],
          "tasks": [
            {
              "type": "item",
              "item": "create:andesite_table_cloth",
              "displayName": "Andesite Table Cloth",
              "mod": "create",
              "count": 1
            }
          ],
          "rewards": [
            {
              "type": "item",
              "item": "create:andesite_scaffolding",
              "displayName": "Andesite Scaffolding",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "create:stock_ticker",
              "displayName": "Stock Ticker",
              "mod": "create",
              "count": 1
            },
            {
              "type": "item",
              "item": "minecraft:lead",
              "displayName": "Lead",
              "mod": "minecraft",
              "count": 1
            }
          ]
        }
      ]
    }
  ]
};
