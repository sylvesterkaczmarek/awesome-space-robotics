# Verification & Validation

## Terrestrial Analogue Sites

- [Atacama Desert](https://en.wikipedia.org/wiki/Atacama_Desert) | Chile - One of the driest places on Earth, used as a Mars analogue for testing rover autonomy and astrobiology experiments due to its extreme aridity, UV radiation, and mineral composition similar to Mars.
- [Devon Island](https://en.wikipedia.org/wiki/Devon_Island) | Canada - The largest uninhabited island on Earth, hosting the Haughton-Mars Project. The Haughton impact crater provides Mars-like terrain used for testing rover operations and space suits.
- [Iceland](https://en.wikipedia.org/wiki/Iceland) - Volcanic island used extensively by NASA and ESA as a planetary analogue. Its glacial landscapes, lava fields, and volcanic terrain simulate lunar and Martian conditions for testing rover operations and sample collection techniques.
- [Lanzarote](https://en.wikipedia.org/wiki/Lanzarote) | Spain - Volcanic island in the Canary Islands used by ESA as an analogue site for lunar and planetary exploration testing. Its volcanic landscapes include lava tubes and basaltic terrain similar to lunar geology.
- [Mount Etna](https://en.wikipedia.org/wiki/Mount_Etna) | Italy - Active volcano with fresh volcanic soils and lava flows, serving as an excellent analogue for the Moon and Mars. ESA and DLR have tested several rovers and robotic operations at this site.

## Laboratory Facilities

### Orbital

- [ESA Orbital Robotics Laboratory](https://www.esa.int/Education/ESA_Academy_Experiments_programme/Orbital_Robotics_Laboratory) | Netherlands - Testbed at ESA's ESTEC featuring Europe's largest 2D free-floating platform, a 4.8x9 m flat floor with air-bearing systems that simulate microgravity for validating satellite docking, debris removal, and in-orbit servicing technologies. It is available to university students through the ESA Academy Experiments Programme.
- [Zero-G Lab](https://www.uni.lu/snt-en/facilities/zero-g-lab) | Luxembourg - Facility at the University of Luxembourg designed for testing 2D and 3D free-floating robotic systems in microgravity conditions. Its dark room features a 5x3 m flat epoxy floor on which pneumatic platforms use pressurized air to emulate free-floating behaviour in a 2D plane, while wall- and ceiling-mounted articulated robotic arms on linear rails extend the workspace into 3D. The lab is equipped with adjustable illumination and a motion capture system.

### Planetary

- [JPL Mars Yard](https://www-robotics.jpl.nasa.gov/how-we-do-it/facilities/marsyard-iii) | USA - Outdoor test facility at JPL designed to emulate the Martian surface. It is used for testing rover mobility, navigation, and instrument deployment on terrain representative of Mars conditions.
- [LUNA](https://luna-analog-facility.de/en) | Germany - ESA-DLR LUNA analogue facility at the European Astronaut Centre in Cologne. It features a large regolith testbed for testing lunar surface operations, including rover navigation and sample collection.
- [LunaLab](https://www.uni.lu/snt-en/facilities/lunalab) | Luxembourg - Moon analogue facility at the University of Luxembourg. It features an indoor 11x7 m area filled with 20 t of basalt gravel to emulate the surface of the Moon. LunaLab is equipped with adjustable illumination and a motion capture system to support the development and testing of lunar rovers.
- [Spaceport Rostock](https://testingfor.space) | Germany - Testing facility at Rostock-Laage Airport developed in collaboration with DLR. It features a test track for lunar and space vehicles and plans for microgravity testing infrastructure, positioning it as a hub for commercial and national space research.

### Navigation

- [TRON](https://www.dlr.de/en/research-and-transfer/research-infrastructure/testbed-for-robotic-optical-navigation-tron) | Germany - Testbed for Robotic Optical Navigation at the DLR Institute of Space Systems in Bremen. A hardware-in-the-loop facility for validating optical navigation sensors including cameras and lidar up to TRL 7. It uses a robotic arm, precision terrain models, and adjustable lighting to simulate lunar landing trajectories and asteroid approach scenarios.

## Runtime Verification

- [Copilot](https://github.com/Copilot-Language/copilot) - NASA's runtime verification framework that generates constant-time, constant-memory C99 monitors from high-level Haskell specifications. It integrates with cFS, F Prime, and ROS 2 for monitoring safety properties of hard real-time aerospace systems.
  - [OGMA](https://github.com/nasa/ogma) - NASA tool for generating safe runtime monitors for flight and robotic applications. It extends Copilot to produce hard real-time C99 verification code, supporting runtime monitoring for cFS, ROS 2, and F' spacecraft software.
