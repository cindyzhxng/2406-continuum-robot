#import the GPIO and time package
import RPi.GPIO as GPIO
import time
import math
from system_config import *

motor_step_size = 1.8
microsteps = 8
steps_per_rev = 360/(motor_step_size)*microsteps
pitch_circumference = math.pi * 40
gear_ratio = 40/12
# distance_per_step = pitch_circumference / steps_per_rev * gear_ratio # in mm per step
wait_time_s = 0.0025 # frequency of 200Hz with period of 5ms

wait_dir_s = 0.001 # 1 ms
wait_ena_s = 0.2 # 200ms

# GPIO pin assignment
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

motors = {
    TRA_1: {"pulse": PUL_1, "dir": DIR_1, "enable": ENA_1},
    ROT_1: {"pulse": PUL_2, "dir": DIR_2, "enable": ENA_2},
    TRA_2: {"pulse": PUL_4, "dir": DIR_4, "enable": ENA_4},
    ROT_2: {"pulse": PUL_3, "dir": DIR_3, "enable": ENA_3},
    TRA_3: {"pulse": PUL_5, "dir": DIR_5, "enable": ENA_5},
    ROT_3: {"pulse": PUL_6, "dir": DIR_6, "enable": ENA_6},
}

# GPIO output
for _, pins in motors.items():
    GPIO.setup(pins["pulse"], GPIO.OUT)
    GPIO.setup(pins["dir"], GPIO.OUT)
    GPIO.setup(pins["enable"], GPIO.OUT)

# set-up limit switches
GPIO.setup(LIMIT_SWITCH_1, GPIO.IN)
GPIO.setup(LIMIT_SWITCH_2, GPIO.IN)
GPIO.setup(LIMIT_SWITCH_3, GPIO.IN)

# function that takes array of degrees for each motor to turn
# and then turns that amt -> translates to number of steps
# if positive degree --> rotate one direction
# if negative degree --> rotate in other direction
def turn_degree(degrees):
    for motor_num in range(len(degrees)):
        motor_degree = degrees[motor_num]
        # Step 1: Set ENA to HIGH; ENA must be ahead of DIR by at least 200ms
        GPIO.output(motors[motor_num]["enable"], True)
    
        # Step 2: Set DIR; DIR must be ahead of PUL effective edge by 2us to ensure correct direction
        if motor_degree >= 0:
            GPIO.output(motors[motor_num]["dir"], True)
        else:
            GPIO.output(motors[motor_num]["dir"], False)
        time.sleep(wait_dir_s)

        # Step 3: Pulse the proper amount
        num_steps = math.ceil(gear_ratio * motor_degree/360 * steps_per_rev)
        pulse_pin = motors[motor_num]["pulse"]
        for _ in range(num_steps):
            GPIO.output(pulse_pin,True)
            time.sleep(wait_time_s)
            GPIO.output(pulse_pin,False)
            time.sleep(wait_time_s)

def translate_steps(distance):
    for motor_num, motor_translation in distance.items():
        # Step 1: Set ENA to HIGH; ENA must be ahead of DIR by at least 200ms
        GPIO.output(motors[motor_num]["enable"], True)
        time.sleep(wait_ena_s)
    
        # Step 2: Set DIR; DIR must be ahead of PUL effective edge by 2us to ensure correct direction
        if motor_translation >= 0:
            GPIO.output(motors[motor_num]["dir"], True)
        else:
            GPIO.output(motors[motor_num]["dir"], False)
        time.sleep(wait_dir_s)

        # Step 3: Pulse the proper amount
        num_steps = math.ceil(math.fabs(motor_translation) * steps_per_rev * gear_ratio / pitch_circumference)
        pulse_pin = motors[motor_num]["pulse"]
        for _ in range(num_steps):
            GPIO.output(pulse_pin,True)
            time.sleep(wait_time_s)
            GPIO.output(pulse_pin,False)
            time.sleep(wait_time_s)

# 0 is Rot_1
# 1 is Tra_1
# 2 is Rot_2
# 3 is Tra_2
# 4 is Rot_3
# 5 is Tra_3

# trans default is backward
try:

    # turn_degree([0,90,0,0,0,0])
    # turn_degree([90,0,0,0,0,0])
    # turn_degree([0,0,0,0,90,0])

    # turn_degree([0,90,0,90,0,90])
    # motion_list = [
    #     [0,120,0,180,0,180],
    # ]

    # for motion in motion_list:
    #     turn_degree(motion)

    motion_list = {TRA_1:-30, ROT_1: 0, TRA_2: 0, ROT_2: 0,TRA_3: 0,ROT_3: 0}
    translate_steps(motion_list)

    time.sleep(3)
    # shut down pins
    for motor_num in range(6):
        GPIO.output(motors[motor_num]["pulse"],False)
    while True:
        continue
        
except KeyboardInterrupt:
    print("Ctrl+C detected. Cleaning up GPIO.")
    for pul in [PUL_1, PUL_2, PUL_3, PUL_4, PUL_5, PUL_6]:
        GPIO.output(pul,False)
    # GPIO.cleanup()