import getpass
import os

def run():
    while(True):
        os.system('cls||clr')
        print("***** Log-In ****")
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        if(authenticate(username, password)):
            break
    

    print(f"Username: {username}")
    print(f"Password: [HIDDEN]")

    #Insert logic to check if valid
    os.environ['username'] = username

    return True

def authenticate(username: str, password: str):
    #Use DAL here to authenticate credentials and return boolean
    return True

if __name__ == '__main__':
    run()