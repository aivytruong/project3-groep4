import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QLabel, QCheckBox, QVBoxLayout, QHBoxLayout, QPushButton, QApplication, QWidget
import DiagramRobberies
import Interactive_map_json


class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
##Legend:
        self.legendlbl = QLabel('Legenda')
        self.dgd1leg = QLabel('00:00 - 06:00')
        self.dgd2leg = QLabel('06:00 - 12:00')
        self.dgd3leg = QLabel('12:00 - 18:00')
        self.dgd4leg = QLabel('18:00 - 00:00')

##Buttons:
        self.pltbtn = QPushButton('Straatroven 2011-2012')
        self.mapbtn = QPushButton('Show map')

##Checkboxes:
        self.dagdeel1 = QCheckBox('00:00 - 06:00')
        self.dagdeel2 = QCheckBox('06:00 - 12:00')
        self.dagdeel3 = QCheckBox('12:00 - 18:00')
        self.dagdeel4 = QCheckBox('18:00 - 00:00')

##Feedback testlabels:
        self.lbl1 = QLabel('dagdeel 1: not checked')
        self.lbl2 = QLabel('dagdeel 2: not checked')
        self.lbl3 = QLabel('dagdeel 3: not checked')
        self.lbl4 = QLabel('dagdeel 4: not checked')

##Colors:
        yellow = QtGui.QPalette()
        yellow.setColor(QtGui.QPalette.Foreground, QtGui.QColor(204,204,0))
        orange = QtGui.QPalette()
        orange.setColor(QtGui.QPalette.Foreground, QtGui.QColor(255,165,0))
        red = QtGui.QPalette()
        red.setColor(QtGui.QPalette.Foreground, QtGui.QColor(255, 0, 0))
        purple = QtGui.QPalette()
        purple.setColor(QtGui.QPalette.Foreground, QtGui.QColor(128,0,128))

        self.dagdeel1.setPalette(yellow)
        self.dagdeel2.setPalette(orange)
        self.dagdeel3.setPalette(red)
        self.dagdeel4.setPalette(purple)

##Checkbox layout:
        vLayout = QVBoxLayout()
        vLayout.addStretch()
        vLayout.addWidget(self.dagdeel1)
        vLayout.addWidget(self.lbl1)
        vLayout.addWidget(self.dagdeel2)
        vLayout.addWidget(self.lbl2)
        vLayout.addWidget(self.dagdeel3)
        vLayout.addWidget(self.lbl3)
        vLayout.addWidget(self.dagdeel4)
        vLayout.addWidget(self.lbl4)
        vLayout.addWidget(self.mapbtn)
        vLayout.addStretch()
        vLayout.addWidget(self.pltbtn)
        vLayout.addWidget(self.legendlbl)
        vLayout.addWidget(self.dgd1leg)
        vLayout.addWidget(self.dgd2leg)
        vLayout.addWidget(self.dgd3leg)
        vLayout.addWidget(self.dgd4leg)



##Final layout:
        hLayout = QHBoxLayout()
        hLayout.addLayout(vLayout)
        hLayout.addStretch()
        self.setLayout(hLayout)

##Checkbox methods:
        self.chk1 = self.dagdeel1.isChecked()
        self.chk2 = self.dagdeel2.isChecked()
        self.chk3 = self.dagdeel3.isChecked()
        self.chk4 = self.dagdeel4.isChecked()

        self.dagdeel1.clicked.connect(lambda: self.btn_clk1(self.dagdeel1.isChecked(), self.lbl1))
        self.dagdeel2.clicked.connect(lambda: self.btn_clk2(self.dagdeel2.isChecked(), self.lbl2))
        self.dagdeel3.clicked.connect(lambda: self.btn_clk3(self.dagdeel3.isChecked(), self.lbl3))
        self.dagdeel4.clicked.connect(lambda: self.btn_clk4(self.dagdeel4.isChecked(), self.lbl4))

        self.pltbtn.clicked.connect(self.plot)
        self.mapbtn.clicked.connect(self.map_clk)

        self.showMaximized()

    def map_clk(self):
        Interactive_map_json.main()

    def plot(self):
        DiagramRobberies.robGraph()

    def btn_clk1(self, chk1, lbl1):
        if chk1:
            lbl1.setText('dagdeel 1: checked')
        else:
            lbl1.setText('dagdeel 1: not checked')
    def btn_clk2(self, chk2, lbl2):
        if chk2:
            lbl2.setText('dagdeel 2: checked')
        else:
            lbl2.setText('dagdeel 2: not checked')
    def btn_clk3(self, chk3, lbl3):
        if chk3:
            lbl3.setText('dagdeel 3: checked')
        else:
            lbl3.setText('dagdeel 3: not checked')
    def btn_clk4(self, chk4, lbl4):
        if chk4:
            lbl4.setText('dagdeel 4: checked')
        else:
            lbl4.setText('dagdeel 4: not checked')


app = QApplication(sys.argv)
a_window = MainWindow()
sys.exit(app.exec_())