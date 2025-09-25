# TALOS MoCap VR (Starter)

> Open-source, room-scale mocap in a 12×12 ft lab using commodity webcams, VR headsets (Quest 3 / OpenXR), and ML-based pose fusion.  
> _Seed repo scaffold generated on 2025-09-25._

## What is this?
A batteries-included starter for your TALOS Labs MoCap/VR stack:
- **Webcam + VR sensor fusion** (Quest 3 or OpenXR) for full-body tracking in small rooms.
- **ML pipeline** for hand/body pose estimation and temporal smoothing.
- **VR integrations** for SteamVR/OpenXR backends.
- **Hardware** CAD/PCB/BOM folders to track rigs, mounts, and lighting layouts.

## Repo Map
```
hardware/              # CAD, PCB, BOM for rigs, mounts, lighting
software/              # Desktop/bridge apps, firmware for microcontrollers
ml/                    # Models, datasets, notebooks
design/                # Diagrams, branding, renders
docs/                  # Specs, architecture, how-tos, images
prototypes/            # Spike tests (e.g., Quest3↔Webcam bridge)
vr-integration/        # SteamVR + OpenXR shims/plugins
sim/                   # Simulation & replay tools
scripts/               # CLI helpers (packing, hashing, linting)
```

## Quickstart
1. **Clone & init LFS**
   ```bash
   git lfs install
   git clone <your-repo-url>
   ```
2. **Create a Python env (for tooling)**
   ```bash
   cd TALOS-MoCap-VR-starter
   python -m venv .venv && source .venv/bin/activate
   pip install -r scripts/requirements.txt
   ```
3. **Ship a Milestone Package**
   ```bash
   python scripts/pack_milestone.py v0.1 "Quest3 webcam bridge POC"
   # Upload the generated ZIP in /releases and paste the SHA-256 in the release notes.
   ```

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License
MIT for code. See `LICENSE`. Hardware and docs under CC-BY 4.0 unless noted.
