import os

os.environ['ORBInitRef'] = 'NameService=corbaloc::corbaserver:2121/NameService'
import sys
from omniORB import CORBA
import CosNaming, PortableServer
from org.amalgam import Service  # REQUIRED


def orb_connection():
    # Initialize the ORB
    orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
    # print("ORB", dir(orb))
    # Obtain a reference to the root naming context ext
    # root_nce = orb.resolve_initial_references("NameService")
    # print("ROOTNCE", dir(root_nce))
    # child_nce = root_nce._narrow(CosNaming.NamingContextExt)
    return orb
    # print("NCE", dir(child_nce))
    # print(player_service_stub)
    # print(dir(player_service_stub))
    # return player_service_stub, game_service_stub


def get_nce(orb):
    root_nce = orb.resolve_initial_references("NameService")
    child_nce = root_nce._narrow(CosNaming.NamingContextExt)
    return child_nce


def get_player_service_stub(nce):
    player_service_stub = nce.resolve_str("PlayerService")
    return player_service_stub


def get_game_service_stub(nce):
    game_service_stub = nce.resolve_str("GameService")
    return game_service_stub


def get_poa(orb):
    # print(dir(orb))
    # poa_helper = PortableServer.POA
    # poa_manager = PortableServer.POAManager
    # print(dir(poa_helper))
    # print(dir(PortableServer))
    # poa = poa_manager._narrow(orb.resolve_initial_references("RootPOA"))
    poa_manager = orb.resolve_initial_references("RootPOA")
    # print(dir(poa_manager))
    poa = poa_manager._narrow(PortableServer.POA)
    poa.the_POAManager.activate()
    # print("POA",dir(poa))
    return poa


if __name__ == "__main__":
    orb = orb_connection()
    get_poa(orb)
    nce = get_nce(orb)
    pss = get_player_service_stub(nce)
    gss = get_game_service_stub(nce)

    print(dir(pss))
    print(dir(gss))
