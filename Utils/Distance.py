class Distance():
    """ A class just for converting distances"""

    def __init__(self, centimeters):
        self.centimeters = centimeters
    
    @property
    def inches(self):
        return self.centimeters / 2.54
    
    @property
    def feet(self):
        return self.inches / 12
    
    @property
    def meters(self):
        return self.centimeters / 100;
