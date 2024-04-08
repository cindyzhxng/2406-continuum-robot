import tty, sys, termios

filedescriptors = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)

def keyboard_to_movement(move):
    match move:
        case "w":
            print("1: we translate first stage")
        case "s":
            print("1: move back")
        case "u":
            print("1: we rotate cw")
        case "i":
            print("1: rotate ccw")
        case "q":
            print("2: move forward")
        case "a":
            print("2: move back")
        case "j":
            print("2: rotate cw")
        case "k":
            print("2: rotate ccw")
        case "e":
            print("3: move forward")
        case "d":
            print("3: move back")
        case "n":
            print("3: rotate cw")
        case "m":
            print("3: rotate ccw")
        case _:
            print("Input is not supported.")

while True:
  move=sys.stdin.read(1)[0]
  print("You pressed", move)
  keyboard_to_movement(move)
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, filedescriptors)


# how much does 1 step turn?
# num_steps = gear_ratio * motor_degree/360 * steps_per_rev
# motor_degree = num_steps / gear_ratio * 360 / steps_per_rev = 0.75 deg

# how much does 1 step move?
# num_steps = math.fabs(motor_translation) * steps_per_rev * gear_ratio / pitch_circumference
# motor_translation = num_steps / steps_per_rev / gear_ratio * pitch_circumference = 0.023562mm

# how much does 1 keyboard input move?
# STAGE 1:
# linear
# w - move forward
# s - move back
# u - rotate cw
# i - rotate ccw

# STAGE 2:
# linear
# q - move forward
# a - move back
# j - rotate cw
# k - rotate ccw

# STAGE 3:
# linear
# e - move forward
# d - move back
# n - rotate cw
# m - rotate ccw



