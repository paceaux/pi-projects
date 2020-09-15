import math
import time
import os
import datetime
from PIL import ImageFont
from Utils.get_oled import get_device
from luma.core.render import canvas
from Sensors.Compass import Compass

def posn(angle, radius):
    dx = int(math.cos(math.radians(angle)) * radius)
    dy = int(math.sin(math.radians(angle)) * radius)

    return (dx, dy)

def main():
    margin = 10
    # center of device
    cx = min(device.width, 128) / 2
    cy = min(device.height, 64) / 2
    sensor = Compass();

    left = cx - cy
    right = cx + cy
    font = ImageFont.load_default()


    with canvas(device) as draw:
        # reduce the bearing to a reasonable number
        bearing = round(sensor.get_bearing(), 1)

        #unsure of exactly why have to use 270 here. I'm guessing the circle doesn't start at the top, at 0 degrees?
        north = posn(bearing + 270, cy - margin);
        south = posn(bearing - 90, cy - margin)

        #output bearing to upper right corner
        draw.text((device.width - 30, 0), str(bearing), font=font, fill="red")
        #put an "N" where north would be
        draw.text((cx + north[0], cy + north[1]), "N", font=font, fill="white" )

        #Draw the rings of the compass
        draw.ellipse(
            (left + margin, 
            margin, 
            right - margin, min(device.height, 64) - margin),
             outline="white" )

        draw.line((cx - south[0], cy - south[1], cx + north[0], cy + north[1]), fill="white")

    time.sleep(0.1)

if __name__ == "__main__":
    try: 
        device = get_device()
        while True:
            main()
    except KeyboardInterrupt:
        pass