from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtWebEngineWidgets
import sys


class MyWebView(QtWebEngineWidgets.QWebEngineView):#KitWidgets.QWebView) werkt niet idk is van pyqt4
    def contextMenuEvent(self, event):
        menu = QtWebEngineWidgets.QWebEngineContextMenuData
        # self.actionCopyText = menu.addAction("Copy Text")
        # self.actionCopyText.triggered.connect(slotCopyText)

        # menu.exec_(self.mapToGlobal(self,QPoint=(event.x(),event.y())))


def main():#Main functie Maar Akin heeft dit in een andere class gezet
    app = QtWidgets.QApplication(sys.argv)
    webWindow = MyWebView()
    webWindow.load(QtCore.QUrl("http://bl.ocks.org/d/c63297c8dd8f7beb97db807deea24df2"))
    webWindow.show()
    webWindow.size()
    return app.exec_()


main()
