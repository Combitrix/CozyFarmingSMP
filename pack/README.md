# Cozy Farming SMP — Modpack

Ein farm-lastiges Kitchen-Sink-SMP für **Minecraft 1.21.1 / NeoForge 21.1.233**.
Verwaltet mit [Packwiz](https://packwiz.infra.link/). **112 Mods** in 0.1.0.

Säulen: Farmen & Leben · MineColonies (mehrere Kolonien/Spieler) · Create + Aeronautics + Zug-Netz ·
riesige Welt (Terralith + Tectonic) · FTB Quests + Coin-Wirtschaft.

---

## Installation — Client

1. **Modrinth App** oder **Prism Launcher** installieren.
2. Die Datei `Cozy Farming SMP-0.1.0.mrpack` importieren
   (Modrinth App: *Add Instance → From file* · Prism: *Add Instance → Import → .mrpack*).
3. Der Instanz **≥ 6–8 GB RAM** zuweisen (Einstellungen → Java/Memory).
4. Starten. Erststart dauert länger (Mod-Setup).

> **Shader/Sichtweite:** Distant Horizons (extreme Sichtweite) und Iris-Shader sind enthalten,
> standardmäßig dezent. Shader liegen nicht bei — ein DH-kompatibles Shaderpack (Iris 1.7+) selbst
> hinzufügen. Auf schwächeren PCs: DH-Qualität runter oder Shader aus.

## Installation — Server (25 GB RAM)

1. NeoForge **21.1.233**-Server für MC 1.21.1 installieren.
2. Pack-Repo (Ordner `pack/`) per HTTP erreichbar machen **oder** lokal nutzen.
3. Mit `packwiz-installer-bootstrap.jar` die Server-Seite ziehen (nur `both`+`server`-Mods):
   ```bash
   java -jar packwiz-installer-bootstrap.jar -g -s server <URL-oder-Pfad>/pack.toml
   ```
   → Client-only-Mods (Sodium, Iris, Distant Horizons, JourneyMap, Inventory Profiles) werden
   **nicht** geladen.
4. RAM setzen: in `user_jvm_args.txt` → `-Xmx24G`.
5. Start: `./run.sh`. Fertig bei `Done (...)! For help, type "help"`.

---

## Wichtige Konfiguration (nach dem 1. Start)

**MineColonies — mehrere Kolonien pro Spieler (unbegrenzt):**
Datei `config/minecolonies-server.toml` (wird beim 1. Start erzeugt). Setzen:
- `maxDistanceFromWorldSpawn` großzügig / aus
- Kolonie-Limit pro Spieler deaktivieren bzw. sehr hoch
- `minTownHallPadding` / Mindestabstand moderat (z.B. 8–16 Chunks), damit viele Kolonien koexistieren
- Claim-Radius **klein** halten → kollidiert weniger mit FTB Chunks

**FTB Chunks ↔ MineColonies:** Beide claimen Land. Bei Konflikten MineColonies-Claim-Radius
reduzieren oder FTB-Chunks-Force-Load-Limits anpassen.

**Wirtschaft:** **Magic Coins** = Währung für FTB-Quests-Belohnungen (Currency Rewards im Quest-Editor
einstellbar). **Create: Numismatics** = physische Münzen/Handel/Automaten (passt zum Zug-/Handels-Thema).

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
