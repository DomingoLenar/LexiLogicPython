import json
import os
import login
from player_callback_impl import PlayerCallbackImpl
from public import index as ORBConnection
from Core import json_parser
from update_dispatcher import UpdateDispatcher

RESPONSE = {
    'response': None
}



class Game(UpdateDispatcher):
    game_room_id = None

    def __init__(self):
        pass

    def update(self, json_string):
        print("GAME UPDATE:", json_string)
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
            # countdown = self.get_countdown(json_string)
            # print("GAME STARTING IN..")
            # while countdown != 0:
            #     print(countdown)
            #     countdown -= 1
            #     time.sleep(1)
            #
            # print("SET PLAYER READY")
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

    def find_match(self):
        global RESPONSE
        print("FINDING MATCH")
        orb = ORBConnection.orb_connection()
        nce = ORBConnection.get_nce(orb)
        game_service_stub = ORBConnection.get_game_service_stub(nce)
        RESPONSE['response'] = game_service_stub.matchMake(
            login.CURRENT_USER['poa'].servant_to_reference(login.CURRENT_USER['player_callback_impl']))
        status = json_parser.parse_match_making(RESPONSE['response'])

        if status == 'timeout':
            # back to main menu
            print("GAME FAILED")
            return False
        elif status == 'success':
            self.init_components()
            return True

    def init_components(self):
        try:
            self.game_room_id = json_parser.parse_game_room(RESPONSE['response'])
            orb = ORBConnection.orb_connection()
            nce = ORBConnection.get_nce(orb)
            game_service_stub = ORBConnection.get_game_service_stub(nce)
            print("invoking handshake")
            game_service_stub.readyHandshake(login.CURRENT_USER['username'], self.game_room_id)
            print("Handshake success")
        except Exception as e:
            print(e)

        # maintain main thread on run
        while True:
            pass

        # # Replace for real logic
        # json_string = ('{"state":"game_started","room_id":0,"current_round":5,"seconds_round_duration":30,'
        #                '"round_done":false,"capacity":2,"char_matrix":[["v","e","f","h","o"],["r","u","t","j","n"],["e",'
        #                '"q","d","h","w"],["p","o","u","h","u"]],"game_room":{"player_0":{"username":"Marven","points":100,'
        #                '"ready":true,"words":[],"duped_words":[]},"player_1":{"username":"Mark","points":50,"ready":true,'
        #                '"words":[],"duped_words":[]},"player_2":{"username":"Sarah","points":75,"ready":true,"words":[],'
        #                '"duped_words":[]},"player_3":{"username":"Emily","points":120,"ready":true,"words":[],"duped_words":[]},'
        #                '"rounds":{"round_1":"No Winner","round_2":"Marven","round_3":"No Winner","round_4":"Marven"}}}')
        #
        # current_round = Game.get_current_round(json_string)
        # print("Current Round:", current_round)
        #
        # letter_box = Game.create_letter_box(json_string)
        # if letter_box:
        #     for row in letter_box:
        #         print(row)
        #
        # submitted_word = input("\nEnter a word (5 Letters Or More)\n")
        #
        # # Replace for real logic
        # calculated_points = 10
        #
        # print("\nSubmitted word:", submitted_word, "\nPoints:", calculated_points)
        #
        # print("\nLeaderboard: ")
        # players_info = Game.get_player_info(json_string)
        # if players_info:
        #     sorted_players = sorted(players_info, key=lambda x: x['Points'], reverse=True)
        #     for player_info in sorted_players:
        #         print(f"Username: {player_info['Username']} Points: {player_info['Points']}")

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


if __name__ == "__main__":
    print(dir(Game))
