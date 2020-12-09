import serial

#ser = serial.Serial('/dev/ttyACM0',9600)
ser = serial.Serial('/dev/ttyUSB0',9600)
while True:
	read_serial=ser.readline()
	mylist = read_serial.split()
	#print(mylist[0]) #read_serial
	print(f'node id: {mylist[0]}.'})
	print(f'parking 1: {mylist[1]}.'})
