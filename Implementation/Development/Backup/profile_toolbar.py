import sys
from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtSql import *

from profile_widget import *
from profile_sql_connections import *
from main_window import *


class DisplayProfileToolbar(QToolBar):
    changedPicture=pyqtSignal()
    def __init__(self):
        super().__init__()

        self.change_picture=QAction("Change Picture",self)

        self.addAction(self.change_picture)


        self.change_picture.triggered.connect(self.change_picture_connection)

    def change_picture_connection(self):
        
        print("Find Picture")
        path=QFileDialog.getOpenFileName()
        if path=="":
            print("Picture not changed.")
        else:
            replace="\."
            path=path.replace("/",replace[0])
            destination=("{0}{1}{2}".format(os.getcwd(),replace[0],"ProfilePicture.jpeg"))
            print(destination)
            print(path)
            shutil.copy2(path,destination)
            self.connection=ProfileSQLConnections()
            self.connection.change_picture(destination)
            print(path)
            self.changedPicture.emit()


        
