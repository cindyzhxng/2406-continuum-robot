#import the GPIO and time package
import RPi.GPIO as GPIO
import time
import math

motor_step_size = 1.8
microsteps = 8
steps_per_rev = 360/(motor_step_size)*microsteps
pitch_circumference = math.pi * 12 # mm
distance_per_step = pitch_circumference / steps_per_rev * gear_ratio # in mm per step
gear_ratio = 40/12
wait_time_s = 0.0025 # frequency of 200Hz with period of 5ms

wait_dir_s = 0.001 # 1 ms
wait_ena_s = 0.2 # 200ms

# GPIO pin assignment
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

pul_1 = 2
dir_1 = 3
ena_1 = 4

pul_2 = 17
dir_2 = 27
ena_2 = 22

pul_3 = 10
dir_3 = 9
ena_3 = 11

pul_4 = 5
dir_4 = 6
ena_4 = 13

pul_5 = 14
dir_5 = 15
ena_5 = 18

pul_6 = 25
dir_6 = 8
ena_6 = 7

motors = {
    0: {"pulse": pul_1, "dir": dir_1, "enable": ena_1},
    1: {"pulse": pul_2, "dir": dir_2, "enable": ena_2},
    2: {"pulse": pul_3, "dir": dir_3, "enable": ena_3},
    3: {"pulse": pul_4, "dir": dir_4, "enable": ena_4},
    4: {"pulse": pul_5, "dir": dir_5, "enable": ena_5},
    5: {"pulse": pul_6, "dir": dir_6, "enable": ena_6},
}

# GPIO output
for pins in motors.items():
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
    for motor_num, motor_degree in degrees.iter():
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
        if motor_degree >= 0:
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

try:
    turn_degree([90,0,0,0,0,0])
    time.sleep(3)
    while True:
        # shut down pins
        for motor_num in range(6):
            GPIO.output(motors[motor_num]["pulse"],False)
except KeyboardInterrupt:
    print("Ctrl+C detected. Cleaning up GPIO.")
    GPIO.output(pul_1,False)
    # GPIO.cleanup()