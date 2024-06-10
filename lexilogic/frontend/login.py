import getpass
import os

def run():
    os.system('cls||clr')
    print("***** Log-In ****")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    print(f"Username: {username}")
    print(f"Password: [HIDDEN]")

    #Insert logic to check if valid
    os.environ['username'] = username

    return True

if __name__ == '__main__':
    run()