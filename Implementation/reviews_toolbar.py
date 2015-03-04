import sys
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtSql import *


class DisplayReviewsToolbar(QToolBar):
    """A class to create the toolbar for the review tab"""
    def __init__(self, parent):
        super().__init__()
        self.parent=parent
        
        self.add_review=QAction("Add Review",self)
        
        self.addAction(self.add_review)

            #connections
        self.add_review.triggered.connect(self.add_review_connection)


    def add_review_connection(self):
        self.parent.add_review_stacked()
        print()
        print("Add Review")
        print()
        
