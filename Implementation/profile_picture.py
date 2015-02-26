import sys
import os
import sqlite3

from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import *
from profile_sql_connections import *

class ProfilePicture(QGraphicsView):
    """This class provies a grpahics view for the profile picture"""
    def __init__(self):
        super().__init__()
        self.PictureSQLConnection=ProfileSQLConnections()
        self.scene=QGraphicsScene()
        
        self.picture()
        
        
        

    def picture(self):
        self.FilePath=self.PictureSQLConnection.get_picture()
        Picture=QPixmap("{0}".format(self.FilePath))
        Picture=Picture.scaled(QSize(160,160))
        
        self.profile_picture=(Picture)
        self.scene.addPixmap(self.profile_picture)

        print(self.scene.items())

        


        self.setScene(self.scene)
        
