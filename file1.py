import sqlite3

connect = sqlite3.connect('test.db')

c = connect.cursor()

def SelectDB():
    c.execute("SELECT R.name, R.latitude, R.longitude, S.Straat FROM Straatroven S, RET R WHERE S.leeftijdslachtoffer = 18-24 AND S.postcode = R.postcode AND S.dagdeel = '00:00-05:59' AND S.Opgelost = 'J' AND S.pogingtotmoord = 'N'")
#    data = c.fetchall()
    #row so data prints in rows
    for row in c.fetchall():
        print(row)
#    print(data)

SelectDB()
