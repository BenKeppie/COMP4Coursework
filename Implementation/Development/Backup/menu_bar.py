from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import *
import shutil


from profile_sql_connections import *

class Menu(QMenu):
    """A class to represent the menu bar for the profile"""
    def __init__(self,parent):
        super().__init__()
        self.parent=parent
        self.MenuBar=QMenuBar()
        #create actions

        self.change_picture=QAction("Change Picture",self)

        self.add_trick=QAction("Add Trick", self)

        self.add_skatepark=QAction("Add Skatepark",self)


        
        #create options
        self.profile_menu=self.MenuBar.addMenu("Profile")
        self.tricks_menu=self.MenuBar.addMenu("Tricks")
        self.skateparks_menu=self.MenuBar.addMenu("Skateparks")
        self.reviews_menu=self.MenuBar.addMenu("Reviews")
        

        #add actions to menu

        self.profile_menu.addAction(self.change_picture)

        self.tricks_menu.addAction(self.add_trick)

        self.skateparks_menu.addAction(self.add_skatepark)

        #connections

        self.change_picture.triggered.connect(self.change_picture_connection)
        self.add_trick.triggered.connect(self.add_trick_connection)
        self.add_skatepark.triggered.connect(self.add_skatepark_connection)

    def change_picture_connection(self):
        self.parent.tabs.setCurrentIndex(0)
        print("Find Picture")
        path=QFileDialog.getOpenFileName()
        
        if path=="":
            print("Picture not changed.")
        else:
            replace="\."
            path=path.replace("/",replace[0])
            destination=("{0}{1}{2}".format(os.getcwd(),replace[0],"ProfilePicture.jpeg"))
            print(destination)
            print(path)
            shutil.copy2(path,destination)
            self.connection=ProfileSQLConnections()
            self.connection.change_picture(destination)
            print(path)

    def add_trick_connection(self):
        self.parent.tabs.setCurrentIndex(1)
        self.parent.tricks_tab.add_trick_stacked()
        print("add Trick")

    def add_skatepark_connection(self):
        self.parent.tabs.setCurrentIndex(2)
        self.parent.skateparks_tab.unfreeze_add_trick()
        
        



