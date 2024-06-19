import os
from public import index as ORBConnection
import player_callback_impl

CURRENT_USER = {
    'username': None,
    'password': None,
    'player_callback': None
}


def login_view():
    global CURRENT_USER
    while True:
        os.system('cls||clr')
        print("***** Log-In ****")
        username = input("Username: ")
        password = input("Password: ")
        if authenticate(username, password):
            CURRENT_USER['username'] = username
            CURRENT_USER['password'] = password
            break

    os.environ['username'] = username

    return True


def authenticate(username: str, password: str):
    global CURRENT_USER
    orb = ORBConnection.orb_connection()
    nce = ORBConnection.get_nce(orb)
    player_service_stub = ORBConnection.get_player_service_stub(nce)
    poa = ORBConnection.get_poa(orb)
    servant_player_callback = player_callback_impl.PlayerCallbackImpl()
    print(servant_player_callback.username())
    servant_player_callback.username = username
    CURRENT_USER['player_callback'] = poa.servant_to_reference(servant_player_callback)
    try:
        player_service_stub.login(CURRENT_USER['player_callback'], password)
    except Exception as e:
        print(e)
    else:
        return True
