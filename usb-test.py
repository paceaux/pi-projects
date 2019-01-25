import usb.core

devices = usb.core.find(find_all=True)

if devices is None:
    raise ValueError('Danger zone?')


for device in devices:
    print('============')
    config = device.get_active_configuration()
    deviceIndex = config.index
    product = device.product

    portNum = device.port_number


    print('index:' + str(deviceIndex))
    print('product' + product)
    print('port number:' + str(portNum))
    
