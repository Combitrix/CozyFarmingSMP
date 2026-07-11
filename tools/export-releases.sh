#!/usr/bin/env bash
# Erzeugt beide Editionen: mrpack (vollständig) + CurseForge-Zip (nur CF-referenzierbare Inhalte).
set -euo pipefail
PACK="$(cd "$(dirname "$0")/../pack" && pwd)"
PW=/home/claude/gopath/bin/packwiz
cd "$PACK"
rm -f *.mrpack *.zip
$PW refresh
$PW modrinth export
# Nicht-CF-Inhalte für den CF-Export temporär entfernen
TMP=$(mktemp -d)
mapfile -t NOCF < <(grep -rL "update.curseforge" mods/*.pw.toml resourcepacks/*.pw.toml shaderpacks/*.pw.toml 2>/dev/null || true)
for f in "${NOCF[@]}"; do mkdir -p "$TMP/$(dirname "$f")"; mv "$f" "$TMP/$f"; done
$PW refresh >/dev/null
$PW curseforge export
for f in "${NOCF[@]}"; do mv "$TMP/$f" "$f"; done
rm -rf "$TMP"
$PW refresh >/dev/null
echo "--- Editionen ---"; ls -lah *.mrpack *.zip | awk '{print $5, substr($0, index($0,$9))}'
[ ${#NOCF[@]} -gt 0 ] && echo "Nicht in CF-Edition: ${NOCF[*]}"
