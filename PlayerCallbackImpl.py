import org
import org__POA


class Player_Callback_Impl(org__POA.amalgam.UIControllers.PlayerCallback):
    username = ""

    def __init__(self): pass

    def set_username(self, username):
        Player_Callback_Impl.username = username


if __name__ == "__main__":
    player_callback_impl = Player_Callback_Impl()
