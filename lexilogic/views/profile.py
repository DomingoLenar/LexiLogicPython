import os
import getpass
import time

def run():
    while(True):
        os.system('cls||clr')
        username = os.environ.get("username")
        print(f"Username: {username}")
        print("**********************")
        print("1. Change Username")
        print("2. Change Password")
        print("3. Back")
        print("**********************")
        choice = input("Choice: ")

def change_password():
    while(True):
        os.system('cls||clr')
        print("**** Change Password *******")
        prev_pass = getpass.getpass("Old Password: ")
        # add logic to validate if old_pass is correct 
        valid = True
        if(valid):
            break

    while(True):
        os.system('clr||cls')
        print("**** Change Password *******")
        new_pass = getpass.getpass("New Password: ")
        confirmation = getpass.getpass("Confirm Password: ")
        if(new_pass == confirmation):
            break
        else:
            print("Confirmation is not the same please enter again")
            time.sleep(0.4)

def change_username():
    while(True):
        os.system('cls||clr')
        currentUsername = os.environ('username')
        print("******* Change Username ********")
        newUsername = input("Enter New Username: ")
        if(not currentUsername == newUsername and check_username_existence(newUsername)):
            #call dal to updater username in the database
            break
        else:
            print("Username is invalid, username already exists or is the same as the current username")

def check_username_existence(uname: str):
    #Use DAL to check if username is already taken
    return True

def change_username():
    print()