import sys
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtSql import *

class DisplayProfileToolbar(QToolBar):
    def __init__(self):
        super().__init__()
        
        self.change_name=QAction("Change Name",self)
        self.change_email=QAction("Change Email",self)
        self.change_picture=QAction("Change Picture",self)
        
        self.addAction(self.change_name)
        self.addAction(self.change_email)
        self.addAction(self.change_picture)

        
        
