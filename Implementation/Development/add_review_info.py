import sqlite3

def add_review_type():
    Finished=False
    while not Finished:
        values=input("Enter Type: ")
        values=(values,)
        if values == ("0",):
            Finished=True
            return False
        else:
        
            with sqlite3.connect("skateboard_progress_tracker.db") as db:
                cursor = db.cursor()
                sql="insert into ProductType(ProductType) values (?)"
                cursor.execute(sql,values)
                db.commit()
                
                
            
    

def add_review_size():
        values=[]
        for value in values:
            values=(value,)
            if values == ("0",):
                Finished=True
                return False
            else:
            
                with sqlite3.connect("skateboard_progress_tracker.db") as db:
                    cursor = db.cursor()
                    sql="insert into ProductSize(ProductSize) values (?)"
                    cursor.execute(sql,values)
                    db.commit()
                

def add_review_brand():
        values=["Shake Junt", "Thunder" ]
        for value in values:
            values=(value,)
            if values == ("0",):
                Finished=True
                return False
            else:
        
                with sqlite3.connect("skateboard_progress_tracker.db") as db:
                    cursor = db.cursor()
                    sql="insert into ProductBrand(ProductBrand) values (?)"
                    cursor.execute(sql,values)
                    db.commit()

def remove():
    data=7
    data=(data,)
    with sqlite3.connect("skateboard_progress_tracker.db") as db:
            cursor=db.cursor()
            sql="delete from ProductType where ProductTypeID=?"
            cursor.execute(sql,data)
            db.commit()
            print()
            print("Trick Successfully Deleted.")
            print()

                


def get_menu_option():
    Option=int(input("Please select an option: "))
    return Option


def display_menu():
    print()
    print("Review Menu")
    print("1. Add Review Type")
    print("2. Add review Size")
    print("3. Add review Brand")
    print()
    print("4. Remove")
    print()

def main():
    Finished=False
    while not Finished:
        display_menu()
        Choice=get_menu_option()
        if Choice==0:
            Finished=True
            print()
        elif Choice==1:
            Finished=add_review_type()
            
            
        elif Choice==2:
            Finished=add_review_size()

        elif Choice==3:
            Finished=add_review_brand()

        elif Choice==4:
            Finished=remove()
        else:
            print()
    print("Menu Terminated")


if __name__=="__main__":
    main()
    
