import matplotlib.pyplot as plt
import sqlite3

connect = sqlite3.connect('test.db')
c = connect.cursor()

# = ("SELECT count (*) FROM Straatroven WHERE dagdeel = '00:00-05:59' AND leeftijdslachtoffer = '18-24'")
#data1 = ("SELECT count (*) FROM Straatroven WHERE dagdeel = '06:00-11:59' AND leeftijdslachtoffer = '18-24'")
#data2 = ("SELECT count (*) FROM Straatroven WHERE dagdeel = '12:00-17:59' AND leeftijdslachtoffer = '18-24'")
#data3= ("SELECT count (*) FROM Straatroven WHERE dagdeel = '18:00-23:59' AND leeftijdslachtoffer = '18-24'")

def listfix():
    c = "SELECT COUNT(*) FROM Straatroven WHERE leeftijdslachtoffer = '18-24' GROUP BY dagdeel"
    args = [[0]]
    c.execute(c, args)
    data = c.fetchall()
    for dagdeel in data:
        one = data[0]
        # two = dagdeel[1]
        # three = dagdeel[2]
        # four = dagdeel[3]
        print(data)

listfix()
c.close
connect.close()

# x = [2]
# y = yo

#x1 = [4]
#y1 = data1

#x2 = [6]
#y2 = data2

#x3 = [8]
#y3 = data3

# plt.bar(x,y)
# # plt.bar(x1,y1)
# # plt.bar(x2,y2)
# # plt.bar(x3,y3)
#
#
# plt.xlabel('dagdeel')
# plt.ylabel('aantal')
# plt.title('Straatroven per dagdeel \n Leeftijdsgroep 18-24 jaar ')
# plt.legend()
# plt.show()
