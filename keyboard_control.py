"""
Main script for controlling the stepper motors of the robot via keyboard inputs.

This script reads keyboard inputs and translates them into corresponding
movements of the stepper motors. It imports functions from the stepper_motor_controls
module to perform the motor movements.

The keyboard inputs are mapped to specific movements of the stepper motors, such as
translation and rotation, for different stages of the robot.

"""

import sys
import termios
import tty
from stepper_motor_controls import *

filedescriptors = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)


def keyboard_to_movement(move):
    """
    Function to convert keyboard inputs to motor movements.

    Args:
        move (str): The keyboard input representing the desired movement.

    Returns:
        None
    """
    match move:
        case "a":
            print("1: we translate first stage")
            # translate_steps(0.023562)
            step_pin(TRA_1, NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
        case "d":
            print("1: move back")
            step_pin(TRA_1, -NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
        case "w":
            print("1: we rotate ccw")
            step_pin(ROT_1, NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
        case "s":
            print("1: rotate cw")
            step_pin(ROT_1, -NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
        case "f":
            print("2: move forward")
            step_pin(TRA_2, NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
        case "h":
            print("2: move back")
            step_pin(TRA_2, -NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
        case "t":
            print("2: rotate ccw")
            step_pin(ROT_2, NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
        case "g":
            print("2: rotate cw")
            step_pin(ROT_2, -NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
        case "j":
            print("3: move forward")
            step_pin(TRA_3, NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
        case "l":
            print("3: move back")
            step_pin(TRA_3, -NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
        case "i":
            print("3: rotate ccw")
            step_pin(ROT_3, NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
        case "k":
            print("3: rotate cw")
            step_pin(ROT_3, -NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
        case ";":
            print("All forward")
            step_pin(TRA_3, NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
            step_pin(TRA_2, NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
            step_pin(TRA_1, NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
        case "\\":
            print("All back")
            step_pin(TRA_3, -NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
            step_pin(TRA_2, -NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
            step_pin(TRA_1, -NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
        case "[":
            print("All CCW")
            step_pin(ROT_3, NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
            step_pin(ROT_2, NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
            step_pin(ROT_1, NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
        case "'":
            print("All CW")
            step_pin(ROT_3, -NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
            step_pin(ROT_2, -NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
            step_pin(ROT_1, -NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
        case _:
            print("Input is not supported.")


try:
    while True:
        move = sys.stdin.read(1)[0]
        print("You pressed", move)
        keyboard_to_movement(move)
except KeyboardInterrupt:
    termios.tcsetattr(sys.stdin, termios.TCSANOW, original_settings)
