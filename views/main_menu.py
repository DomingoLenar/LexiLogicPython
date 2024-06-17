import os
import sys
import game
import match_history
import leaderboards
import profile


def main_menu_prompt():
    while True:
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
            return game.start_game()
        elif choice == "2":
            return match_history.display_match_history()
        elif choice == "3":
            return leaderboards.display_leaderboard()
        elif choice == "4":
            return profile.display_profile()
        elif choice == "5":
            sys.exit(1)
