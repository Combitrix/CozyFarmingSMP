# Design: Cozy-Farming-SMP Modpack

**Datum:** 2026-06-15
**Status:** Genehmigt (Design), QoL-Kategorie wird im Aufbau erweitert
**Arbeitstitel:** TBD (Pack-Name wird vor Export festgelegt)

## Vision

Ein farm-lastiges Multiplayer-Modpack (SMP) im Stil von *Society: Sunlit Valley* /
*Create Colonies* — gemütliches Cozy-/Stardew-Feeling kombiniert mit Engineering und
Gemeinschaftsaufbau. Spieler farmen, kochen, züchten Tiere, bauen ihre Kolonie, automatisieren
mit Create (inkl. Luftschiffen) und folgen Quests mit einer Coin-Wirtschaft als rotem Faden.

Die Welt ist **riesig und realistisch** (Terralith + Tectonic): weitläufige, epische
Landschaften, in denen **mehrere Zivilisationen** entstehen, die über ein **Zug-Netz**
(Create + Steam 'n' Rails) miteinander verbunden werden. Reisen, Handel und Logistik
zwischen den Siedlungen sind ein zentrales Spielziel.

## Rahmenbedingungen (entschieden)

| Punkt | Entscheidung |
|-------|--------------|
| Minecraft-Version | **1.21.1** |
| Mod-Loader | **NeoForge** |
| Spielmodus | **Multiplayer / SMP** (mit Freunden) |
| Umfang | **Kitchen-Sink, ~150+ Mods** |
| Build-Tooling | **Packwiz** (Pack als Textdateien, versionierbar) |
| Export-Ziele | **.mrpack** (Client) + **Server-Pack** |
| Optik | **Shader-ready, standardmäßig aus** (optionales Iris/Oculus-Äquivalent) |
| Land-Schutz | **FTB Chunks** (Claims + Schutz, integriert mit FTB Teams) |
| Progression/Wirtschaft | **FTB Quests + Magic Coins** (Currency-Rewards-Integration) |
| Weltgenerierung | **Terralith + Tectonic** (riesige, realistische Biome) |
| Create-Addons | **So viele wie möglich** (auf 1.21.1 NeoForge kompatibel) |
| Gameplay-Ziel | Mehrere Zivilisationen, per **Zug-Netz** verbunden |

### Begründung der Versionswahl
Beide Anker-Mods werden aktiv auf 1.21.1 NeoForge gepflegt:
- **Create Aeronautics** v1.3.0 (Update 13.06.2026) — aktive Entwicklung auf 1.21.1.
- **MineColonies** — aktuelle 1.21.1-NeoForge-Builds.
- **Farmer's Delight** 1.3.2 (Mai 2026), **FTB Quests** 2101.1.15, **Magic Coins** — alle auf 1.21.1 NeoForge verfügbar.

1.20.1 wurde verworfen, weil Create Aeronautics dort kaum noch Updates bekommt.

## Ansatz

*Society: Sunlit Valley* existiert nur für 1.20.1 und kann nicht 1:1 übernommen werden.
Stattdessen wird das Cozy-Farming-Erlebnis **aus Einzel-Mods auf 1.21.1 neu zusammengestellt** —
volle Kontrolle, aktuelle Versionen, saubere SMP-Tauglichkeit.

## Die 4 Säulen

1. **Farmen & Leben** — Crops, Kochen, Jahreszeiten, Tiere, Skills (Cozy-Herzstück)
2. **Bauen & Gemeinschaft** — MineColonies + mehrere Zivilisationen in einer riesigen Welt
3. **Technik & Mobilität** — Create (so viele Addons wie möglich) + Aeronautics + Zug-Netz
4. **Welt & Vernetzung** — riesige realistische Biome (Terralith + Tectonic), per Zug verbunden
5. **Ziele & Wirtschaft** — FTB Quests + Coin-Währung als roter Faden

## Mod-Kategorien

Die exakte, versions-gepinnte Mod-Liste entsteht im Implementierungsplan (jede Mod einzeln auf
1.21.1-NeoForge-Verfügbarkeit geprüft). Kategorien und Anker-Mods:

### 🌱 Farming – Crops & Kochen
- Farmer's Delight (1.3.2) + Croptopia + Kompatibilitäts-Bridge
- Create-Farming-/Verarbeitungs-Addons

### ☀️ Cozy / Stardew-Feeling
- Serene Seasons (Jahreszeiten, beeinflusst Anbau)
- Sunlit/Pufferfish's Skills (Skill-Trees: Farming, Mining, Fishing, Husbandry, Adventuring)
- Fishing-Mod, Möbel- & Deko-Mods (z.B. Macaw's, Another Furniture)

### 🐄 Tiere & Zucht
- Mehr Tierarten + erweiterte Zuchtmechanik (z.B. Naturalist + Husbandry-Mod)

### 🏘️ Gemeinschaft
- MineColonies + Dependencies (Structurize, Domum Ornamentum, BlockUI) + Kompatibilitäts-Addon

### ⚙️ Technik & Mobilität (Create + so viele Addons wie möglich)
- **Create** (Basis) + **Create Aeronautics** (v1.3.0, Luftschiffe/Flugzeuge)
- **Züge:** Create-eigenes Zug-System + **Create: Steam 'n' Rails** (Gleise, Signale, Schaffner, Kupplungen, Monorail)
- **Ziel: maximale Create-Addon-Abdeckung** auf 1.21.1 NeoForge. Kandidaten u.a.:
  Crafts & Additions (Strom), Create: Garnished, Create: Estrogen, Create Big Cannons,
  Create: New Age, Create Deco, Create: Copycats+, Create: Enchantment Industry,
  Create: Diesel Generators, Create Encased, Create Stuff & Additions, Create: Connected,
  Steam 'n' Rails u.v.m.
- **Auswahlregel:** Jedes Addon wird im Implementierungsplan einzeln auf 1.21.1-NeoForge-
  Verfügbarkeit + Kompatibilität mit der verwendeten Create-Version geprüft; nur kompatible kommen rein.

### 🌍 Weltgenerierung (riesig & realistisch)
- **Terralith** (95+ realistische/fantastische Biome, Strukturen, Höhlentypen)
- **Tectonic v3.0** (deutlich größeres, epischeres Terrain; mit Terralith kompatibel)
- Großzügige Biom-/Terrain-Skalierung konfiguriert für weitläufige Landschaften
- Optional: weitere Stardust-Labs-/Worldgen-Mods, sofern kompatibel

### 📜 Quests & Wirtschaft
- FTB Quests (2101.1.15) — Aufgaben/Belohnungen
- Magic Coins — Währung, integriert in FTB-Quest-Belohnungen, + Shop-Mechanik

### 🛡️ Server / SMP-Basis
- FTB Chunks (Claims/Schutz) + FTB Teams, Sleep-Voting, optional Grab-/Death-Komfort

### 🚀 Performance (Pflicht bei Kitchen-Sink)
- Embeddium (+Embeddium Extra), FerriteCore, ModernFix, Entity Culling, Starlight u.a.

### ✨ QoL (erweiterbar)
- Rezept-Anzeige (JEI/EMI), Map (JourneyMap/Xaero's), Inventar-Sortierung, Waypoints
- **Hinweis:** Diese Kategorie wird im Aufbau gemeinsam erweitert (weitere QoL-Mods nach Wunsch).

### 🎨 Optik (optional, shader-ready)
- Iris/Oculus-Äquivalent für NeoForge 1.21.1, Shader standardmäßig deaktiviert

## Packwiz-Struktur

```
modpack/
├── pack.toml              # Metadaten: MC 1.21.1, NeoForge
├── index.toml             # auto-generiert
├── mods/*.pw.toml         # je Mod eine versionierte Referenz
├── config/                # vorkonfigurierte Configs (Seasons, Quests, Coins, Chunks…)
└── README                 # Export-/Installations-Anleitung
```

Export: `packwiz modrinth export` (Client-.mrpack) und Server-Pack via packwiz-installer.

## Risiken & Annahmen

- **Create Aeronautics ist Alpha** → gelegentliche Bugs/Crashes möglich. Bleibt drin (Kernwunsch),
  wird auf eine stabile Version gepinnt.
- **Kitchen-Sink + MineColonies + Aeronautics + viele Create-Addons + Tectonic ist sehr serverlastig**
  → Server mit **≥ 8–10 GB RAM** empfohlen; ggf. Chunk-Pregeneration für die große Welt.
- **Viele Create-Addons** erhöhen Konflikt-/Update-Risiko → alle gegen dieselbe Create-Version pinnen,
  inkompatible weglassen statt erzwingen.
- **Tectonic/Terralith = große, komplexe Worldgen** → langsamere Chunk-Generierung; Pregen + großzügige
  Render-/Simulation-Distanz-Einstellung einplanen.
- **Mod-Konflikte** bei 150+ Mods → Performance-Mods + schrittweiser Aufbau/Test mindern das Risiko.
- Annahme: Alle Mitspieler nutzen denselben Launcher (Modrinth/Prism) zum Installieren des .mrpack.

## Offene Punkte (für Implementierung)

- Pack-Name + Icon
- Exakte versions-gepinnte Mod-Liste (~150+), pro Mod verifiziert
- Konkrete Quest-Linie / Coin-Balancing
- Finale QoL-Mod-Auswahl (gemeinsam erweitern)
