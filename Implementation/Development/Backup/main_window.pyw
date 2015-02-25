import sys
import time
import os
import subprocess
import os.path
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *


from menu_bar import *
from profile_widget import *
from profile_toolbar import *

from tricks_widget import *
from tricks_toolbar import *

from skateparks_widget import *
from skateparks_toolbar import *

from reviews_widget import *


class MainWindow(QMainWindow):
    """Class for the main window of my program"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Skateboard Progress Tracker")
        self.app = QtGui.QApplication([])
        self.set_icon()

        #create tabs
        self.create_tabs()
       
        #Create Menu Bar
        self.Menu=Menu(self)
        self.setMenuBar(self.Menu.MenuBar)

        #Create Statusbar
        self.StatusBar=QStatusBar()
        self.setStatusBar(self.StatusBar)
        
        
        

    def set_icon(self):
        self.app_icon=QtGui.QIcon()
        self.app_icon.addFile("ProgramIcon.png",QSize(16,16))
        self.app.setWindowIcon(self.app_icon)
        
        

    def create_tabs(self):
        
        
        self.tabs=QTabWidget()

        #Create Widgets
        self.profile_tab=DisplayProfileWidget(self)
        
        self.tricks_tab=DisplayTricksWidget(self)
        self.skateparks_tab=DisplaySkateparksWidget(self)
        self.reviews_tab=DisplayReviewsWidget(self)
        self.support_tab=QWidget()

        
        #Add Tabs
        self.tabs.addTab(self.profile_tab, "Profile")
        self.tabs.addTab(self.tricks_tab, "Tricks")
        self.tabs.addTab(self.skateparks_tab, "Skateparks")
        self.tabs.addTab(self.reviews_tab, "Reviews")
        self.tabs.addTab(self.support_tab, "Support")

        


        


 

        #Add all to the main window
        self.setCentralWidget(self.tabs)
        
def splash_screen():
    splash_pix = QPixmap('SplashScreen1.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    time.sleep(2)
    splash.finish(splash)        

def main():
    application=QApplication(sys.argv)
    window=MainWindow()
    #splash_screen()

    
    window.show()
    window.raise_()
    application.exec_()
    print()



if __name__=="__main__":
    main()
    
