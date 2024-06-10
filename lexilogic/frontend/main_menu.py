import os
import sys

def run():
    while(True):
        os.system('clr||cls')
        print("****** Main Menu *******")
        print("1. Play")
        print("2. Match History")
        print("3. Leaderboards")
        print("4. Profile")
        print("5. Exit")
        print("************************")
        choice = input("choice: ")

        if(choice == "1"):
            return "play"
        elif(choice == "2"):
            return "match_history"
        elif(choice == "3"):
            return "leaderboards"
        elif(choice == "4"):
            return "profile"
        elif(choice == "5"):
            sys.exit(1)