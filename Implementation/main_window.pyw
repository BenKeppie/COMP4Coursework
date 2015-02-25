import sys
import time
import os
import subprocess
import os.path
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

from profile_widget import *
from menu_bar import *
from profile_toolbar import *


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
        self.Menu=Menu()
        self.setMenuBar(self.Menu.MenuBar)
        
        
        

    def set_icon(self):
        self.app_icon=QtGui.QIcon()
        self.app_icon.addFile("ProgramIcon.png",QSize(16,16))
        self.app.setWindowIcon(self.app_icon)
        
        

    def create_tabs(self):
        
        #toolbars
        self.ProfileToolBar=DisplayProfileToolbar()
        
        self.tabs=QTabWidget()

        #Create Widgets
        self.profile_tab=DisplayProfileWidget()
        
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

        #Add Toolbars to tabs
        


 

        #Add all to the main window
        self.setCentralWidget(self.tabs)
        
def splash_screen():
    splash_pix = QPixmap('SplashScreen1.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    time.sleep(2)
    splash.finish(splash)        

def splash_screen2():
    splash_pix = QPixmap('SplashScreen2.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    time.sleep(2)
    splash.finish(splash)        


def splash_screen3():
    splash_pix = QPixmap('SplashScreen3.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    time.sleep(2)
    splash.finish(splash)        
        


if __name__=="__main__":
    application=QApplication(sys.argv)
    window=MainWindow()
    splash_screen()
    #splash_screen2()
    #splash_screen3()
    
    window.show()
    window.raise_()
    application.exec_()
    print()

