import time

from Displays.Led import Led
from Sensors.DistanceSensor import DistanceSensor

# Known working pins for the hcsr04 sensor
GPIO_TRIGGER = 18 # should be PWM pins: 12, 13, 18, 19
GPIO_ECHO = 24 # generic ones: 17, 27, 22, 23, 24, 25

# how much time between scans
INTERVAL_TIME = .5

def printDistance(distance, label):
    if (distance.feet > 1):
        print(label + " = %.1f feet" % distance.feet)

    if (dist2.feet < 1):
        print(label + " = %.1f inches" % distance.inches)

def blinkDistance(amount, led):
    led.blink(amount, INTERVAL_TIME / amount)

if __name__ == '__main__':
    try:
        # Create a sensor
        sensor1 = DistanceSensor(GPIO_TRIGGER, GPIO_ECHO)
        sensor2 = DistanceSensor(12, 23);
        # create some Leds
        led1 = Led(19)
        led2 = Led(17)

        # Create an infinite loop
        while True:
            # Get the distance (returns a Distance object so we can get cm, m, ft, in off of it)
            dist1 = sensor1.getDistance()
            dist2 = sensor2.getDistance()

            # do some stuff
            printDistance(dist1, "left Sensor")
            printDistance(dist2, "right Sensor")
            blinkDistance(dist1.inches, led1 )
            blinkDistance(dist2.inches, led2 )
            time.sleep(INTERVAL_TIME)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        sensor1.tearDown()