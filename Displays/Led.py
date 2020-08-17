import RPi.GPIO as GPIO
import time
import math

class Led:
    """ Class to represent a single, MONOCHROME LED. Recommended ports are 19, 17 """
    def __init__(self, pin):
        self.pin = pin
        self.isOn = False
        GPIO.setup(self.pin, GPIO.OUT)
    def on(self):
        self.isOn = True
        GPIO.output(self.pin, True)
    def off(self):
        self.isOn = False
        GPIO.output(self.pin, False)
    def toggle(self):
        if (self.isOn == True) :
            self.off()
        else:
            self.on()
    def blink(self, cycles = 1, interval = .25):
        counter = 0
        
        while counter < cycles:
            self.on()
            time.sleep(interval)
            self.off()
            time.sleep(interval)
            counter +=1
