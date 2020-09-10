import time
from Sensors.Compass import Compass



if __name__ == "__main__":
    try:
        sensor= Compass()
        sensor.set_declination(-2)
        while True:
            print(sensor.get_bearing())
            time.sleep(1)
    except KeyboardInterrupt:
        sensor.mode_stby()
        print ("Stopped getting bearing");
