# Design: Cozy-Farming-SMP Modpack

**Datum:** 2026-06-15
**Status:** Genehmigt (Design), QoL-Kategorie wird im Aufbau erweitert
**Arbeitstitel:** TBD (Pack-Name wird vor Export festgelegt)

## Vision

Ein farm-lastiges Multiplayer-Modpack (SMP) im Stil von *Society: Sunlit Valley* /
*Create Colonies* — gemütliches Cozy-/Stardew-Feeling kombiniert mit Engineering und
Gemeinschaftsaufbau. Spieler farmen, kochen, züchten Tiere, bauen ihre Kolonie, automatisieren
mit Create (inkl. Luftschiffen) und folgen Quests mit einer Coin-Wirtschaft als rotem Faden.

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
2. **Bauen & Gemeinschaft** — MineColonies (Kolonie/Dorf aufbauen)
3. **Technik & Mobilität** — Create + Create Aeronautics (Automatisierung + Luftschiffe)
4. **Ziele & Wirtschaft** — FTB Quests + Coin-Währung als roter Faden

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

### ⚙️ Technik & Mobilität
- Create + Create Aeronautics (v1.3.0) + ausgewählte Create-Addons

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
- **Kitchen-Sink + MineColonies + Aeronautics ist serverlastig** → Server mit **≥ 6–8 GB RAM**
  empfohlen.
- **Mod-Konflikte** bei 150+ Mods → Performance-Mods + schrittweiser Aufbau/Test mindern das Risiko.
- Annahme: Alle Mitspieler nutzen denselben Launcher (Modrinth/Prism) zum Installieren des .mrpack.

## Offene Punkte (für Implementierung)

- Pack-Name + Icon
- Exakte versions-gepinnte Mod-Liste (~150+), pro Mod verifiziert
- Konkrete Quest-Linie / Coin-Balancing
- Finale QoL-Mod-Auswahl (gemeinsam erweitern)
