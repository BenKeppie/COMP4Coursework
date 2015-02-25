from profile_edit_options import *
from trick_edit_options import *
from skatepark_edit_options import *
from review_edit_options import *
from get_menu_option import *
from database import *
from menu import *

def database_creator_menu():
    print()
    print("Database Table Management")
    print()
    print("1.  (Re)Create All Tables")
    print("2.  (Re)Create User Table")
    print("3.  (Re)Create Difficulty Table")
    print("4.  (Re)Create Trick Table")
    print("5.  (Re)Create Review Table")
    print("6.  (Re)Create Product Brand Table")
    print("7.  (Re)Create Product Type Table")
    print("8.  (Re)Create Product Size Table")
    print("9.  (Re)Create Skatepark Table")
    print("10. (Re)Create User Trick Table")
    print("11. (Re)Create User Review Table")
    print("12. (Re)Create User Skatepark Table")
    print("13. (Re)Create Review Table")
    print("0. Exit")

def database_creator():
    Finished=False
    while not Finished:
        database_creator_menu()
        Choice=get_menu_option()
        if Choice==0:
            return False
        elif Choice==1:
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
            Finished=create_product_table()
            
        elif Choice == 2:
            create_user_table()
        elif Choice == 3:
            create_difficulty_table()
        elif Choice == 4:
            create_trick_table()
        elif Choice ==5:
            create_review_table()
        elif Choice==6:
            create_product_brand_table()
        elif Choice==7:
            create_product_type_table()
        elif Choice==8:
            create_product_size_table()
        elif Choice==9:
            create_skatepark_table()
        elif Choice==10:
            create_user_trick_table()
        elif Choice==11:
            create_user_review_table()
        elif Choice==12:
            create_user_skatepark_table()
        elif Choice==13:
            create_product_table()
            
            
            
            
            

def profile_table_menu():
    print()
    print("Profile Table Management")
    print()
    print("1. Add Profile")
    print("2. Change Name")
    print("3. Change Email")
    print("4. Change Picture")
    print("5. Delete Profile")
    print("0. Exit")

def profile_table():
    Finished=False
    while not Finished:
        profile_table_menu()
        Choice=get_menu_option()
        if Choice==0:
            return False
        elif Choice==1:
            Finished=add_profile()
            
        elif Choice == 2:
            Finished=change_name()
        elif Choice == 3:
            Finished=change_email()
        elif Choice == 4:
            Finished=change_picture()
        elif Choice ==5:
            Finished=delete_profile()

    
def trick_table_menu():
    print()
    print("Trick Table Management")
    print()
    print("1. Add a New Trick")
    print("2. Edit an Existing Trick")
    print("3. Delete an Existing Trick")
    print("0. Exit")

def trick_table():
    Finished=False
    while not Finished:
        trick_table_menu()
        Choice=get_menu_option()
        if Choice==0:
            return False
            
        elif Choice == 1:
            Finished=add_trick()
        elif Choice == 2:
            Finished=edit_trick()
        elif Choice == 3:
            Finished=delete_trick()


def skatepark_table_menu():
    print()
    print("Skatepark Table Management")
    print()
    print("1. Add a New Skatepark")
    print("2. Edit an Existing Skatepark")
    print("3. Delete an Existing Skatepark")
    print("0. Exit")

def skatepark_table():
    Finished=False
    while not Finished:
        skatepark_table_menu()
        Choice=get_menu_option()
        if Choice==0:
            return False
        elif Choice == 1:
            Finsihed=add_skatepark()
        elif Choice == 2:
            Finished=edit_skatepark()
        elif Choice == 3:
            Finished=delete_skatepark()


def review_table_menu():
    print()
    print("Skatepark Table Management")
    print()
    print("1. Add a New Review")
    print("2. Edit an Existing Review")
    print("3. Delete an Existing Review")
    print("4. Filter Brand")
    print("5. Filter Type")
    print("6. Filter Size")
    print("0. Exit")
    
def review_table():
    Finished=False
    while not Finished:
        review_table_menu()
        Choice=get_menu_option()
        if Choice==0:
            return False
        elif Choice == 1:
            
            Finished=add_review()
        elif Choice == 2:
            Finishededit_review()
        elif Choice == 3:
            Finished=delete_review()
        elif Choice==4:
            Finished=filter_brand()
        elif Choice ==5():
            Finished=filter_type()
        elif Choice==6():
            Finished=filter_size()

if __name__=="__main__":
    pass
    
        
