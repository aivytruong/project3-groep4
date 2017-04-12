import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QLabel, QCheckBox, QVBoxLayout, QHBoxLayout, QPushButton, QApplication, QWidget)
from PyQt5.QtGui import (QIcon, QPixmap)


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.dagdeel1 = QCheckBox('00:00 - 06:00')
        self.dagdeel2 = QCheckBox('06:00 - 12:00')
        self.dagdeel3 = QCheckBox('12:00 - 18:00')
        self.dagdeel4 = QCheckBox('18:00 - 00:00')
        self.btn_show = QPushButton('Show on map')
        self.lbl1 = QLabel('dagdeel 1: not checked')
        self.lbl2 = QLabel('dagdeel 2: not checked')
        self.lbl3 = QLabel('dagdeel 3: not checked')
        self.lbl4 = QLabel('dagdeel 4: not checked')

        vLayout = QVBoxLayout()
        vLayout.addWidget(self.dagdeel1)
        vLayout.addWidget(self.lbl1)
        vLayout.addWidget(self.dagdeel2)
        vLayout.addWidget(self.lbl2)
        vLayout.addWidget(self.dagdeel3)
        vLayout.addWidget(self.lbl3)
        vLayout.addWidget(self.dagdeel4)
        vLayout.addWidget(self.lbl4)
        vLayout.addWidget(self.btn_show)
        vLayout.addStretch()

        self.setLayout(vLayout)

        self.chk1 = self.dagdeel1.isChecked()
        self.chk2 = self.dagdeel2.isChecked()
        self.chk3 = self.dagdeel3.isChecked()
        self.chk4 = self.dagdeel4.isChecked()

        self.dagdeel1.clicked.connect(lambda: self.btn_clk1(self.dagdeel1.isChecked(), self.lbl1))
        self.dagdeel2.clicked.connect(lambda: self.btn_clk2(self.dagdeel2.isChecked(), self.lbl2))
        self.dagdeel3.clicked.connect(lambda: self.btn_clk3(self.dagdeel3.isChecked(), self.lbl3))
        self.dagdeel4.clicked.connect(lambda: self.btn_clk4(self.dagdeel4.isChecked(), self.lbl4))

#        self.btn_show.clicked.connect(self.btn_show_clk, self.chk1, self.chk2, self.chk3, self.chk4, self.lbl1, self.lbl2, self.lbl3, self.lbl4)

        self.show()

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
a_window = Window()
sys.exit(app.exec_())