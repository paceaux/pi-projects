# pimylifeup.com/raspberry-pi-distance-sensor/
# this maybe ran successfully once?

import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BOARD)

PIN_TRIGGER = 7
PIN_ECHO = 11

GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)




def distance():
    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, False)

    pulse_start =time.time()
    pulse_end = time.time()
   
    print("first pulse start" + str(pulse_start))
    while (GPIO.input(PIN_ECHO)==0):
        pulse_start = time.time()
    
    print("second pulse" + str(pulse_start_time))
    while GPIO.input(PIN_ECHO) == 1:
        pulse_end= time.time()

       
    pulse_duration = pulse_end - pulse_start
    distance = round(pulse_duration * 17150, 2)

    return distance

if __name__ =='__main__':
    try:
        while True:
            print("trying to get distance")
            GPIO.output(PIN_TRIGGER, GPIO.LOW)
            print("Let sensor settle")
            time.sleep(2)
            dist = distance()
            print("Distance is " + str(dist) + " cm")
            time.sleep(1)
    except KeyboardInterrupt:
        print("stopped measuring")

        GPIO.cleanup()
