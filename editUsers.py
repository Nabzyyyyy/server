import sqlite3
import datetime
import json
import database as db
import connections as con

def createUpdate(plate, action):
    request = {}
    
    if action == 'update': 
        request['updateAccess'] = db.userInfo(plate)
    elif action == 'delete':
        request['removeAccess'] = db.userInfo(plate)
    else:
        request['addAccess'] = db.userInfo(plate)

    return request
        
def updateAccess():
    action = 'update'
    plate = raw_input("What is the user's license plate that you would like to update? : ")

    invalid = True
    while(invalid):
        access = raw_input("What would like the access for plate " + plate + " to be? (t/f) : ")

        if access == 't':
            db.updateUser(plate, True)
            con.updateDB(createUpdate(plate, action))
            invalid = False
        elif access == 'f':
            db.updateUser(plate, False)
            con.updateDB(createUpdate(plate, action))
            invalid = False
        else:
            print 'Please input only "t" or "f"'
    
    

#removes user from Users database
def deleteUser():
    action = 'delete'
    #print "What is the user's license plate that you wish to delete?"
    plate = raw_input("What is the user's license plate that you wish to delete? : ")
    
    #calls function to remove user
    request = createUpdate(plate, action)
    db.removeUser(plate)
    #sends delete update to gate
    con.updateDB(request)

# asks user for information and adds a table entry for that user
def createUser():
    action = 'create'
    incorrect = True
    request = {}
    user = {}
    plate = ''
    #loops if the user didn't enter information correctly
    while(incorrect):
    
        print 'Add user information for entry to add: '
        #print 'Name: '
        user['name'] = raw_input('Name: ')

        #print 'Plate: '
        user['plate'] = raw_input('Plate: ')
        
        #print 'Make: '
        user['make'] = raw_input('Make: ')

        #print 'Model: '
        user['model'] = raw_input('Model: ')

        dt = datetime.datetime.now()
        dt = dt.replace(microsecond=0)
        user['timestamp'] = str(dt)

        invalid = True
        while(invalid):
            #print 'Access: Is the user permitted into the lot (y/n)?\n'
            acc = raw_input('Access: Is the user permitted into the lot? (y/n) : ')
        
            if acc == 'y':
                user['access'] = True
                invalid = False
            elif acc == 'n':
                user['access'] = False
                invalid = False
            else:   
                print 'Invalid input, please input only a "y" or "n" \n'

            invalid = True
            
            print ''
            print 'Name  : ', user['name']
            print 'Plate : ', user['plate']
            print 'Make  : ', user['make']
            print 'Model : ', user['model']
            print 'Access: ', user['access'], '\n'
            
            while(invalid):
                #print 'Is the above information correct (y/n)? \n'
                cor = raw_input('Is the above information correct? (y/n) : ')
                if cor == 'y':
                    invalid = False
                    incorrect = False
                elif cor == 'n':
                    invalid = False
                    incorrect = True
                    print 'Ok. Re-enter the user information.'
                else:
                    invalid = True
                    print 'Invalid input, please input only a "y" or "n" \n'
                    
    plate = user['plate']
    request ['user'] = user
    request['end'] = True
    db.addUser(request['user'])
    con.updateDB(createUpdate(plate, action))

invalid = True

while(invalid):
    inp = raw_input('Would you like to add, remove, or update a user? (Enter add / remove  / update) : ')

    if inp == 'add':
        createUser()
        invalid = False
    elif inp == 'remove':
        deleteUser()
        invalid = False
    elif inp == 'update':
        updateAccess()
        invalid = False
    else:
        print ('Please input only "add", "remove", "update".')



#print 'Id, Plate, Make, Model, Timestamp, Access'
#for row in cur:
#    show = ''
#    i = 1
#    for col in row:
##        if i != len(row):
 #           show += str(col) + ', '
 #           i += 1
 #       else:
 ##           show += str(col)
  #  print show

