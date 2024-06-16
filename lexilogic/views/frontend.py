import runpy
# def main():
#     login = runpy.run_path(path_name="lexilogic/frontend/login.py")
#     menu = runpy.run_path(path_name="lexilogic/frontend/index.py")
#     main_menu = runpy.run_path(path_name="lexilogic/frontend/main_menu.py")
#     profile = runpy.run_path(path_name="lexilogic/frontend/profile.py")
#     leaderboards = runpy.run_path(path_name="lexilogic/frontend/leaderboards.py")
#
#     choice = menu.run()
#     if choice == "Log-In":
#         authenticated = login.run()
#         if authenticated:
#             choice = main_menu.run()
#             if choice == "profile":
#                 profile.run()
#             elif choice == "leaderboards":
#                 leaderboards.run()
#     elif choice == "Exit":
#         exit()
#
# if __name__ == "__main__":
#     main()
# TODO: relate this file on index.py (i.e., main entry point)