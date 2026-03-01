# Navigation

## Planetary Navigation

- [Enhanced Autonomous Navigation (ENav)](https://doi.org/10.1109/TFR.2025.3636366) - Enhanced Navigation system used on NASA's Perseverance rover. It builds on AutoNav with improved processing speed and smarter path planning, allowing the rover to drive faster and more autonomously on Mars than any previous mission.
- [Terrain Relative Navigation (TRN)](https://www.nasa.gov/space-technology-mission-directorate/tdm/terrain-relative-navigation-trn) - NASA's Lander Vision System developed for Mars 2020. It uses a downward-facing camera during descent to match terrain features against onboard orbital maps, fusing landmarks with inertial measurements to estimate position within 60 metres. This enabled Perseverance to autonomously divert to a safe landing site within the hazardous Jezero Crater.

## Orbital Navigation

- [dSGP4](https://github.com/esa/dSGP4) - ESA's differentiable SGP4 orbital propagation library reimplemented with PyTorch automatic differentiation support. It enables gradient-based orbit determination, covariance propagation, and hybrid ML-augmented propagation with GPU-accelerated batch TLE processing.
- [Orekit](https://www.orekit.org) - Open source low-level space dynamics library written in Java. It provides tools for orbit propagation, coordinate transformations, and attitude computation used in spacecraft navigation and mission analysis.
