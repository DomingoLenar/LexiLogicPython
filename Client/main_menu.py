import os
import sys
import match_history
import leaderboards
import profile
import game
import login



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
        obj_game = game.Game()
        login.CURRENT_USER['player_callback_impl'].controller_interface(obj_game)
        obj_game.find_match()
    elif choice == "2":
        match_history.display_match_history()
    elif choice == "3":
        leaderboards.display_leaderboard()
    elif choice == "4":
        profile.display_profile()
    elif choice == "5":
        sys.exit(1)
