import RPi.GPIO as GPIO
import time
import math

class Led:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
    def on(self):
        GPIO.output(self.pin, True)
    def off(self):
        GPIO.output(self.pin, False)
    def blink(self, cycles = 1, interval = .25):
        counter = 0
        
        while counter < cycles:
            self.on()
            time.sleep(interval)
            self.off()
            time.sleep(interval)
            counter +=1
