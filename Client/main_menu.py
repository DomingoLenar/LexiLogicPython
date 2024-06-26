import os
import sys
from game2 import loader as Loader
from game2 import user_interface as GameInterface
import match_history
import leaderboards
import profile


def main_menu_prompt():
    os.system('clr||cls')
    print("****** Main Menu *******")
    print("1. Play")
    print("2. Match History")
    print("3. Leaderboards")
    print("4. Profile")
    print("5. Exit")
    print("************************")
    choice = input("choice: ")

    if choice == "1":
        loader = Loader()

        if loader.find_match():
            game = GameInterface()
            game.run()

    elif choice == "2":
        match_history.display_match_history()
    elif choice == "3":
        leaderboards.display_leaderboard()
    elif choice == "4":
        profile.display_profile()
    elif choice == "5":
        sys.exit(1)
