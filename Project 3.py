import sys
from PyQt5 import QtWidgets

yearList = ['2006', '2007', '2008', '2009', '2010', '2011']
class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.b = QtWidgets.QPushButton('COMPARE')
        self.b_print = QtWidgets.QPushButton('print')
        self.yearTitle = QtWidgets.QLabel('Pick 2 years:')
        self.l1 = QtWidgets.QLabel('Not clicked.')
        self.comboYear = QtWidgets.QComboBox()
        self.comboYear2 = QtWidgets.QComboBox()

        self.comboYear.addItems(sorted(yearList))
        self.comboYear2.addItems(sorted(yearList))

        yearTitle_box = QtWidgets.QHBoxLayout()
        yearTitle_box.addStretch()
        yearTitle_box.addWidget(self.yearTitle)
        yearTitle_box.addStretch()
        year_box = QtWidgets.QHBoxLayout()
        year_box.addStretch()
        year_box.addWidget(self.comboYear)
        year_box.addWidget(self.comboYear2)
        year_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l1)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(yearTitle_box)
        v_box.addLayout(year_box)
        v_box.addWidget(self.b)
        v_box.addWidget(self.b_print)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle('Project 3')

        self.b.clicked.connect(self.btn_click)
        self.b_print.clicked.connect(self.print_click)

        self.show()

    def btn_click(self):
        self.l1.setText('Clicked!')

    def print_click(self):
        yearIndex = self.comboYear.currentIndex()
        yearIndex2 = self.comboYear2.currentIndex()
        print(yearIndex)
        print(yearIndex2)

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())