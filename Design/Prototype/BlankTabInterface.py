import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabbed Interface")
        self.create_tabs()

    def create_tabs(self):

        self.tabs=QTabWidget()

        #Create Widgets
        self.profile_tab=QWidget()
        self.tricks_tab=QWidget()
        self.skateparks_tab=QWidget()
        self.reviews_tab=QWidget()
        self.support_tab=QWidget()
        
        #Add Tabs
        self.tabs.addTab(self.profile_tab, "Profile")
        self.tabs.addTab(self.tricks_tab, "Tricks")
        self.tabs.addTab(self.skateparks_tab, "Skateparks")
        self.tabs.addTab(self.reviews_tab, "Reviews")
        self.tabs.addTab(self.support_tab, "Support")

        self.setCentralWidget(self.tabs)
        
if __name__=="__main__":
    application=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    window.raise_()
    application.exec_()
