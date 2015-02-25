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
        query.prepare(""" SELECT ProductType,ProductName,ReviewDescription,ReviewRating,ProductBrand,ProductSize,ReviewCreator FROM review, product, productbrand,producttype,productsize""")
        query.exec_()
        return query

    def get_all_product_type(self):
        query=QSqlQuery()
        query.prepare("""SELECT ProductType FROM ProductType""")
        query.exec_()
        model=QSqlQueryModel().setQuery(query)
        return model
        
        
                

    def get_deck_sizes(self):
        pass

    def get_trucks_sizes(self):
        pass

    def get_wheels_sizes(self):
        pass

    def get_bearings_sizes(self):
        pass

    def get_griptape_sizes(self):
        pass

    def get_bolts_sizes(self):
        pass

    def get_all_product_brand(self):
        pass

    def add_review_to_database(self,ReviewType,ReviewSize,ReviewBrand,ReviewName,ReviewRating,ReviewReview):
        pass
