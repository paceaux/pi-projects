# will flash LEDs BASED ON A COUNTDOWN

import RPi.GPIO as GPIO
import time
import math
from led import Led # a very simple class for manipulating Leds on a GPIO breadboard

# CONSTANTS: change these as you see fit
PIN1 = 18 # set to whatever GPIO port the led is on
PIN2 = 17 # set to whatever GPIO port the led is on
TIME = 30 # seconds

# set it all up like usual
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# create leds
timingLed = Led(PIN1) # keeps a steady pace
notifyingLed = Led(PIN2) # will change based on how close we are to the end

counter = TIME #set the counter to be the same as the seconds
third = math.floor(TIME / 3)
twothirds = third * 2
half = math.floor(TIME / 2)

while (counter > 0):
    counter-=1 #step backwards by one
    time.sleep(1)
    timingLed.toggle() #put the led in the opposite state it was in before
    
    # first third
    if (counter > half and counter < twothirds ): 
        notifyingLed.on()
    
    # halfway
    if (counter <= half and counter > third) :
        notifyingLed.toggle()
    
    # last third
    if (counter <= third):
        notifyingLed.blink(2, .05)
