# Cozy-Integration (Pack 0.11.0)

Macht aus 200 Mods **ein** Spiel: kanonische Zutaten, Create als zentrale
Verarbeitung, Farm-Güter als Treibstoff der Robotik. Alles in `pack/kubejs/`.

## Phase 1 — Basiszutaten vereinheitlicht (`unify_food.js`)
Ein kanonisches Item pro Konzept; Duplikate werden in **allen** Rezepten ersetzt
(Input+Output) und sind 1:1 umtauschbar (Umtausch-Rezepte `cozy:unify/*`):

| Konzept | Kanonisch | ersetzt |
|---|---|---|
| Teig | `farmersdelight:wheat_dough` | create, farm_and_charm, pamhc2foodcore |
| Mehl | `create:wheat_flour` | pamhc2foodcore, farm_and_charm, bountifulfares |
| Käse | `brewinandchewin:flaxen_cheese_wedge` | pamhc2foodcore, extradelight, create_bic_bit, pizzadelight |
| Käsescheibe | `expandeddelight:cheese_slice` | pizzadelight |
| Butter | `extradelight:butter` | farm_and_charm, pamhc2foodcore |
| Salz | `expandeddelight:salt` | ratatouille, meadow (alpine), garnished (crushed) |

*Bewusst NICHT vereinheitlicht:* Reis/Zwiebel & Co. (FD vs. Pam's) — das sind
Crop-**Loot-Drops**, keine Rezept-Outputs; bräuchte LootJS (Kandidat Phase 7).

## Phase 2 — Create als Verarbeitungszentrum (`create_food_bridges.js` + Overrides)
- Milling: Pam's Gerste/Hafer/Roggen + F&C Gerste/Hafer → Mehl
- Mixing (erhitzt): 1000 mB Milch + Salz → 2× Käse · Compacting: 500 mB Milch → Butter
- Cutting: Käse → 3 Scheiben
- **18 Create-Diesel-Generators-Rezepte repariert** (`fluid_tag`→`neoforge:tag`):
  alle Beton-Mixings + **Biodiesel** — damit ist der Farm→Treibstoff-Loop
  (Fermentation → Ethanol + Pflanzenöl → Biodiesel) endlich funktionsfähig.
- pizzadelight `rolling/flat_dough` repariert: jeder `c:doughs`-Teig → Flachteig.

## Phase 3 — Bionics ↔ Farm (`bionics_farm_link.js`)
Alle Bionics-Rezepte nutzen **Biomasse-Pellets** (Create-Addition) statt Kohle —
Roboter laufen mit Ernteabfällen. (Die `noyoudon't:`-Fehler der Organ-Roboter
sind Absicht des Mod-Autors: nicht craftbar.)

## Phase 4 — MineColonies (`kubejs/data/minecolonies/crafterrecipes/`)
Bäcker: Grilled Cheese, Apple Pie, Honig-Kekse · Chef: Fried Rice, Beef Stew,
Käsepizza — Kolonisten kochen jetzt Pack-Gerichte.

## Phase 5 — Serene Seasons (`kubejs/data/sereneseasons/tags/`)
97 Pam's-Crops + Cultural-Delights-Mais nach Kategorie auf Jahreszeiten verteilt
(Grünzeug Frühling/Sommer · Fruchtgemüse Sommer/Herbst · Getreide/Wurzeln
Frühling–Herbst · Winterhartes Herbst/Winter). 12 Mods bringen eigene Tags mit.

## Phase 6 — Fischerei (`kubejs/data/cozy/recipe/cutting/`)
30 Aquaculture-Fische → 2× Filet + Knochenmehl (Messer/Cutting Board);
Filets zählen als `farmersdelight:fish_slices` → alle FD-Fischgerichte.

## Bekannte Restfehler im Log (unkritisch, Fremd-Mods)
598× FFB-Markt (Einträge für nicht installierte Mods) · 20× reestrogen ·
16× suppsquared · 8× createbionics (Absicht) · 8× create_ironworks.
