import sys
import os
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import *

class ProfilePicture(QGraphicsView):
    """This class provies a grpahics view for the profile picture"""
    def __init__(self):
        super().__init__()
        self.scene=QGraphicsScene()
        
        self.picture()
        
        
        

    def picture(self):
        print(os.getcwd())
        self.profile_picture=QPixmap(os.getcwd()+"\ProgramIcon.png")
        self.scene.addPixmap(self.profile_picture)
        self.setScene(self.scene)
