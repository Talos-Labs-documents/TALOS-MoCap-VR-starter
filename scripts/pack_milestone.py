#!/usr/bin/env python3
import os, sys, zipfile, hashlib, time, pathlib

def sha256sum(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def pack(tag, note):
    root = pathlib.Path('.').resolve()
    out_dir = root / 'releases'
    out_dir.mkdir(exist_ok=True)
    zpath = out_dir / f'{root.name}-{tag}.zip'
    with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
        for p in root.rglob('*'):
            if str(p).startswith(str(out_dir)): 
                continue
            if p.is_file():
                z.write(p, p.relative_to(root))
    digest = sha256sum(zpath)
    readme = out_dir / f'{root.name}-{tag}-SHA256.txt'
    readme.write_text(f'{zpath.name}\nSHA-256: {digest}\nNotes: {note}\nTimestamp: {time.ctime()}\n')
    print(f'Packed {zpath}')
    print(f'SHA-256: {digest}')
    print(f'Notes saved to {readme}')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: pack_milestone.py <tag> <notes...>")
        sys.exit(1)
    tag = sys.argv[1]
    note = " ".join(sys.argv[2:])
    pack(tag, note)
