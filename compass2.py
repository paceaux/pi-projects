# ONLY WORKS IN PYTHON3

import py_qmc5883l

sensor = py_qmc5883l.QMC5883L()
sensor.mode_continuous()
sensor.declination = 0
m = sensor.get_magnet()
bearing = sensor.get_bearing()



print(m)
print(bearing)

