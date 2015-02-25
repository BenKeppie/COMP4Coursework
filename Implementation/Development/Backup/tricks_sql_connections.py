import sqlite3
from PyQt4.QtSql import *

class TricksSQLConnections:
    """Handles the connection to the SQL database for the tricks tab"""

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

    def show_all_tricks(self):
        query = QSqlQuery()
        query.prepare(""" SELECT * FROM Trick""")
        query.exec_()
        return query

    def add_trick_to_database(self,DifficultyID,TrickName,TrickDescription,TrickObsticle,TrickImage,TrickTutorialLink):
        print("hi2")
    
        values=(DifficultyID, "Ben Keppie", TrickName, TrickDescription, TrickObsticle, TrickImage, TrickTutorialLink)
        with sqlite3.connect("skateboard_progress_tracker.db") as db:
            cursor = db.cursor()
            sql="insert into Trick(DifficultyID, TrickCreator,TrickName,TrickDescription,TrickObsticle,TrickImage,TrickTutorialLink) values (?,?,?,?,?,?,?)"
            cursor.execute(sql,values)
            db.commit()
            print()
            print("Trick Successfully Created.")
            print()

         

           
  
