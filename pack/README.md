# Cozy Farming SMP — Modpack

Ein farm-lastiges Kitchen-Sink-SMP für **Minecraft 1.21.1 / NeoForge 21.1.233**.
Verwaltet mit [Packwiz](https://packwiz.infra.link/). **163 Mods + 5 Shaderpacks** (Stand 0.9.12) — stark Create- & Farming-lastig.

Säulen: Farmen & Leben · MineColonies (mehrere Kolonien/Spieler) · Create + Aeronautics + Zug-Netz ·
riesige Welt (Terralith + Tectonic) · FTB Quests + Coin-Wirtschaft.

---

## Installation — Client

1. **Modrinth App** oder **Prism Launcher** installieren.
2. Die aktuelle `.mrpack`-Datei importieren
   (Modrinth App: *Add Instance → From file* · Prism: *Add Instance → Import → .mrpack*).
3. Der Instanz **≥ 6–8 GB RAM** zuweisen (Einstellungen → Java/Memory).
4. **Java-Args setzen** (siehe Abschnitt „Beste Java-Args" unten).
5. Starten. Erststart dauert länger (Mod-Setup).

> **Shader:** 5 beliebte Shaderpacks **liegen bei** (in `shaderpacks/`): Complementary Reimagined,
> Complementary Unbound, BSL, Sildur's Vibrant, Photon. Aktivieren in *Optionen → Sodium/Iris →
> Shader Packs* — standardmäßig ist **keiner** an. Auf schwächeren PCs Shader aus + DH-Qualität runter.

## 🗺️ Web-Maps
- **squaremap** (Server, 2D, leichtgewichtig) — Live-Karte der ganzen Welt im Browser.
  Standard-Port **8080**, Config in `config/squaremap/`. Auf AMP den Port freigeben/forwarden.
- **BlueMap** (Server, 3D, zum Testen) — Standard-Port **8100**, Config in `config/bluemap/`.
  `accept-download: true` ist vorgesetzt (lädt die Web-Oberfläche beim 1. Start). Erst-Render dauert,
  kostet CPU/Speicher — bei Bedarf wieder rausnehmen.
- **JourneyMap-Webmap** (Client, nur DEINE erkundete Karte, lokal): im Vollbild-Map-Screen →
  *Optionen* die Web-Map einschalten; läuft dann auf `localhost` im Browser. (Pro Spieler, nicht geteilt.)

## Installation — Server (25 GB RAM)

1. NeoForge **21.1.233**-Server für MC 1.21.1 installieren.
2. Pack-Repo (Ordner `pack/`) per HTTP erreichbar machen **oder** lokal nutzen.
3. Mit `packwiz-installer-bootstrap.jar` die Server-Seite ziehen (nur `both`+`server`-Mods):
   ```bash
   java -jar packwiz-installer-bootstrap.jar -g -s server <URL-oder-Pfad>/pack.toml
   ```
   → Client-only-Mods (Sodium, Iris, Distant Horizons, JourneyMap, Inventory Profiles) werden
   **nicht** geladen.
4. **Java-Args setzen** (siehe Abschnitt „Beste Java-Args" unten) — bei AMP ins Feld
   *Configuration → Java/Startup → Additional Java Arguments* bzw. in `user_jvm_args.txt`.
5. Start: `./run.sh`. Fertig bei `Done (...)! For help, type "help"`.

---

## Beste Java-Args (Performance)

Beide Profile nutzen **Aikar's Flags** (G1GC, auf Minecraft abgestimmt) und setzen
**dieselbe Zahl für `-Xms` und `-Xmx`** — das verhindert teures Heap-Resizing und GC-Spikes.
Voraussetzung: ein **moderner Java-17+-Build** (Java 21 empfohlen für MC 1.21.1).

> ⚠️ **Nicht** mehr RAM als nötig geben. G1GC arbeitet bei riesigen Heaps schlechter; lieber
> 8–12 GB sauber konfiguriert als 24 GB ohne passende Flags.

### Client (Prism Launcher) — ~8 GB

Prism: *Instanz → Settings → Java → JVM arguments* (und „Memory" auf min=max=8192 MB stellen,
oder via `-Xms`/`-Xmx` hier). Empfohlen **6–10 GB** je nach PC; unten 8 GB:

```
-Xms8G -Xmx8G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true
```

> Distant Horizons + Sodium/Iris sind CPU/GPU-lastig, nicht RAM-lastig. Mehr als ~10 GB bringt
> dem Client kaum etwas — eher DH-LOD-Threads und Render-Distanz justieren.

> 🟢 **Distant-Horizons-Empfehlung (statt G1GC): ZGC.** DH warnt beim Start, dass G1GC mit DH
> Mikroruckler verursachen kann, und empfiehlt einen nebenläufigen Collector. Mit **Java 21**
> (NeoForge 1.21.1) ist **Generational ZGC** für den Client die ruhigere Wahl. Dann **nur** diese
> Flags nutzen (NICHT mit den G1GC-Aikar-Flags mischen):
> ```
> -Xms8G -Xmx8G -XX:+UseZGC -XX:+ZGenerational -XX:+AlwaysPreTouch -XX:+PerfDisableSharedMem -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC
> ```
> Ältere Java-Version (8–17)? Dann statt ZGC `-XX:+UseShenandoahGC` verwenden. Der Server kann bei
> den G1GC-Aikar-Flags bleiben (dort ist Durchsatz wichtiger als ruckelfreies LOD-Rendering).

### Server (AMP, 25 GB Box) — 16 GB Heap (`>12 GB`-Variante)

**Nicht** die vollen 25 GB an die JVM geben! Reserviere RAM fürs OS, Distant-Horizons-Serverdaten
und Off-Heap (Chunky/Worldgen). **16 GB Heap** ist für ~5 Spieler + MineColonies + Create reichlich;
notfalls auf 20 GB erhöhen, falls GC-Logs Druck zeigen. Die Flags unten sind die offizielle Aikar-
**>12-GB-Variante** (größere Young-Gen, früheres Mixed-GC):

```
-Xms16G -Xmx16G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=40 -XX:G1MaxNewSizePercent=50 -XX:G1HeapRegionSize=16M -XX:G1ReservePercent=15 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=20 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true
```

**Unterschiede zur Client-Variante** (>12 GB Heap): `G1NewSizePercent=40`,
`G1MaxNewSizePercent=50`, `G1HeapRegionSize=16M`, `G1ReservePercent=15`,
`InitiatingHeapOccupancyPercent=20`.

**In AMP setzen:**
- Heap-Größe: *Configuration → Java/Startup* → Min/Max-Heap **beide 16384 MB** (= `-Xms`/`-Xmx`).
- Restliche Flags (ab `-XX:+UseG1GC` …) ins Feld **Additional Java Arguments**.
- AMP verwaltet `-Xms`/`-Xmx` selbst — diese **nicht** zusätzlich in die Additional Args schreiben,
  sonst doppelt. Nur die `-XX:`/`-D`-Flags dort eintragen.

> RAM-Budget der 25-GB-Box (Richtwert): **16 GB JVM-Heap** + ~2–3 GB JVM-Off-Heap/Metaspace +
> ~2 GB Distant-Horizons-Serverdaten/Chunky + Rest fürs LXC-OS. Lässt komfortablen Puffer.

---

## Wichtige Konfiguration (nach dem 1. Start)

**MineColonies — mehrere Kolonien pro Spieler (unbegrenzt):**
Liegt dem Pack als `config/minecolonies-server.toml` **bei** (wird mit ausgeliefert; fehlende Keys
ergänzt MineColonies beim 1. Start mit Defaults). Gesetzte Werte (Keys gegen den MineColonies-
Quellcode verifiziert, `ServerConfiguration.java`):

| Sektion | Key | Wert | Wirkung |
|---|---|---|---|
| `[gameplay]` | `allowinfinitecolonies` | `true` | **Kernschalter** — erlaubt jedem Spieler beliebig viele Kolonien (Default = 1). |
| `[gameplay]` | `forceloadcolony` | `true` | Kolonie-Chunks bleiben geladen (Arbeiter laufen auch ohne Spieler). |
| `[gameplay]` | `colonyloadstrictness` | `3` | Geladener Radius (Chunks) je Kolonie. Höher = mehr RAM/TPS-Last. |
| `[claims]` | `maxColonySize` | `30` | Claim-Radius je Kolonie in Chunks (Default 20) — **erhöht für große Kolonien** (~480 Blöcke). |
| `[claims]` | `minColonyDistance` | `16` | Mindestabstand zwischen Kolonien in Chunks. Verhindert Überlappung großer Claims, lässt Platz für Zug-Trassen. |
| `[claims]` | `maxdistancefromworldspawn` | *(Default 30000)* | Nicht gesetzt — Default reicht für die große Terralith-Welt. |
| `[permissions]` | `enablecolonyprotection` | `true` | Grief-Schutz im Claim (Mobs/fremde Spieler). |

> Auf dem Server liegt die maßgebliche Datei in `config/minecolonies-server.toml` — sie wird beim
> Connect auf die Clients gesynct. Werte änderbar im laufenden Betrieb über das MineColonies-Config-
> GUI oder direkt in der Datei (danach Server-Reload/-Neustart).

**FTB Chunks ↔ MineColonies (zwei getrennte Claim-Systeme):**
- MineColonies **lädt und schützt seine Kolonie-Chunks selbst** (`forceloadcolony`/`colonyloadstrictness`).
  FTB-Chunks-Claims sind für **persönliche Bauten außerhalb** der Kolonien gedacht. Sie dürfen sich
  optisch überlappen, kollidieren funktional aber nicht.
- **Wichtig:** Kolonie-Chunks **nicht zusätzlich** per FTB Chunks force-loaden — spart das
  FTB-Force-Load-Budget (Default **25** Chunks/Team, Key `max_force_loaded_chunks`).
- FTB-Chunks-Limits (für große Bau-/Zug-Areale) bei Bedarf erhöhen — am einfachsten in-game über
  `/ftbchunks admin` (GUI), Keys: `max_claimed_chunks` (Default 500/Team) und
  `max_force_loaded_chunks` (Default 25/Team). Für ~5 Spieler reichen die Defaults meist.
- Kolonie-Claims sind groß (`maxColonySize=30`). Wenn Spieler **zusätzlich** per FTB Chunks rund um
  ihre Kolonie claimen wollen, ggf. das FTB-Claim-Limit (`max_claimed_chunks`) erhöhen — beide
  Schutzzonen dürfen sich überlagern.

**Wirtschaft:** **Magic Coins** = Währung für FTB-Quests-Belohnungen (Currency Rewards im Quest-Editor
einstellbar). **Create: Numismatics** = physische Münzen/Handel/Automaten (passt zum Zug-/Handels-Thema).

**Quest-Linie (liegt dem Pack bei, `config/ftbquests/quests/`):** EIN großer Quest-Baum auf
**einer einzigen Seite** (`chapters/questline.snbt`, **154 Quests**), der sich **progressiv
aufbaut** — eine durchgehende Haupt-Linie mit Seitenzweigen, alles über Abhängigkeiten verkettet:

- **👋 Willkommen** (ATM-Style: zentrale Wurzel + EMI/JourneyMap/IPN/FTB-Chunks-Intro)
  → **🌱 Farmen & Leben** → **🏘 Bauen & Gemeinschaft** (MineColonies)
  → **⚙ Create** (~**16 aufbauende Kontraptions-Meilensteine**: erste Maschine → Pressen → Erz-
  Verarbeitung → Auto-Crafting → Farm-/Baumfarm-Kontraption → Küche/Fabrik/Strom → Züge →
  **Industrie-Komplex**) → **🌍 Welt** → **🪙 Wirtschaft** → **🏆 Endgame**.
- **🎈 Aeronautics** (**28 Quests**, inkl. Massenproduktion: Propeller → Hülle → Levitite → Flotte → „Herr der Lüfte")
  als großer Seitenzweig rechts, hinter den Create-Kontraptionen; mündet ins Endgame.

**Keine Klick-Checkmarks als Fortschritt:** Fortschritts-Quests sind **Item-Tasks**, die
**automatisch erfasst** werden, sobald man die Items/Maschinen hat. Checkmarks gibt es nur für
reine **Info-Quests** (EMI, Karte, IPN, Jahreszeiten, Skills, DH) — diese geben **keine Belohnung**.
Belohnungen (Silber→Gold→Kristall) skalieren mit der Größe des Meilensteins.

**Endgame = Massenautomatisierung:** sehr große, automatisierbare Ziele, die per Quest-Buch
abgegeben werden (`consume_items`) — u. a. **10.000 Precision Mechanisms**, 50.000 Andesite Alloy,
50.000 Eisen, 50.000 Holz, 50.000 Kartoffeln, 30.000 Kupfer, 20.000 Messing, 10.000 Diamanten,
10.000 gekochter Reis, 5.000 Levitite, 64 Kristallmünzen → Capstone **„Legende des SMP"**.
Bearbeitbar im FTB-Quests-Editor (Server-Op: `/ftbquests editing_mode true`).

> Erzeugt von `gen-quests.py` als **ein** Kapitel (`chapters/questline.snbt`, alle Cluster versetzt
> zusammengeführt). Blueprint: `docs/quest-line-blueprint.md`.

**Distant Horizons + Chunky:** DH meldet evtl. „Chunky detected" — Chunky kann Chunks schneller
erzeugen, als DH die LODs verarbeitet (→ Löcher in der Fernsicht). Abhilfe: entweder DHs **eigenen**
Distant-Generator nutzen **oder** DHs CPU-Thread-Zahl erhöhen. Chunky ist absichtlich dabei (Pregen
v.a. serverseitig sinnvoll).

**Pregeneration (große Welt):** Server-Konsole → `chunky radius 5000` dann `chunky start`.

---

## 🖐️ Verifikations-Checkliste (auf deinem PC/Server)

Diese Schritte konnten beim Bau nicht automatisch getestet werden (kein Minecraft in der Build-Umgebung):

- [ ] **Client startet** bis Hauptmenü, keine „Missing dependencies".
- [ ] **Create-6-Kompat:** Addons aus `EXCLUDED.md` (⚠️-Liste: Aeronautics, Nuclear, Dreams&Desires,
      Misc&Things, Enchantment Industry, Railways Navigator) auf Crash/Mixin-Konflikte prüfen.
      Bei Crash: einzeln entfernen (`packwiz remove <slug>`), in `EXCLUDED.md` notieren.
- [ ] **Worldgen:** Test-Welt → Terralith-Biome + episches Tectonic-Terrain, keine Worldgen-Crashes.
- [ ] **Server startet** ohne client-only-Mods.
- [ ] **MineColonies:** 2 Kolonien als ein Spieler gründbar (Abstand testen).
- [ ] **Quests/Coins:** FTB-Quest mit Coin-Reward funktioniert.
- [ ] **Distant Horizons:** LOD-Sichtweite + optionale Shader spielen zusammen.
- [ ] **Terrain↔Zug:** Falls Tectonic zu extrem für Zug-Trassen → `config/tectonic.json` entschärfen
      (vor ernsthaftem Spielstart, da Welt-Neugenerierung!).

## Update-Politik

Alle Versionen sind via Packwiz **gepinnt**. Updates nur bewusst (`packwiz update <slug>`), **immer mit
Backup vorher** — Create Aeronautics ist Alpha und kann Kontraptionen/Welt brechen.

## Pack neu bauen / exportieren

```bash
cd pack
packwiz refresh
packwiz modrinth export      # erzeugt die .mrpack
```

Siehe `EXCLUDED.md` für weggelassene Mods, Risiko-Addons und Design-Entscheidungen.
