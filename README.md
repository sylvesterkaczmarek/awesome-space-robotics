# Awesome Space Robotics [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Robotic systems designed for space environments.

<p>
<a href="https://AndrejOrsula.github.io/awesome-space-robotics"> <img alt="HTML" src="theme/icon_html.svg" width="96" height="96"></a>
<a href="https://AndrejOrsula.github.io/awesome-space-robotics/awesome-space-robotics.pdf"> <img alt="PDF" src="theme/icon_pdf.svg" width="96" height="96"></a>
<a href="#contents"> <img alt="MD" src="theme/icon_md.svg" width="96" height="96"></a>
</p>

---

## Contents

- [Systems](#systems)
  - [Hardware Platforms](#hardware-platforms)
  - [Software Frameworks](#software-frameworks)
  - [Simulation Environments](#simulation-environments)
  - [Verification & Validation](#verification--validation)
- [Algorithms](#algorithms)
  - [Perception](#perception)
  - [Navigation](#navigation)
  - [Manipulation](#manipulation)
  - [Human-Robot Interaction](#human-robot-interaction)
  - [Robot Learning](#robot-learning)
- [Missions & Applications](#missions--applications)
  - [Space Exploration](#space-exploration)
  - [Assembly & Servicing](#assembly--servicing)
- [Resources](#resources)
  - [Education](#education)
  - [Demos](#demos)
  - [Datasets](#datasets)
  - [Competitions](#competitions)
- [Community](#community)
  - [Organizations](#organizations)
  - [Recurring Events](#recurring-events)

## Systems

### Hardware Platforms

#### Surface Vehicles

- [CADRE](https://www.jpl.nasa.gov/missions/cadre) - Cooperative Autonomous Distributed Robotic Exploration, a NASA JPL project deploying a team of shoebox-sized rovers to the Moon. They will autonomously coordinate to map the lunar surface using multi-robot exploration strategies without human intervention.
- [Curiosity](#mars) - NASA's car-sized Mars rover powered by a radioisotope thermoelectric generator. It uses a rocker-bogie suspension, a 2.1-metre robotic arm with a drill and spectrometers, and autonomous navigation to traverse Gale Crater since 2012.
- [ExoMy](https://esa-prl.github.io/ExoMy) - Open source build-it-yourself rover developed by ESA. It is inspired by the ExoMars rover and designed to be a low-cost platform for educational purposes. ExoMy features Ackermann steering and can be controlled via ROS using an onboard Raspberry Pi.
- [JPL Open Source Rover](https://jplopensourcerover.com) - Open source build-it-yourself rover developed by JPL. It is based on the deployed Mars rovers and designed to be an affordable platform for education and research. The rover can be controlled via ROS using an onboard Raspberry Pi.
- [LEMUR](https://www.jpl.nasa.gov/robotics-at-jpl/freeclimber-lemur-3) - Limbed Excursion Mechanical Utility Robot developed by JPL. A four-limbed climbing robot with hundreds of micro-spine grippers that can scale rock walls and inspect spacecraft exteriors in microgravity.
- [Mars Exploration Rovers (Spirit & Opportunity)](#mars) - NASA's twin solar-powered rovers with rocker-bogie suspension and a five-degree-of-freedom instrument arm. Designed for 90 sols, Spirit operated until 2010 and Opportunity until 2018, validating long-duration autonomous rover operations on Mars.
- [MASCOT](#small-bodies) - Mobile Asteroid Surface Scout developed by DLR and CNES. The shoebox-sized lander was deployed from JAXA's Hayabusa2 spacecraft to the asteroid Ryugu in 2018, where it hopped across the surface to perform in situ measurements.
- [Perseverance](#mars) - NASA's Mars rover that landed in Jezero Crater in 2021. It carries seven science instruments, a robotic arm with a drill for coring rock samples, and deployed the Ingenuity helicopter for the first powered flight on another planet.
- [RASSOR](https://technology.nasa.gov/patent/KSC-TOPS-7) - Regolith Advanced Surface Systems Operations Robot developed by NASA Kennedy Space Center. A compact excavation robot designed to mine regolith on the Moon and Mars using counter-rotating bucket drums.
- [RoboSimian](https://www-robotics.jpl.nasa.gov/how-we-do-it/systems/robosimian) - Four-limbed robot developed by JPL with seven degrees of freedom per limb. Originally built for the DARPA Robotics Challenge, it now serves as a wheel-on-limb rover research platform for planetary exploration, with mobility tested on ocean-world analogue terrain.
- [Sojourner](#mars) - NASA's first Mars rover, a 10.6 kg six-wheeled microrobot that landed in 1997 as part of the Mars Pathfinder mission. It demonstrated semi-autonomous navigation with hazard avoidance and conducted soil and rock analyses using an alpha proton X-ray spectrometer over 83 sols.

#### Aerial Vehicles

- [Dragonfly](#space-exploration) - NASA dual-quadcopter rotorcraft designed to fly on Saturn's moon Titan. Leveraging Titan's dense atmosphere and low gravity, the 450 kg lander will hop between multiple sites to study prebiotic chemistry using a mass spectrometer, gamma-ray spectrometer, and drill.
- [Ingenuity](#mars) - NASA's 1.8 kg coaxial-rotor helicopter that achieved the first powered, controlled flight on another planet. Solar-powered with autonomous flight capability, it completed 72 flights over nearly three years on Mars, serving as a technology demonstrator and aerial scout for the Perseverance rover.

#### Free-Flying Robots

- [Astrobee](https://nasa.gov/astrobee) - Free-flying robotic system developed by NASA to assist astronauts inside the ISS. Three Astrobees were launched to the ISS in 2019, each equipped with cameras, sensors, and a perching arm. The software stack is open source and built using ROS and Gazebo.
- [Int-Ball2](https://doi.org/10.1109/MRA.2024.3505776) - Second-generation free-flying camera robot developed by JAXA for the ISS Kibo module. Building on the original Int-Ball deployed in 2017, it features improved autonomous navigation and positioning, enabling ground controllers to remotely capture images and video of crew activities and experiments without astronaut assistance.

#### Robotic Manipulators

- [Canadarm2](https://www.asc-csa.gc.ca/eng/iss/canadarm2/about.asp) - Robotic arm on the ISS built by MDA for the Canadian Space Agency. The 17-metre arm is used for station maintenance, moving supplies, and supporting spacewalks. It can move end-over-end to reach many parts of the ISS.
- [Canadarm3](https://www.asc-csa.gc.ca/eng/canadarm3/about.asp) - Next-generation robotic system being developed by MDA for the Lunar Gateway. It consists of a large and a small dexterous arm with AI-based autonomy, designed to maintain and repair the Gateway station with minimal crew intervention.
- [Dextre](https://www.asc-csa.gc.ca/eng/iss/dextre/about.asp) - Two-armed dexterous manipulator on the ISS that serves as a robotic handyman for delicate maintenance tasks. Built by MDA for the Canadian Space Agency, Dextre is mounted on Canadarm2 and can handle orbital replaceable units.
- [ERA](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/International_Space_Station/European_Robotic_Arm) - European Robotic Arm installed on the Russian segment of the ISS. The 11.3-metre arm can move from one base point to another around the station's exterior for maintenance and payload handling tasks.
- [GITAI Inchworm Robot](https://gitai.tech/inchworm-robot) - Robotic arm developed by GITAI for in-orbit and lunar surface operations. It uses an inchworm locomotion concept to move along spacecraft structures and perform assembly, inspection, and maintenance tasks.
- [JEM-RMS](https://iss.jaxa.jp/en/kibo/about/kibo/rms) - Japanese Experiment Module Remote Manipulator System on the ISS Kibo module. It consists of a main arm and a small fine arm for handling experiments and payloads on the external platform.

#### Humanoids

- [Robonaut 2 (R2)](https://nasa.gov/robonaut2) - Humanoid robot developed by NASA to assist astronauts onboard the ISS. R2 was launched in 2011 as the first humanoid robot in space and has since been used in various experiments on simple manipulation tasks.
- [Rollin' Justin](https://www.dlr.de/en/rm/research/robotic-systems/humanoids/rollin-justin) - Mobile humanoid robot developed by DLR with two torque-controlled arms and dexterous hands mounted on a wheeled platform. It serves as a testbed for autonomous and teleoperated space robotics research, including Earth-to-space teleoperation experiments.
- [Valkyrie (R5)](https://www.nasa.gov/technology/r5) - NASA's bipedal humanoid robot designed for disaster response and space exploration. Standing 1.8 m tall, Valkyrie is used as a research platform for developing dexterous manipulation and locomotion capabilities for future planetary surface operations.

### Software Frameworks

#### Robotics Middleware

- [Robot Operating System (ROS)](https://www.ros.org) - Open source middleware framework widely used in space robotics for development and ground testing. NASA's Astrobee free-flyers run on ROS, and platforms like ExoMy and the JPL Open Source Rover use ROS for control and navigation.
  - [Space ROS](https://space.ros.org) - Fork of ROS 2 that aims to align with the safety and reliability requirements of space missions.

#### Flight Software

- [core Flight System (cFS)](https://cfs.gsfc.nasa.gov) - NASA's platform-independent and mission-independent flight software framework. It provides a reusable software architecture for spacecraft with a layered design that separates the operating system, platform, and application layers.
- [F´ (F-Prime)](https://fprime.jpl.nasa.gov) - Component-driven framework for spaceflight applications and embedded systems with limited resources. It has been successfully deployed on several space missions, including Mars Helicopter Ingenuity.

#### Ground Systems

- [Yamcs](https://yamcs.org) - Open source mission control framework for command and control of spacecraft, satellites, payloads, and ground equipment. It features built-in support for CCSDS, CFDP, and XTCE standards, and can serve as a backend for OpenMCT.

#### Mission Planning

- [GMAT](https://gmat.atlassian.net/wiki/spaces/GW/overview) - General Mission Analysis Tool, NASA's open source space mission design tool for trajectory optimization and mission planning. It supports analysis from low-Earth orbit to interplanetary trajectories.
- [SPICE Toolkit](https://naif.jpl.nasa.gov/naif/toolkit.html) - NASA's observation geometry system used for space science mission planning and data analysis. It provides ephemerides, reference frames, instrument pointing, and other ancillary data required for computing observation geometry.

### Simulation Environments

#### General Purpose

- [Gazebo](https://gazebosim.org) - Open source robotics simulator that provides accurate physics simulation, sensor models, and 3D visualization. It is widely used with ROS for developing and testing robotic systems. NASA's Astrobee software stack uses Gazebo for simulation.
- [Isaac Sim](https://developer.nvidia.com/isaac-sim) - NVIDIA's robotics simulation platform built on Omniverse. It provides photorealistic rendering, accurate physics via PhysX, and domain randomization capabilities for sim-to-real transfer of robotic systems.
- [Project Chrono](https://projectchrono.org) - Open source multi-physics simulation engine handling rigid and flexible body dynamics, collision detection, and vehicle-terrain interaction. It provides granular material and deformable terrain simulation relevant to planetary rover mobility studies.

#### Space Robotics

- [DARTS](https://www-robotics.jpl.nasa.gov/how-we-do-it/facilities/the-darts-simulation-laboratory) - Dynamics Algorithms for Real-Time Simulation developed by JPL. It provides high-fidelity multibody dynamics simulation for space robotic systems, including articulated mechanisms, contact dynamics, and flexible structures.
- [Space Robotics Bench (SRB)](https://andrejorsula.github.io/space_robotics_bench) (*Disclaimer: Author's project*) - Collection of environments and tasks for space robotics research built on NVIDIA Isaac Sim. It provides highly parallelized simulation with procedural environment generation and extensive domain randomization for developing and validating autonomous space systems.
- [Space ROS Demos](https://github.com/space-ros/demos) - Collection of Space ROS simulation examples featuring Canadarm2, Curiosity rover, and lunar terrain environments. Built on Gazebo, the demos are containerized with Docker for easy deployment and serve as reference implementations for space robotics development with Space ROS.

#### Scene Generation

- [PANGU](https://pangu.software) - Planet and Asteroid Natural Scene Generation Utility developed by the University of Dundee for ESA. It generates synthetic images of planetary surfaces for testing and validating vision-based navigation algorithms for landing and surface exploration.

#### Spacecraft Dynamics

- [42](https://github.com/ericstoneking/42) - NASA Goddard's general-purpose spacecraft simulation environment. It provides high-fidelity attitude and orbit dynamics, sensor and actuator models, and visualization for multi-body spacecraft systems.
- [Basilisk](https://avslab.github.io/basilisk) - Astrodynamics simulation framework developed at the University of Colorado Boulder. It supports modular spacecraft simulation with customizable flight software, dynamics, and environment models for autonomous mission scenarios.

#### Simulation Frameworks

- [Trick](https://github.com/nasa/trick) - NASA's simulation development framework that provides common simulation capabilities for rapid prototyping of space vehicle simulations. It handles infrastructure such as job scheduling, data recording, and checkpoint/restart, enabling engineers to focus on domain-specific models.

### Verification & Validation

#### Terrestrial Analogue Sites

- [Atacama Desert](https://en.wikipedia.org/wiki/Atacama_Desert) | Chile - One of the driest places on Earth, used as a Mars analogue for testing rover autonomy and astrobiology experiments due to its extreme aridity, UV radiation, and mineral composition similar to Mars.
- [Devon Island](https://en.wikipedia.org/wiki/Devon_Island) | Canada - The largest uninhabited island on Earth, hosting the Haughton-Mars Project. The Haughton impact crater provides Mars-like terrain used for testing rover operations and space suits.
- [Iceland](https://en.wikipedia.org/wiki/Iceland) - Volcanic island used extensively by NASA and ESA as a planetary analogue. Its glacial landscapes, lava fields, and volcanic terrain simulate lunar and Martian conditions for testing rover operations and sample collection techniques.
- [Lanzarote](https://en.wikipedia.org/wiki/Lanzarote) | Spain - Volcanic island in the Canary Islands used by ESA as an analogue site for lunar and planetary exploration testing. Its volcanic landscapes include lava tubes and basaltic terrain similar to lunar geology.
- [Mount Etna](https://en.wikipedia.org/wiki/Mount_Etna) | Italy - Active volcano with fresh volcanic soils and lava flows, serving as an excellent analogue for the Moon and Mars. ESA and DLR have tested several rovers and robotic operations at this site.

#### Laboratory Facilities

- [ESA Orbital Robotics Laboratory](https://www.esa.int/Education/ESA_Academy_Experiments_programme/Orbital_Robotics_Laboratory) | Netherlands - Testbed at ESA's ESTEC featuring Europe's largest 2D free-floating platform, a 4.8x9 m flat floor with air-bearing systems that simulate microgravity for validating satellite docking, debris removal, and in-orbit servicing technologies. It is available to university students through the ESA Academy Experiments Programme.
- [JPL Mars Yard](https://www-robotics.jpl.nasa.gov/how-we-do-it/facilities/marsyard-iii) | USA - Outdoor test facility at JPL designed to emulate the Martian surface. It is used for testing rover mobility, navigation, and instrument deployment on terrain representative of Mars conditions.
- [LUNA](https://luna-analog-facility.de/en) | Germany - ESA-DLR LUNA analogue facility at the European Astronaut Centre in Cologne. It features a large regolith testbed for testing lunar surface operations, including rover navigation and sample collection.
- [LunaLab](https://www.uni.lu/snt-en/facilities/lunalab) | Luxembourg - Moon analogue facility at the University of Luxembourg. It features an indoor 11x7 m area filled with 20 t of basalt gravel to emulate the surface of the Moon. LunaLab is equipped with adjustable illumination and a motion capture system to support the development and testing of lunar rovers.
- [Spaceport Rostock](https://testingfor.space) | Germany - Testing facility at Rostock-Laage Airport developed in collaboration with DLR. It features a test track for lunar and space vehicles and plans for microgravity testing infrastructure, positioning it as a hub for commercial and national space research.
- [TRON](https://www.dlr.de/en/research-and-transfer/research-infrastructure/testbed-for-robotic-optical-navigation-tron) | Germany - Testbed for Robotic Optical Navigation at the DLR Institute of Space Systems in Bremen. A hardware-in-the-loop facility for validating optical navigation sensors including cameras and lidar up to TRL 7. It uses a robotic arm, precision terrain models, and adjustable lighting to simulate lunar landing trajectories and asteroid approach scenarios.
- [Zero-G Lab](https://www.uni.lu/snt-en/facilities/zero-g-lab) | Luxembourg - Facility at the University of Luxembourg designed for testing 2D and 3D free-floating robotic systems in microgravity conditions. Its dark room features a 5x3 m flat epoxy floor on which pneumatic platforms use pressurized air to emulate free-floating behaviour in a 2D plane, while wall- and ceiling-mounted articulated robotic arms on linear rails extend the workspace into 3D. The lab is equipped with adjustable illumination and a motion capture system.

#### Runtime Verification

- [Copilot](https://github.com/Copilot-Language/copilot) - NASA's runtime verification framework that generates constant-time, constant-memory C99 monitors from high-level Haskell specifications. It integrates with cFS, F Prime, and ROS 2 for monitoring safety properties of hard real-time aerospace systems.
  - [OGMA](https://github.com/nasa/ogma) - NASA tool for generating safe runtime monitors for flight and robotic applications. It extends Copilot to produce hard real-time C99 verification code, supporting runtime monitoring for cFS, ROS 2, and F' spacecraft software.

## Algorithms

### Perception

#### Image Processing

- [VICAR](https://github.com/NASA-AMMOS/VICAR) - Video Image Communication And Retrieval, JPL's open source image processing system developed since 1966. It includes VISOR for operational rover image processing and has been used on all Mars surface missions including Spirit, Opportunity, Curiosity, Perseverance, Ingenuity, InSight, and Phoenix.

#### Terrain Analysis

- [Ames Stereo Pipeline (ASP)](https://github.com/NeoGeographyToolkit/StereoPipeline) - NASA's open source suite for generating digital terrain models, orthoimages, and 3D point clouds from satellite, rover, and aerial stereo imagery. It supports bundle adjustment, shape-from-shading, and multiple planetary sensor formats.

### Navigation

#### Planetary Navigation

- [Enhanced Autonomous Navigation (ENav)](https://doi.org/10.1109/TFR.2025.3636366) - Enhanced Navigation system used on NASA's Perseverance rover. It builds on AutoNav with improved processing speed and smarter path planning, allowing the rover to drive faster and more autonomously on Mars than any previous mission.
- [Terrain Relative Navigation (TRN)](https://www.nasa.gov/space-technology-mission-directorate/tdm/terrain-relative-navigation-trn) - NASA's Lander Vision System developed for Mars 2020. It uses a downward-facing camera during descent to match terrain features against onboard orbital maps, fusing landmarks with inertial measurements to estimate position within 60 metres. This enabled Perseverance to autonomously divert to a safe landing site within the hazardous Jezero Crater.

#### Orbital Navigation

- [dSGP4](https://github.com/esa/dSGP4) - ESA's differentiable SGP4 orbital propagation library reimplemented with PyTorch automatic differentiation support. It enables gradient-based orbit determination, covariance propagation, and hybrid ML-augmented propagation with GPU-accelerated batch TLE processing.
- [Orekit](https://www.orekit.org) - Open source low-level space dynamics library written in Java. It provides tools for orbit propagation, coordinate transformations, and attitude computation used in spacecraft navigation and mission analysis.

### Manipulation

#### Motion Planning

- [MoveIt](https://moveit.ros.org) - Open source general-purpose motion planning framework built on top of ROS. MoveIt combines kinematic solvers, collision checking, path planning, trajectory optimization, perception, and control in a unified framework for robotic manipulation.
- [OMPL](https://ompl.kavrakilab.org) - Open Motion Planning Library, a collection of sampling-based motion planning algorithms. It provides implementations of PRM, RRT, and many variants used for planning robot arm motions in complex environments.

#### Dynamics & Control

- [Drake](https://drake.mit.edu) - Model-based design and verification toolbox for robotics developed at MIT and now maintained by Toyota Research Institute. It provides multibody dynamics, mathematical optimization, and control algorithms for planning and control of robotic systems.
- [Pinocchio](https://github.com/stack-of-tasks/pinocchio) - Fast and flexible C++ library for rigid body dynamics algorithms. It provides efficient implementations of forward/inverse kinematics, dynamics, and their analytical derivatives for articulated robotic systems.

### Human-Robot Interaction

#### Teleoperation

- [METERON](https://www.esa.int/Enabling_Support/Space_Engineering_Technology/Automation_and_Robotics/METERON_Project) - Multi-purpose End-To-End Robotic Operation Network, an ESA project for teleoperation of robots on Earth from the ISS. It validates time-delayed telerobotic control techniques across the space-to-ground communication link.

#### User Interfaces

- [OpenMCT](https://nasa.github.io/openmct) - Open source mission control framework developed by NASA Ames. It provides a web-based platform for visualizing telemetry data and commanding spacecraft and robotic systems.

### Robot Learning

#### Simulation-Based Learning

- [Space Robotics Bench (SRB)](#space-robotics) (*Disclaimer: Author's project*) - Suite of GPU-accelerated environments for space robotics reinforcement learning built on NVIDIA Isaac Lab. It provides parallelized training scenarios with procedural generation and domain randomization for learning autonomous orbital and planetary surface tasks.

## Missions & Applications

### Space Exploration

#### Lunar

- [Astrobotic Peregrine](https://www.astrobotic.com/lunar-delivery/landers/peregrine-lander) - First mission under NASA's Commercial Lunar Payload Services program, launched in January 2024. The lander carried multiple science payloads bound for the Moon but experienced a propellant leak that prevented lunar landing.
- [Blue Ghost](https://fireflyspace.com/blue-ghost) - Firefly Aerospace's lunar lander selected under NASA's CLPS program. It carries 10 science and technology payloads to Mare Crisium to study the lunar regolith, magnetic fields, and geophysical properties.
- [Chandrayaan-3](https://www.isro.gov.in/Chandrayaan3.html) - ISRO's lunar mission that successfully soft-landed the Vikram lander and Pragyan rover near the lunar south pole in 2023. Pragyan is a six-wheeled rover that conducted in situ chemical analysis of the lunar surface.
- [Chang'e Program](https://en.wikipedia.org/wiki/Chinese_Lunar_Exploration_Program) - China's lunar exploration program operated by CNSA. Chang'e 4 achieved the first soft landing on the far side of the Moon in 2019 with the Yutu-2 rover; Chang'e 5 returned samples in 2020; and Chang'e 6 returned the first far-side samples in 2024.
- [Lunokhod Program](https://en.wikipedia.org/wiki/Lunokhod_programme) - Soviet robotic lunar rover program that deployed the first remote-controlled rovers on another world. Lunokhod 1 (1970) and Lunokhod 2 (1973) traversed the lunar surface collecting soil data and imagery, pioneering planetary surface robotics.
- [LUPEX](https://global.jaxa.jp/activity/pr/jaxas/no092/02.html) - Lunar Polar Exploration mission jointly developed by JAXA and ISRO. It aims to explore the lunar south pole with a rover equipped with a drill and instruments to investigate the presence and distribution of water ice.
- [Nova-C (Odysseus)](https://www.intuitivemachines.com/im-1) - Intuitive Machines' IM-1 lunar lander that became the first commercial spacecraft to soft-land on the Moon in February 2024. It landed near the Malapert A crater at the lunar south pole, carrying six NASA payloads.
- [SLIM](https://global.jaxa.jp/projects/sas/slim) - Smart Lander for Investigating Moon, JAXA's precision lunar landing demonstrator that touched down in January 2024. It achieved pinpoint landing accuracy within 55 metres of its target using image-matching navigation, and deployed the LEV-1 and LEV-2 small rovers for surface exploration.
- [VIPER](https://science.nasa.gov/mission/viper) - Volatiles Investigating Polar Exploration Rover, a NASA lunar rover designed to map water ice deposits at the Moon's south pole.

#### Mars

- [ExoMars](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Exploration/ExoMars) - ESA's mission to search for signs of past life on Mars. Its Rosalind Franklin rover is designed to drill up to 2 metres below the Martian surface and carry analytical instruments to study subsurface samples for biosignatures. It is planned for launch in 2028.
- [Mars 2020](https://mars.nasa.gov/mars2020) - NASA mission that landed the Perseverance rover and Ingenuity helicopter in Jezero Crater in 2021. Perseverance carries seven science instruments and a robotic arm with a drill for coring rock samples, while Ingenuity demonstrated the first powered, controlled flight on another planet, completing 72 flights over nearly three years.
- [Mars Exploration Rovers](https://science.nasa.gov/mission/mars-exploration-rovers-spirit-and-opportunity) - NASA's twin-rover mission that landed Spirit and Opportunity on Mars in 2004 to search for evidence of past water activity. Spirit operated until 2010 and Opportunity until 2018, far exceeding their 90-day design life and fundamentally advancing Mars geology.
- [Mars Pathfinder](https://science.nasa.gov/mission/mars-pathfinder) - NASA's first rover mission to Mars, which landed in 1997. Its Sojourner rover, a 10.6 kg microrobot, demonstrated the feasibility of low-cost rover operations on Mars and conducted soil and rock analyses over 83 sols.
- [Mars Science Laboratory](https://mars.nasa.gov/msl) - NASA mission that landed the Curiosity rover in Gale Crater in 2012. Curiosity carries a suite of instruments including a laser spectrometer and a drill, and has been characterizing Mars' climate, geology, and habitability potential.
- [Tianwen-1](https://en.wikipedia.org/wiki/Tianwen-1) - China's first Mars mission, which landed the Zhurong rover in Utopia Planitia in 2021. The solar-powered rover conducted geological surveys and subsurface radar exploration of the Martian surface.

#### Saturn

- [Dragonfly](https://dragonfly.jhuapl.edu) - NASA rotorcraft lander planned for Saturn's moon Titan. The dual-quadcopter will fly between multiple landing sites to study Titan's prebiotic chemistry and habitability, leveraging Titan's dense atmosphere and low gravity.

#### Small Bodies

- [Hayabusa2](https://www.hayabusa2.jaxa.jp/en) - JAXA's asteroid sample-return mission to Ryugu. It deployed multiple small rovers (MINERVA-II) and the MASCOT lander, collected subsurface samples via a kinetic impactor, and returned them to Earth in 2020.
- [MMX](https://www.mmx.jaxa.jp/en) - Martian Moons eXploration, JAXA's mission to return samples from Mars's moon Phobos. It will deploy the IDEFIX rover to survey the surface and collect samples, marking the first sample return from the Martian system.
- [OSIRIS-REx](https://science.nasa.gov/mission/osiris-rex) - NASA's asteroid sample-return mission to Bennu. It used a Touch-And-Go Sample Acquisition Mechanism to collect surface material and returned the sample to Earth in 2023, the largest asteroid sample ever collected.
- [Rosetta](https://www.esa.int/Science_Exploration/Space_Science/Rosetta) - ESA's Rosetta spacecraft orbited comet 67P/Churyumov-Gerasimenko and deployed the Philae lander in November 2014, achieving the first-ever landing on a comet. Philae collected surface data despite landing in a shadowed area.
- [Tianwen-2](https://en.wikipedia.org/wiki/Tianwen-2) - CNSA mission launched in 2025 to collect samples from near-Earth asteroid Kamoʻoalewa and return them to Earth. It combines asteroid sample collection with a subsequent flyby of a main-belt comet.

### Assembly & Servicing

#### On-Orbit Servicing

- [ADRAS-J](https://astroscale.com/missions/adras-j) - Active Debris Removal by Astroscale-Japan, a JAXA-contracted mission launched in 2024. It demonstrated rendezvous and proximity operations with a spent rocket upper stage, capturing close-range imagery for planning future debris removal.
- [ClearSpace-1](https://clearspace.today/missions/clearspace-1) - ESA-commissioned mission to remove a piece of space debris from orbit, planned as the first active debris removal mission. A capture spacecraft will use robotic arms to grasp a derelict Vespa upper stage and deorbit it.
- [Mission Extension Vehicle (MEV)](https://www.northropgrumman.com/space/space-logistics-services) - Northrop Grumman's satellite life-extension spacecraft. MEV-1 docked with Intelsat 901 in 2020, providing propulsion and attitude control to extend the aging satellite's operational lifetime.
- [Mission Robotic Vehicle (MRV)](#on-orbit-servicing) - Northrop Grumman's next-generation servicing spacecraft designed to perform hands-on satellite maintenance in GEO. Unlike MEV's whole-vehicle docking approach, MRV uses robotic arms to inspect, refuel, relocate, and repair client satellites.
- [RSGS](https://www.darpa.mil/program/robotic-servicing-of-geosynchronous-satellites) - Robotic Servicing of Geosynchronous Satellites, a DARPA program to develop a robotic servicing vehicle for GEO satellites. It utilizes dexterous robotic arms to inspect, reposition, and repair satellites.

## Resources

### Education

#### Study Programmes

- [Erasmus Mundus — SpaceMaster](https://spacemaster.eu) - Joint European master's degree in space science and technology offered by a consortium of European universities. It provides a multidisciplinary education including spacecraft systems, remote sensing, and space robotics.
- [University of Luxembourg — Master in Space Technologies and Business](https://www.uni.lu/fstm-en/study-programs/master-in-space-technologies-and-business) - A two-year program that combines technical and business aspects of the space industry with the opportunity to focus on space robotics. The curriculum also includes space systems engineering, informatics, entrepreneurship, and management.

### Demos

#### Web

- [Eyes on the Solar System](https://eyes.nasa.gov/apps/solar-system) - NASA's real-time 3D visualization of the solar system. It allows interactive exploration of spacecraft trajectories, planetary positions, and mission events using real mission data.
- [JPL Open Source Rover (Homepage)](#surface-vehicles) - Simulated Mars rover that can be controlled through a simple teleoperation interface.
- [KeepTrack](https://app.keeptrack.space) - Open source web application for visualizing satellites and space debris in real time. It categorizes objects by type and provides detailed orbital information, useful for understanding the space environment around robotic missions.
- [LeoLabs Visualization](https://platform.leolabs.space/visualization) - Interactive 3D visualization of tracked objects in low Earth orbit. It provides real-time situational awareness of the space debris environment and conjunction events for orbital operations planning.
- [Mars Trek](https://trek.nasa.gov/mars) - NASA's web-based portal for exploring the surface of Mars using data from multiple missions. It provides interactive maps, elevation profiles, and 3D terrain visualization.
- [Moon Trek](https://trek.nasa.gov/moon) - NASA's web-based portal for interactive exploration of the lunar surface. It offers access to imagery, topography data, and analysis tools from past and current lunar missions.

### Datasets

#### Assets

- [ESA Planetary Science Archive (PSA)](https://psa.esa.int/psa/#/pages/home) - ESA's central repository for data from all planetary science missions. It provides calibrated data products from missions including Rosetta, Mars Express, and BepiColombo.
- [NASA-3D-Resources](https://github.com/nasa/NASA-3D-Resources) - Collection of copyright-free 3D models, textures, and images from NASA. It includes models of spacecraft, planets, rovers, and other assets suitable for visualization and simulation.

#### Imagery & Terrain

- [HiRISE](https://www.uahirise.org) - High Resolution Imaging Science Experiment aboard NASA's Mars Reconnaissance Orbiter. It provides the most detailed images of the Martian surface at resolutions up to 25 cm/pixel, used for landing site selection and terrain analysis.
- [Lunar Reconnaissance Orbiter Camera (LROC)](https://www.lroc.asu.edu) - Camera system aboard NASA's LRO that has imaged the lunar surface at resolutions up to 50 cm/pixel. The data is used for mapping, landing site selection, and generating terrain models for rover simulations.
- [Planetary Data System (PDS)](https://pds.nasa.gov) - NASA's archive of data from planetary missions. It provides standardized, peer-reviewed datasets including imagery, spectral data, and topographic maps from missions across the solar system.

#### Spacecraft Pose & Proximity

- [SPARK](https://cvi2.uni.lu/spark-spades) - SPAcecraft Recognition leveraging Knowledge dataset from the University of Luxembourg. It provides synthetic and real images of spacecraft with multiple annotation types for training spacecraft detection and pose estimation models.
- [SPEED+](https://zenodo.org/records/6327547) - Spacecraft Pose Estimation Dataset, providing synthetic and real images of satellites with ground truth 6-DOF pose labels. It is used for benchmarking spacecraft pose estimation algorithms for proximity operations.

### Competitions

#### Robotic Challenges

- [ESA ESRIC Space Resources Challenge](https://src.esa.int) - ESA challenge focused on developing robotic technologies for lunar resource prospecting and in-situ resource utilization.
- [European Rover Challenge (ERC)](https://roverchallenge.eu) - Annual competition in planetary exploration where student teams design and test rovers. The event features tasks such as navigation, sample collection, and maintenance.
- [University Rover Challenge (URC)](https://urc.marssociety.org) - Mars Society's annual competition held in the Utah desert. University teams design and build Mars rover prototypes to complete science, delivery, equipment servicing, and autonomous navigation tasks.

## Community

### Organizations

#### Governmental

- [ASI](https://www.asi.it/en) | Italy - Italian Space Agency
- [CNES](https://cnes.fr/en) | France - Centre National d'Études Spatiales
- [CNSA](https://www.cnsa.gov.cn) | China - China National Space Administration
- [CSA](https://www.asc-csa.gc.ca/eng) | Canada - Canadian Space Agency
- [DLR](https://www.dlr.de/en/rm) | Germany - German Aerospace Center, Institute of Robotics and Mechatronics
- [ESA](https://www.esa.int) | Europe - European Space Agency
- [ISRO](https://www.isro.gov.in) | India - Indian Space Research Organisation
- [JAXA](https://global.jaxa.jp) | Japan - Japan Aerospace Exploration Agency
- [KASA](https://www.kasa.go.kr/eng/index.do) | South Korea - Korea AeroSpace Administration
- [NASA](https://www.nasa.gov) | USA - National Aeronautics and Space Administration
  - [ARC](https://www.nasa.gov/ames) | USA - NASA Ames Research Center
  - [GSFC](https://www.nasa.gov/goddard) | USA - NASA Goddard Space Flight Center
  - [JPL](https://www.jpl.nasa.gov) | USA - NASA Jet Propulsion Laboratory
  - [JSC](https://www.nasa.gov/johnson) | USA - NASA Johnson Space Center
- [UKSA](https://www.gov.uk/government/organisations/uk-space-agency) | United Kingdom - UK Space Agency

#### Academic

- [AAU Space Robotics](https://spacerobotics.es.aau.dk) | Denmark - Aalborg University
- [Space Robotics Group (SRG)](https://www.srg.mech.keio.ac.jp/en) | Japan - Keio University
- [Space Robotics Lab (SRL)](https://astro.mech.tohoku.ac.jp/e/index.html) | Japan - Tohoku University
- [Space Robotics Research Group (SpaceR)](https://www.spacer.lu) | Luxembourg - University of Luxembourg
- [The Laboratory for Autonomous Systems in Exploration and Robotics (LASER)](https://usclaser.github.io) | USA - University of Southern California

#### Corporate

- [Astrobotic](https://www.astrobotic.com) | USA - Lunar logistics and delivery services
- [Astroscale](https://astroscale.com) | Japan/UK - On-orbit servicing and debris removal
- [ClearSpace](https://clearspace.today) | Switzerland - Space debris removal and in-orbit servicing
- [GITAI](https://gitai.tech) | Japan/USA - Space robotics and labor automation
- [Honeybee Robotics (Blue Origin)](https://www.blueorigin.com/exploration-systems) | USA - Spacecraft mechanisms and planetary drilling systems, now a subsidiary of Blue Origin
- [Intuitive Machines](https://www.intuitivemachines.com) | USA - Lunar landers and space infrastructure
- [ispace](https://ispace-inc.com) | Japan - Lunar exploration and resource development
- [MDA](https://mda.space) | Canada - Canadarm, robotics, and satellite systems
- [Motiv Space Systems](https://motivss.com) | USA - Robotic arms and actuators for space
- [Northrop Grumman](https://www.northropgrumman.com/space) | USA - Satellite servicing and space logistics
- [Redwire Space](https://redwirespace.com) | USA - In-space manufacturing and robotics
- [Starfish Space](https://www.starfishspace.com) | USA - Satellite servicing and space sustainability

### Recurring Events

#### Conferences

- [ASTRA](https://www.esa.int/Enabling_Support/Space_Engineering_Technology/Automation_and_Robotics/Proceedings_of_ASTRA) - Advanced Space Technologies for Robotics and Automation, ESA's symposium on space robotics held biennially at ESTEC. It covers robotic systems, autonomy, and mechanisms for space exploration.
- [i-SAIRAS](https://www.esa.int/Enabling_Support/Space_Engineering_Technology/Automation_and_Robotics/i-SAIRAS) - International Symposium on Artificial Intelligence, Robotics and Automation in Space. A long-running conference series focusing on AI and robotics technologies for space missions, held approximately every two years.
- [IAC](https://www.iafastro.org/events/iac) - International Astronautical Congress, the world's largest annual gathering of space professionals. It includes dedicated sessions on space robotics and automation organized by the International Astronautical Federation.
- [ICRA](https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra) - IEEE International Conference on Robotics and Automation. The flagship IEEE robotics conference regularly features workshops and sessions on space robotics, orbital manipulation, and planetary exploration.
- [IROS](https://www.ieee-ras.org/conferences-workshops/financially-co-sponsored/iros) - IEEE/RSJ International Conference on Intelligent Robots and Systems. One of the largest robotics conferences, it regularly includes workshops and papers on space robotics applications.
- [iSpaRo](https://isparo.space) - International Conference on Space Robotics. Annual peer-reviewed conference aiming to provide a framework for academia and industry to engage in discussions and share their insights on emerging topics in space robotics.
- [SPAICE](https://spaice.esa.int) - ESA academic conference on AI in and for space. It focuses on the application of AI techniques to space missions, covering onboard autonomy, computer vision, and machine learning for robotic spacecraft.

---

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) before submitting a pull request.
