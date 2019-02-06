import os
import datetime
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import time



def dabasedump(db_name):
    now = str(datetime.datetime.now())
    strs, replacements = now, {"-": "_", " ": "", ":": "_"}
    now = "".join([replacements.get(c, c) for c in strs])
    os.system("mysqldump --databases " + db_name + " > " + now + ".sql")


def googledrive(filename):
    g_login = GoogleAuth()
    g_login.LocalWebserverAuth()
    drive = GoogleDrive(g_login)
    with open(filename, "r") as f:
        file_drive = drive.CreateFile({'title': filename})
    file_drive.SetContentString(f.read())
    file_drive.Upload()
    print("backup Completed. Saved as :" + filename)


db_name = ""
dabasedump(db_name)
time.sleep(5)
googledrive(db_name+".sql")
