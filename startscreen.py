import sys
from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
import pygame
import Interactive_map_json
import MonthDiagram
import DaypartDiagram
import Legenda
import postcodes

##Background music:
musicfile = 'please dont.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(musicfile)
pygame.mixer.music.play()

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Robberdam')

##Buttons:
        self.bmap = QPushButton('Map')
        self.bmap.setFixedSize(290, 60)
        self.bmap.setStyleSheet('font-size: 20pt')
        self.bdim = QPushButton('Months')
        self.bdim.setFixedSize(290, 60)
        self.bdim.setStyleSheet('font-size: 20pt')
        self.bleg = QPushButton('Legend')
        self.bleg.setFixedSize(290, 60)
        self.bleg.setStyleSheet('font-size: 20pt')
        self.bdid = QPushButton('Dayparts')
        self.bdid.setFixedSize(290, 60)
        self.bdid.setStyleSheet('font-size: 20pt')
        self.bdin = QPushButton('Near metrostations')
        self.bdin.setFixedSize(290, 60)
        self.bdin.setStyleSheet('font-size: 20pt')

##Layouts:
        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.bdin)
        h_box.addWidget(self.bdid)
        h_box.addWidget(self.bdim)
        h_box.addWidget(self.bmap)
        h_box.addWidget(self.bleg)
        h_box.addStretch()

        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h_box)
        self.setLayout(v_box)

        self.showMaximized()

##Background:
        oImage = QImage("RobberdamLogo.png")
        sImage = oImage.scaled(QSize(1700, 1000))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
        self.setPalette(palette)

##Signals:
        self.bmap.clicked.connect(self.bmap_clk)
        self.bdim.clicked.connect(self.bdia_clk)
        self.bleg.clicked.connect(self.bleg_clk)
        self.bdid.clicked.connect(self.bdid_clk)
        self.bdin.clicked.connect(self.bdin_clk)

##Slots:
    def bdia_clk(self):
        MonthDiagram.robGraph()

    def bmap_clk(self):
        Interactive_map_json.webWindow.main()

    def bleg_clk(self):
        Legenda.legenda.runlegenda()

    def bdid_clk(self):
        DaypartDiagram.daygraph()

    def bdin_clk(self):
        postcodes.codegraph()


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())