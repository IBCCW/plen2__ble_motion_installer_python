import serial.tools.list_ports
 
for device in list(serial.tools.list_ports.comports()):
	if 'Bluegiga' in device[1]:
		print device[1]

	if 'Arduino Micro' in device[1]:
		print device[1]