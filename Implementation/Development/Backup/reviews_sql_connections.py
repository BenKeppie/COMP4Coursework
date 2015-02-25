import sqlite3
from PyQt4.QtSql import *

class ReviewsSQLConnections:
    """Handles the connection to the SQL database for the reviews tab"""

    def __init__(self,path):
        self.path=path
        self.db=None

    def open_database(self):
        if self.db:
            self.close_database()

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.path)

        opened_ok=self.db.open()
        return opened_ok

    def show_all_reviews(self):
        query = QSqlQuery()
        query.prepare(""" SELECT * FROM review""")
        query.exec_()
        return query

    def add_review_to_database(self,ReviewType,ReviewSize,ReviewBrand,ReviewName,ReviewRating,ReviewReview):
        pass
