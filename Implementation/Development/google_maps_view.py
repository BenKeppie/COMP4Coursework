from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

from skateparks_widget import * 


class CustomWebView(QWebView):

    updateTest=pyqtSignal()
    def __init__(self):
        super().__init__()
        
        self.urlChanged.connect(self.url_changed)

    def url_changed(self):
        print("Change")
        print(self.url())
        self.updateTest.emit()

    def reset_url(self):
        print(self.view.url().path())
        
        
        if self.view.url().path()=="/IframeLoginPopupSuccess":
            print("Reset url")
            self.LogInSuccess="https://mapsengine.google.com{0}".format("/IframeLoginPopupSuccess")
            self.load(QUrl(self.LogInSuccess))
    
            
        
    def createWindow(self,webWindowType):
        self.view=CustomWebView()
        self.view.updateTest.connect(self.reset_url)
        
        #self.view.show()
        print(self.view)
        return self.view
