import os
import time
import asyncio
import json
import login
from update_dispatcher import UpdateDispatcher
from public import index as ORBConnection
from Core import json_parser

RESPONSE = {
    'response': None
}


class user_interface(UpdateDispatcher):
    response: str
    game_room_id = 0

    def __init__(self):
        self.response = ""

    def update(self, json_string: str):
        print(json_string)
        self.response = json_string

    def run(self):
        self.init_components()
        while not self.response == 'game_ended':
            pass
        print("GAME_ENDED")

    def init_components(self):
        global RESPONSE
        try:
            self.game_room_id = json_parser.parse_status_state(RESPONSE['response'])
            orb = login.orb
            nce = ORBConnection.get_nce(orb)
            game_service_stub = ORBConnection.get_game_service_stub(nce)
            print("Hanshake in progress")
            game_service_stub.readyHandshake(os.environ['username'], self.game_room_id)
            print("Handshake success")
            print("5 second Countdown")
            time.sleep(5)
            game_service_stub.playerReady(os.environ['username'], self.game_room_id)
            print("Player Sent ready")
        except Exception as e:
            print(e)


class loader():
    def find_match(self):
        global RESPONSE
        orb = login.orb
        nce = ORBConnection.get_nce(orb)
        poa = ORBConnection.get_poa(orb)
        game_service_stub = ORBConnection.get_game_service_stub(nce)
        RESPONSE['response'] = game_service_stub.matchMake(poa.servant_to_reference(login.CALLBACK_IMPL))

        status = self.parse_match_making(RESPONSE['response'])

        if status == 'timeout':
            print("MATCHMAKE FAILED")
            return False
            pass
        else:
            print(RESPONSE['response'])
            return True

    def parse_match_making(self, json_string):
        data = json.loads(json_string)
        status = data['status']
        return status
