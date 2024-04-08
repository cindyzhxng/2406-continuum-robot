#import the GPIO and time package
import RPi.GPIO as GPIO
import time
import math
import numpy as np
from system_config import *

motor_step_size = 1.8
microsteps = 8
D = 40
d = 12
steps_per_rev = 360/(motor_step_size)*microsteps
pitch_circumference = math.pi * 40
gear_ratio = D/d
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

        # Step 3: Pulse the proper amount
        num_steps = int(math.ceil(gear_ratio * motor_degree/360 * steps_per_rev))
        step_pin(motor_num, num_steps, DEFAULT_FREQ)

def translate_steps(distances):
    # convert distaces to degrees
    degrees = np.array(distances)*gear_ratio/(D/2)
    turn_degree(degrees)

def step_pin(motor_ID, num_steps, step_freq=DEFAULT_FREQ):
    pulse_pin = motors[motor_ID]["pulse"]
    if num_steps >= 0:
        GPIO.output(motors[motor_ID]["dir"], False)
    else:
        GPIO.output(motors[motor_ID]["dir"], True)
        
    # Set DIR; DIR must be ahead of PUL effective edge by 2us to ensure correct direction
    time.sleep(wait_dir_s)
    for _ in range(abs(num_steps)):
        GPIO.output(pulse_pin,True)
        time.sleep(1/step_freq)
        GPIO.output(pulse_pin,False)
        time.sleep(1/step_freq)

def home_translation(stages = [3, 2, 1]):
    print("-----------TRANSLATION HOMING STARTED-----------")
    motor_ID_dict = {3: TRA_3, 2: TRA_2, 1: TRA_1}
    limit_dict = {3: LIMIT_SWITCH_3, 2: LIMIT_SWITCH_2, 1: LIMIT_SWITCH_1}
    for stage in stages:
        limit_pin = limit_dict[stage]
        while True:
            while GPIO.input(limit_pin) == GPIO.HIGH:
                step_pin(motor_ID_dict[stage], -1, DEFAULT_FREQ)
            count = 0
            while count < 4:
                time.sleep(10e-3)
                if GPIO.input(limit_pin) == GPIO.LOW:
                    count += 1
                if GPIO.input(limit_pin) == GPIO.HIGH:
                    break
            if count == 3:
                break
        print(f"Stage {stage}: Translation Homed Successfully")
    print("-----------TRANSLATION HOMING COMPLETED-----------")
                
        
        
    

# 0 is Rot_1
# 1 is Tra_1
# 2 is Rot_2
# 3 is Tra_2
# 4 is Rot_3
# 5 is Tra_3

# trans default is backward
if __name__ == "__main__":
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