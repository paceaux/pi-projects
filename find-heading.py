from Sensors.Compass import Compass

sensor= Compass()
m= sensor.get_magnet()
bearing = sensor.get_bearing()
temp = sensor.get_temp()
print(m);
print(bearing)
print(temp)