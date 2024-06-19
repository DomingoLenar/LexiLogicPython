import frontend.login as login
import frontend.menu as menu
import frontend.main_menu as main_menu
import frontend.profile as profile
import frontend.leaderboards as leaderboards


def main():
    choice = menu.run()
    if choice == "Log-In":
        authenticated = login.run()
        if authenticated:
            choice = main_menu.run()
            if choice == "profile":
                profile.run()
            elif choice == "leaderboards":
                leaderboards.run()
    elif choice == "Exit":
        exit()

if __name__ == "__main__":
    main()
            



