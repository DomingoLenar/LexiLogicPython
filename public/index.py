import os

os.environ['ORBInitRef'] = 'NameService=corbaloc::corbaserver:2121/NameService'
import sys
from omniORB import CORBA
import CosNaming, PortableServer
from org.amalgam import Service  # REQUIRED


def orb_connection():
    # Initialize the ORB
    orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
    return orb


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
    poa_manager = orb.resolve_initial_references("RootPOA")
    poa = poa_manager._narrow(PortableServer.POA)
    poa.the_POAManager.activate()
    return poa


if __name__ == "__main__":
    orb = orb_connection()
    get_poa(orb)
    nce = get_nce(orb)
    pss = get_player_service_stub(nce)
    gss = get_game_service_stub(nce)
