import database as db
import socket import *
import json

HOST = '192.168.43.48'
PORT = 50007
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

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
