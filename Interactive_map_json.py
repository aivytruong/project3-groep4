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

        webWindow.load(QtCore.QUrl(
            "http://geojson.io/#id=gist:anonymous/be7878c28a6a466694e22a3a2942f4ec&map=2/4.456415/51.90766"))
        webWindow.show()
        webWindow.size()
        app.exec_()

app = QtWidgets.QApplication(sys.argv)
webWindow = MyWebView()
#webWindow.main()