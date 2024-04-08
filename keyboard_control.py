from stepper_motor_controls import * 

def keyboard_to_movement(move):
    match move:
        case "t":
            print("1: we translate first stage")
            # translate_steps(0.023562)
            step_pin(TRA_1, NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
        case "g":
            print("1: move back")
            step_pin(TRA_1, -NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
        case "y":
            print("1: we rotate ccw")
            step_pin(ROT_1, NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
        case "h":
            print("1: rotate cw")
            step_pin(ROT_1, -NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
        case "e":
            print("2: move forward")
            step_pin(TRA_2, NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
        case "d":
            print("2: move back")
            step_pin(TRA_2, -NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
        case "r":
            print("2: rotate ccw")
            step_pin(ROT_2, NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
        case "f":
            print("2: rotate cw")
            step_pin(ROT_2, -NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
        case "q":
            print("3: move forward")
            step_pin(TRA_3, NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
        case "a":
            print("3: move back")
            step_pin(TRA_3, -NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
        case "w":
            print("3: rotate ccw")
            step_pin(ROT_3, NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
        case "s":
            print("3: rotate cw")
            step_pin(ROT_3, -NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
        case "u":
            print("All forward")
            step_pin(TRA_3, NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
            step_pin(TRA_2, NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
            step_pin(TRA_1, NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
        case "j":
            print("All back")
            step_pin(TRA_3, -NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
            step_pin(TRA_2, -NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
            step_pin(TRA_1, -NUM_MANUAL_STEP, MANUAL_TRANS_FREQ)
        case "i":
            print("All CCW")
            step_pin(ROT_3, NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
            step_pin(ROT_2, NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
            step_pin(ROT_1, NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
        case "k":
            print("All CW")
            step_pin(ROT_3, -NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
            step_pin(ROT_2, -NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
            step_pin(ROT_1, -NUM_MANUAL_STEP, MANUAL_ROT_FREQ)
        case _:
            print("Input is not supported.")

while True:
  move=sys.stdin.read(1)[0]
  print("You pressed", move)
  keyboard_to_movement(move)



