
import sqlite3

def create_table(db_name, table_name, sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?", (table_name,))
        result=cursor.fetchall()

        keep_table=True
        if len(result)==1:
            response=input("The table {0} already exists, do you wish to recreate it? (y/n) ".format(table_name))
            if response == "y":
                keep_table=False
                print("The {0} table will be recreated - all existing data will be lost".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept")
        else:
            keep_table=False
        if not keep_table:
            
            cursor.execute(sql)
            db.commit()
        
        db.commit()

def create_user_table():
    db_name="skateboard_progress_tracker.db"
    sql= """create table User (UserID integer, FirstName text, LastName text, UserPicture image, UserEmail text, Primary Key(UserID))"""
    create_table(db_name,"User", sql)
    print("Blank User Table Created.")

def create_user_trick_table():
    db_name="skateboard_progress_tracker.db"
    sql= """create table UserTrick (UserTrickID integer, UserID integer, TrickID integer, Primary Key(UserTrickID), Foreign Key(UserID) references User(UserID), Foreign Key(TrickID) references Trick(TrickID))"""
    create_table(db_name,"UserTrick", sql)
    print("Blank UserTrick Table Created.")
    

def create_trick_table():
    db_name="skateboard_progress_tracker.db"
    sql= """create table Trick (TrickID integer, DifficultyID integer, TrickCreator text, TrickName text, TrickDescription text, TrickObsticle text, TrickImage image, TrickTutorialLink text, TrickCompleted boolean,
    TrickCompletedDate text, Primary Key(TrickID), Foreign Key(DifficultyID) references Difficulty(DifficultyID))"""
    create_table(db_name,"Trick", sql)
    print("Blank Trick Table Created.")

def create_difficulty_table():
    db_name="skateboard_progress_tracker.db"
    sql= """create table Difficulty (DifficultyID integer, TrickDifficulty text, DifficultyDescription text, Primary Key(DifficultyID))"""
    create_table(db_name,"Difficulty", sql)
    print("Blank Difficulty Table Created.")
    

def create_user_review_table():
    db_name="skateboard_progress_tracker.db"
    sql= """create table UserReview (UserReviewID integer, UserID integer, ReviewID integer, Primary Key(UserReviewID), Foreign Key(UserID) references User(UserID), Foreign Key(ReviewID) references Review(ReviewID))"""
    create_table(db_name,"UserReview", sql)
    print("Blank UserReview Table Created.")

def create_review_table():
    db_name="skateboard_progress_tracker.db"
    sql= """create table Review (ReviewID integer, ProductID integer, ReviewCreator text, ReviewDescription text, ReviewRating integer , Primary Key(ReviewID), Foreign Key(ProductID) references Product(ProductID))"""
    create_table(db_name,"Review", sql)
    print("Blank Review Table Created.")

def create_product_table():
    db_name="skateboard_progress_tracker.db"
    sql= """create table Product(ProductID integer, ProductBrandID integer, ProductTypeID integer, ProductSizeID integer, ProductName text ,
    Primary Key(ProductID), Foreign Key(ProductBrandID) references ProductBrand(ProductBrandID),Foreign Key(ProductSizeID) references ProductSize(ProductSizeID),Foreign Key(ProductTypeID) references ProductType(ProductTypeID))"""
    create_table(db_name,"Product", sql)
    print("Blank Product Table Created.")


def create_product_brand_table():
    db_name="skateboard_progress_tracker.db"
    sql= """create table ProductBrand (ProductBrandID integer, ProductBrand text , Primary Key(ProductBrandID))"""
    create_table(db_name,"ProductBrand", sql)
    print("Blank ProductBrand Table Created.")

def create_product_type_table():
    db_name="skateboard_progress_tracker.db"
    sql= """create table ProductType (ProductTypeID integer, ProductType text , Primary Key(ProductTypeID))"""
    create_table(db_name,"ProductType", sql)
    print("Blank ProductType Table Created.")

def create_product_size_table():
    db_name="skateboard_progress_tracker.db"
    sql= """create table ProductSize (ProductSizeID integer, ProductSize text , Primary Key(ProductSizeID))"""
    create_table(db_name,"ProductSize", sql)
    print("Blank ProductSize Table Created.")

def create_user_skatepark_table():
    db_name="skateboard_progress_tracker.db"
    sql= """create table UserSkatepark (UserSkateparkID integer, UserID integer, SkateparkID integer, Primary Key(UserSkateparkID), Foreign Key(UserID) references User(UserID), Foreign Key(SkateparkID) references Skatepark(SkateparkID))"""
    create_table(db_name,"UserSkatepark", sql)
    print("Blank UserTrick Table Created.")

def create_skatepark_table():
    db_name="skateboard_progress_tracker.db"
    sql= """create table Skatepark (SkateparkID integer, SkateparkName text, SkateparkLongitude integer, SkateparkLatitude integer, SkateparkDescription text,  Primary Key(SkateparkID))"""
    create_table(db_name,"Skatepark", sql)
    print("Blank ProductType Table Created.")


if __name__=="__main__":
    create_user_table()
    create_difficulty_table()
    create_trick_table()
    create_review_table()
    create_product_brand_table()
    create_product_type_table()
    create_product_size_table()
    create_skatepark_table()
    create_user_trick_table()
    create_user_review_table()
    create_user_skatepark_table()
    create_product_table()
    
