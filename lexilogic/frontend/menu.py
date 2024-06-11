import os
import sys
import time


def show():
    print("*****************")
    print("1. Login")
    print("2. Exit")
    print("*****************")

def run():
    while(True):
        os.system('cls||clr')
        show()
        userChoice = input()
        if(userChoice == "1"):
            print("Valid")
            break
        elif(userChoice == "2"):
            sys.exit(1)
        else:
            print("Invalid Choice")
            time.sleep(0.3)
    return "Log-In"

if __name__ == '__main__':
    run()