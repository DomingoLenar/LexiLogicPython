import os
import time
import asyncio
import json
import login
from Client.game import RESPONSE
from Core import json_parser
from update_dispatcher import UpdateDispatcher
from public import index as ORBConnection


class user_interface(UpdateDispatcher):
    # response: str
    game_room_id = 0

    def __init__(self):
        self.response = ""

    def update(self, json_string: str):
        # self.response = json_string
        self.update_data(json_string)

    def update_data(self, json_string):
        print("GAME UPDATE DATA")
        state = json_parser.parse_status_state(json_string)
        room_id = json_parser.parse_room(json_string)

        if state == "staging":
            print("Round ", self.get_current_round(json_string))
            letter_box = self.create_letter_box(json_string)
            if letter_box:
                for row in letter_box:
                    print(row)
            # todo: raises a bug where another player game_started json string isn't returned
            countdown = self.get_countdown(json_string)
            print("GAME STARTING IN..")
            while countdown != 0:
                print(countdown)
                countdown -= 1
                time.sleep(1)
            print("SET PLAYER READY")
            self.set_ready(login.CURRENT_USER['username'], room_id)
            pass

        if state == "game_started":
            print("GAME START")
            word = input("\nEnter a word (5 Letters Or More)\n")
            print("SUBMITTING A WORD...")
            try:
                self.submit_word(word, login.CURRENT_USER['username'], room_id)
            except Exception as e:
                print(e)
            # calculated_points = 10
            # print("\nSubmitted word:", word, "\nPoints:", calculated_points)
            pass

        if state == "game_done":
            self.check_winner(json_string)
            pass

        if state == "invalid_word":
            print("INVALID WORD, please try again")
            pass

        pass


    def run(self):
        self.init_components()
        # while not self.response == 'game_ended':
        #     pass
        while True:
            pass

        # print("GAME_ENDED")

    def init_components(self):
        try:
            # game_room = 0  #this is a dummy value for now
            self.game_room_id = json_parser.parse_game_room(RESPONSE['response'])
            orb = login.orb
            nce = ORBConnection.get_nce(orb)
            game_service_stub = ORBConnection.get_game_service_stub(nce)
            print("Hanshake in progress")
            game_service_stub.readyHandshake(os.environ['username'], self.game_room_id)
            print("Handshake success")
            # print("5 second Countdown")
            # countdown = self.get_countdown(self.response)
            # print("GAME STARTING IN..")
            # while countdown != 0:
            #     print(countdown)
            #     countdown -= 1
            #     time.sleep(1)
            # game_service_stub.playerReady(os.environ['username'], self.game_room_id)
            # print("Player Sent ready")
        except Exception as e:
            print(e)

    def create_letter_box(self, json_string):
        try:
            data = json.loads(json_string)
            char_matrix = data.get("char_matrix", None)
            if not char_matrix:
                print("Character matrix not found in JSON.")
                return None
            return char_matrix
        except json.JSONDecodeError as e:
            print("Error parsing JSON:", e)
            return None

    def get_current_round(self, json_string):
        try:
            data = json.loads(json_string)
            return data.get("current_round", None)
        except json.JSONDecodeError as e:
            print("Error parsing JSON:", e)
            return None

    def get_player_info(self, json_string):
        try:
            data = json.loads(json_string)
            players = []
            for key, player_info in data["game_room"].items():
                if key.startswith("player_"):
                    username = player_info["username"]
                    points = player_info["points"]
                    players.append({"Username": username, "Points": points})
            return players
        except json.JSONDecodeError as e:
            print("Error parsing JSON:", e)
            return None

    def submit_word(self, word, username, game_room_id):
        orb = ORBConnection.orb_connection()
        nce = ORBConnection.get_nce(orb)
        game_service_stub = ORBConnection.get_game_service_stub(nce)
        game_service_stub.verifyWord(word, username, game_room_id)

    def set_ready(self, username, room_id):
        orb = ORBConnection.orb_connection()
        nce = ORBConnection.get_nce(orb)
        game_service_stub = ORBConnection.get_game_service_stub(nce)
        game_service_stub.playerReady(username, room_id)
        pass

    def check_winner(self, json_string):
        data = json.loads(json_string)
        winner = data["winner"]
        print("Winner", winner)

        if login.CURRENT_USER['username'] == winner:
            print("VICTORY")
        else:
            print("DEFEAT")

        pass

    def get_countdown(self, json_string):
        data = json.loads(json_string)
        countdown = data['countdown']
        return int(countdown)
        pass

    def get_round_duration(self, json_string):
        data = json.loads(json_string)
        round_duration = data['seconds_round_duration']
        return int(round_duration)
        pass


class loader():
    def find_match(self):
        orb = login.orb
        nce = ORBConnection.get_nce(orb)
        poa = ORBConnection.get_poa(orb)
        game_service_stub = ORBConnection.get_game_service_stub(nce)
        response = game_service_stub.matchMake(poa.servant_to_reference(login.CALLBACK_IMPL))

        status = self.parse_match_making(response)

        if status == 'timeout':
            print("MATCHMAKE FAILED")
            return False
            pass
        else:
            return True

    def parse_match_making(self, json_string: str):
        data = json.loads(json_string)
        status = data['status']
        return status
