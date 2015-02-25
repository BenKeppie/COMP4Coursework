import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *



class MainWindow(QMainWindow):
    """The main window for my application"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Google Maps PyQt")
        self.create_layout()

    def create_layout(self):
        self.label=QWebView()
        self.label.load(QUrl("http://www.google.com/maps"))
        self.label.show()

        self.layout=QVBoxLayout()
        self.layout.addWidget(self.label)

        self.widget=QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        

                                    




if __name__ == "__main__":
    application=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    window.raise_()
    application.exec_()
