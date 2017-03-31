import sqlite3

conn = sqlite3.connect('pass.db')

cur = conn.execute('SELECT * FROM Logs')

print 'Id, Plate, Timestamp, Access'
for row in cur:
    show = ''
    i = 1
    for col in row:
        if i != len(row):
            show += str(col) + ', '
            i += 1
        else:
            show += str(col)
    print show

conn.close()
