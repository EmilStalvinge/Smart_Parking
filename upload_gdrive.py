#class to upload file with fileID to GDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import serial

ser = serial.Serial('/dev/ttyACM0',9600) # arduino uno
#ser = serial.Serial('/dev/ttyUSB0',9600) # arduino nano

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
drive = GoogleDrive(gauth)
yourfile_id = '19CB-WbL9MCQZRHkfxaWsMDz8ssHcAPEV'
new_file = drive.CreateFile({'title': 'boro.json', 'id': yourfile_id})

#file_content = new_file.GetContentString()
#file_content = file_content + '\ntest 2'

while True:
	read_serial=ser.readline()
	if read_serial != null:
		print(read_serial)
		print('hello there')
		datalist = read_serial.split()
		#print(mylist[0])
		#print(f'nodeid: {mylist[0]}')
		#print(f'nodeid: {mylist[1]}')

		#file_content = " {\"park1\": 1, \"park2\": 0, \"park3\": 0,\"park4\": 1,\"park5\": 1,\"park6\": 1,\"park7\": 1,\"park8\": 1}"
		#new_file.SetContentString(file_content)
		#new_file.Upload()
