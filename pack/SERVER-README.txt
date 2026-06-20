Cozy Farming SMP — Server-Pack
==============================
Minecraft 1.21.1  /  NeoForge 21.1.233

INHALT DIESES ZIPS
  mods/      -> alle server-relevanten Mods (client-only wie Sodium/Iris/Distant
                Horizons/JourneyMap/Inventory Profiles/Controlling sind NICHT enthalten)
  config/    -> mitgelieferte Konfigurationen (u.a. minecolonies-server.toml,
                FTB-Quests-Questline) — beim ersten Start vorhanden
  kubejs/    -> server-seitige Rezept-Anpassungen (server_scripts/cozy_recipes.js)

INSTALLATION (AMP / generischer NeoForge-Server)
  1. NeoForge 21.1.233 fuer MC 1.21.1 installieren.
  2. Inhalt dieses Zips (mods/, config/, kubejs/) in den Server-Ordner entpacken
     (zu den vom NeoForge-Installer erzeugten run-Dateien).
  3. RAM/Java-Args setzen — siehe README.md des Packs (Server: 16 GB Heap, Aikar-G1GC).
     Bei AMP: Configuration -> Java/Startup -> Additional Java Arguments.
  4. Server starten. Fertig bei: Done (...)! For help, type "help".

CLIENTS
  Die Spieler nutzen das .mrpack (Prism/Modrinth-App). Die client-only Mods sind
  bewusst nur dort enthalten und werden vom Server nicht gebraucht.

WICHTIG
  - Vor dem ersten ernsthaften Start ggf. Welt mit Chunky vorgenerieren:
      chunky radius 5000   dann   chunky start
  - MineColonies-Einstellungen liegen in config/minecolonies-server.toml.
  - Versionsstand siehe pack.toml (version) im Packwiz-Repo.
