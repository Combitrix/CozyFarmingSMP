#!/usr/bin/env bash
# Erzeugt beide Editionen: mrpack (vollständig) + CurseForge-Zip (nur CF-referenzierbare Inhalte).
set -euo pipefail
PACK="$(cd "$(dirname "$0")/../pack" && pwd)"
PW=/home/claude/gopath/bin/packwiz
cd "$PACK"
rm -f *.mrpack *.zip
$PW refresh
# ARR/Opt-out-Mods: nicht ins mrpack einbettbar -> temporär raus (manueller Download, siehe README)
MREXCL=(mods/simulated-jet-engines-aero-propulsion.pw.toml mods/create-simulated-jet-engines-aero-propulsion.pw.toml)
TMPMR=$(mktemp -d)
for f in "${MREXCL[@]}"; do [ -f "$f" ] && mkdir -p "$TMPMR/$(dirname "$f")" && mv "$f" "$TMPMR/$f"; done
$PW refresh >/dev/null
$PW modrinth export
for f in "${MREXCL[@]}"; do [ -f "$TMPMR/$f" ] && mv "$TMPMR/$f" "$f"; done
rm -rf "$TMPMR"
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
