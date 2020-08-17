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