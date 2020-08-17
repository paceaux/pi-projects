import time

from led import Led
from Sensors.DistanceSensor import DistanceSensor

GPIO_TRIGGER = 18
GPIO_ECHO = 24

if __name__ == '__main__':
    try:
        sensor = DistanceSensor(GPIO_TRIGGER, GPIO_ECHO)
        yellow = Led(19)
        green = Led(17)
        while True:
            dist = sensor.getDistance()
            if (dist.feet > 1):
                print("Measured Distance = %.1f feet" % dist.feet)
                green.blink(round(dist.feet), (1 / dist.feet))
            if (dist.feet < 1):
                print("Measured Distance = %.1f inches" % dist.inches)
            
                yellow.blink(round(dist.inches), (1/ dist.inches) - .02)

            time.sleep(2)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        sensor.tearDown()