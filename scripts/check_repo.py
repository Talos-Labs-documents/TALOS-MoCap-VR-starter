#!/usr/bin/env python3
import os, sys, shutil

errors = []

def assert_exists(path):
    if not os.path.exists(path):
        errors.append(f"Missing: {path}")

# Minimal checks
for p in ["README.md", "LICENSE", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", ".gitattributes", ".gitignore"]:
    assert_exists(p)

if errors:
    print("\n".join(errors))
    sys.exit(1)
else:
    print("Repo looks good ✨")
