import os
import asyncio
import json
import login
from update_dispatcher import UpdateDispatcher
from public import index as ORBConnection


class user_interface(UpdateDispatcher):
    def __init__(self):
        response:str

    def update(self, json_string: str):
        self.response = json_string

    def run(self):
        self.init_components()
        while not self.response == 'game_ended':
            print("GAME STATE: "+self.response)
            pass


    def init_components(self):
        try:
            login.CALLBACK_IMPL.controller_interface(self)
            game_room = 0 #this is a dummy value for now
            orb = login.orb
            nce = ORBConnection.get_nce(orb)
            game_service_stub = ORBConnection.get_game_service_stub(nce)
            print("Hanshake in progress")
            game_service_stub.readyHandshake(os.environ['username'], game_room)
            print("Handshake success")
        except Exception as e:
            print(e)


class loader():
    def find_match(self):
        orb = login.orb
        nce = ORBConnection.get_nce(orb)
        game_service_stub = ORBConnection.get_game_service_stub(nce)
        response = game_service_stub.matchMake(login.CALLBACK_IMPL)

        status = self.parse_match_making(response)

        if status == 'timeout':
            print("MATCHMAKE FAILED")
            return False
            pass
        else:
            return True

    def parse_match_making(self, json_string:str):
        data = json.loads(json_string)
        status = data['status']
        return status