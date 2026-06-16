#!/usr/bin/env python3
"""Baut ein server-gefiltertes Pack-Zip aus dem Packwiz-Repo (pack/mods/*.pw.toml).

- Schließt client-only Mods aus (side = "client") — die crashen einen Dedicated Server.
- Nimmt "both" + "server" Mods.
- Modrinth-Mods: direkte [download]-URL. CurseForge-Mods: ForgeCDN-URL aus der file-id.
- Ergebnis: pack/Cozy-Farming-SMP-<version>-SERVER.zip (mods/ + SERVER-README.txt).

Aufruf:  python3 build-server-pack.py
"""
import os, re, sys, time, zipfile, tempfile, urllib.request, urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))
MODS = os.path.join(ROOT, "pack", "mods")
README = os.path.join(ROOT, "pack", "SERVER-README.txt")

def pack_version():
    t = open(os.path.join(ROOT, "pack", "pack.toml")).read()
    return (re.search(r'^version\s*=\s*"([^"]+)"', t, re.M) or [None, "0.0.0"])[1]

def download(url, dest):
    for _ in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 packbuild"})
            with urllib.request.urlopen(req, timeout=60) as r, open(dest, "wb") as f:
                f.write(r.read())
            return os.path.getsize(dest) > 0
        except Exception:
            time.sleep(1)
    return False

def main():
    tmp = tempfile.mkdtemp()
    moddir = os.path.join(tmp, "mods"); os.makedirs(moddir)
    ok = skip = 0; fails = []
    for fn in sorted(os.listdir(MODS)):
        if not fn.endswith(".pw.toml"):
            continue
        t = open(os.path.join(MODS, fn)).read()
        side = (re.search(r'^side\s*=\s*"([^"]+)"', t, re.M) or [None, "both"])[1]
        if side == "client":
            skip += 1; continue
        jar = re.search(r'^filename\s*=\s*"([^"]+)"', t, re.M).group(1)
        m = re.search(r'url\s*=\s*"([^"]+)"', t)
        if m:
            url = m.group(1)
        else:  # CurseForge: ForgeCDN aus file-id
            fid = int(re.search(r'file-id\s*=\s*(\d+)', t).group(1))
            url = f"https://mediafilez.forgecdn.net/files/{fid//1000}/{fid%1000}/" + urllib.parse.quote(jar)
        if download(url, os.path.join(moddir, jar)):
            ok += 1
        else:
            fails.append(fn)
    ver = pack_version()
    zpath = os.path.join(ROOT, "pack", f"Cozy-Farming-SMP-{ver}-SERVER.zip")
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        if os.path.exists(README):
            z.write(README, "SERVER-README.txt")
        for j in sorted(os.listdir(moddir)):
            z.write(os.path.join(moddir, j), "mods/" + j)
    print(f"downloaded={ok} client-skipped={skip} failed={len(fails)} -> {zpath}")
    for x in fails:
        print("  FAIL", x)
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
