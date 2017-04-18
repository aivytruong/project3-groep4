import sys
from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
import Interactive_map_json
import DiagramRobberies


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Robberdam')

##Buttons:
        self.bmap = QPushButton('Map')
        self.bmap.setFixedSize(300, 70)
        self.bmap.setStyleSheet('font-size: 20pt')
        self.bdia = QPushButton('Diagram')
        self.bdia.setFixedSize(300, 70)
        self.bdia.setStyleSheet('font-size: 20pt')

##Layouts:
        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.bdia)
        v_box.addWidget(self.bmap)

        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        self.setLayout(h_box)

        self.showMaximized()

##Background:
        oImage = QImage("RobberdamLogo.png")
        sImage = oImage.scaled(QSize(1700, 1000))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
        self.setPalette(palette)

##Signals:
        self.bmap.clicked.connect(self.bmap_clk)
        self.bdia.clicked.connect(self.bdia_clk)

##Slots:
    def bdia_clk(self):
        DiagramRobberies.robGraph()

    def bmap_clk(self):
        Interactive_map_json.webWindow.main()


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())