import py_qmc5883l

sensor = py_qmc5883l.QMC5883L()
sensor.mode_continuous()
sensor.declination = -4
m = sensor.get_magnet()




print(m)


