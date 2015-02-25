import sqlite3

class SkateparksSQLConnections:
    """Handles the connection to the SQL database for the skateparks tab"""

    def __init__(self):
        print("Skatepark SQL Connection")

    def add_skatepark(self,SkateparkName,SkateparkDescription,Latitude,Longitude):
        values=(SkateparkName,SkateparkDescription,Latitude,Longitude)
        with sqlite3.connect("skateboard_progress_tracker.db") as db:
            cursor = db.cursor()
            sql="insert into Skatepark(SkateparkName,SkateparkDescription, SkateparkLatitude, SkateparkLongitude) values (?,?,?,?)"
            cursor.execute(sql,values)
            db.commit()
            print()
            print("Skatepark Successfully Created.")
            print()
        
        
        
