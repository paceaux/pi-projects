import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess


class Oled:
    """ It draws an Oled"""
    def __init__(self, RST = 0, width = 128, height = 64):
        self.display = Adafruit_SSD1306.SSD1306_128_64(RST)
        self.width = width
        self.height = height
        self.initDisplay()

    def initDisplay(self):
        self.display.begin()
        self.refreshDisplay()
        self.width = self.display.width
        self.height = self.display.height


    def getDrawingImage(self):
        return Image.new('1', (self.width, self.height))

    def getDrawingSpace(self):
        self.drawingImage = self.getDrawingImage()
        draw = ImageDraw.Draw(self.drawingImage)
        draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)

        return draw

    def refreshDisplay(self):
        self.display.clear()
        self.display.display()
    
    def displayText(self, linesOfText):
        draw = self.getDrawingSpace()
        padding = -2
        top = padding
        bottom = self.height-padding
        x = 0
        font = ImageFont.load_default()


        # Write two lines of text.

        self.refreshDisplay()
        for index, val in enumerate(linesOfText):
            draw.text((x, top + (index* 8)), val, font=font, fill=255)

        # displaylay image.
        self.display.image(self.drawingImage)
        self.display.display()
        time.sleep(2)


oled = Oled() 