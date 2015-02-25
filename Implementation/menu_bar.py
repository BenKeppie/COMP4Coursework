from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import *

class Menu(QMenu):
    """A class to represent the menu bar for the profile"""
    def __init__(self):
        super().__init__()
        self.MenuBar=QMenuBar()
        #create actions
        self.change_name=QAction("Change Name",self)
        self.change_email=QAction("Change Email",self)
        self.change_picture=QAction("Change Picture",self)
        #create options
        self.profile_menu=self.MenuBar.addMenu("Profile")
        #add actions to menu
        self.profile_menu.addAction(self.change_name)
        self.profile_menu.addAction(self.change_email)
        self.profile_menu.addAction(self.change_picture)
        
        



