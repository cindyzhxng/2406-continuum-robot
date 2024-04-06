#import the GPIO and time package
import RPi.GPIO as GPIO
import time
import math
from system_config import *

motor_step_size = 1.8
microsteps = 8
steps_per_rev = 360/(motor_step_size)*microsteps
pitch_circumference = math.pi * 12 # mm
gear_ratio = 40/12
distance_per_step = pitch_circumference / steps_per_rev * gear_ratio # in mm per step
wait_time_s = 0.0025 # frequency of 200Hz with period of 5ms

wait_dir_s = 0.001 # 1 ms
wait_ena_s = 0.2 # 200ms

# GPIO pin assignment
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

pul_1 = 2
dir_1 = 3
ena_1 = 4

pul_3 = 17
dir_3 = 27
ena_3 = 22

pul_4 = 10
dir_4 = 9
ena_4 = 11

pul_6 = 5
dir_6 = 6
ena_6 = 13

pul_2 = 14
dir_2 = 15
ena_2 = 18

pul_5 = 25
dir_5 = 8
ena_5 = 7

# feel free to rename
# furthest aka the one farthest from u on the rack
limit_switch_furthest = 21
limit_switch_middle = 20
limit_switch_closest = 16

motors = {
    TRA_1: {"pulse": pul_1, "dir": dir_1, "enable": ena_1},
    ROT_1: {"pulse": pul_2, "dir": dir_2, "enable": ena_2},
    TRA_2: {"pulse": pul_4, "dir": dir_4, "enable": ena_4},
    ROT_2: {"pulse": pul_3, "dir": dir_3, "enable": ena_3},
    TRA_3: {"pulse": pul_5, "dir": dir_5, "enable": ena_5},
    ROT_3: {"pulse": pul_6, "dir": dir_6, "enable": ena_6},
}

# GPIO output
for _, pins in motors.items():
    GPIO.setup(pins["pulse"], GPIO.OUT)
    GPIO.setup(pins["dir"], GPIO.OUT)
    GPIO.setup(pins["enable"], GPIO.OUT)

# GPIO pins still available to use
# GPIO: 19, 26, 23, 24, 12, 16, 20 21

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
    for motor_num, motor_translation in distance.iter():
        # Step 1: Set ENA to HIGH; ENA must be ahead of DIR by at least 200ms
        GPIO.output(motors[motor_num]["enable"], True)
        time.sleep(wait_ena_s)
    
        # Step 2: Set DIR; DIR must be ahead of PUL effective edge by 2us to ensure correct direction
        if distance >= 0:
            GPIO.output(motors[motor_num]["dir"], True)
        else:
            GPIO.output(motors[motor_num]["dir"], False)
        time.sleep(wait_dir_s)

        # Step 3: Pulse the proper amount
        num_steps = math.ceil(distance / distance_per_step)
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
    motion_list = [
        [0,120,0,180,0,180],
    ]

    for motion in motion_list:
        turn_degree(motion)

    time.sleep(3)
    # shut down pins
    for motor_num in range(6):
        GPIO.output(motors[motor_num]["pulse"],False)
    while True:
        continue
        
except KeyboardInterrupt:
    print("Ctrl+C detected. Cleaning up GPIO.")
    for pul in [pul_1, pul_2, pul_3, pul_4, pul_5, pul_6]:
        GPIO.output(pul,False)
    # GPIO.cleanup()