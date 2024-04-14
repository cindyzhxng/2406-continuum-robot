"""
Sanity check script for controlling the stepper motors of the robot.

This script initializes the robot's home position and then enters a loop
until the user interrupts the code. It handles keyboard interrupts 
to ensure proper cleanup of GPIO resources.
"""

from stepper_motor_controls import *

if __name__ == "__main__":
    try:
        home_robot()

        while True:
            continue
    except KeyboardInterrupt:
        print("Ctrl+C detected. Cleaning up GPIO.")
        termios.tcsetattr(sys.stdin, termios.TCSANOW, original_settings)
        for pul in [PUL_1, PUL_2, PUL_3, PUL_4, PUL_5, PUL_6]:
            GPIO.output(pul, False)
