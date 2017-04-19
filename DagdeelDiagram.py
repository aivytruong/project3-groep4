import matplotlib.pyplot as plt
import sqlite3

connect = sqlite3.connect('test.db')
c = connect.cursor()


def dagdeel1(): #function for picking up the first value from our database
    c.execute ("SELECT count (*) FROM Straatroven WHERE dagdeel = '00:00-05:59' AND leeftijdslachtoffer = '18-24'")
    rows = c.fetchall()
    for r in rows:
        return (int(r[0]))


def dagdeel2(): #function for picking up the second value from our database
    c.execute ("SELECT count (*) FROM Straatroven WHERE dagdeel = '06:00-11:59' AND leeftijdslachtoffer = '18-24'")
    rows = c.fetchall()
    for r in rows:
        return (int(r[0]))

def dagdeel3(): #function for picking up the third value from our database
    c.execute ("SELECT count (*) FROM Straatroven WHERE dagdeel = '12:00-17:59' AND leeftijdslachtoffer = '18-24'")
    rows = c.fetchall()
    for r in rows:
        return (int(r[0]))

def dagdeel4(): #function for picking up the fourth value from our database
    c.execute ("SELECT count (*) FROM Straatroven WHERE dagdeel = '18:00-23:59' AND leeftijdslachtoffer = '18-24'")
    rows = c.fetchall()
    for r in rows:
        return (int(r[0]))


x = [2]
y = dagdeel1() #adding values

x1 = [4]
y1 = dagdeel2() #adding values

x2 = [6]
y2 = dagdeel3() #adding values

x3 = [8]
y3 = dagdeel4() #adding values

plt.bar(x,y)
plt.bar(x1,y1)
plt.bar(x2,y2)
plt.bar(x3,y3)


plt.legend(['00:00-05:59', '06:00-11:59', '12:00-17:59', '18:00-23:59'], loc='upper left') #legend with 4 values (the 4 daytimes)
plt.grid()

plt.xlabel('time of day')
plt.ylabel('amount of roberries')
plt.title('robberies by times of the day \n age group 18-24 years')
plt.legend()
plt.show()

