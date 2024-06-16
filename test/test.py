import index
import PlayerCallbackImpl
import org
orb = index.orb_connection()
nce = index.get_nce(orb)
pss = index.get_player_service_stub(nce)
player_callback_impl = PlayerCallbackImpl.Player_Callback_Impl()
player_callback_impl.username = "Lou"
player_callback = org.UIControllers_idl._0_org.amalgam.UIControllers.PlayerCallback
print(dir(player_callback))
print(dir(player_callback_impl))
poa = index.get_poa(orb)
print(dir(poa))
player_callback = nce._narrow(poa.servant_to_reference(player_callback_impl))
# print(dir(orb))
# print(dir(org.amalgam.UIControllers.PlayerCallback))
print("pss",dir(pss))
# pss.changeUsername("Dagul", "Lou")
# pss.login(player_callback, "pass123")

# TODO:
#  Traceback (most recent call last):
#  File "C:\Users\loudi\PycharmProjects\2024-2_9329_finteam1_python\test.py", line 22, in <module>
#     pss.login(player_callback, "pass123") # TODO:
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\loudi\PycharmProjects\2024-2_9329_finteam1_python\PlayerService_idl.py", line 117, in login
#     return self._obj.invoke("login", _0_org.amalgam.Service.PlayerServiceModule.PlayerService._d_login, args)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# omniORB.CORBA._omni_sys_exc: CORBA.UNKNOWN(0x535500ca, CORBA.COMPLETED_MAYBE)