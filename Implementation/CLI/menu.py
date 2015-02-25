from database import *
from database_table_menu import *
from get_menu_option import *


def display_menu():
    print()
    print("Skateboard Progress Tracker Database Management")
    print()
    print("1. (Re)Create Database")
    print("2. Edit Profile Table")
    print("3. Edit Trick Table")
    print("4. Edit Skatepark Table")
    print("5. Edit Review Table")
    print("0. Exit")


def main():
    Finished=False
    while not Finished:
        display_menu()
        Choice=get_menu_option()
        if Choice==0:
            Finished=True
            print()
        elif Choice==1:
            Finished=database_creator()
            
            
        elif Choice==2:
            Finished=profile_table()

        elif Choice==3:
            Finished=trick_table()

        elif Choice==4:
            Finished=skatepark_table()

        elif Choice==5:
            Finished=review_table()
        else:
            print()
    print("Menu Terminated")

if __name__=="__main__":
    main()
    
