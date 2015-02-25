import sqlite3

def test_profile():
    with sqlite3.connect("skateboard_progress_tracker.db") as db:
        cursor=db.cursor()
        cursor.execute("select * from User")
        User=cursor.fetchall()
        User=len(User)
        return User
        

def add_profile():
    existing_user=test_profile()
    if existing_user==0:
        FirstName=get_first_name()
        LastName=get_last_name()
        Email=get_email()
        FilePath=get_file_path()
        values=(FirstName,LastName,Email,FilePath)
        with sqlite3.connect("skateboard_progress_tracker.db") as db:
            cursor = db.cursor()
            sql="insert into User(FirstName,LastName,UserEmail,UserPicture) values (?,?,?,?)"
            cursor.execute(sql,values)
            db.commit()
            print()
            print("Profile Successfully Created.")
            print()
    else:
        print()
        print("Profile already exists - To create a new profile, please delete the existing profile.")
        print()

def delete_profile():
    Finished=False
    while not Finished:
        Delete=input("Are you sure you wish to delete your profile? (Y/N) ")
        Delete=Delete.upper()

        if Delete=="Y":
    
            data=(1,)
            with sqlite3.connect("skateboard_progress_tracker.db") as db:
                cursor=db.cursor()
                sql="delete from User where UserID=?"
                cursor.execute(sql,data)
                db.commit()
                print()
                print("Profile Successfully Deleted.")
                print()
                Finished=True
        elif Delete =="N":
            print()
            print("Delete Aborted")
            print()
            Finished=True
        else:
            print()
            print("Incorrect input")
            print()
    
    


def get_first_name():
    print()
    FirstName=input("Please Enter Your First Name: ")
    print()
    return FirstName
    

def get_last_name():
    print()
    LastName=input("Please Enter Your Last Name: ")
    print()
    return LastName

def change_name():
    FirstName=get_first_name()
    LastName=get_last_name()
    values=(FirstName,LastName, 1)
    with sqlite3.connect("skateboard_progress_tracker.db") as db:
        cursor = db.cursor()
        sql="update User set FirstName=?, LastName=? where UserID=?"
        cursor.execute(sql,values)
        db.commit()


def get_email():
    print()
    Email=input("Please Enter Your Email Address: ")
    print()
    return Email

def change_email():
    Email=get_email()
    values=(Email,1)
    with sqlite3.connect("skateboard_progress_tracker.db") as db:
        cursor = db.cursor()
        sql="update User set UserEmail=? where UserID=?"
        cursor.execute(sql,values)
        db.commit()

def get_file_path():
    print()
    FilePath=input("Please Enter The File Path For The JPEG Image: ")
    print()
    return FilePath

def change_picture():
    FilePath=get_file_path()
    values=(FilePath,1)
    with sqlite3.connect("skateboard_progress_tracker.db") as db:
        cursor = db.cursor()
        sql="update User set UserPicture=? where UserID=?"
        cursor.execute(sql,values)
        db.commit()

if __name__=="__main__":
    test_profile()
    
