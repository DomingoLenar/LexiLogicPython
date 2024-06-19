import json


def create_letter_box(json_string):
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


def get_current_round(json_string):
    try:
        data = json.loads(json_string)
        return data.get("current_round", None)
    except json.JSONDecodeError as e:
        print("Error parsing JSON:", e)
        return None


def get_player_info(json_string):
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


def start_game():
    # Replace for real logic
    json_string = ('{"state":"game_started","room_id":0,"current_round":5,"seconds_round_duration":30,'
                   '"round_done":false,"capacity":2,"char_matrix":[["v","e","f","h","o"],["r","u","t","j","n"],["e",'
                   '"q","d","h","w"],["p","o","u","h","u"]],"game_room":{"player_0":{"username":"Marven","points":100,'
                   '"ready":true,"words":[],"duped_words":[]},"player_1":{"username":"Mark","points":50,"ready":true,'
                   '"words":[],"duped_words":[]},"player_2":{"username":"Sarah","points":75,"ready":true,"words":[],'
                   '"duped_words":[]},"player_3":{"username":"Emily","points":120,"ready":true,"words":[],"duped_words":[]},'
                   '"rounds":{"round_1":"No Winner","round_2":"Marven","round_3":"No Winner","round_4":"Marven"}}}')

    current_round = get_current_round(json_string)
    print("Current Round:", current_round)

    letter_box = create_letter_box(json_string)
    if letter_box:
        for row in letter_box:
            print(row)

    submitted_word = input("\nEnter a word (5 Letters Or More)\n")

    # Replace for real logic
    calculated_points = 10

    print("\nSubmitted word:", submitted_word, "\nPoints:", calculated_points)

    print("\nLeaderboard: ")
    players_info = get_player_info(json_string)
    if players_info:
        sorted_players = sorted(players_info, key=lambda x: x['Points'], reverse=True)
        for player_info in sorted_players:
            print(f"Username: {player_info['Username']} Points: {player_info['Points']}")
