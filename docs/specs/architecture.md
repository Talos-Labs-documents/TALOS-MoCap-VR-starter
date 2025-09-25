# Architecture

- **Sensors**: commodity webcams + VR IMUs (Quest 3/OpenXR)
- **Fusion**: pose estimation (hands/body) → temporal filter → IK solver
- **Transport**: local UDP/WebSocket → SteamVR/OpenXR driver
- **Room**: 12×12 ft reference lab layout with lighting map
