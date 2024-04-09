from stepper_motor_controls import *

if __name__ == "__main__":
    try:
        # home_translation([1])
        # home_rotation([2])
        home_robot()
        # translate_steps([100,0,0,0,0,0])

        while True:
            continue
    except KeyboardInterrupt:
        print("Ctrl+C detected. Cleaning up GPIO.")
        termios.tcsetattr(sys.stdin, termios.TCSANOW, original_settings)
        for pul in [PUL_1, PUL_2, PUL_3, PUL_4, PUL_5, PUL_6]:
            GPIO.output(pul,False)