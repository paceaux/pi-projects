#  https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/

# need GPIO for the fun stuffs
import RPi.GPIO as GPIO
import time

# Get a "convenience class" that will convert distances automagically
from Distance import Distance

class HCSR04():
    """A class that will get distance from an hc-sr04 sensor"""
    def __init__(self, triggerPin, echoPin):
        """Initialize the GPIO pins"""
        self.trigger = triggerPin
        self.echo = echoPin
        self.setup()

    def setup(self):
        """ sets up the pins and the directionality"""
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
    
    def getDistance(self):
        """returns a Distance object """
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
 