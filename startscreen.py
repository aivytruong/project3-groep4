import sys
from PyQt5 import QtWidgets


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


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
