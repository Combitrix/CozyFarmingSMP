# Mod-Status-Log

**Pinned Create: 6.0.10+mc1.21.1 (Create-6-Linie)** — alle Create-Addons müssen dazu passen.

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
