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

        #Resize width and height
        #self.tabs.resize(250, 150)
    
        #Move QTabWidget to x:300,y:300
        #self.tabs.move(300, 300)
        
        #Add Tabs
        self.tabs.addTab(self.profile_tab, "Profile")
        self.tabs.addTab(self.tricks_tab, "Tricks")
        self.tabs.addTab(self.skateparks_tab, "Skateparks")
        self.tabs.addTab(self.reviews_tab, "Reviews")
        self.tabs.addTab(self.support_tab, "Support")


        #Put information into tabs
        self.profile_filled_tab()
        self.tricks_filled_tab()

        #Add all to the main window
        self.setCentralWidget(self.tabs)
        
        
    def profile_filled_tab(self):
        
        if not hasattr(self,"AwesomeButton"):
            self.AwesomeButton=QPushButton("Generate Profile")
            self.vBoxLayout=QVBoxLayout()
            self.vBoxLayout.addWidget(self.AwesomeButton)

        self.profile_tab.setLayout(self.vBoxLayout)

    def tricks_filled_tab(self):
        self.vBoxLayoutTricks=QVBoxLayout()
        
        if not hasattr(self,"text_box"):
            self.text_box=QLineEdit()
            self.vBoxLayoutTricks.addWidget(self.text_box)
        
        if not hasattr(self,"button"):
            self.button=QPushButton("Add Trick")
            self.vBoxLayoutTricks.addWidget(self.button)

        if not hasattr(self,"label"):
            self.label=QLabel("Enter Trick Name")
            self.vBoxLayoutTricks.addWidget(self.label)

        
        self.tricks_tab.setLayout(self.vBoxLayoutTricks)
        
        

    def skateparks_filled_tab(self):
        pass

    def reviews_filled_tab(self):
        pass

    def support_filled_tab(self):
        pass
        


if __name__=="__main__":
    application=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    window.raise_()
    application.exec_()
