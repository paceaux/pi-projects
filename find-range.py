import time

from DistanceSensor import DistanceSensor

GPIO_TRIGGER = 18
GPIO_ECHO = 24

if __name__ == '__main__':
    try:
        sensor = DistanceSensor(GPIO_TRIGGER, GPIO_ECHO)
        while True:
            dist = sensor.getDistance()
            print ("Measured Distance = %.1f cm" % dist.centimeters)
            print ("Measured Distance = %.1f inches" % dist.inches)
            if (dist.feet > 1):
                print("Measured Distance = %.1f feet" % dist.feet)

            time.sleep(.5)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        sensor.tearDown()