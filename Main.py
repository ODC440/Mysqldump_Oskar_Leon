#Oskar,Leon 05.05.2021


import os
import pipes
import time

import pymysql

# MySQL-Datenbank-Details, fuer welche Sicherung eine Sicherung erfolgen soll. Stellen Sie sicher, dass der Benutzer ueber ausreichende Berechtigungen verfuegt, um Datenbanken zu sichern.

DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_USER_PASSWORD = 'password'
DB_NAME = 'Leon'
BACKUP_PATH = '/home/oskar/Oskar_Leon_Dump_SQl'
conn = pymysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_USER_PASSWORD, db=DB_NAME)

# Aktuelle Zeit abrufen, um einen separaten Sicherungsordner wie "MySQL.backup(test) 15.03.2019_16;10;45" zu erstellen.

ZEIT = time.strftime('%d.%m.%Y_%H;%M')
ACKTUELLEBACKUPPATH = BACKUP_PATH + '/MySQL.backup(' + DB_NAME + ') ' + ZEIT

# Ueberpruefen, ob der Sicherungsordner bereits existiert oder nicht. Wenn nicht vorhanden wird es erstellt.
try:
    os.stat(ACKTUELLEBACKUPPATH)
except:
    os.mkdir(ACKTUELLEBACKUPPATH)
# Starten dea Sicheungs Prozess.
print("Start der Datenbank Sicherung von " + DB_NAME)
db = DB_NAME
dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + pipes.quote(
    ACKTUELLEBACKUPPATH) + "/" + db + ".sql"
os.system(dumpcmd)
gzipcmd = "gzip " + pipes.quote(ACKTUELLEBACKUPPATH) + "/" + db + ".sql"
os.system(gzipcmd)
print("")
print("Sicherung erfolgreich beendet")
print("die Sicherung wurde in dem Ortner: \n" + ACKTUELLEBACKUPPATH + " \ngespeichert")
