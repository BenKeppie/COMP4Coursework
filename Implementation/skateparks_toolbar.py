import sys
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtSql import *


class DisplaySkateparksToolbar(QToolBar):
    """A class to represent the skateparks tab toolbar"""
    def __init__(self,parent):
        super().__init__()
        self.parent=parent

        self.add_skatepark=QAction("Add Skatepark",self)

        self.addAction(self.add_skatepark)

        self.add_skatepark.triggered.connect(self.add_skatepark_connection)

    def add_skatepark_connection(self):
        print("Add Skatepark")
        self.parent.view_add_skatepark()
