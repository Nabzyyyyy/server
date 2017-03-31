import database as db
import socket
import json

HOST = '192.168.43.48'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def openConnection():
    s.connect((HOST, PORT))

def closeConnection():
    s.close()

def updateDB(plate)
    db.userInfo(plate)
    openConnection()
    s.sendall(json.dumps(request))
    response = s.recv(1024)
    print 'Update sent to gate successfully'
    closeConnection()
