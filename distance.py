#  https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/
# IT WORKS!!!!!!!
import RPi.GPIO as GPIO
import time

# GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 18
GPIO_ECHO = 24

# GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
# GPIO.setup(GPIO_ECHO, GPIO.IN)

class Distance():
    """ A class just for converting distances"""

    def __init__(self, centimeters):
        self.centimeters = centimeters
    
    @property
    def inches(self):
        return self.centimeters / 2.54
    
    @property
    def feet(self):
        return self.inches / 12
    
    @property
    def meters(self):
        return self.centimeters / 100;

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
 
if __name__ == '__main__':
    try:
        while True:
            sensor = DistanceSensor(GPIO_TRIGGER, GPIO_ECHO)
            dist = sensor.getDistance()
            print ("Measured Distance = %.1f cm" % dist.centimeters)
            print ("Measured Distance = %.1f inches" % dist.inches)
            if (dist.feet > 1):
                print("Measured Distance = %.1f feet" % dist.feet)

            time.sleep(.5)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()