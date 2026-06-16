# Quest-Linie — Blueprint (FTB Quests)

Roter Faden des Packs: **FTB Quests** als Progression, **Magic Coins** als Belohnungs-Währung
(Currency Reward). Aufbau entlang der **5 Säulen**. Jedes Kapitel ist eine FTB-Quests-*Chapter*,
gruppiert in *Chapter Groups*. Belohnungen: Items + **Münzen** (skalierend mit Schwierigkeit).

Dateien später unter `config/ftbquests/quests/` (`chapter_groups.snbt`, `chapters/*.snbt`, `data.snbt`).
Reihenfolge der Umsetzung: **Kap. 0 + 1 zuerst** (onboarding + farming), dann 2–5.

Legende: `[T]` = Task (Sammeln/Herstellen/etc.) · `[R]` = Reward · 🪙 = Magic-Coins-Reward.

---

## Chapter Group 0 — 👋 Willkommen (Onboarding)

**Kap. 0.1 — Start ins Leben**
- [T] Hol dir Holz / craff einen Crafting Table (Einstieg).
- [T] Öffne **EMI** (Rezept-Viewer) — Quest erklärt: Rezepte links, Nutzungen rechts.
- [T] Öffne **JourneyMap** (Karte) — Wegpunkte setzen.
- [R] Starter-Kit (Werkzeuge, Brot) · 🪙 10 Coins.

**Kap. 0.2 — Inventar-Komfort (Inventory Profiles Next)** ← *vom User gewünscht*
- **Beschreibungstext der Quest** (kein Task, reine Info-Quest):
  > Die **lila Pfeile** in der Hotbar gehören zu *Inventory Profiles Next* (IPN) — dem
  > „Hotbar-Swapping". Damit kannst du ganze Hotbar-Belegungen per Tastendruck umschalten.
  > Wir haben die Pfeile **standardmäßig ausgeblendet**, weil sie im Weg waren — das **Feature
  > bleibt aber aktiv**. So aktivierst/zeigst du es wieder:
  > 1. Inventar öffnen → oben (Mitte/nahe Inventar) sind die **IPN-Buttons** (Sortieren etc.).
  > 2. **Einstellungen → Inventory Profiles Next** (oder Taste `O`): dort *Hotbar Swapping* /
  >    *Show hotbar buttons* wieder einschalten.
  > 3. Die zwei Symbole oben links wurden in die **Mitte/an den Inventar-Rand** verschoben.
- [T] Sortiere einmal dein Inventar mit dem IPN-Sortier-Button (Detection: optional/manuell hakbar).
- [R] 🪙 5 Coins.

---

## Chapter Group 1 — 🌱 Farmen & Leben (Säule 1)

**Kap. 1.1 — Erste Ernte**
- [T] Ernte Weizen/Karotten · [T] Pflanze ein **HarvestCraft-2**-Crop · [T] baue eine Hacke.
- [R] Saatgut-Mix (HarvestCraft/Veggies/Delightful) · 🪙 15.

**Kap. 1.2 — Die Küche (Farmer's Delight)**
- [T] Cooking Pot · [T] Cutting Board · [T] koche ein FD-Gericht.
- [R] Skillet + Zutaten · 🪙 20.

**Kap. 1.3 — Genuss & Vielfalt (Let's Do / *-Delight-Suite)**
- Verzweigt: **Vinery** (Wein), **Meadow** (Käse/Milch), **Bakery/Confectionery**,
  **Herbalbrews** (Tee), **Brewin' & Chewin'**. Je Zweig 1–2 Tasks.
- [R] je Zweig themen-Items · 🪙 15 je Zweig.

**Kap. 1.4 — Jahreszeiten (Serene Seasons)**
- [T] Info-Quest: Pflanzen wachsen je nach Saison. [T] Ernte in passender Saison.
- [R] Greenhouse-Glas/Agri-Items · 🪙 15.

**Kap. 1.5 — Tiere & Zucht (Naturalist)**
- [T] Züchte 2 Tierarten · [T] fange/beobachte eine Naturalist-Kreatur.
- [R] Futter/Eimer · 🪙 15.

**Kap. 1.6 — Skills (Pufferfish's Skills)**
- [T] Info-Quest: Skill-Trees (Farming/Mining/Fishing/Husbandry). Erreiche Farming-Lvl X.
- [R] Skill-Buch/Bonus · 🪙 20.

**Kap. 1.7 — Angeln (Aquaculture + Delight, Fish of Thieves)**
- [T] Angelrute · [T] fange 3 Fischarten · [T] koche ein Fisch-Gericht.
- [R] bessere Rute/Köder · 🪙 15.

---

## Chapter Group 2 — 🏘️ Bauen & Gemeinschaft (Säule 2 — MineColonies)

**Kap. 2.1 — Die erste Kolonie**
- [T] Supply Camp/Ship platzieren · [T] **Town Hall** · [T] **Builder's Hut** + Bauauftrag.
- [R] Bau-Materialien · 🪙 30.

**Kap. 2.2 — Bürger & Versorgung**
- [T] erste Bürger · [T] Tavern/Haus · [T] Restaurant + Koch (verbindet zu Farming!).
- [R] 🪙 30.

**Kap. 2.3 — Mehrere Zivilisationen** *(allowinfinitecolonies=true)*
- [T] Gründe eine **zweite Kolonie** (Mindestabstand 12 Chunks beachten).
- [R] 🪙 50.

**Kap. 2.4 — Schöner Bauen (Structurize / Domum Ornamentum / Furniture)**
- [T] eigenes Blueprint mit Structurize · [T] Domum-Ornamentum-Block · [T] Möbel (Macaw/Another Furniture).
- [R] Deko-Set · 🪙 25.

---

## Chapter Group 3 — ⚙️ Technik & Mobilität (Säule 3 — Create)

**Kap. 3.1 — Kinetik-Grundlagen**
- [T] Cogwheel · [T] Water Wheel/Windmill · [T] Mechanical Press.
- [R] Andesite Alloy-Vorrat · 🪙 25.

**Kap. 3.2 — Verarbeitung & Automatik**
- [T] Mixer + Basin · [T] Mechanical Crafter · [T] Create-**Central-Kitchen** (Auto-Cooking!).
- [R] 🪙 30.

**Kap. 3.3 — Energie & Addons (so viele wie möglich)**
- Showcase-Zweige: **Create: New Age** (Strom), **Diesel Generators/TFMG**, **Createaddition**,
  **Create: Factory**, **Encased**. Je Zweig 1 Schlüssel-Item.
- [R] 🪙 20 je Zweig.

**Kap. 3.4 — Schienen & Züge (Steam 'n' Rails + Train Utilities + Navigator)**
- [T] Train Track · [T] Train Station · [T] zusammengebauter Zug · [T] Navigator-Item.
- [R] Schienen-Paket · 🪙 40.

**Kap. 3.5 — In die Lüfte (Create Aeronautics)** ⚠️ *Alpha — als Bonus/Endgame*
- [T] eine fliegende Kontraption bauen.
- [R] 🪙 60.

---

## Chapter Group 4 — 🌍 Welt & Vernetzung (Säule 4)

**Kap. 4.1 — Entdecke die Welt (Terralith + Tectonic)**
- [T] Besuche 3 verschiedene Terralith-Biome (Trigger per Biome-Detection).
- [R] Karten/Kompass · 🪙 20.

**Kap. 4.2 — Das Schienennetz**
- [T] Verbinde **zwei Kolonien** per Zugstrecke (Station↔Station).
- [R] 🪙 50.

**Kap. 4.3 — Weite Sicht (Distant Horizons)**
- [T] Info-Quest: DH-LOD erklären, Sichtweite-Tipps, Shader-Hinweis.
- [R] 🪙 10.

---

## Chapter Group 5 — 🪙 Ziele & Wirtschaft (Säule 5)

**Kap. 5.1 — Münzwirtschaft (Magic Coins)**
- [T] Info: Coins kommen aus Quests. [T] Gib Coins für ein Reward-Item aus (Shop/Quest).
- [R] Coin-Beutel · 🪙 25.

**Kap. 5.2 — Handel (Create: Numismatics)**
- [T] baue einen **Numismatics**-Automaten/Handelsposten · [T] erster Handel.
- [R] 🪙 30.

**Kap. 5.3 — Endgame-Ziele**
- [T] große Kolonie (Bürgerzahl X) · [T] funktionierendes Zugnetz · [T] Aeronautics-Schiff
  · [T] X Coins angespart.
- [R] Prestige-Item / Titel · 🪙 200.
- *(Hook für späteres Teilprojekt: **Kartoffelboss** als optionale Boss-Quest.)*

---

## Technische Hinweise für die SNBT-Umsetzung
- Item-IDs **gegen die installierten Mods verifizieren** (EMI in-game zeigt die exakte ID).
- Magic-Coins-Reward = FTB-Quests *Currency Reward* (sofern Magic-Coins-Bridge vorhanden),
  sonst Item-Reward mit dem Münz-Item.
- Biome-Tasks: FTB-Quests „Observe"/Dimension-Task bzw. KubeJS-Trigger (kein KubeJS im Pack →
  ggf. manuell hakbare Checkmark-Tasks für Biome/Info-Quests).
- Info-Quests (IPN, DH, Saisons) = Tasks vom Typ *Checkmark* (manuell abhakbar) + langer Text.
- Reihenfolge-Abhängigkeiten über Quest-`dependencies` (Hex-IDs) setzen.
