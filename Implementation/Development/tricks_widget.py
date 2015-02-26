from tricks_toolbar import *
from tricks_sql_connections import *

import os
import sys
import re 

class DisplayTricksWidget(QWidget):
    """A class to display the Tricks widget"""
    

    def __init__(self,parent):
        super().__init__()
        self.parent=parent
        self.RedBorder="border: 1px solid red;"
        self.GreenBorder="border: 1px solid green;"
        self.TrickFilePath="{0}\ProgramIcon.png".format(os.getcwd())
        self.main_stacked_layout=QStackedLayout()
        self.add_trick_VBoxLayout=QVBoxLayout()
        self.add_trick_button_layout=QHBoxLayout()
        self.add_trick_HBoxLayout=QHBoxLayout()
        self.add_trick_widget=QWidget()
        self.add_trick_table=QTableView()

        
        self.stacked_layout=QStackedLayout()
        self.results_table=QTableView()
        self.results_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.results_layout=QVBoxLayout()
        self.results_widget=QWidget()
        
        
       
        self.LayoutWidget=QWidget()
        self.ToolBarWidgetLayout=QVBoxLayout()
        

        self.open_connection()
        self.display_results()
        self.show_tricks_layout()
        
        

        self.add_tricks()

        self.display_tricks_layout()
        self.display_tricks_toolbar_widget()
        self.setLayout(self.ToolBarWidgetLayout)


        self.trick_image.clicked.connect(self.image_button_clicked)
        self.cancel_trick.clicked.connect(self.cancel_button_clicked)
        self.save_trick.clicked.connect(self.save_button_clicked)
        self.trick_name.textChanged.connect(self.validate_trick_name)
        self.trick_description.textChanged.connect(self.validate_trick_description)
        self.trick_obsticle.textChanged.connect(self.validate_trick_obsticle)
        self.trick_tutorial.textChanged.connect(self.validate_trick_tutorial)

    def keyPressEvent(self,event):
        indexes=self.results_table.selectionModel().selectedRows()
        for index in indexes:
            Row=index.row()
            if event.key()==Qt.Key_Delete:
                    self.delete_trick_warning(Row)

        

    def delete_trick_warning(self,Row):
        self.delete_dialog=QDialog()
        self.dialog_VBoxLayout=QVBoxLayout()
        self.dialog_button_layout=QHBoxLayout()
        if not hasattr(self,"delete_message"):
            self.delete_message=QLabel("Are you sure you wish to delete this trick?")
            self.dialog_VBoxLayout.addWidget(self.delete_message)
        if not hasattr(self,"delete_cancel"):
            self.delete_cancel=QPushButton("Cancel")
            self.dialog_button_layout.addWidget(self.delete_cancel)
        if not hasattr(self,"delete_save"):
            self.delete_save=QPushButton("Save")
            self.dialog_button_layout.addWidget(self.delete_save)
        self.dialog_VBoxLayout.addLayout(self.dialog_button_layout)
        self.delete_dialog.setLayout(self.dialog_VBoxLayout)
        self.delete_dialog.show()
        self.delete_cancel.clicked.connect(self.delete_cancel_clicked)
        self.delete_save.clicked.connect(self.delete_save_clicked,Row)

    def delete_cancel_clicked(self):
        self.delete_dialog.close()
        self.parent.StatusBar.showMessage("Trick Not Deleted",2000)

    def delete_save_clicked(self,Row):
        self.delete_dialog.close()
        self.connection.delete_row(Row)
        query = self.connection.show_all_tricks()
        self.model.setQuery(query)
        self.parent.StatusBar.showMessage("Trick Successfully Deleted",2000)
        
        
        
         

    def validate_add_trick(self):
        TrickName=self.validate_trick_name()
        print(self.validate_trick_name())
        TrickDescription=self.validate_trick_description()
        TrickObsticle=self.validate_trick_obsticle()
        if self.trick_tutorial.text()=="":
            TrickTutorial=True
        else:
            TrickTutorial=self.validate_trick_tutorial()
        
        
        if (TrickName==True) and (TrickDescription==True) and (TrickObsticle==True) and (TrickTutorial==True):
            self.connection.add_trick_to_database(self.trick_difficulty.currentIndex()+1 ,self.trick_name.text(),self.trick_description.text(),self.trick_obsticle.text(),self.TrickFilePath, self.trick_tutorial.text())
            self.parent.StatusBar.showMessage("Trick Successfully Saved.",2000)
            query = self.connection.show_all_tricks()
            self.model.setQuery(query)
            return True
        else:
            self.parent.StatusBar.showMessage("Not all Fields are Valid.",2000)
            return False
        
        

    def validate_trick_name(self):
        Text=self.trick_name.text()
        TrickNameExpression=re.compile("^(?!\s*$).+")
        Match=TrickNameExpression.match(Text.upper())
        if Match:
            self.trick_name.setStyleSheet(self.GreenBorder)
            return True
        else:
            self.trick_name.setStyleSheet(self.RedBorder)
            return False
     
            

    def validate_trick_description(self):
        Text=self.trick_description.text()
        TrickDescriptionExpression=re.compile("^(?!\s*$).+")
        Match=TrickDescriptionExpression.match(Text.upper())
        if Match:
            self.trick_description.setStyleSheet(self.GreenBorder)
            return True
        else:
            self.trick_description.setStyleSheet(self.RedBorder)
            return False

    def validate_trick_obsticle(self):
        Text=self.trick_obsticle.text()
        TrickObsticleExpression=re.compile("^(?!\s*$).+")
        Match=TrickObsticleExpression.match(Text.upper())
        if Match:
            self.trick_obsticle.setStyleSheet(self.GreenBorder)
            return True
        else:
            self.trick_obsticle.setStyleSheet(self.RedBorder)
            return False

    def validate_trick_tutorial(self):
        Text=self.trick_tutorial.text()
        TrickTutorialExpression=re.compile("(?:.+?)?(?:\/v\/|watch\/|\?v=|\&v=|youtu\.be\/|\/v=|^youtu\.be\/)([a-zA-Z0-9_-]{11})+")
        Match=TrickTutorialExpression.match(Text)
        if Match:
            self.trick_tutorial.setStyleSheet(self.GreenBorder)
            return True
        else:
            self.trick_tutorial.setStyleSheet(self.RedBorder)
            return False
        
        

    def clear_trick_line_edit(self):
        self.trick_name.clear()
        self.trick_description.clear()
        self.trick_obsticle.clear()
        self.trick_tutorial.clear()
        self.trick_difficulty.setCurrentIndex(0)
        

    def display_results(self):       
        self.results_layout.addWidget(self.results_table)
        self.results_widget.setLayout(self.results_layout)

        self.stacked_layout.addWidget(self.results_widget)
        

    def open_connection(self):
        self.path=("{0}{1}".format(os.getcwd(),"\skateboard_progress_tracker.db"))
        print(self.path)
        self.connection=TricksSQLConnections(self.path)
        self.connection.open_database()

    def show_tricks_layout(self):
        
        if self.connection != None:
            self.query = self.connection.show_all_tricks()
            
            self.show_results(self.query)
        else:
            print("A DB Connection must be opened")


    def show_results(self,query):
        
        self.model = QSqlQueryModel()
        self.model.setQuery(query)
        self.results_table.setModel(self.model)
        self.results_table.show()



        


    def display_tricks_layout(self):
        self.stacked_layout.addWidget(self.add_trick_widget)
        
        self.LayoutWidget.setLayout(self.stacked_layout)

    def table_stacked(self):
        self.stacked_layout.setCurrentIndex(0)

    def add_trick_stacked(self):
        self.stacked_layout.setCurrentIndex(1)

        
        
        

    def display_tricks_toolbar_widget(self):
        if not hasattr(self,"tricks_tool_bar"):
            self.tricks_tool_bar=DisplayTricksToolbar(self)
            self.ToolBarWidgetLayout.addWidget(self.tricks_tool_bar)
        self.ToolBarWidgetLayout.addWidget(self.LayoutWidget)

    def add_tricks(self):
        self.add_trick_table.setModel(self.model)
        if not hasattr(self,"trick_name"):
            self.trick_name=QLineEdit()
            self.trick_name.setPlaceholderText("Trick name")
            
            self.add_trick_VBoxLayout.addWidget(self.trick_name)
        if not hasattr(self,"trick_description"):
            self.trick_description=QLineEdit()
            self.trick_description.setPlaceholderText("Trick Description")
            self.add_trick_VBoxLayout.addWidget(self.trick_description)
        if not hasattr(self,"trick_obsticle"):
            self.trick_obsticle=QLineEdit()
            self.trick_obsticle.setPlaceholderText("Trick Obsticle")
            self.add_trick_VBoxLayout.addWidget(self.trick_obsticle)
        if not hasattr(self,"trick_image"):
            self.trick_image=QPushButton("Browse Trick Image")
            self.add_trick_VBoxLayout.addWidget(self.trick_image)
        if not hasattr(self,"trick_tutorial"):
            self.trick_tutorial=QLineEdit()
            self.trick_tutorial.setPlaceholderText("Trick Tutorial Link")
            self.add_trick_VBoxLayout.addWidget(self.trick_tutorial)
        if not hasattr(self,"trick_difficulty"):
            self.trick_difficulty=QComboBox()
            self.trick_difficulty.addItem("Easy")
            self.trick_difficulty.addItem("Medium")
            self.trick_difficulty.addItem("Hard")
            self.add_trick_VBoxLayout.addWidget(self.trick_difficulty)

        if not hasattr(self,"cancel_trick"):
            self.cancel_trick=QPushButton("Cancel")
            self.add_trick_button_layout.addWidget(self.cancel_trick)
        if not hasattr(self,"save_trick"):
            self.save_trick=QPushButton("Save")
            self.add_trick_button_layout.addWidget(self.save_trick)
        self.add_trick_VBoxLayout.addLayout(self.add_trick_button_layout)
        self.add_trick_HBoxLayout.addLayout(self.add_trick_VBoxLayout)
        self.add_trick_HBoxLayout.addWidget(self.add_trick_table)
        self.add_trick_widget.setLayout(self.add_trick_HBoxLayout)

    def cancel_button_clicked(self):
        print("Cancel")
        self.table_stacked()
        self.clear_trick_line_edit()

    def save_button_clicked(self):
        Valid=self.validate_add_trick()
        if Valid:
            self.clear_trick_line_edit()
        else:
            print()
        
        
       
        


    def image_button_clicked(self):
        print("hi")
        path=QFileDialog.getOpenFileName()
        if path=="":
            print("No picture Added")
        else:
            
            
            replace="\."
            path=path.replace("/",replace[0])
            print(path)
            self.TrickFilePath=path
            
            
            

            
        
        
