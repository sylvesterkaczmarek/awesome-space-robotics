# Simulation Environments

## General Purpose

- [Gazebo](https://gazebosim.org) - Open source robotics simulator that provides accurate physics simulation, sensor models, and 3D visualization. It is widely used with ROS for developing and testing robotic systems. NASA's Astrobee software stack uses Gazebo for simulation.
- [Isaac Sim](https://developer.nvidia.com/isaac-sim) - NVIDIA's robotics simulation platform built on Omniverse. It provides photorealistic rendering, accurate physics via PhysX, and domain randomization capabilities for sim-to-real transfer of robotic systems.
- [Project Chrono](https://projectchrono.org) - Open source multi-physics simulation engine handling rigid and flexible body dynamics, collision detection, and vehicle-terrain interaction. It provides granular material and deformable terrain simulation relevant to planetary rover mobility studies.

## Space Robotics

- [DARTS](https://www-robotics.jpl.nasa.gov/how-we-do-it/facilities/the-darts-simulation-laboratory) - Dynamics Algorithms for Real-Time Simulation developed by JPL. It provides high-fidelity multibody dynamics simulation for space robotic systems, including articulated mechanisms, contact dynamics, and flexible structures.
- [Space Robotics Bench (SRB)](https://andrejorsula.github.io/space_robotics_bench) - Collection of environments and tasks for space robotics research built on NVIDIA Isaac Sim. It provides highly parallelized simulation with procedural environment generation and extensive domain randomization for developing and validating autonomous space systems.
- [Space ROS Demos](https://github.com/space-ros/demos) - Collection of Space ROS simulation examples featuring Canadarm2, Curiosity rover, and lunar terrain environments. Built on Gazebo, the demos are containerized with Docker for easy deployment and serve as reference implementations for space robotics development with Space ROS.

## Scene Generation

- [PANGU](https://pangu.software) - Planet and Asteroid Natural Scene Generation Utility developed by the University of Dundee for ESA. It generates synthetic images of planetary surfaces for testing and validating vision-based navigation algorithms for landing and surface exploration.

## Spacecraft Dynamics

- [42](https://github.com/ericstoneking/42) - NASA Goddard's general-purpose spacecraft simulation environment. It provides high-fidelity attitude and orbit dynamics, sensor and actuator models, and visualization for multi-body spacecraft systems.
- [Basilisk](https://avslab.github.io/basilisk) - Astrodynamics simulation framework developed at the University of Colorado Boulder. It supports modular spacecraft simulation with customizable flight software, dynamics, and environment models for autonomous mission scenarios.

## Simulation Frameworks

- [Trick](https://github.com/nasa/trick) - NASA's simulation development framework that provides common simulation capabilities for rapid prototyping of space vehicle simulations. It handles infrastructure such as job scheduling, data recording, and checkpoint/restart, enabling engineers to focus on domain-specific models.
