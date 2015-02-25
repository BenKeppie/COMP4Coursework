import sys
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtSql import *

from main_window import *
from profile_toolbar import *
from profile_picture import *

class DisplayProfileWidget(QWidget):
    """A class to display the model and represent a view on the profile tab"""

    def __init__(self):
        super().__init__()
        self.ToolBarWidgetLayout=QVBoxLayout()
        self.LayoutWidget=QWidget()
        self.HBoxLayout=QHBoxLayout()
        self.LeftWidgetsLayout=QHBoxLayout()
        self.RightWidgetsLayout=QVBoxLayout()
        self.display_profile_layout()
        self.display_profile_toolbar_widget()
        self.setLayout(self.ToolBarWidgetLayout)
        self.model=None
        
        
        
       
        

    def display_profile_layout(self):
        self.HBoxLayout.addLayout(self.LeftWidgetsLayout)
        self.HBoxLayout.addLayout(self.RightWidgetsLayout)
        if not hasattr(self,"profile_picture"):
            self.profile_picture=ProfilePicture()
            self.LeftWidgetsLayout.addWidget(self.profile_picture)
        if not hasattr(self,"first_name"):
            self.first_name=QLabel("FirstName")
            self.LeftWidgetsLayout.addWidget(self.first_name)
        if not hasattr(self,"last_name"):
            self.last_name=QLabel("LastName")
            self.LeftWidgetsLayout.addWidget(self.last_name)

        self.HBoxLayout.addLayout(self.LeftWidgetsLayout)

        if not hasattr(self,"user_email"):
            self.user_email=QLabel("Email")
            self.RightWidgetsLayout.addWidget(self.user_email)
        if not hasattr(self,"recent_tricks"):
            self.recent_tricks=QLabel("Recently Completed Tricks")
            self.RightWidgetsLayout.addWidget(self.recent_tricks)
        if not hasattr(self,"recent_tricks_list"):
            self.recent_tricks_list=QLabel("Recently Completed Tricks List")
            self.RightWidgetsLayout.addWidget(self.recent_tricks_list)

        self.HBoxLayout.addLayout(self.RightWidgetsLayout)
        self.LayoutWidget.setLayout(self.HBoxLayout)
        
        

    def display_profile_toolbar_widget(self):
        if not hasattr(self,"profile_tool_bar"):
            self.profile_tool_bar=DisplayProfileToolbar()
            self.ToolBarWidgetLayout.addWidget(self.profile_tool_bar)
        self.ToolBarWidgetLayout.addWidget(self.LayoutWidget)
        
    

        
        
        


       
        
        
        
    
