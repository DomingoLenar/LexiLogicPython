class Lobby:
    def __init__(self, lobby_id=None, winner=None):
        self._lobby_id = lobby_id
        self._winner = winner

    # Getter
    def get_lobby_id(self):
        return self._lobby_id

    def get_winner(self):
        return self._winner

    # Setter
    def set_lobby_id(self, value):
        self._lobby_id = value

    def set_winner(self, value):
        self._winner = value