from public import index
import PlayerCallbackImpl
import org
orb = index.orb_connection()
nce = index.get_nce(orb)
pss = index.get_player_service_stub(nce)
servant_player_callback_impl = PlayerCallbackImpl.Player_Callback_Impl()
servant_player_callback_impl.username = "Marven"
poa = index.get_poa(orb)
obj_ref_player_callback = poa.servant_to_reference(servant_player_callback_impl)
print("obj_ref dir:", (obj_ref_player_callback.Session))
# pss.changeUsername("Dagul", "Lou")
# pss.login(obj_ref_player_callback, "pass123")