import sqlite3

def get_difficulty_id():
    Finished=False
    while not Finished:
        Difficulty=input("Please enter a difficulty: (Easy/Medium/Hard) ")
        Difficulty=Difficulty.lower()
        if Difficulty=="easy":
            Difficulty=1
            Finished=True
        elif Difficulty =="medium":
            Difficulty=2
            Finished=True
        elif Difficulty=="hard":
            Difficulty=3
            Finished=True
        else:
            print()
            print("Please select a correct difficulty.")
            print()
    return Difficulty

def get_trick_creator():
    User="Name"
    return User
        
    

def get_trick_name():
    TrickName=input("Please enter the trick name: ")
    return TrickName

def get_trick_description():
    TrickDescription=input("Please enter the trick description: ")
    return TrickDescription

def get_trick_obsticle():
    TrickObsticle=input("Please enter the trick obsticle: ")
    return TrickObsticle

def get_trick_image():
    TrickImage = input("Please enter a JPEG images file path: ")
    return TrickImage

def get_trick_tutorial_link():
    TrickTutorialLink=input("Please enter a trick tutorial link: ")
    return TrickTutorialLink

def get_trick_completed():
    pass

def get_trick_completed_date():
    pass

def add_trick():
    DifficultyID=get_difficulty_id()
    TrickCreator=get_trick_creator()
    TrickName=get_trick_name()
    TrickDescription=get_trick_description()
    TrickObsticle=get_trick_obsticle()
    TrickImage=get_trick_image()
    TrickTutorialLink=get_trick_tutorial_link()
    TrickCompleted=get_trick_completed()
    TrickCompletedDate=get_trick_completed_date()

    values=(DifficultyID,TrickCreator,TrickName,TrickDescription,TrickObsticle,TrickImage,TrickTutorialLink,TrickCompleted,TrickCompletedDate)
    with sqlite3.connect("skateboard_progress_tracker.db") as db:
        cursor = db.cursor()
        sql="insert into Trick(DifficultyID, TrickCreator,TrickName,TrickDescription,TrickObsticle,TrickImage,TrickTutorialLink,TrickCompleted,TrickCompletedDate) values (?,?,?,?,?,?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()
        print()
        print("Trick Successfully Created.")
        print()

def edit_trick():
    TrickID=int(input("Please enter the TrickID of the trick you wish to edit: "))
    DifficultyID=get_difficulty_id()
    TrickCreator=get_trick_creator()
    TrickName=get_trick_name()
    TrickDescription=get_trick_description()
    TrickObsticle=get_trick_obsticle()
    TrickImage=get_trick_image()
    TrickTutorialLink=get_trick_tutorial_link()
    TrickCompleted=get_trick_completed()
    TrickCompletedDate=get_trick_completed_date()
    
    values=(DifficultyID,TrickCreator,TrickName,TrickDescription,TrickObsticle,TrickImage,TrickTutorialLink,TrickCompleted,TrickCompletedDate, TrickID)
    with sqlite3.connect("skateboard_progress_tracker.db") as db:
        cursor = db.cursor()
        sql="update Trick set DifficultyID=?, TrickCreator=?, TrickName=?, TrickDescription=?, TrickObsticle=?,TrickImage=?, TrickTutorialLink=?,TrickCompleted=?, TrickCompletedDate=?  where TrickID=?"
        cursor.execute(sql,values)
        db.commit()

def delete_trick():
    data=int(input("Please enter the TrickID of the trick you wish to delete: "))
    data=(data,)
    with sqlite3.connect("skateboard_progress_tracker.db") as db:
            cursor=db.cursor()
            sql="delete from Trick where TrickID=?"
            cursor.execute(sql,data)
            db.commit()
            print()
            print("Trick Successfully Deleted.")
            print()


if __name__=="__main__":
    get_trick_creator()
