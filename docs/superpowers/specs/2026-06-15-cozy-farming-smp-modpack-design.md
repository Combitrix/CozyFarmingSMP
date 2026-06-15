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
| Optik | **Shader-ready, standardmäßig aus** + **Distant Horizons** (extreme Sichtweite) |
| Pregeneration | **Chunky** (Welt im Voraus generieren) |
| Land-Schutz | **FTB Chunks** (Claims + Schutz, integriert mit FTB Teams) |
| Progression/Wirtschaft | **FTB Quests + Magic Coins** (Currency-Rewards-Integration) |
| Weltgenerierung | **Terralith + Tectonic** (riesige, realistische Biome) |
| Create-Addons | **So viele wie möglich** (auf 1.21.1 NeoForge kompatibel) |
| Gameplay-Ziel | Mehrere Zivilisationen, per **Zug-Netz** verbunden |
| Kolonien pro Spieler | **Unbegrenzt** (über Mindestabstand geregelt) |
| Abenteuer/Combat | **Leichte Würze** (etwas Gefahr/Dungeons), kein Combat-Fokus |
| Eigene Mods | **Optional, späteres Teilprojekt** (z.B. „Kartoffelboss") |
| Server-Hardware | **25 GB RAM**, max. ~**5 Spieler** |

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

## Die 5 Säulen

1. **Farmen & Leben** — Crops, Kochen, Jahreszeiten, Tiere, Skills (Cozy-Herzstück)
2. **Bauen & Gemeinschaft** — MineColonies, **mehrere Kolonien pro Spieler (unbegrenzt)** in einer riesigen Welt
3. **Technik & Mobilität** — Create (so viele Addons wie möglich) + Aeronautics + Zug-Netz
4. **Welt & Vernetzung** — riesige realistische Biome (Terralith + Tectonic), per Zug verbunden
5. **Ziele & Wirtschaft** — FTB Quests + Coin-Währung als roter Faden

Leichte Würze: etwas Gefahr/Dungeons (kein Combat-Fokus). Optionales Folge-Teilprojekt:
eigene, thematische Mods (z.B. ein „Kartoffelboss") — siehe Abschnitt „Eigene Inhalte".

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
- **Multiplayer-Config (wichtig):** mehrere Kolonien pro Spieler **unbegrenzt** erlauben
  (kein Kolonie-Limit), Gründung über **Mindestabstand** zwischen Kolonien geregelt.
- **Claim-Koexistenz:** MineColonies-Claim-Radius bewusst mit **FTB Chunks** abstimmen, damit sich
  die beiden Claim-/Schutzsysteme nicht beißen (Radien/Regeln im Plan festlegen).

### ⚔️ Abenteuer & Gefahr (leicht, optional würzig)
- Etwas Erkundung/Dungeons/Strukturen + moderate Gegner — **kein Hardcore-Combat-Fokus**
- Kandidaten im Plan prüfen (z.B. Strukturen-/Dungeon-Mod, dezente Mob-Erweiterung), so dosiert,
  dass das Cozy-Farming-Gefühl dominant bleibt

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
- **Chunky** — Chunk-Pregeneration der großen Terralith/Tectonic-Welt im Voraus
- **Backups** — automatische, regelmäßige Server-Backups (z.B. FTB Backups / serverseitig);
  Pflicht wegen Alpha-Aeronautics und langlebigem SMP

### 🚀 Performance (Pflicht bei Kitchen-Sink)
- **Renderer:** Sodium **oder** Embeddium — Auswahl hängt an der Render-Stack-Entscheidung unter
  „Optik & Sichtweite" (Sodium+Iris bevorzugt wegen DH+Shader-Kompatibilität auf NeoForge)
- FerriteCore, ModernFix, Entity Culling u.a.
- **Starlight:** auf NeoForge 1.21.1 erst auf Verfügbarkeit/Nutzen prüfen, ggf. weglassen
  (Lighting hier teils schon optimiert)

### ✨ QoL (erweiterbar)
- Rezept-Anzeige (JEI/EMI), Map (JourneyMap/Xaero's), Inventar-Sortierung, Waypoints
- **Hinweis:** Diese Kategorie wird im Aufbau gemeinsam erweitert (weitere QoL-Mods nach Wunsch).

### 🎨 Optik & Sichtweite (extreme Distanzen, shader-ready)
- **Distant Horizons 2.x** — extreme Sichtweite per LOD (clientseitig, kaum Server-TPS-Last);
  passt ideal zu den riesigen Terralith/Tectonic-Landschaften
- **Render-Stack-Entscheidung (Implementierung):** kohärenten Stack wählen, damit
  Distant Horizons + optionale Shader auf NeoForge zusammenspielen — voraussichtlich
  **Sodium + Iris (1.7+, DH-fähig)** statt Embeddium, da Embeddium auf NeoForge nicht sauber
  mit Iris/Shadern läuft. Shader standardmäßig deaktiviert, mit DH-kompatiblem Shaderpack als Empfehlung.

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

**Client-/Server-Seiten-Trennung (wichtig):** Jede Mod bekommt in ihrer `*.pw.toml` ein
`side = "client" | "server" | "both"`.
- **client-only:** Distant Horizons (Renderer), Sodium/Iris bzw. Embeddium, Minimap/Map-Rendering,
  Shader, Embeddium-Extra
- **server-only:** Chunky, ggf. Backup-Mod
- **both:** alle Gameplay-Mods (Create, MineColonies, Farming, Quests, Worldgen, …)
Ohne diese Trennung crasht der Server an client-only-Mods. Hinweis: Distant Horizons hat ab 2.1+
eine optionale Server-Komponente zum Teilen von LODs — separat prüfen.

## Eigene Inhalte (optionales Folge-Teilprojekt)

Eigene, thematische Mods passend zum Farming-Thema — z.B. ein **„Kartoffelboss"** (themen­gerechter
Boss/Dungeon). Dies ist **nicht Teil des Pack-Aufbaus**, sondern ein eigenes Projekt mit eigenem
Spec → Plan → Umsetzung (NeoForge-Mod-Entwicklung für 1.21.1), das später ins Pack integriert wird.
Wird hier nur als Vision festgehalten, um den aktuellen Plan fokussiert zu lassen.

## Risiken & Annahmen

- **Create Aeronautics ist Alpha** → gelegentliche Bugs/Crashes möglich. Bleibt drin (Kernwunsch),
  wird auf eine stabile Version gepinnt.
- **Server:** **25 GB RAM**, max. ~**5 Spieler** → reichlich Reserve für Kitchen-Sink + viele
  Create-Addons + Tectonic. RAM ist kein Engpass; Hauptlast bleibt **Single-Thread-TPS**
  (MineColonies-Bürger, Create-Kontraptionen, Aeronautics-Physik) — daher TPS-schonende Configs
  und Performance-Mods trotzdem Pflicht.
- **Viele Create-Addons** erhöhen Konflikt-/Update-Risiko → alle gegen dieselbe Create-Version pinnen,
  inkompatible weglassen statt erzwingen.
- **Tectonic/Terralith = große, komplexe Worldgen** → langsamere Chunk-Generierung; Chunk-Pregen
  (z.B. Chunky) für die große Welt einplanen, großzügige Render-/Simulation-Distanz möglich.
- **Mod-Konflikte** bei 150+ Mods → Performance-Mods + schrittweiser Aufbau/Test mindern das Risiko.
- **Client-Hardware:** 150+ Mods + Distant Horizons + Shader brauchen client-seitig ~6–8 GB RAM
  + brauchbare GPU. DH/Shader bleiben optional & abschaltbar; für schwächere PCs dokumentieren.
- **Terrain ↔ Zug-Netz-Spannung:** Tectonic macht das Gelände extrem → Zivilisationen per Zug zu
  verbinden ist ein großes Bauprojekt. Im Plan entscheiden: Tectonic-Intensität justieren ODER
  bewusst als Endgame-Herausforderung akzeptieren.
- **Update-/Versions-Politik:** Alle Mod-Versionen einfrieren (Packwiz pinnt). Updates nur bewusst,
  vorher Backup — Create Aeronautics (Alpha) kann Kontraptionen/Welt brechen.
- Annahme: Alle Mitspieler nutzen denselben Launcher (Modrinth/Prism) zum Installieren des .mrpack.

## Offene Punkte (für Implementierung)

- Pack-Name + Icon
- **Exakte NeoForge-Build-Version für 1.21.1 festlegen** (pinnen)
- Exakte versions-gepinnte Mod-Liste (~150+), pro Mod verifiziert + `side`-Zuordnung
- **Render-Stack final entscheiden** (Sodium+Iris vs. Embeddium) inkl. DH-/Shader-Kompatibilität
- MineColonies-Multiplayer-Werte (Mindestabstand, Claim-Radius) + FTB-Chunks-Abstimmung
- Tectonic-Intensität (extrem belassen vs. justieren) wegen Zug-Netz
- Dosierung Abenteuer/Gefahr (welche Dungeon-/Mob-Mods, wie viel)
- Konkrete Quest-Linie / Coin-Balancing (idealerweise entlang der 5 Säulen)
- Finale QoL-Mod-Auswahl (gemeinsam erweitern)
- Backup-Lösung wählen + Intervall

## Spätere Teilprojekte (eigener Spec/Plan)

- Eigene Mods („Kartoffelboss" etc.) — NeoForge-1.21.1-Mod-Entwicklung, danach Integration ins Pack
