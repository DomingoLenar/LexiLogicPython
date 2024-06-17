import json
from Utilities.Reference_Objects import LeaderBoard


def parse_leaderboard_json_string(json_string):
    data = json.loads(json_string)
    leaderboard_entries = data['leaderboard']
    leaderboard_list = []
    for idx, entry in enumerate(leaderboard_entries, start=1):
        leaderboard_item = LeaderBoard.LeaderBoard(
            leader_board_id=idx,
            username=entry['username'],
            points=entry['pts'],
            rank=entry['rank']
        )
        leaderboard_list.append(leaderboard_item)

    return leaderboard_list


if __name__ == '__main__':
    json_string = '{"object":"leaderboard","leaderboard":[{"username":"Lou","pts":1750,"rank":1},{"username":"Lenar","pts":1290,"rank":2},{"username":"Geo","pts":760,"rank":3},{"username":"Mark","pts":760,"rank":3},{"username":"Gebreyl","pts":730,"rank":5},{"username":"Marven","pts":640,"rank":6}]}'
    # json_string = "{"object":"leaderboard","leaderboard":[{"username":"Lou","pts":1750,"rank":1},{"username":"Lenar","pts":1290,"rank":2},{"username":"Geo","pts":760,"rank":3},{"username":"Mark","pts":760,"rank":3},{"username":"Gebreyl","pts":730,"rank":5},{"username":"Marven","pts":640,"rank":6}]}"
    data = json.loads(json_string)
    print(dir(data))
    # print(dir(LeaderBoard.LeaderBoard))
    leaderboard_entries = data['leaderboard']
    print(leaderboard_entries)
    leaderboard_list = []
    for idx, entry in enumerate(leaderboard_entries, start=1):
        leaderboard_item = LeaderBoard.LeaderBoard(
            leader_board_id=idx,
            username=entry['username'],
            points=entry['pts'],
            rank=entry['rank']
        )
        leaderboard_list.append(leaderboard_item)

    for item in leaderboard_list:
        print(item.get_username(), item.get_points(), item.get_rank())
    # json.dumps()
    # parse_json_string()
