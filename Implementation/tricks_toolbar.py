import sys
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtSql import *


class DisplayTricksToolbar(QToolBar):
    def __init__(self, parent):
        super().__init__()
        self.parent=parent
        
        self.add_trick=QAction("Add Trick",self)
        
        self.addAction(self.add_trick)

            #connections
        self.add_trick.triggered.connect(self.add_trick_connection)


    def add_trick_connection(self):
        self.parent.add_trick_stacked()
        
