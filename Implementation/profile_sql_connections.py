import sqlite3
import shutil
import os
import sys





class ProfileSQLConnections:
    """Handles the connection to the SQL database for the profile tab"""
    
    def __init__(self):
        print("Profile SQL Connection")

    def change_name(self,FirstName,LastName):
        FirstName=FirstName
        LastName=LastName
        if (FirstName=="") or (LastName==""):
            print("Name Not Changed")
        else:
            values=(FirstName,LastName, 1)
            with sqlite3.connect("skateboard_progress_tracker.db") as db:
                cursor = db.cursor()
                sql="update User set FirstName=?, LastName=? where UserID=?"
                cursor.execute(sql,values)
                db.commit()
                
            

    def change_email(self,Email):
        Email=Email
        if (Email==""):
            print("Email Not Changed")
        else:
            values=(Email,1)
            with sqlite3.connect("skateboard_progress_tracker.db") as db:
                cursor = db.cursor()
                sql="update User set UserEmail=? where UserID=?"
                cursor.execute(sql,values)
                db.commit()
            
           

    def change_picture(self,FilePath):
        FilePath=FilePath
    
        values=(FilePath,1)
        with sqlite3.connect("skateboard_progress_tracker.db") as db:
            cursor = db.cursor()
            sql="update User set UserPicture=? where UserID=?"
            cursor.execute(sql,values)
            db.commit()
            print("Picture Changed")
        
        


    def get_first_name(self):
        with sqlite3.connect("skateboard_progress_tracker.db") as db:
                cursor=db.cursor()
                cursor.execute("select FirstName from User where UserID=?",(1,))
                FirstName=cursor.fetchone()
                print(FirstName)
                return FirstName
    def get_last_name(self):
        with sqlite3.connect("skateboard_progress_tracker.db") as db:
                cursor=db.cursor()
                cursor.execute("select LastName from User where UserID=?",(1,))
                LastName=cursor.fetchone()
                return LastName
    def get_email(self):
        with sqlite3.connect("skateboard_progress_tracker.db") as db:
                cursor=db.cursor()
                cursor.execute("select UserEmail from User where UserID=?",(1,))
                UserEmail=cursor.fetchone()
                return UserEmail
    def get_picture(self):
        FilePath=("{0}{1}".format(os.getcwd(),"\ProfilePicture.jpeg"))
        print(FilePath)
        return FilePath
        
        


        
            


        
