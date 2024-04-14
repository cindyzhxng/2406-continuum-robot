"""
Module for defining pin mappings and speed settings for the stepper motors and drivers.

This module provides mappings for GPIO pins corresponding to different stepper motors,
stepper motor drivers, and limit switches. It also defines speed settings for manual
movements of the motors.

"""

# Pin mappings for stepper motors
TRA_1 = 0  # Translate stage 1
ROT_1 = 1  # Rotate stage 1
TRA_2 = 2  # Translate stage 2
ROT_2 = 3  # Rotate stage 2
TRA_3 = 4  # Translate stage 3
ROT_3 = 5  # Rotate stage 3

# Pin mappings for stepper motor driver 2
PUL_2 = 2
DIR_2 = 3
ENA_2 = 4

# Pin mappings for stepper motor driver 4
PUL_4 = 17
DIR_4 = 27
ENA_4 = 22

# Pin mappings for stepper motor driver 3
PUL_3 = 10
DIR_3 = 9
ENA_3 = 11

# Pin mappings for stepper motor driver 5
PUL_5 = 5
DIR_5 = 6
ENA_5 = 13

# Pin mappings for stepper motor driver 1
PUL_1 = 14
DIR_1 = 15
ENA_1 = 18

# Pin mappings for stepper motor driver 6
PUL_6 = 25
DIR_6 = 8
ENA_6 = 7

# Limit switches GPIO pins
LIMIT_SWITCH_3 = 21  # Stage 3 limit switch
LIMIT_SWITCH_2 = 20  # Stage 2 limit switch
LIMIT_SWITCH_1 = 16  # Stage 1 limit switch

# Speed settings
DEFAULT_FREQ = 200  # Default frequency (Hz)
MANUAL_TRANS_FREQ = 20 * DEFAULT_FREQ  # Manual translation frequency
MANUAL_ROT_FREQ = 20 * DEFAULT_FREQ  # Manual rotation frequency

NUM_MANUAL_STEP = 10  # Number of steps for manual movement
# GPIO pins still available to use
# GPIO: 19, 26, 23, 24, 12, 0
