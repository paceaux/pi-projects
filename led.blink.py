# Will blink two LEDs in a loop
import RPi.GPIO as GPIO
import time

# CONSTANTS: change these as you see fit
PIN1 = 18 # set to whatever GPIO port the led is on
PIN2 = 17 # set to whatever GPIO port the led is on
INTERVAL = .125 # time between on and off
CYCLES = 30 # number of cycles 


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)

counter = 0
isBlinking = False

while counter < CYCLES:
    GPIO.output(PIN1, isBlinking) # turn on first pin
    GPIO.output(PIN2,not(isBlinking)) #PIN2 is opposite of PIN1
    time.sleep(INTERVAL)

    isBlinking = not(isBlinking) #reverse blinking

    GPIO.output(PIN1, not(isBlinking))
    GPIO.output(PIN2, isBlinking) 
    time.sleep(INTERVAL/2)
    counter +=1

# after it's all over, turn off all the pins
if counter == CYCLES:
    GPIO.output(PIN1, False)
    GPIO.output(PIN2, False)


