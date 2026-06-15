# Cozy-Farming-SMP Modpack — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ein farm-lastiges, kitchen-sink SMP-Modpack für Minecraft 1.21.1 / NeoForge mit Packwiz aufbauen, das inkrementell und konfliktfrei lädt und als Client-`.mrpack` + Server-Pack exportierbar ist.

**Architecture:** Pack wird als Packwiz-Repo (Textdateien, git-versioniert) **schichtweise** aufgebaut. Reihenfolge: Fundament → Performance/Render-Stack → Worldgen → Create → Farming → MineColonies → Quests/Wirtschaft → Abenteuer → QoL/Sichtweite → Server/Side-Split/Pregen → Quest-Linie → finaler Integrationstest & Export. Nach **jeder Schicht** wird geladen/getestet und committet, damit Mod-Konflikte sofort lokalisierbar sind.

**Tech Stack:** Minecraft 1.21.1, NeoForge (21.1.x), Packwiz (CLI), Sodium+Iris (Render-Stack), Distant Horizons, Chunky, FTB-Suite, Create + Addons, MineColonies, Terralith + Tectonic.

**Spec:** `docs/superpowers/specs/2026-06-15-cozy-farming-smp-modpack-design.md`

---

## Konventionen & Voraussetzungen

**Test-Adaption (statt Unit-Tests):** Jede Schicht hat eine **Lade-Verifikation**:
- **Packwiz-Verifikation** (hier/überall machbar): `packwiz refresh` läuft fehlerfrei; `index.toml` enthält die erwarteten Einträge.
- **Client-Verifikation** (auf deinem PC): Pack im Modrinth-/Prism-Launcher starten → Spiel erreicht Hauptmenü ohne „Missing dependencies"/Crash.
- **Server-Verifikation** (auf dem Server, ab Phase 10): `./run.sh` → Konsole erreicht `Done (xxs)! For help, type "help"` ohne fehlende serverseitige Mods.

**🖐️ Manuelle Schritte** (nicht in dieser Umgebung möglich) sind mit 🖐️ markiert — sie erfordern deinen PC/Server mit Minecraft.

**Werkzeuge installieren (einmalig):**
- Packwiz: `go install github.com/packwiz/packwiz@latest` (oder Release-Binary). Verifiziere: `packwiz --help`.
- Für CurseForge-only-Mods: CurseForge-API-Key bzw. manueller `.jar`-Import via `packwiz url add`.

**Mod hinzufügen — Standardprozedur (überall referenziert):**
```bash
# Bevorzugt Modrinth (Slug oder Suchbegriff):
packwiz modrinth add <slug>
# Exakte Version per URL (wenn nötig):
packwiz modrinth install <modrinth-version-url>
# CurseForge:
packwiz curseforge add <slug>
```
Packwiz löst automatisch die **neueste mit MC 1.21.1 + NeoForge kompatible** Version + Abhängigkeiten auf. Bei Mehrdeutigkeit interaktiv die NeoForge-1.21.1-Datei wählen. Nach jedem Add: `packwiz refresh`.

**Kompatibilitätsregel (gilt für alle Mod-Tasks):** Wenn packwiz keine 1.21.1-NeoForge-Version findet ODER eine andere Create-Version verlangt als die gepinnte → **Mod weglassen** und im `EXCLUDED.md` mit Grund notieren. Niemals erzwingen.

**Commit-Regel:** Nach jeder erfolgreichen Schicht committen. Commit-Messages ohne Wasserzeichen/Co-Author-Zeilen.

---

## Phase 0 — Fundament

### Task 0: Packwiz-Repo initialisieren

**Files:**
- Create: `pack/pack.toml`, `pack/index.toml` (auto)
- Create: `pack/EXCLUDED.md` (Log für weggelassene Mods)
- Modify: Projekt-`.gitignore`

- [ ] **Step 1: NeoForge-Zielversion ermitteln**

🖐️/Recherche: Neueste **stabile** NeoForge-`21.1.x` für MC 1.21.1 bestimmen, die von **Create (NeoForge 1.21.1)** verlangt wird. Quelle: Create-Modrinth-Seite „Required NeoForge version". Notiere die exakte Versionsnummer (z.B. `21.1.xxx`).

Expected: Eine konkrete Versionsnummer, z.B. `21.1.193`.

- [ ] **Step 2: Pack initialisieren**

```bash
mkdir -p pack && cd pack
packwiz init \
  --name "Cozy Farming SMP" \
  --author "<dein-name>" \
  --version "0.1.0" \
  --mc-version 1.21.1 \
  --modloader neoforge \
  --neoforge-version <21.1.x aus Step 1>
```

- [ ] **Step 3: EXCLUDED-Log + gitignore anlegen**

```bash
printf '# Weggelassene Mods (mit Grund)\n\n' > pack/EXCLUDED.md
printf 'pack/.index-cache/\n*.mrpack\nserver-pack/\n' >> .gitignore
```

- [ ] **Step 4: Verifizieren**

```bash
cd pack && packwiz refresh
```
Expected: läuft fehlerfrei; `pack.toml` zeigt `mc-version = "1.21.1"` und die NeoForge-Version.

- [ ] **Step 5: Commit**

```bash
git add -A && git commit -m "Initialize packwiz pack: MC 1.21.1 NeoForge"
```

---

## Phase 1 — Performance & Render-Stack

> Entscheidung aus Spec: **Sodium + Iris** (NeoForge-Ports) statt Embeddium, wegen Distant-Horizons-/Shader-Kompatibilität. Fallback Embeddium nur falls Sodium+Iris auf NeoForge 1.21.1 nicht sauber zusammenspielt (dann im EXCLUDED.md begründen).

### Task 1: Core-Performance-Mods (server-tauglich)

**Files:** `pack/mods/*.pw.toml`

- [ ] **Step 1: Server-/beidseitige Performance-Mods hinzufügen**

```bash
cd pack
packwiz modrinth add ferrite-core
packwiz modrinth add modernfix
packwiz modrinth add entityculling
packwiz modrinth add lithium        # falls 1.21.1-NeoForge-Port vorhanden, sonst weglassen
packwiz refresh
```
Kompatibilitätsregel beachten (nicht vorhandene → EXCLUDED.md).

- [ ] **Step 2: Verifizieren**

`packwiz list` zeigt die hinzugefügten Mods; `packwiz refresh` fehlerfrei.

- [ ] **Step 3: Commit**

```bash
git add -A && git commit -m "Add core performance mods (FerriteCore, ModernFix, EntityCulling)"
```

### Task 2: Render-Stack (client-only) + Side-Markierung

**Files:** `pack/mods/sodium.pw.toml`, `pack/mods/iris.pw.toml` (Seiten-Attribut)

- [ ] **Step 1: Sodium + Iris (NeoForge) hinzufügen**

```bash
cd pack
packwiz modrinth add sodium     # NeoForge 1.21.1 Variante wählen
packwiz modrinth add iris       # Iris 1.7+ (DH-fähig)
packwiz refresh
```

- [ ] **Step 2: Als client-only markieren**

In `pack/mods/sodium.pw.toml` und `pack/mods/iris.pw.toml` jeweils unter `[option]`/Top-Level ergänzen:
```toml
side = "client"
```
(Falls packwiz das Feld bereits korrekt aus den Metadaten setzt, prüfen und nur bei `both` auf `client` korrigieren.)

- [ ] **Step 3: Verifizieren**

`grep -l 'side = "client"' pack/mods/*.pw.toml` listet sodium + iris.

- [ ] **Step 4: 🖐️ Client-Smoke-Test**

Pack im Launcher starten → Hauptmenü erreicht, keine Crash-Logs zu Renderer/Iris.

- [ ] **Step 5: Commit**

```bash
git add -A && git commit -m "Add client-only render stack (Sodium + Iris)"
```

---

## Phase 2 — Weltgenerierung

### Task 3: Terralith + Tectonic

**Files:** `pack/mods/*.pw.toml`, `pack/config/` (Tectonic-Config)

- [ ] **Step 1: Worldgen-Mods hinzufügen**

```bash
cd pack
packwiz modrinth add terralith
packwiz modrinth add tectonic
packwiz refresh
```

- [ ] **Step 2: Tectonic-Intensität konfigurieren**

Entscheidung aus Spec offen lassen → **Default belassen** (extrem) für ersten Durchlauf. Tectonic-Config-Datei (nach erstem Start generiert, z.B. `config/tectonic.json`) später anpassen, falls Zug-Trassen zu schwierig (siehe Phase 11-Review).

- [ ] **Step 3: 🖐️ Worldgen-Verifikation**

Neue Test-Welt erstellen → Terralith-Biome + episches Tectonic-Terrain sichtbar; keine Worldgen-Crashes im Log.

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "Add worldgen: Terralith + Tectonic"
```

---

## Phase 3 — Create-Stack (Kernschicht)

> Reihenfolge bewusst: erst Create-Basis pinnen, dann Addons **einzeln** dagegen prüfen.

### Task 4: Create-Basis + Aeronautics + Steam 'n' Rails

**Files:** `pack/mods/*.pw.toml`

- [ ] **Step 1: Create-Basis hinzufügen & Version notieren**

```bash
cd pack
packwiz modrinth add create        # NeoForge 1.21.1
packwiz refresh
```
Notiere die aufgelöste Create-Version in `EXCLUDED.md`-Kopf als „Pinned Create: <version>" — alle Addons müssen dazu passen.

- [ ] **Step 2: Aeronautics + Steam 'n' Rails**

```bash
packwiz modrinth add create-aeronautics            # v1.3.0 für 1.21.1
packwiz modrinth add create-steam-n-rails-1.21.1   # NeoForge-Port-Slug
packwiz refresh
```

- [ ] **Step 3: 🖐️ Client-Verifikation**

Spiel starten → kein Missing-Dependency; Create-Items im EMI/JEI vorhanden (EMI kommt in Phase 8 — hier nur Crash-Check).

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "Add Create base + Aeronautics + Steam 'n' Rails"
```

### Task 5: Create-Addons — maximale Abdeckung (iterativ)

**Files:** `pack/mods/*.pw.toml`, `pack/EXCLUDED.md`

Kandidatenliste (jeweils Standardprozedur + Kompatibilitätsregel). **Eines nach dem anderen** hinzufügen, nach jedem `packwiz refresh`:

- [ ] **Step 1: Addons durchgehen**

```bash
cd pack
for slug in \
  create-crafts-and-additions \
  create-deco \
  createaddition \
  create-enchantment-industry \
  create-encased \
  create-stuff-additions \
  create-connected \
  create-garnished \
  create-big-cannons \
  create-new-age \
  copycats ; do
    echo "=== $slug ==="; packwiz modrinth add "$slug" || echo "SKIP $slug -> EXCLUDED.md"; packwiz refresh; done
```
Für jeden, der keine 1.21.1-NeoForge-Version hat oder eine andere Create-Version verlangt: Zeile in `EXCLUDED.md` mit Grund. (Weitere Addons via Modrinth-Suche „create" + Filter 1.21.1/NeoForge ergänzen.)

- [ ] **Step 2: Verifizieren**

`packwiz list | grep -i create` zeigt alle aufgenommenen Create-Mods.

- [ ] **Step 3: 🖐️ Client-Verifikation**

Spiel starten → kein Crash, keine Mixin-Konflikte zwischen Addons im Log.

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "Add Create addons (max compatible coverage)"
```

---

## Phase 4 — Farming-Schicht

### Task 6: Crops, Kochen, Jahreszeiten

**Files:** `pack/mods/*.pw.toml`

- [ ] **Step 1: Farming-Mods hinzufügen**

```bash
cd pack
packwiz modrinth add farmers-delight
packwiz modrinth add croptopia
packwiz modrinth add farmers-croptopia    # Bridge Delight<->Croptopia
packwiz modrinth add serene-seasons
packwiz refresh
```

- [ ] **Step 2: Serene-Seasons-Kompatibilität sichern**

Sicherstellen, dass die Farmer's-Delight-Version mit Serene-Seasons-Fix verwendet wird (Spec-Recherche: FD ≥ 1.3 / Refabricated 2.4.0 hat den Fix). Bei Konflikt FD-Version per `packwiz modrinth install <url>` pinnen.

- [ ] **Step 3: 🖐️ Verifikation**

Welt starten → Crops/Gerichte im Inventar/EMI; Jahreszeiten-HUD vorhanden; kein Crash.

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "Add farming layer: Farmer's Delight, Croptopia, Serene Seasons"
```

### Task 7: Cozy-Skills, Tiere, Deko

**Files:** `pack/mods/*.pw.toml`

- [ ] **Step 1: Cozy/Skills/Tiere/Deko hinzufügen**

```bash
cd pack
packwiz modrinth add pufferfish-skills    # bzw. sunlit-skills
packwiz modrinth add naturalist           # mehr Tiere
packwiz modrinth add macaws-furniture     # Deko (Beispiel)
packwiz modrinth add another-furniture
packwiz refresh
```
Fishing-Mod (cozy) ergänzen, sofern 1.21.1-NeoForge vorhanden (sonst EXCLUDED.md).

- [ ] **Step 2: 🖐️ Verifikation**

Skill-Tree-UI öffnet; neue Tiere spawnen; Möbel platzierbar; kein Crash.

- [ ] **Step 3: Commit**

```bash
git add -A && git commit -m "Add cozy layer: skills, animals, furniture"
```

---

## Phase 5 — MineColonies

### Task 8: MineColonies + Multiplayer-Config

**Files:** `pack/mods/*.pw.toml`, `pack/config/minecolonies-server.toml`

- [ ] **Step 1: MineColonies + Abhängigkeiten**

```bash
cd pack
packwiz modrinth add minecolonies       # zieht Structurize, BlockUI, Domum Ornamentum
packwiz modrinth add minecolonies-compatibility   # falls als separater Slug nötig
packwiz refresh
```

- [ ] **Step 2: 🖐️ Erststart, um Config zu generieren**

Welt starten (damit `config/minecolonies-server.toml` erzeugt wird), dann beenden.

- [ ] **Step 3: Multiplayer-Werte setzen**

In `pack/config/minecolonies-server.toml` (Werte gemäß Spec: unbegrenzte Kolonien/Spieler, Steuerung über Abstand):
- Kolonie-Limit pro Spieler: deaktivieren bzw. sehr hoch (`maxColonySize`/`restrictColonies`-Flag aus, je nach Feldname).
- **Mindestabstand** zwischen Kolonien: moderat (z.B. `minColonyDistance = 8` Chunks) — verhindert Überlappung, erlaubt aber viele Kolonien.
- Claim-Radius kleinhalten, damit er mit FTB Chunks (Phase 6) koexistiert.

Konkrete Feldnamen beim Erststart prüfen und eintragen; Datei in git aufnehmen.

- [ ] **Step 4: 🖐️ Verifikation**

Zwei Kolonien als ein Spieler gründen (Abstand testen) → beide erlaubt; Bürger spawnen; kein Crash.

- [ ] **Step 5: Commit**

```bash
git add -A && git commit -m "Add MineColonies + multiplayer colony config"
```

---

## Phase 6 — Quests, Wirtschaft & SMP-Basis

### Task 9: FTB-Suite + Chunks

**Files:** `pack/mods/*.pw.toml`

- [ ] **Step 1: FTB-Mods hinzufügen**

```bash
cd pack
packwiz modrinth add ftb-quests          # zieht FTB Library/Teams
packwiz modrinth add ftb-chunks
packwiz refresh
```

- [ ] **Step 2: 🖐️ Verifikation & Claim-Abstimmung**

Welt starten → FTB-Chunks-Map (Karte) claimt Chunks; gegenprüfen, dass MineColonies-Claims sich nicht mit FTB-Claims beißen (ggf. MineColonies-Claim-Radius in Task 8 nachjustieren).

- [ ] **Step 3: Commit**

```bash
git add -A && git commit -m "Add FTB Quests, Teams/Library, FTB Chunks"
```

### Task 10: Coin-Wirtschaft (Magic Coins)

**Files:** `pack/mods/*.pw.toml`, `pack/config/` (Magic-Coins/Quests-Reward-Config)

- [ ] **Step 1: Magic Coins hinzufügen**

```bash
cd pack
packwiz modrinth add magic-coins
packwiz refresh
```

- [ ] **Step 2: FTB-Quests-Currency-Reward verbinden**

Sicherstellen, dass FTB Quests Magic-Coins als Currency-Reward erkennt (Spec-Recherche bestätigt Integration). Test-Quest mit Coin-Belohnung im Quest-Editor anlegen (Detail-Quests in Phase 11).

- [ ] **Step 3: 🖐️ Verifikation**

Coins erhältlich; FTB-Quest-Reward gibt Coins ins Wallet; kein Crash.

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "Add coin economy (Magic Coins) + FTB Quests integration"
```

---

## Phase 7 — Abenteuer (leichte Würze)

### Task 11: Dezente Dungeons/Strukturen/Mobs

**Files:** `pack/mods/*.pw.toml`

- [ ] **Step 1: Leichte Adventure-Mods hinzufügen**

```bash
cd pack
packwiz modrinth add dungeons-and-taverns   # oder vergleichbare Struktur-Mod (1.21.1)
packwiz modrinth add friends-and-foes        # dezente Mob-Erweiterung
packwiz refresh
```
Dosierung niedrig halten — Cozy-Farming bleibt dominant. Spawn-/Schwierigkeits-Configs später moderat einstellen. Inkompatible → EXCLUDED.md.

- [ ] **Step 2: 🖐️ Verifikation**

Neue Strukturen generieren in Test-Welt; Spiel stabil.

- [ ] **Step 3: Commit**

```bash
git add -A && git commit -m "Add light adventure layer (structures + mild mobs)"
```

---

## Phase 8 — QoL & Sichtweite

### Task 12: QoL-Mods

**Files:** `pack/mods/*.pw.toml`

- [ ] **Step 1: QoL hinzufügen**

```bash
cd pack
packwiz modrinth add emi                 # Rezept-Anzeige (client) — side beachten
packwiz modrinth add journeymap          # Map (client)
packwiz modrinth add jade                # Tooltips (both)
packwiz modrinth add inventory-profiles-next   # Sortierung (client)
packwiz refresh
```

- [ ] **Step 2: Side-Markierung**

Client-only QoL (EMI-Renderteil, JourneyMap-Client, Inventory-Profiles) korrekt `side = "client"` setzen (analog Task 2). EMI hat client+server-Teile → Doku prüfen; im Zweifel `both`.

- [ ] **Step 3: 🖐️ Verifikation**

Rezept-Anzeige, Map, Tooltips, Sortierung funktionieren.

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "Add QoL: EMI, JourneyMap, Jade, inventory sorting"
```

### Task 13: Distant Horizons (extreme Sichtweite)

**Files:** `pack/mods/distanthorizons.pw.toml`

- [ ] **Step 1: Distant Horizons hinzufügen**

```bash
cd pack
packwiz modrinth add distanthorizons     # 2.x, NeoForge 1.21.1
packwiz refresh
```

- [ ] **Step 2: Side setzen**

DH-Renderer ist **client-only** → `side = "client"`. (DH 2.1+ Server-Komponente separat evaluieren; im ersten Durchlauf client-only.)

- [ ] **Step 3: 🖐️ Verifikation**

Spiel starten → DH lädt; LOD-Sichtweite hochstellbar; Zusammenspiel mit Iris/Shader testen (Iris 1.7+ mit DH-fähigem Shaderpack).

- [ ] **Step 4: Commit**

```bash
git add -A && git commit -m "Add Distant Horizons (client-only extreme view distance)"
```

---

## Phase 9 — Server-Pack, Side-Split & Pregen

### Task 14: Side-Split-Audit

**Files:** alle `pack/mods/*.pw.toml`

- [ ] **Step 1: Vollständiges Side-Audit**

```bash
cd pack
grep -L 'side =' mods/*.pw.toml    # Mods OHNE explizites side -> prüfen
grep -l 'side = "client"' mods/*.pw.toml
```
Sicherstellen: client-only = Sodium, Iris, DH, JourneyMap, Inventory-Profiles, (EMI-Render). Alles andere `both`. Chunky/Backup = `server` (Task 16).

- [ ] **Step 2: Commit**

```bash
git add -A && git commit -m "Audit and finalize client/server side assignments"
```

### Task 15: Server-seitige Mods (Chunky, Backups)

**Files:** `pack/mods/chunky.pw.toml`, `pack/mods/ftb-backups.pw.toml`

- [ ] **Step 1: Hinzufügen + side = server**

```bash
cd pack
packwiz modrinth add chunky
packwiz modrinth add ftb-backups        # oder vergleichbare Backup-Mod (1.21.1)
packwiz refresh
```
In beiden `*.pw.toml`: `side = "server"`.

- [ ] **Step 2: Commit**

```bash
git add -A && git commit -m "Add server-only mods: Chunky pregen + backups"
```

### Task 16: Export & Server aufsetzen

**Files:** `server-pack/` (generiert), `<launcher>` (Client)

- [ ] **Step 1: Client-.mrpack exportieren**

```bash
cd pack && packwiz modrinth export
```
Expected: `Cozy Farming SMP-0.1.0.mrpack` erzeugt.

- [ ] **Step 2: 🖐️ Server-Pack via packwiz-installer**

Auf dem Server: NeoForge-1.21.1-Server installieren, dann `packwiz-installer-bootstrap.jar` mit der gehosteten `pack.toml`-URL + `-s server` ausführen (lädt nur `both`+`server`-Mods).

- [ ] **Step 3: 🖐️ Server-Start-Verifikation**

`./run.sh` → Konsole erreicht `Done`; keine client-only-Mods geladen (kein Sodium/Iris/DH auf Server). 25 GB RAM in `user_jvm_args.txt` setzen (`-Xmx24G`).

- [ ] **Step 4: 🖐️ Chunk-Pregen**

In Server-Konsole: `chunky radius <z.B. 5000>` + `chunky start`. Auf Fertigstellung warten.

- [ ] **Step 5: Commit**

```bash
git add -A && git commit -m "Export client mrpack; document server setup + pregen"
```

---

## Phase 10 — Quest-Linie & Balancing

### Task 17: Quest-Linie entlang der 5 Säulen

**Files:** `pack/config/ftbquests/` (Quest-Dateien)

- [ ] **Step 1: 🖐️ Quest-Kapitel im Editor anlegen**

In-Game FTB-Quests-Editor (Admin) → Kapitel entlang der Säulen:
1. Farmen & Leben (erste Crops, Kochen, Skills)
2. Bauen & Gemeinschaft (erste MineColonies-Kolonie)
3. Technik (erste Create-Maschine → Automatisierung)
4. Welt & Vernetzung (erste Zugstrecke zwischen zwei Kolonien)
5. Wirtschaft (Coin-Belohnungen, Shop-Aufbau)

- [ ] **Step 2: Coin-Belohnungen balancen**

Frühe Quests kleine Coin-Beträge, späte größere; Magic-Coins-Reward-Werte moderat (kein Inflation-Bruch).

- [ ] **Step 3: Quest-Dateien ins Pack übernehmen**

Generierte `config/ftbquests/**`-Dateien nach `pack/config/ftbquests/` kopieren, sodass sie im Export landen.

- [ ] **Step 4: 🖐️ Verifikation**

Frischer Spielstart → Quest-Buch zeigt alle Kapitel; Belohnungen funktionieren.

- [ ] **Step 5: Commit**

```bash
git add -A && git commit -m "Author quest line along the five pillars + coin balancing"
```

---

## Phase 11 — Finaler Integrationstest & Übergabe

### Task 18: Vollintegration & Doku

**Files:** `pack/README` (Installations-/Hardware-Doku), `pack/pack.toml` (Version-Bump)

- [ ] **Step 1: 🖐️ Voller SMP-Probelauf**

Server + ≥2 Clients: Kolonie gründen, farmen, Create-Maschine bauen, kurze Zugstrecke, Quest abschließen, Coins erhalten, Distant-Horizons-Sicht prüfen. Stabilität über längere Session beobachten (TPS).

- [ ] **Step 2: Terrain↔Zug-Review**

Falls Zug-Trassen wegen Tectonic zu mühsam: `config/tectonic.json`-Intensität reduzieren (Spec-Entscheidungspunkt) und Welt-Neugenerierung erwägen (vor ernsthaftem Spielstart!).

- [ ] **Step 3: README schreiben**

Inhalt: Installation (Launcher + .mrpack), Server-Setup, **Client-Hardware-Hinweis** (~6–8 GB RAM, DH/Shader optional/abschaltbar), Update-Politik (Versionen einfrieren, vor Update Backup), Liste der EXCLUDED-Mods.

- [ ] **Step 4: Version-Bump + Final-Export**

`pack.toml` Version → `1.0.0`; `packwiz refresh`; `packwiz modrinth export`.

- [ ] **Step 5: Commit**

```bash
git add -A && git commit -m "v1.0.0: full integration test, docs, final export"
```

---

## Spätere Teilprojekte (eigener Spec/Plan)

- **Eigene Mods („Kartoffelboss" etc.):** NeoForge-1.21.1-Mod-Entwicklung als getrenntes Brainstorming → Spec → Plan → Umsetzung, danach Integration ins Pack (als lokale Mod in `pack/mods/` mit `side = both`).

## Self-Review-Notiz

- **Spec-Abdeckung:** Alle 5 Säulen, Worldgen, Züge, Create-Addons, Quests+Coins, Side-Split, Backups, DH, Chunky, MineColonies-MP, Adventure, Custom-Mod-Subprojekt sind je einem Task zugeordnet. ✓
- **Offene Spec-Entscheidungen** (Render-Stack, Tectonic-Intensität, NeoForge-Pin) sind als konkrete Steps mit Default + Review-Punkt verankert, nicht als TODO. ✓
- **Mod-Slugs** sind Best-Effort-Kandidaten; die Kompatibilitätsregel + EXCLUDED.md fängt nicht-verfügbare/inkompatible Slugs deterministisch ab. ✓
