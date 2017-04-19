import matplotlib.pyplot as plt
import sqlite3

connect = sqlite3.connect('test.db')
c = connect.cursor()

#functions for picking up the values from our database

def january():
    c.execute("SELECT COUNT(*) FROM Straatroven s, RET r WHERE r.postcode = s.postcode AND s.maand = 'jan'")
    rows = c.fetchall()
    for r in rows:
        return (int(r[0]))

def february():
    c.execute("SELECT COUNT(*) FROM Straatroven s, RET r WHERE r.postcode = s.postcode AND s.maand = 'feb'")
    rows = c.fetchall()
    for r in rows:
        return (int(r[0]))

def march():
    c.execute("SELECT COUNT(*) FROM Straatroven s, RET r WHERE r.postcode = s.postcode AND s.maand = 'mar'")
    rows = c.fetchall()
    for r in rows:
        return (int(r[0]))

def april():
    c.execute("SELECT COUNT(*) FROM Straatroven s, RET r WHERE r.postcode = s.postcode AND s.maand = 'apr'")
    rows = c.fetchall()
    for r in rows:
        return (int(r[0]))

def may():
    c.execute("SELECT COUNT(*) FROM Straatroven s, RET r WHERE r.postcode = s.postcode AND s.maand = 'may'")
    rows = c.fetchall()
    for r in rows:
        return (int(r[0]))

def june():
    c.execute("SELECT COUNT(*) FROM Straatroven s, RET r WHERE r.postcode = s.postcode AND s.maand = 'jun'")
    rows = c.fetchall()
    for r in rows:
        return (int(r[0]))

def july():
    c.execute("SELECT COUNT(*) FROM Straatroven s, RET r WHERE r.postcode = s.postcode AND s.maand = 'jul'")
    rows = c.fetchall()
    for r in rows:
        return (int(r[0]))

def august():
    c.execute("SELECT COUNT(*) FROM Straatroven s, RET r WHERE r.postcode = s.postcode AND s.maand = 'aug'")
    rows = c.fetchall()
    for r in rows:
        return (int(r[0]))

def september():
    c.execute("SELECT COUNT(*) FROM Straatroven s, RET r WHERE r.postcode = s.postcode AND s.maand = 'sep'")
    rows = c.fetchall()
    for r in rows:
        return (int(r[0]))

def october():
    c.execute("SELECT COUNT(*) FROM Straatroven s, RET r WHERE r.postcode = s.postcode AND s.maand = 'oct'")
    rows = c.fetchall()
    for r in rows:
        return (int(r[0]))

def november():
    c.execute("SELECT COUNT(*) FROM Straatroven s, RET r WHERE r.postcode = s.postcode AND s.maand = 'nov'")
    rows = c.fetchall()
    for r in rows:
        return (int(r[0]))

def december():
    c.execute("SELECT COUNT(*) FROM Straatroven s, RET r WHERE r.postcode = s.postcode AND s.maand = 'dec'")
    rows = c.fetchall()
    for r in rows:
        return (int(r[0]))

#adding values

x = [2]
y = january()

x1 = [4]
y1 = february()

x2 = [6]
y2 = march()

x3 = [8]
y3 = april()

x4 = [10]
y4 = may()

x5 = [12]
y5 = june()

x6 = [14]
y6 = july()

x7 = [16]
y7 = august()

x8 = [18]
y8 = september()

x9 = [20]
y9 = october()

x10 = [22]
y10 = november()

x11 = [24]
y11 = december()

plt.bar(x,y)
plt.bar(x1,y1)
plt.bar(x2,y2)
plt.bar(x3,y3)
plt.bar(x4,y4)
plt.bar(x5,y5)
plt.bar(x6,y6)
plt.bar(x7,y7)
plt.bar(x8,y8)
plt.bar(x9,y9)
plt.bar(x10,y10)
plt.bar(x11,y11)


#legend with 12 months
plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], loc='upper right')
plt.grid()

plt.xlabel('Months')
plt.ylabel('Amount of robberies')
plt.title('Robberies near metro stops by each month')
plt.legend()
plt.show()

