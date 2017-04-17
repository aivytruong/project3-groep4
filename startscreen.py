import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush



class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.b = QtWidgets.QPushButton('continue')
        self.b.setFixedSize(300, 100)
        self.b.setStyleSheet('font-size: 20pt')



        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.b)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle('Robberdam')


        self.showMaximized()

        oImage = QImage("RobberdamLogo.png")
        sImage = oImage.scaled(QSize(1700, 1000))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
        self.setPalette(palette)



app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
