import sys
import sqlite3
from PyQt4.QtSql import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *



class MainWindow(QMainWindow):
    """The main window for my application"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Display Table")
        self.stacked_layout=QStackedLayout()
        self.results_table=QTableView()
        self.results_layout=QVBoxLayout()
        self.results_widget=QWidget()

        self.open_connection()
        self.show_layout()
        self.display_results()
        
        

    def display_results(self):
        self.results_layout.addWidget(self.results_table)
        self.results_widget.setLayout(self.results_layout)

        self.stacked_layout.addWidget(self.results_widget)
    def open_connection(self):
        self.path=r"U:\git\COMP4Coursework\Implementation\Development\skateboard_progress_tracker.db"
    def show_layout(self):
        
        self.query = self.show_all_tricks()
            
        self.show_results()
      
    def show_results(self):
        self.model = QSqlQueryModel()
        self.model.setQuery(self.query)
        self.results_table.setModel(self.model)
        self.results_table.show()
        print("working")
    def show_all_tricks(self):
        self.query = QSqlQuery()
        self.query.prepare(""" SELECT * FROM Trick""")
        self.query.exec_()
        return self.query
    def open_database(self):
        if self.db:
            self.close_database()

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.path)

        opened_ok=self.db.open()
        return opened_ok
        
        
                                    




if __name__ == "__main__":
    application=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    window.raise_()
    application.exec_()
