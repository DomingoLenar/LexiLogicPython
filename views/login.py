import os
from public import index as ORBConnection
import PlayerCallbackImpl


def login_view():
    while True:
        os.system('cls||clr')
        print("***** Log-In ****")
        username = input("Username: ")
        password = input("Password: ")
        if authenticate(username, password):
            break

    print(f"Username: {username}")
    print(f"Password: [HIDDEN]")

    #Insert logic to check if valid
    os.environ['username'] = username

    return True


def authenticate(username: str, password: str):
    print(username)
    print(password)
    orb = ORBConnection.orb_connection()
    nce = ORBConnection.get_nce(orb)
    player_service_stub = ORBConnection.get_player_service_stub(nce)
    poa = ORBConnection.get_poa(orb)
    servant_player_callback = PlayerCallbackImpl.Player_Callback_Impl()
    servant_player_callback.username = username
    obj_ref_player_callback = poa.servant_to_reference(servant_player_callback)
    try:
        player_service_stub.login(obj_ref_player_callback, password)
    except Exception as e:
        print(e)
    else:
        return True
