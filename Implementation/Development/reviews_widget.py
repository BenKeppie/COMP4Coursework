from reviews_toolbar import *
from reviews_sql_connections import *

import os
import sys
import re 
class DisplayReviewsWidget(QWidget):
    """A class to display the reviews widget"""

    def __init__(self,parent):
        super().__init__()
        self.parent=parent

        
        self.RedBorder="border: 1px solid red;"
        self.GreenBorder="border: 1px solid green;"

        self.main_stacked_layout=QStackedLayout()

        self.add_review_VBoxLayout=QVBoxLayout()
        self.add_review_button_layout=QHBoxLayout()
        self.add_review_HBoxLayout=QHBoxLayout()
        self.add_review_widget=QWidget()
        self.add_review_table=QTableView()

        self.stacked_layout=QStackedLayout()
        self.results_table=QTableView()
        self.results_layout=QVBoxLayout()
        self.results_widget=QWidget()

        self.LayoutWidget=QWidget()
        self.ToolBarWidgetLayout=QVBoxLayout()

        self.open_connection()
        self.display_results()
        self.show_review_layout()
        
        

        self.add_review()

        self.display_review_layout()
        self.display_review_toolbar_widget()
        self.setLayout(self.ToolBarWidgetLayout)

        self.cancel_review.clicked.connect(self.cancel_button_clicked)
        self.save_review.clicked.connect(self.save_button_clicked)
        self.review_type.currentIndexChanged.connect(self.update_review_boxes)

    def cancel_button_clicked(self):
        self.clear_review_line_edit()
        self.table_stacked()
        

    

    def save_button_clicked(self):
        Valid=self.validate_add_review()
        if Valid:
            self.clear_review_line_edit()
        else:
            print()
    def validate_add_review(self):
        ReviewType=self.validate_review_type()
        ReviewSize=self.validate_review_size()
        ReviewName=self.validate_review_name()
        ReviewRating=self.validate_review_rating()
        ReviewReview=self.validate_review_review()
        if (ReviewType==True) and (ReviewSize==True) and (ReviewName==True) and (ReviewName==True) and (ReviewRating==True) and (ReviewReview==True):
            self.connection.add_review_to_database(self.review_type.currentText(),self.review_size.currentText(), self.review_brand.currentText(),self.review_name.text(),self.review_rating.currentText(), self.review_review.text())
            query=self.connection.show_all_reviews()
            self.model.setModel(query)
            return True
        else:
            print("Not all fields valid")
            return False

    def validate_review_type(self):
        return True

    def validate_review_size(self):
        return True
    def validate_review_name(self):
        return True
    def validate_review_brand(self):
        return True
    def validate_review_rating(self):
        return True
    def validate_review_review(self):
        return True

    def clear_review_line_edit(self):
        self.review_type.setCurrentIndex(0)
        self.review_size.setCurrentIndex(0)
        self.review_brand.setCurrentIndex(0)
        self.review_name.clear()
        self.review_rating.setCurrentIndex(0)
        self.review_review.clear()
        self.review_review.setText("Review")

    



    def open_connection(self):
        self.path=("{0}{1}".format(os.getcwd(),"\skateboard_progress_tracker.db"))
        self.connection=ReviewsSQLConnections(self.path)
        self.connection.open_database()

    def display_results(self):
        self.results_layout.addWidget(self.results_table)
        self.results_widget.setLayout(self.results_layout)

        self.stacked_layout.addWidget(self.results_widget)
    

        

    def show_review_layout(self):
        if self.connection != None:
            self.query = self.connection.show_all_reviews()
        
            self.show_results(self.query)
        else:
            print("A DB Connection must be opened")

    def show_results(self,query):
        self.model = QSqlQueryModel()
        self.model.setQuery(query)
        self.results_table.setModel(self.model)
        self.results_table.show()

    def update_review_boxes(self):
        self.review_size.clear()
        self.review_brand.clear()
        self.review_size.addItem("-Select a Size-")
        self.review_brand.addItem("-Select a Brand-")

        
        SizeOptions=self.size_options_check(self.review_type.currentText())
        for Size in SizeOptions:
            self.review_size.addItem(Size)

    def type_options_check(self):
        self.type_options=self.connection.get_all_product_type()
        #self.type_options=["Deck","Trucks","Wheels","Bearings","Griptape","Bolts"]
        return self.type_options

    def size_options_check(self,Type):
        pass
##        if Type=="Deck":
##            self.size_options=
##        elif Type=="Trucks":
##            self.size_options=
##        elif Type=="Wheels":
##            self.size_options=
##        elif Type=="Bearings":
##            self.size_options=
##        elif Type=="Griptape":
##            self.size_options=
##        elif Type=="Bolts":
##            self.size_options=
##        else:
##            self.size_options=[]
##        return self.size_options

    def brand_options_check(self,):
        self.brand_options=self.connection.get_all_product_brand()

        return self.brand_options
        

    

    def add_review(self):
        self.add_review_table.setModel(self.model)

        if not hasattr(self,"review_type"):
            self.review_type=QComboBox()
            self.review_type.addItem("-Select a Type-")
            TypeOptions=self.type_options_check()
            self.review_type.setModel(TypeOptions)
           
            self.add_review_VBoxLayout.addWidget(self.review_type)
        if not hasattr(self,"review_size"):
            self.review_size=QComboBox()
            self.review_size.addItem("-Select a Size-")
            
            self.add_review_VBoxLayout.addWidget(self.review_size)
        if not hasattr(self,"review_brand"):
            self.review_brand=QComboBox()
            self.review_brand.addItem("-Select a Brand-")
            self.add_review_VBoxLayout.addWidget(self.review_brand)
        if not hasattr(self,"review_name"):
            self.review_name=QLineEdit()
            self.review_name.setPlaceholderText("Product Name")
            self.add_review_VBoxLayout.addWidget(self.review_name)
        if not hasattr(self,"review_rating"):
            self.review_rating=QComboBox()
            self.review_rating.addItem("-Select a Rating-")
            for count in range(1,6):
                self.review_rating.addItem(str(count))
            self.add_review_VBoxLayout.addWidget(self.review_rating)
        if not hasattr(self,"review_review"):
            self.review_review=QTextEdit("Review")
            self.add_review_VBoxLayout.addWidget(self.review_review)
        
            
            

        if not hasattr(self,"cancel_review"):
            self.cancel_review=QPushButton("Cancel")
            self.add_review_button_layout.addWidget(self.cancel_review)
        if not hasattr(self,"save_review"):
            self.save_review=QPushButton("Save")
            self.add_review_button_layout.addWidget(self.save_review)

        self.add_review_VBoxLayout.addLayout(self.add_review_button_layout)
        self.add_review_HBoxLayout.addLayout(self.add_review_VBoxLayout)
        self.add_review_HBoxLayout.addWidget(self.add_review_table)
        self.add_review_widget.setLayout(self.add_review_HBoxLayout)

    def display_review_layout(self):
        self.stacked_layout.addWidget(self.add_review_widget)
    
        self.LayoutWidget.setLayout(self.stacked_layout)



    def display_review_toolbar_widget(self):
        if not hasattr(self,"reviews_tool_bar"):
            self.reviews_tool_bar=DisplayReviewsToolbar(self)
            self.ToolBarWidgetLayout.addWidget(self.reviews_tool_bar)
        self.ToolBarWidgetLayout.addWidget(self.LayoutWidget)

    def table_stacked(self):
        self.stacked_layout.setCurrentIndex(0)

    def add_review_stacked(self):
        self.stacked_layout.setCurrentIndex(1)

    

    
