import RPi.GPIO as GPIO
from system_config import *

# GPIO pin assignment
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
DIR_2 = 3

GPIO.setup(DIR_2, GPIO.OUT)
GPIO.output(DIR_2, True)