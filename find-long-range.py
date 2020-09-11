#!/usr/bin/python3
# Filename: rangeFind.py

# sample script to read range values from Maxbotix ultrasonic rangefinder

from time import sleep
from Sensors.MaxSonarTTY import MaxSonarTTY

serialPort = "/dev/ttyS0"
maxRange = 5000  # change for 5m vs 10m sensor
sleepTime = 5
minMM = 9999
maxMM = 0

sensor = MaxSonarTTY(serialPort)
while True:
    mm = sensor.measure()
    if mm >= maxRange:
        print("no target")
        sleep(sleepTime)
        continue
    if mm < minMM:
        minMM = mm
    if mm > maxMM:
        maxMM = mm

    print("distance:", mm, "  min:", minMM, "max:", maxMM)
    sleep(sleepTime)
