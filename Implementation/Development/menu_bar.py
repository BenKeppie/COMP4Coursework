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

        self.add_review=QAction("Add Review",self)

        self.contact_support=QAction("Contact Support",self)


        
        #create options
        self.profile_menu=self.MenuBar.addMenu("Profile")
        self.tricks_menu=self.MenuBar.addMenu("Tricks")
        self.skateparks_menu=self.MenuBar.addMenu("Skateparks")
        self.reviews_menu=self.MenuBar.addMenu("Reviews")
        self.support_menu=self.MenuBar.addMenu("Support")
        

        #add actions to menu

        self.profile_menu.addAction(self.change_picture)

        self.tricks_menu.addAction(self.add_trick)

        self.skateparks_menu.addAction(self.add_skatepark)

        self.reviews_menu.addAction(self.add_review)

        self.support_menu.addAction(self.contact_support)

        #connections

        self.change_picture.triggered.connect(self.change_picture_connection)
        self.add_trick.triggered.connect(self.add_trick_connection)
        self.add_skatepark.triggered.connect(self.add_skatepark_connection)
        self.add_review.triggered.connect(self.add_review_connection)
        self.contact_support.triggered.connect(self.contact_support_connection)


    def contact_support_connection(self):
        self.parent.tabs.setCurrentIndex(4)
        print("Contact Support")

    def add_review_connection(self):
        self.parent.tabs.setCurrentIndex(3)
        self.parent.reviews_tab.add_review_stacked()
        print("add Trick")


    def change_picture_connection(self):
        self.parent.StatusBar.showMessage("Changing Profile Picture...")
        self.parent.tabs.setCurrentIndex(0)
        print("Find Picture")
        path=QFileDialog.getOpenFileName()
        
        if path=="":
            print("Picture not changed.")
            self.parent.StatusBar.showMessage("Profile Picture Not Changed.",2000)
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
            self.parent.StatusBar.showMessage("Profile Picture Successfully Changed.",2000)

    def add_trick_connection(self):
        self.parent.tabs.setCurrentIndex(1)
        self.parent.tricks_tab.add_trick_stacked()
        print("add Trick")

    def add_skatepark_connection(self):
        self.parent.tabs.setCurrentIndex(2)
        self.parent.skateparks_tab.view_add_skatepark()
        
        



