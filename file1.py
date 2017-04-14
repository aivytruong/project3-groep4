import sqlite3

connect = sqlite3.connect('test.db')

c = connect.cursor()

def SelectDB():
    c.execute('SELECT * FROM Straatroven')
    data = c.fetchall()
    print(data)

SelectDB()
