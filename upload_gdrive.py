#class to upload file with fileID to GDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

drive = GoogleDrive(gauth)

#myfile = drive.CreateFile({'title':'p_data.json', 'mimeType':'application/json'})
#myfile.SetContentString('{"Parking 1": "0", "Parking 2": "0", "Parking 3": "0", "Parking 4": "1"}')
#myfile.Upload() # Upload file.

yourfile_id = '19CB-WbL9MCQZRHkfxaWsMDz8ssHcAPEV'
new_file = drive.CreateFile({'title': 'boro.json', 'id': yourfile_id})
#file_content = new_file.GetContentString()
#file_content = file_content + '\ntest 2'
file_content = " {\"park1\": 1, \"park2\": 0, \"park3\": 0,\"park4\": 1,\"park5\": 1,\"park6\": 1,\"park7\": 1,\"park8\": 1}"
new_file.SetContentString(file_content)
new_file.Upload()
