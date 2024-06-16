import os
import sys
import time
import login


def index_view():
    print("*****************")
    print("1. Login")
    print("2. Exit")
    print("*****************")


def index():
    while (True):
        os.system('cls||clr')
        index_view()
        user_choice = input()
        if user_choice == "1":
            login.login_view()
            break
        elif user_choice == "2":
            sys.exit(1)
        else:
            print("Invalid Choice")
            time.sleep(0.3)


if __name__ == "__main__":
    index()
