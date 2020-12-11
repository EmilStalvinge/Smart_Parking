#class to upload file with fileID to GDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import serial
from pathlib import Path

myfile = Path("/home/pi/pingpark/ski_parking_sensor/client_secrets.json")

GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = myfile 

#ser = serial.Serial('/dev/ttyACM0',9600) # arduino uno
ser = serial.Serial('/dev/ttyUSB0',9600) # arduino nano
node1 = ['0']*4
node2 = ['0']*4
gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
drive = GoogleDrive(gauth)
yourfile_id = '19CB-WbL9MCQZRHkfxaWsMDz8ssHcAPEV'
new_file = drive.CreateFile({'title': 'boro.json', 'id': yourfile_id})

#file_content = new_file.GetContentString()
#file_content = file_content + '\ntest 2'

while True:
	read_serial=ser.readline() #waits for an message until timeout
	#print(read_serial)
	#print('hello there')
	data_list = read_serial.split()
	node_id = int(data_list[0].decode('utf-8'))
	print(f'recieved data from node: {node_id}')

	if node_id == 1:
		node1.clear()
		for p_aval in data_list[1:]:
			if p_aval.decode('utf-8') == 'Available':
				node1.append('0')
			else:
				node1.append('1')
	if node_id == 2:
		node2.clear()
		for p_aval in data_list[1:]:
			if p_aval.decode('utf-8') == 'Available':
				node2.append('0')
			else:
				 node2.append('1')


	file_content = " {\"park1\": " + node1[0] + ", \"park2\": " +node1[1]+ ", \"park3\": " +node1[2]+ ",\"park4\": " +node1[3]+ ",\"park5\": " + \
				node2[0]+ ",\"park6\": " +node2[1]+ ",\"park7\": " +node2[2]+ ",\"park8\": " +node2[3]+ "}"
	print(f'uploading string: {file_content}')
	new_file.SetContentString(file_content)
	new_file.Upload()
