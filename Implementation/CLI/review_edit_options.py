import sqlite3

def get_product_id():
    value=int(input("Please enter the product id of the product you wish to review: "))
    with sqlite3.connect("skateboard_progress_tracker.db") as db:
        cursor=db.cursor()
        cursor.execute("select ProductID from Product where ProductID=?",(value,))
        ProductID=cursor.fetchone()
        return productID

def get_review_creator():
    with sqlite3.connect("skateboard_progress_tracker.db") as db:
        cursor=db.cursor()
        cursor.execute("select FirstName,LastName from User where UserID=?",(1,))
        User=cursor.fetchone()
        User= ("{0} {1}".format(User[0], User[1]))
        return User

def get_review_description():
    ReviewDescription=input("Please enter a description for your review: ")
    return ReviewDescription

def get_review_rating():
    Finished=False
    while not Finished:
        ReviewRating=int(input("Please rate the product: (1-5) "))
        if (ReviewRating>0) and (ReviewRating<=5):
            Finished=True
            print()
        else:
            print("Invalid entry")
            print()
    return ReviewRating



def add_review():
    ProductID= get_product_id
    ReviewCreator=get_review_creator()
    ReviewDescription=get_review_description()
    ReviewRating=get_review_rating()
    
    values=(ProductID,ReviewCreator,ReviewDescription,ReviewRating)
    with sqlite3.connect("skateboard_progress_tracker.db") as db:
        cursor = db.cursor()
        sql="insert into Review(ProductID, ReviewCreator,ReviewDescription,ReviewRating) values (?,?,?,?)"
        cursor.execute(sql,values)
        db.commit()
        print()
        print("Review Successfully Created.")
        print()

def edit_review():
    TrickID=int(input("Please enter the TrickID of the trick you wish to edit: "))
    ProductID=get_product_id()
    ReviewCreator=get_review_creator()
    ReviewDescription=get_review_description()
    ReviewRating=get_review_rating()
    
    values=(ProductID,ReviewCreator,ReviewDescription,ReviewRating,TrickID)
    with sqlite3.connect("skateboard_progress_tracker.db") as db:
        cursor = db.cursor()
        sql="update Review set ProductID=?, ReviewCreator=?, ReviewDescription=?, ReviewRating=?   where TrickID=?"
        cursor.execute(sql,values)
        db.commit()


def delete_review():
    data=int(input("Please enter the ReviewID of the review you wish to delete: "))
    data=(data,)
    with sqlite3.connect("skateboard_progress_tracker.db") as db:
            cursor=db.cursor()
            sql="delete from Review where ReviewID=?"
            cursor.execute(sql,data)
            db.commit()
            print()
            print("Review Successfully Deleted.")
            print()

def filter_size():
    pass

def filter_brand():
    pass

def filter_size():
    pass
