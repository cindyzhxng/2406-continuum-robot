# Continuum Robot Control System

## Overview

This repository contains the codebase for controlling a robot using Raspberry Pi GPIO pins. The system utilizes stepper motors for translation and rotation, along with limit switches for homing, and provides functionalities for manual movement and homing of the robot.

## Features

- **Stepper Motor Control**: Precise control over the translation and rotation of the robot's stages using stepper motors.
- **Limit Switch Homing**: Automatic homing of the robot's translation stages using limit switches for accurate positioning.
- **Manual Movement**: Ability to manually move the robot's stages with customizable step sizes and frequencies.
- **GPIO Pin Mapping**: Clear mapping of GPIO pins for each stepper motor, motor driver, and limit switch for easy configuration.

## Prerequisites

- Raspberry Pi with GPIO support
- Python 3.x
- RPi.GPIO library
- Numpy library
  
## Configuration
Configure GPIO pin mappings and speed settings in system_config.py according to your hardware setup and requirements.

## Installation

1. Clone this repository to your Raspberry Pi:

```bash
git clone https://github.com/cindyzhxng/2406-continuum-robot.git
Follow the on-screen instructions to perform translations, rotations, homing, and manual movements of the robot.
