import math
import time
import os
import datetime
from PIL import ImageFont
from get_oled import get_device
from luma.core.render import canvas
from Sensors.Compass import Compass

def posn(angle, arm_length):
    dx = int(math.cos(math.radians(angle)) * arm_length)
    dy = int(math.sin(math.radians(angle)) * arm_length)

    return (dx, dy)

def main():
    margin = 10
    cx = 30
    cy = min(device.height, 64) / 2
    sensor = Compass();

    left = cx - cy
    right = cx + cy
    font = ImageFont.load_default()


    with canvas(device) as draw:
        bearing = sensor.get_bearing()

        draw.text((cx,0), "N", font=font, fill="white" )
        draw.ellipse((left + margin, margin, right - margin, min(device.height, 64) - margin), outline="white" )
        hrs = posn(bearing, cy - margin - 7)

        draw.line((cx, cy, cx + hrs[0], cy + hrs[1]), fill="white")

    time.sleep(0.1)

if __name__ == "__main__":
    try: 
        device = get_device()
        while True:
            main()
    except KeyboardInterrupt:
        pass