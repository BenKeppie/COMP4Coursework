import sqlite3

def get_skatepark_name():
    Name=input("Please enter the skateparks name: ")
    return Name

def get_skatepark_description():
    Description=input("Please enter the description for the skatepark: ")
    return Description

def get_skatepark_longitude():
    Longitude = input("Please enter the longitude for the skatepark: ")
    return Longitude

def get_skatepark_latitude():
    Latitude=input("Please enter the latitude for the skatepark: ")
    return Latitude 




def add_skatepark():
    SkateparkName=get_skatepark_name()
    SkateparkDescription=get_skatepark_description()
    SkateparkLongitude=get_skatepark_longitude()
    SkateparkLatitude=get_skatepark_latitude()
    values=(SkateparkName,SkateparkLongitude,SkateparkLatitude,SkateparkDescription)
    with sqlite3.connect("skateboard_progress_tracker.db") as db:
        cursor = db.cursor()
        sql="insert into Skatepark(SkateparkName,SkateparkLongitude,SkateparkLatitude,SkateparkDescription) values(?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()
        print()
        print("Skatepark Successfully Created.")
        print()

def edit_skatepark():
    SkateparkID=int(input("Please enter the SkateparkID of the skatepark you wish to edit: "))
    SkateparkName=get_skatepark_name()
    SkateparkDescription=get_skatepark_description()
    SkateparkLongitude=get_skatepark_longitude()
    SkateparkLatitude=get_skatepark_latitude()
    values=( SkateparkName,SkateparkLongitude,SkateparkLatitude,SkateparkDescription,SkateparkID)
    with sqlite3.connect("skateboard_progress_tracker.db") as db:
        cursor = db.cursor()
        sql="update Skatepark set SkateparkName=?, SkateparkLongitude=?, SkateparkLatitude=?, SkateparkDescription=? where SkateparkID=?"
        cursor.execute(sql,values)
        db.commit()

def delete_skatepark():
    data=int(input("Please enter the SkateparkID of the skatepark you wish to delete: "))
    data=(data,)
    with sqlite3.connect("skateboard_progress_tracker.db") as db:
            cursor=db.cursor()
            sql="delete from Skatepark where SkateparkID=?"
            cursor.execute(sql,data)
            db.commit()
            print()
            print("Skatepark Successfully Deleted.")
            print()
