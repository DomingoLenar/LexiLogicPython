import frontend.login as login
import frontend.menu as menu
import frontend.main_menu as main_menu
import frontend.profile as profile



if __name__ == '__main__':
    choice = menu.run()
    if(choice == "Log-In"):
        authenticated = login.run()
    else:
        exit
    
    if(authenticated):
        choice = main_menu.run()
    
    if(choice == "profile"):
        profile.run()

            



