from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtWebEngineWidgets
import sys

class MyWebView(QtWebEngineWidgets.QWebEngineView):#KitWidgets.QWebView):
    def main(self):
        # menu = QtWebEngineWidgets.QWebEngineContextMenuData
        # self.actionCopyText = menu.addAction("Copy Text")
        # self.actionCopyText.triggered.connect(slotCopyText)
        # menu.exec_(self.mapToGlobal(self,QPoint=(event.x(),event.y())))

        webWindow.load(QtCore.QUrl("http://bl.ocks.org/d/986d3f8d3039c971c7b8cf6bd7135eb0"))
        webWindow.show()
        webWindow.size()
        app.exec_()

app = QtWidgets.QApplication(sys.argv)
webWindow = MyWebView()
#webWindow.main()