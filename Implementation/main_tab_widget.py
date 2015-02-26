from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import *

class CustomQTabWidget(QTabWidget):
    def __init__(self,parent):
        super().__init__()
        self.parent=parent

    def currentChanged(self):
        print("Change in tab")
