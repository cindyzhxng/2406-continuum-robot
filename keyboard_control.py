import tty, sys, termios
from stepper_motor_controls import * 

filedescriptors = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)

def keyboard_to_movement(move):
    match move:
        case "w":
            print("1: we translate first stage")
            # translate_steps(0.023562)
            step_pin(TRA_1, NUM_MANUAL_STEP, MANUAL_FREQ)
        case "s":
            print("1: move back")
            step_pin(TRA_1, -NUM_MANUAL_STEP, MANUAL_FREQ)
        case "u":
            print("1: we rotate ccw")
            step_pin(ROT_1, NUM_MANUAL_STEP, MANUAL_FREQ)
        case "i":
            print("1: rotate cw")
            step_pin(ROT_1, -NUM_MANUAL_STEP, MANUAL_FREQ)
        case "q":
            print("2: move forward")
            step_pin(TRA_2, NUM_MANUAL_STEP, MANUAL_FREQ)
        case "a":
            print("2: move back")
            step_pin(TRA_2, -NUM_MANUAL_STEP, MANUAL_FREQ)
        case "j":
            print("2: rotate ccw")
            step_pin(ROT_2, NUM_MANUAL_STEP, MANUAL_FREQ)
        case "k":
            print("2: rotate cw")
            step_pin(ROT_2, -NUM_MANUAL_STEP, MANUAL_FREQ)
        case "e":
            print("3: move forward")
            step_pin(TRA_3, NUM_MANUAL_STEP, MANUAL_FREQ)
        case "d":
            print("3: move back")
            step_pin(TRA_3, -NUM_MANUAL_STEP. MANUAL_FREQ)
        case "n":
            print("3: rotate ccw")
            step_pin(ROT_3, NUM_MANUAL_STEP, MANUAL_FREQ)
        case "m":
            print("3: rotate cw")
            step_pin(ROT_3, -NUM_MANUAL_STEP, MANUAL_FREQ)
        case _:
            print("Input is not supported.")

while True:
  move=sys.stdin.read(1)[0]
  print("You pressed", move)
  keyboard_to_movement(move)



