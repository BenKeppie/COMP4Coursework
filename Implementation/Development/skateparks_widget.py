from PyQt4.QtWebKit import *

from skateparks_toolbar import *
from skateparks_sql_connections import *
from skatepark_view_only import *
import re

 


from google_maps_view import *
from google_maps_test import *

#GOOGLE MAPS API KEY: AIzaSyC5RcJ7vLSEYF32KqDusnuRcLJiHW8EbDg


class DisplaySkateparksWidget(QWidget):
    """A class to display the Skatepark Widget"""

    def __init__(self,parent):
        super().__init__()
        self.parent=parent
        
        self.RedBorder="border: 1px solid red;"
        self.GreenBorder="border: 1px solid green;"
        self.SkateparksSQLConnections=SkateparksSQLConnections()
        self.coordinate_change=None
 
        self.add_skatepark_VBoxLayout=QVBoxLayout()
        self.add_skatepark_HBoxLayout=QHBoxLayout()
        self.add_skatepark_button_layout=QHBoxLayout()
        self.add_skatepark_widget=QWidget()
        

        self.LayoutWidget=QWidget()
        self.ToolBarWidgetLayout=QVBoxLayout()
        self.VBoxLayout=QVBoxLayout()

        self.add_skatepark()
        self.display_skateparks_toolbar_widget()
        self.setLayout(self.ToolBarWidgetLayout)

        self.cancel_skatepark.clicked.connect(self.cancel_button_clicked)
        self.save_skatepark.clicked.connect(self.save_button_clicked)
        self.skatepark_name.textChanged.connect(self.validate_skatepark_name)
        self.skatepark_description.textChanged.connect(self.validate_skatepark_description)
        self.skatepark_latitude.textChanged.connect(self.validate_latitude)
        self.skatepark_longitude.textChanged.connect(self.validate_longitude)

    def validate_skatepark_description(self):
        Text=self.skatepark_description.text()
        SkateparkDescriptionExpression=re.compile("^(?!\s*$).+")
        Match=SkateparkDescriptionExpression.match(Text.upper())
        if Match:
            self.skatepark_description.setStyleSheet(self.GreenBorder)
            return True
        else:
            self.skatepark_description.setStyleSheet(self.RedBorder)
            return False

    def validate_skatepark_name(self):
        Text=self.skatepark_name.text()
        SkateparkNameExpression=re.compile("^(?!\s*$).+")
        Match=SkateparkNameExpression.match(Text.upper())
        if Match:
            self.skatepark_name.setStyleSheet(self.GreenBorder)
            return True
        else:
            self.skatepark_name.setStyleSheet(self.RedBorder)
            return False
    def validate_longitude(self):
        Text=self.skatepark_longitude.text()
        if Text=="":
            self.skatepark_longitude.setStyleSheet(self.RedBorder)
            return False
        else:
            self.skatepark_longitude.setStyleSheet(self.GreenBorder)
            return True
    def validate_latitude(self):
        Text=self.skatepark_latitude.text()
        print(Text)
        if Text=="":
            self.skatepark_latitude.setStyleSheet(self.RedBorder)
            return False
        else:
            self.skatepark_latitude.setStyleSheet(self.GreenBorder)
            return True
        
        

    def validate_add_skatepark(self):
        SkateparkName=self.validate_skatepark_name()
        SkateparkDescription=self.validate_skatepark_description()
        SkateparkLatitude=self.validate_latitude()
        print(SkateparkLatitude)
        SkateparkLongitude=self.validate_longitude()
        if (SkateparkName==True) and (SkateparkDescription==True) and (SkateparkLatitude==True) and (SkateparkLongitude==True):
            self.parent.StatusBar.showMessage("Skatepark Successfully Saved.",2000)
            return True
        else:
            self.parent.StatusBar.showMessage("Not all Fields are Valid.",2000)
            return False

    def cancel_button_clicked(self):
        print("Cancel")
        self.clear_skatepark_line_edit()
        self.skatepark_name.hide()
        self.skatepark_description.hide()
        self.skatepark_longitude.hide()
        self.skatepark_latitude.hide()
        self.cancel_skatepark.hide()
        self.save_skatepark.hide()
        self.add_skatepark_map.delete_all_markers()
        self.add_skatepark_map.get_marker_coordinates()
        

    def save_button_clicked(self):
        print("Save")
        Valid=self.validate_add_skatepark()
        if Valid:
            self.SkateparksSQLConnections.add_skatepark(self.skatepark_name.text(),self.skatepark_description.text(),self.skatepark_latitude.text(),self.skatepark_longitude.text())
            self.clear_skatepark_line_edit()
            self.add_skatepark_map.delete_all_markers()
            self.add_skatepark_map.get_marker_coordinates()
            
        else:
            print()

    def view_add_skatepark(self):
        self.skatepark_name.show()
        self.skatepark_description.show()
        self.skatepark_longitude.show()
        self.skatepark_latitude.show()
        self.cancel_skatepark.show()
        self.save_skatepark.show()
        

    def clear_skatepark_line_edit(self):
        self.skatepark_name.clear()
        self.skatepark_description.clear()
        self.skatepark_latitude.clear()
        self.skatepark_longitude.clear()
        
    def fill_line_edits(self,LastMarker):
        self.latitude_coor=str(LastMarker[0])
        self.longitude_coor=str(LastMarker[1])
        self.skatepark_latitude.setText(self.latitude_coor)
        self.skatepark_longitude.setText(self.longitude_coor)
        


    def add_skatepark(self):
        if not hasattr(self,"skatepark_name"):
            self.skatepark_name=QLineEdit()
            self.skatepark_name.setPlaceholderText("Skatepark Name")
            self.skatepark_name.hide()
            self.add_skatepark_VBoxLayout.addWidget(self.skatepark_name)
        if not hasattr(self,"skatepark_description"):
            self.skatepark_description=QLineEdit()
            self.skatepark_description.setPlaceholderText("Skatepark Description")
            self.skatepark_description.hide()
            self.add_skatepark_VBoxLayout.addWidget(self.skatepark_description)

        if not hasattr(self,"skatepark_latitude"):
            self.skatepark_latitude=QLineEdit()
            self.skatepark_latitude.setPlaceholderText("Latitude")
            self.skatepark_latitude.setReadOnly(True)
            self.skatepark_latitude.hide()
            self.add_skatepark_VBoxLayout.addWidget(self.skatepark_latitude)
        if not hasattr(self,"skatepark_longitude"):
            self.skatepark_longitude=QLineEdit()
            self.skatepark_longitude.setPlaceholderText("Longitude")
            self.skatepark_longitude.setReadOnly(True)
            self.skatepark_longitude.hide()
            self.add_skatepark_VBoxLayout.addWidget(self.skatepark_longitude)

        if not hasattr(self,"cancel_skatepark"):
            self.cancel_skatepark=QPushButton("Cancel")
            self.cancel_skatepark.hide()
            self.add_skatepark_button_layout.addWidget(self.cancel_skatepark)
        if not hasattr(self,"save_skatepark"):
            self.save_skatepark=QPushButton("Save")
            self.save_skatepark.hide()
            self.add_skatepark_button_layout.addWidget(self.save_skatepark)

        if not hasattr(self,"add_skatepark_map"):
            self.add_skatepark_map=ViewOnlyMap(self)

            
            
            
        self.add_skatepark_VBoxLayout.addLayout(self.add_skatepark_button_layout)
        self.add_skatepark_HBoxLayout.addLayout(self.add_skatepark_VBoxLayout)
        
        self.add_skatepark_HBoxLayout.addWidget(self.add_skatepark_map)

        self.LayoutWidget.setLayout(self.add_skatepark_HBoxLayout)            

            
                     


    def display_skateparks_toolbar_widget(self):
        if not hasattr(self,"skateparks_tool_bar"):
            self.skateparks_tool_bar=DisplaySkateparksToolbar(self)
            self.ToolBarWidgetLayout.addWidget(self.skateparks_tool_bar)
        self.ToolBarWidgetLayout.addWidget(self.LayoutWidget)
        
        
