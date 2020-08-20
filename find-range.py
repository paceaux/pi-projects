import time

from led import Led
from Sensors.DistanceSensor import DistanceSensor

# Known working pins for the hcsr04 sensor
GPIO_TRIGGER = 18 # should be PWM pins: 12, 13, 18, 19
GPIO_ECHO = 24 # generic ones: 17, 27, 22, 23, 24, 25

# how much time between scans
INTERVAL_TIME = .5

if __name__ == '__main__':
    try:
        # Create a sensor
        sensor1 = DistanceSensor(GPIO_TRIGGER, GPIO_ECHO)
        sensor2 = DistanceSensor(12, 23);
        # create some Leds
        closeLight = Led(19)
        farLight = Led(17)

        # Create an infinite loop
        while True:
            # Get the distance (returns a Distance object so we can get cm, m, ft, in off of it)
            dist1 = sensor1.getDistance()
            dist2 = sensor2.getDistance()

            # do some stuff
            print(dist2.inches)
            if (dist1.feet > 1):
                print("Measured Distance = %.1f feet" % dist1.feet)
                # Blink the number of times, rounding
                # also set the Interval to blink to be less than a second. This way we can set our loop to at least 1 second and get all our blinks in
                farLight.blink(round(dist1.feet), (INTERVAL_TIME / dist1.feet))
            if (dist1.feet < 1):
                print("Measured Distance = %.1f inches" % dist1.inches)
            
                closeLight.blink(round(dist1.inches), (INTERVAL_TIME/ dist1.inches))

            time.sleep(INTERVAL_TIME)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        sensor1.tearDown()