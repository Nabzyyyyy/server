import sqlite3

def connect():
    return sqlite3.connect('pass.db', detect_types = sqlite3.PARSE_DECLTYPES)

def exists(table):
    conn = connect()
    cur = conn.execute('''
        SELECT name
        FROM sqlite_master
        WHERE type='table' AND name=?''', (table,))
    return cur.fetchone() != None
    

def createLogTable():
    conn = connect()
    conn.execute('''
        CREATE TABLE Logs
        (
            Id          INTEGER PRIMARY KEY AUTOINCREMENT,
            Plate       TEXT                NOT NULL,
            Timestamp   TEXT                NOT NULL,
            Access      BIT                 NOT NULL
        );''')

def createUserTable():
    conn = connect()
    conn.execute('''
        CREATE TABLE Users
        (
            Id          INTEGER PRIMARY KEY AUTOINCREMENT,
            Name        TEXT                NOT NULL,
            Plate       TEXT    UNIQUE      NOT NULL,
            Make        TEXT                NOT NULL,
            Model       TEXT                NOT NULL,
            Timestamp   TEXT                NOT NULL,
            Access      BIT                 NOT NULL
        );''')

def addLog(log):
    if not exists('Logs'):
        createLogTable()

    conn = connect()
    cur = conn.execute('''
        INSERT INTO Logs
        (Plate, Timestamp, Access)
        VALUES
        (:plate, :timestamp, :access)
        ''', log)
    conn.commit()
    print 'Logs added: ', cur.rowcount
    return cur.rowcount
    

def addUser(user):
    if not exists('Users'):
        createUserTable()

    conn = connect()
    cur = conn.execute('''
        INSERT INTO Users
        (Name, Plate, Make, Model, Timestamp, Access)
        VALUES
        (:name, :plate, :make, :model, :timestamp, :access)
        ''', user)
    conn.commit()
    print 'User added'
    return cur.rowcount

def removeUser(plate):
    if not exists('Users'):
        createUserTable()
        print 'There are no users to delete'

    conn = connect()

    #gets name of user to delete
    cursor = conn.execute('SELECT name FROM Users WHERE Plate = ?', (plate,) )
    for row in cursor:
        name = row[0]

    #deletes user
    cur = conn.execute('DELETE FROM Users WHERE Plate = ?', (plate,) )
    conn.commit()
    
    #displays which user was deleted, if any
    if cur.rowcount > 0:
        print 'User ',name, ' deleted.'
    else:
        print 'User with requested license plate does not exist'
    

def updateUser(plate, access):
    if not exists('Users'):
        createUserTable()
        print 'There are no users to update'

    conn = connect()

    #gets name of user to update
    cursor = conn.execute('SELECT name FROM Users WHERE Plate = ?', (plate,) )
    for row in cursor:
        name = row[0]

    #deletes user
    cur = conn.execute('UPDATE Users SET access = ? WHERE Plate = ?', (access, plate,) )
    conn.commit()
    
    #displays which user was deleted, if any
    if cur.rowcount > 0:
        print 'User ',name, "'s access set to ", access, '.'
    else:
        print 'User with requested license plate does not exist.'

def userInfo(plate):
    
    if not exists('Users'):
        print 'There are no users.'

    conn = connect()
    
    cursor  = conn.execute('SELECT * FROM Users WHERE Plate = ?', (plate,) )
    row = cursor.fetchone()
    
    log = {}
    log['id'] = row[0]
    log['name'] = row[1]
    log['plate'] = row[2]
    log['make'] =  row [3]
    log['model'] = row[4]
    log ['timestamp'] = row[5]
    log['access'] = row[6]
    return log
    
    
