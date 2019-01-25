import RPi.GPIO as GPIO
import time
colors = [0xff0000, 0x00ff00, 0xc0ffee, 0xfadfad]
PINS = {'r': 11, 'g': 19, 'b': 13}

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for i in PINS:
    GPIO.setup(PINS[i], GPIO.OUT)
    GPIO.output(PINS[i], GPIO.HIGH)

RGB = {
    'R' : GPIO.PWM(PINS['r'], 1000),
    'G' : GPIO.PWM(PINS['g'], 1000),
    'B' : GPIO.PWM(PINS['b'], 1000)
}

for c in RGB:
    RGB[c].start(0)

def off():
    for i in PINS:
        GPIO.output(PINS[i], GPIO.LOW)


def setColor(r, g, b):

    RGB['R'].ChangeFrequency(200)
    RGB['G'].ChangeFrequency(6700)
    RGB['B'].ChangeFrequency(2000)
try:
    off()
    time.sleep(2)
    setColor(100, 160, 200)
except KeyboardInterrupt:

    for i in PINS:
        GPIO.output(PINS[i], GPIO.HIGH)
    GPIO.cleanup()
    off()