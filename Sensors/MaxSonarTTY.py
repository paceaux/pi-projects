#!/usr/bin/python3
# Filename: maxSonarTTY.py

# Reads serial data from Maxbotix ultrasonic rangefinders
# Gracefully handles most common serial data glitches
# Use as an importable module with "import MaxSonarTTY"
# Returns an integer value representing distance to target in millimeters

from time import time
from serial import Serial

class MaxSonarTTY:
    """Uses the MaxSonarTTY to find a range"""

    def __init__(self, serialDevice = "/dev/ttyS0", maxWait = 3):
        self.serialDevice = serialDevice
        self.maxWait = maxWait

        print('self.device', self.serialDevice)
        print('self.maxWait', self.maxWait)

    def measure(self):
        print("serialDevice", self.serialDevice)
        ser = Serial(self.serialDevice, 9600, 8, 'N', 1, timeout=1)
        timeStart = time()
        valueCount = 0

        print(ser);
        while time() < timeStart + self.maxWait:
            if ser.inWaiting():
                print("it's waiting")
                bytesToRead = ser.inWaiting()
                valueCount += 1
                if valueCount < 2: # 1st reading may be partial number; throw it out
                    continue
                testData = ser.read(bytesToRead)
                if not testData.startswith(b'R'):
                    # data received did not start with R
                    continue
                try:
                    sensorData = testData.decode('utf-8').lstrip('R')
                except UnicodeDecodeError:
                    # data received could not be decoded properly
                    continue
                try:
                    mm = int(sensorData)
                except ValueError:
                    # value is not a number
                    continue
                ser.close()
                return(mm)

        ser.close()

