import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

class legenda(QtWidgets.QWidget):
    def runlegenda(self):
        self.pic = QLabel()
        self.pic.setPixmap(QPixmap('Legenda_voor_map.png'))
        self.pic.show()
        app.exec_()

app = QtWidgets.QApplication(sys.argv)
legenda = legenda()