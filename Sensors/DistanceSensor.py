#  https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/

import RPi.GPIO as GPIO
import time
from Distance import Distance

class DistanceSensor():
    """A class that will get distance from an hc-sr04 sensor"""
    def __init__(self, triggerPin, echoPin):
        """Initialize the GPIO pins"""
        self.trigger = triggerPin
        self.echo = echoPin
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
    
    def getDistance(self):
        GPIO.output(self.trigger, True)
    
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)
    
        StartTime = time.time()
        StopTime = time.time()
    
        while GPIO.input(self.echo) == 0:
            StartTime = time.time()
    
        while GPIO.input(self.echo) == 1:
            StopTime = time.time()
    
        TimeElapsed = StopTime - StartTime
        distance = Distance((TimeElapsed * 34300) / 2)
    
        return distance

    def tearDown(self):
        GPIO.cleanup()   
 