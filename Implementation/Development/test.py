import sys
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout=QHBoxLayout()
        self.set_layout()
        self.hide()

    def hide(self):
        self.ProgressBar.hide()
        self.ProgressBar.show()



    def set_layout(self):
        self.ProgressBar=QProgressBar()
        self.ProgressBar.setValue(99)
        #self.layout.addWidget(self.ProgressBar)
        self.setCentralWidget(self.ProgressBar)

if __name__=="__main__":
    application=QApplication(sys.argv)
    window=MainWindow()
    
    window.show()
    window.raise_()
    application.exec_()
    print()
    
        
                            
        
