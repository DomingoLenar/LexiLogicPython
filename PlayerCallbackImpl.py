import org
import org__POA

print("org",dir(org.UIControllers_idl._0_org.amalgam.UIControllers.PlayerCallback))
print(dir(org__POA.amalgam.UIControllers.PlayerCallback))
class Player_Callback_Impl(org__POA.amalgam.UIControllers.PlayerCallback):
    username = ""
    def __init__(self): pass

    def set_username(self, username):
        username = username

if __name__ == "__main__":
    player_callback_impl = Player_Callback_Impl()
    player_callback_impl.username = "Lou"
    print(player_callback_impl.username)
    print(dir(player_callback_impl))
