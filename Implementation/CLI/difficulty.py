import sqlite3

def get_difficulty():
    difficulty=input("Please enter a difficulty: ")
    return difficulty

def get_description():
    description=input("Please enter a description: ")
    return description
    

def create_difficulties():
    TrickDifficulty=get_difficulty()
    DifficultyDescription=get_description()
    values=(TrickDifficulty,DifficultyDescription)
    with sqlite3.connect("skateboard_progress_tracker.db") as db:
        cursor = db.cursor()
        sql="insert into Difficulty(TrickDifficulty,DifficultyDescription) values (?,?)"
        cursor.execute(sql,values)
        db.commit()
        print()
        print("Difficulty Successfully Created.")
        print()


if __name__ == "__main__":
    create_difficulties()
        
