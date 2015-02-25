import sys
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout=QHBoxLayout()
        self.widget=QWidget()
        self.set_layout()
        self.remove_test2()

    def remove_test2(self):
        #self.layout.removeWidget(self.Test2)
        self.layout.removeWidget(self.Test)
        self.Test.deleteLater()
        self.Test=None

    def set_layout(self):
        self.Test=QPushButton("Test1")
        self.layout.addWidget(self.Test)
        self.Test2=QPushButton("Test2")
        self.layout.addWidget(self.Test2)
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

if __name__=="__main__":
    application=QApplication(sys.argv)
    window=MainWindow()
    
    window.show()
    window.raise_()
    application.exec_()
    print()
    
        
                            
        
