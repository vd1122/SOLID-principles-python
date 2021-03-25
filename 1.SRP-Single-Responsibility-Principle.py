"""
SRP --> Single Responsibility Principle

"A class should have one, and only one, reason to change"

i.e. If a class is doing anything other than what is intrinsic to its existence then it is breaking SR principle.

"""

"""
Example of SR principle violation
"""


class Player:
    def __init__(self, player_name: str, player_age: int):
        self.player_name = player_name
        self.player_age = player_age

    def get_player_name(self) -> str:
        return self.player_name

    def get_player_age(self) -> int:
        return self.player_age

    def save_player_details(self, player: Player):
        pass


"""
The Player class breaks the SR principle, as it is having "save_player_details" method which is DB related operation
and not intrinsic to Player attributes/methods. 

In order to make it SRP compatible, we need to separate out non intrinsic method to another class.
"""

"""
Example of SR principle implementation
"""


class Player:
    def __init__(self, player_name: str):
        self.player_name = player_name
        self.player_age = player_age

    def get_player_name(self):
        return self.player_name

    def get_player_age(self) -> int:
        return self.player_age


class PlayerDB:
    def get_player(self) -> Player:
        pass

    def save_player_details(self, player: Player):
        pass
