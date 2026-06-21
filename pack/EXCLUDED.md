# Mod-Status-Log

**Pinned Create: 6.0.10+mc1.21.1 (Create-6-Linie)** — alle Create-Addons müssen dazu passen.

## 📋 To Be Added (geplant, noch NICHT im Pack)
- **create-simple-ore-doubling** — *on hold:* User macht Ore Doubling stattdessen via **KubeJS** (KubeJS+Rhino+KubeJS-Create in 0.10.11 wieder rein). Mod bleibt als Fallback vorgemerkt, falls kubejs-create serverseitig doch crasht.

## 🔁 0.10.11 — KubeJS zurück
- **KubeJS 2101.7.2 + Rhino 2101.2.7 + KubeJS Create 2101.3.1** (alle side=both) wieder hinzugefügt, um Ore Doubling per Rezept-Script zu machen.
- ⚠️ **Achtung Dedicated Server:** kubejs-create build.18 crashte bei 0.9.8 beim Laden — `IllegalArgumentException: Wrapper for class …ProcessingOutput already exists!` in `KubeJSCreatePlugin.registerTypeWrappers` (Doppel-Registrierung des Rhino-Type-Wrappers, **nicht** scriptbedingt — Crash passiert vor jeder Script-Ausführung). Singleplayer lädt laut User normal; Pack hat sich seit 0.9.8 stark geändert. **Vor Server-Deploy auf MeinPack01 testen.** Falls es serverseitig wieder crasht: kubejs-create auf `side=client` setzen (dann fehlen aber serverseitige KubeJS-Create-Rezepte) oder den kollidierenden Create-Addon-KubeJS-Plugin finden.

## ⚠️ Aufgenommen, aber in-game gegen Create 6 verifizieren (🖐️)
Diese Addons hatten lt. Recherche evtl. ältere Create-5-Bauten oder Beta/Alpha-Stand —
beim ersten Start auf Crashes/Mixin-Konflikte prüfen, ggf. einzeln entfernen:
- create-aeronautics (Alpha, Kernwunsch)
- create-misc-and-things
- create-dreams-and-desires (Beta)
- createnuclear (Beta)
- create-enchantment-industry (preview-alpha)
- create-railways-navigator (Beta)

### Neu dazu (v0.8.0) — Create-6-Kompat & Stabilität in-game prüfen
Create-Addons: create-cafe, create-ratatouille, create-food, create-deepfried (+create-bitterballen),
create-integrated-farming, create-applied-kinetics, create-vibrant-vaults, create-storage-neo-forge,
create-mechanical-spawner (+mechanicals-lib).
Farming/Cooking: chefs-delight, more-delight (+delight-lib), rustic-delight, corn-delight (+mmlib),
fruits-delight, storage-delight, farming-for-blockheads (+balm), harvest-with-ease (+cobweb, server-side).
Cozy/Deko: handcrafted (+resourceful-lib), macaws-roofs, macaws-paths-and-pavings, chipped
(+athena-ctm client, +resourceful-lib), every-compat (+moonlight), dye-depot.
Tiere/Atmosphäre: critters-and-companions, companions-dogfolk, ribbits (+yungs-api), falling-leaves
(client), ambient-environment (client), sound-physics-remastered (client).
→ Alle Dependencies wurden gegen die Modrinth-API auditiert (vollständig vorhanden). Bei Crash einzeln
  via `packwiz remove <slug>` entfernen.

## ❌ Nicht verfügbar für 1.21.1 / NeoForge (weggelassen)
- **croptopia** — nur Fabric. Ersetzt durch Pam's HarvestCraft 2 + Farmer's-Delight-Addon-Suite.
- **farmers-croptopia** (Bridge) — hängt an Croptopia, daher unnötig.
- **friends-and-foes** — keine 1.21.1-NeoForge-Version.
- **numismatic-overhaul** — nur Fabric (ersetzt durch Magic Coins + Create: Numismatics).
- **memoryleakfix / catalogue / configured** — nicht auf Modrinth/NeoForge; durch ModernFix+FerriteCore abgedeckt.
- **mob-variants / more-mob-variants** — ersetzt durch more-mob-variants-renewed.
- **towers-of-the-wild-reworked** — nur Datapack, kein NeoForge-Mod.

## ℹ️ Entscheidungen
- Render-Stack: **Sodium + Iris** (nicht Embeddium — würde mit Iris/DH auf NeoForge kollidieren).
- Karte: **JourneyMap** (Xaero weggelassen, um Redundanz zu vermeiden).
- Rezept-Viewer: **EMI** (statt JEI).
- Wirtschaft: **Magic Coins** (FTB-Quests-Integration) + **Create: Numismatics** (Handel/Trains-Thema).

## ❌ Entfernt nach Crash-Test 0.8.0
- **create-applied-kinetics** — harter Crash beim Start: braucht **Applied Energistics 2** (`appeng.block.AEBaseEntityBlock`), das NICHT installiert ist (auf Modrinth nicht als *required* deklariert → Auto-Audit verfehlte es). AE2 ist bewusst **nicht** im Pack (Cozy-Farming-Fokus, kein schweres Tech-Storage). Bridge-Mod daher entfernt.

- **kubejs-create** — Server-Crash beim Laden: `IllegalArgumentException: Wrapper for class …ProcessingOutput already exists!` (KubeJS-Create-Bug, doppelte Wrapper-Registrierung). Entfernt; KubeJS + Rhino bleiben. Create-Maschinen-Rezepte erst mit kompatibler Version wieder möglich.

- **bluemap** — beim Servertest gecrasht; auf Wunsch komplett entfernt. Geteilte Web-Karte läuft stattdessen über **squaremap** (leichter, 2D). BlueMap-Config (`config/bluemap/`) ebenfalls entfernt.

## 🔄 Großer Umbau 0.10.0
- **Rezept-Viewer:** EMI → **JEI** (+ JER, Just Enough Professions/Breeding, NERB, JEED).
- **Coin-System entfernt** (Magic Coins + Create: Numismatics) — Quests geben jetzt XP; Wirtschaft via Vanilla-Smaragde/Villager.
- **KubeJS-Rezepte entfernt** (funktionierten nicht); KubeJS+Rhino raus.
- **Inventory Profiles Next entfernt** (unerwünscht) → MouseTweaks + CraftingTweaks; libipn raus.
- **squaremap entfernt** (Render-NPE durch Bountiful-Fares-getMapColor-Mixin), **BlueMap entfernt** (Server-Crash).
- **LambDynamicLights → sodium-dynamic-lights** (LambDL verlangte fabric-api auf NeoForge).
- **ambient-environment + falling-leaves entfernt** (Partikel in Menüs).
- **Alex's Mobs / Fast-Leaf-Decay(Modrinth) / Continuity:** nicht für 1.21.1-NeoForge verfügbar — Fast Leaf Decay via CurseForge ergänzt; Continuity-Ersatz = Athena (CTM, via Chipped).

- **sodium-dynamic-lights (+sodium-options-api +reeses-sodium-options)** — Crash beim Öffnen der Video-/Optionen-Settings: `sodium-options-api` mixin-t `FlatButtonWidget` (`@Shadow field dim`), inkompatibel mit Sodium 0.8-beta. Ganze Dynamic-Lights-Kette entfernt. Dynamic Lights vorerst nicht verfügbar (sodium-gebundene Addons brechen auf der Sodium-Beta). **ModernUI bleibt** (vom User gewünscht).

## 🔄 0.10.5 — Optik & Sortierer
- **Fresh Animations** (Resourcepack) + **FA: Extensions (All)** + **FA: Player Extension** — flüssige Mob-/Spieler-Animationen. Benötigt die Mods **EMF (Entity Model Features)** + **ETF (Entity Texture Features)**, beide ergänzt. Alle drei Packs in `options.txt` aktiviert (FA-Addons über der Basis).
- **3D Skin Layers** (client) — 3D-Skin-Auflagen.
- **Inventory-Sortierer: IPN → „Inventory Tweaks: ReFoxed"** (modId `invtweaks`, das ist auch ATM10s Sortierer). Sort-Button im Container + Sortierregeln + Auto-Refill, **ohne** die IPN-Hotbar-Pfeile, die der User nicht mochte. libIPN dadurch ebenfalls raus.
