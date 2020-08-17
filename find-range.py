import time

from led import Led
from Sensors.DistanceSensor import DistanceSensor

# Known working pins for the hcsr04 sensor
GPIO_TRIGGER = 18
GPIO_ECHO = 24

# how much time between scans
INTERVAL_TIME = .5

if __name__ == '__main__':
    try:
        # Create a sensor
        sensor = DistanceSensor(GPIO_TRIGGER, GPIO_ECHO)
        # create some Leds
        closeLight = Led(19)
        farLight = Led(17)

        # Create an infinite loop
        while True:
            # Get the distance (returns a Distance object so we can get cm, m, ft, in off of it)
            dist = sensor.getDistance()

            # do some stuff
            if (dist.feet > 1):
                print("Measured Distance = %.1f feet" % dist.feet)
                # Blink the number of times, rounding
                # also set the Interval to blink to be less than a second. This way we can set our loop to at least 1 second and get all our blinks in
                farLight.blink(round(dist.feet), (INTERVAL_TIME / dist.feet))
            if (dist.feet < 1):
                print("Measured Distance = %.1f inches" % dist.inches)
            
                closeLight.blink(round(dist.inches), (INTERVAL_TIME/ dist.inches))

            time.sleep(INTERVAL_TIME)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        sensor.tearDown()