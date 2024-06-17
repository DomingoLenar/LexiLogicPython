def get_leaderboard_data():
    # Function to fetch leaderboard data from a database or file
    leaderboard_data = [
        {'name': 'Lestat', 'score': 1200},
        {'name': 'Marven', 'score': 1050},
        {'name': 'Lenar', 'score': 980467},
        {'name': 'Gebreyl', 'score': 3482}
    ]
    return leaderboard_data


def display_leaderboard_prompt(leaderboard_data):
    sorted_data = sorted(leaderboard_data, key=lambda entry: entry['score'], reverse=True)

    print("****** Leaderboard *******")
    print("Rank | Name      | Score")
    print("------------------------")
    for i, entry in enumerate(sorted_data, start=1):
        print(f"{i:3d} | {entry['name']:10s} | {entry['score']}")
    print("************************")


def display_leaderboard():
    leaderboard_data = get_leaderboard_data()
    display_leaderboard_prompt(leaderboard_data)
