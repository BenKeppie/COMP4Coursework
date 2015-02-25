import sys
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtSql import *

from main_window import *
from profile_toolbar import *
from profile_picture import *
from profile_sql_connections import *


class DisplayProfileWidget(QWidget):
    """A class to display the model and represent a view on the profile tab"""

    def __init__(self,parent):
        super().__init__()
        self.parent=parent

        
        self.ProfileSQLConnections=ProfileSQLConnections()
        self.ToolBarWidgetLayout=QVBoxLayout()
        self.LayoutWidget=QWidget()

        self.HBoxLayout=QHBoxLayout()
        self.LeftVBoxLayout=QVBoxLayout()
        self.LeftHBoxLayout=QHBoxLayout()
        self.MiddleVBoxLayout=QVBoxLayout()
        self.RightVBoxLayout=QVBoxLayout()
        

        self.display_profile_layout()
        self.display_profile_toolbar_widget()
        self.setLayout(self.ToolBarWidgetLayout)
        self.model=None

        self.edit_button.clicked.connect(self.edit_button_clicked)
        self.save_button.clicked.connect(self.save_button_clicked)
        
        
        
       
        

    def display_profile_layout(self):
        if not hasattr(self,"profile_picture"):
            self.profile_picture=ProfilePicture()
            self.profile_picture.setHorizontalScrollBarPolicy(1)
            self.profile_picture.setVerticalScrollBarPolicy(1)
            self.profile_picture.setMinimumSize(QSize(160,160))
            self.profile_picture.setMaximumSize(QSize(160,160))
            self.LeftVBoxLayout.addWidget(self.profile_picture)
        if not hasattr(self,"edit_button"):
            self.edit_button=QPushButton("Edit")
            self.LeftHBoxLayout.addWidget(self.edit_button)
        if not hasattr(self,"save_button"):
            self.save_button=QPushButton("Save")
            self.LeftHBoxLayout.addWidget(self.save_button)
        self.LeftVBoxLayout.addLayout(self.LeftHBoxLayout)
        self.HBoxLayout.addLayout(self.LeftVBoxLayout)

            


        if not hasattr(self,"first_name"):
            self.FirstName=self.ProfileSQLConnections.get_first_name()
            
            self.first_name=QLineEdit(self.FirstName[0])
            self.first_name.setReadOnly(True)
            self.MiddleVBoxLayout.addWidget(self.first_name)
        if not hasattr(self,"last_name"):
            self.LastName=self.ProfileSQLConnections.get_last_name()
            
            self.last_name=QLineEdit(self.LastName[0])
            self.last_name.setReadOnly(True)
            self.MiddleVBoxLayout.addWidget(self.last_name)
        if not hasattr(self,"user_email"):
            self.UserEmail=self.ProfileSQLConnections.get_email()
            self.user_email=QLineEdit("{0}".format(self.UserEmail[0]))
            self.user_email.setReadOnly(True)
            self.MiddleVBoxLayout.addWidget(self.user_email)

        self.HBoxLayout.addLayout(self.MiddleVBoxLayout)

       
        if not hasattr(self,"recent_tricks"):
            self.recent_tricks=QLabel("Recently Completed Tricks")
            self.RightVBoxLayout.addWidget(self.recent_tricks)
        if not hasattr(self,"recent_tricks_list"):
            self.recent_tricks_list=QListWidget()
            #self.recent_tricks_list.addItem("Ollie")
            self.RightVBoxLayout.addWidget(self.recent_tricks_list)

        self.HBoxLayout.addLayout(self.RightVBoxLayout)
        self.LayoutWidget.setLayout(self.HBoxLayout)
        
        

    def display_profile_toolbar_widget(self):
        if not hasattr(self,"profile_tool_bar"):
            self.profile_tool_bar=DisplayProfileToolbar()
            self.profile_tool_bar.changedPicture.connect(self.refresh_picture)
            self.ToolBarWidgetLayout.addWidget(self.profile_tool_bar)
        self.ToolBarWidgetLayout.addWidget(self.LayoutWidget)

    def refresh_picture(self):
        print("Refresh Picture")
        self.profile_picture.picture()

    def edit_button_clicked(self):
        self.change_name_edit()
        self.change_email_edit()

    def change_name_edit(self):
        self.first_name.setReadOnly(False)
        self.last_name.setReadOnly(False)

    def change_email_edit(self):
        self.user_email.setReadOnly(False)
        

    def save_button_clicked(self):
        self.ProfileSQLConnections.change_name(self.first_name.text(),self.last_name.text())
        self.ProfileSQLConnections.change_email(self.user_email.text())
        self.first_name.setReadOnly(True)
        self.last_name.setReadOnly(True)
        self.user_email.setReadOnly(True)
                                         



        
        
        


       
        
        
        
    
