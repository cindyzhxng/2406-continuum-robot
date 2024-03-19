#import the GPIO and time package
import RPi.GPIO as GPIO
import time
import math

motor_step_size = 1.8
microsteps = 8
steps_per_rev = 360/(motor_step_size)*microsteps
gear_ratio = 40/12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
wait_time_s = 0.0025

# function that takes angle of degree and then turns that amt -> translates to number of steps
def turn_degree(degree):
    num_steps = math.ceil(gear_ratio * degree/360 * steps_per_rev)
    for _ in range(num_steps):
        GPIO.output(7,True)
        time.sleep(wait_time_s)
        GPIO.output(7,False)
        time.sleep(wait_time_s)

try:
    turn_degree(90)
    time.sleep(3)
    while True:
        GPIO.output(7,False)
    # GPIO.cleanup()
except KeyboardInterrupt:
    print("Ctrl+C detected. Cleaning up GPIO.")
    GPIO.output(7,False)
    # GPIO.cleanup()