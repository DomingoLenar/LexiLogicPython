import os
from public import index as ORBConnection
from player_callback_impl import PlayerCallbackImpl

CURRENT_USER = {
    'username': None,
    'password': None,
    'player_callback': None,
    'player_callback_impl': None
}

CALLBACK_IMPL: PlayerCallbackImpl


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
    global CALLBACK_IMPL
    orb = ORBConnection.orb_connection()
    nce = ORBConnection.get_nce(orb)
    player_service_stub = ORBConnection.get_player_service_stub(nce)
    poa = ORBConnection.get_poa(orb)
    servant_player_callback = PlayerCallbackImpl()
    servant_player_callback.username = username
    CALLBACK_IMPL = servant_player_callback

    CURRENT_USER['player_callback_impl'] = servant_player_callback
    CURRENT_USER['player_callback'] = poa.servant_to_reference(servant_player_callback)
    try:
        player_service_stub.login(CURRENT_USER['player_callback'], password)
    except Exception as e:
        print(e)
    else:
        return True
