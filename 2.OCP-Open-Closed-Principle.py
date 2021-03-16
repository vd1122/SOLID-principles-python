"""
OCP --> Open-Closed Principle

"The Open-Closed Principle (OCP) states that software entities (classes, modules, methods, etc.)
should be open for extension, but closed for modification"

"""


"""
Example of OC principle violation
"""

class Game:
    def __init__(self, game_code: str, game_name: str):
        self.game_code = game_code
        self.game_name = game_name

    def get_game_name(self) -> str:
        return self.game_name

    def get_players_required(self) -> str:
        if self.game_code == 'LawnTennisSingles':
            return 2
        elif self.game_code == 'LawnTennisDoubles':
            return 4
        else:
            raise f'"get_players_required" function needs to implemented for {self.game_name}'


games = [
    Game('LawnTennisSingles', 'Lawn-Tennis Singles'),
    Game('LawnTennisDoubles', 'Lawn-Tennis Doubles'),
]


def games_players_requirement(games: list):
    for game in games:
        print(f'"{game.get_game_name()}" require {game.get_players_required()} players')

games_players_requirement(games)


"""
The function "get_players_required" breaks OC principle because for any new game type "get_players_required"
will need to be modified.
"""

"""
Example of OC principle implementation
"""

class Game:
    def __init__(self, game_code: str, game_name: str):
        self.game_code = game_code
        self.game_name = game_name

    def get_game_name(self) -> str:
        return self.game_name

    def get_players_required(self) -> int:
        raise f'"get_players_required" function needs to implemented for {self.game_name}'

class LawnTennisSingles(Game):
    def __init__(self):
        super().__init__('LawnTennisSingles', 'Lawn-Tennis Singles')

    def get_players_required(self) -> int:
        return 2

class LawnTennisDoubles(Game):
    def __init__(self):
        super().__init__('LawnTennisDoubles', 'Lawn-Tennis Doubles')

    def get_players_required(self) -> int:
        return 4

class BadmintonSingles(Game):
    def __init__(self):
        super().__init__('BadmintonSingles', 'Badminton Singles')

    def get_players_required(self) -> int:
        return 2

class BadmintonDoubles(Game):
    def __init__(self):
        super().__init__('BadmintonDoubles', 'Badminton Doubles')

    def get_players_required(self) -> int:
        return 4


games = [
    LawnTennisSingles(),
    LawnTennisDoubles(),
    BadmintonSingles(),
    BadmintonDoubles()
]


def games_players_requirement(games: list):
    for game in games:
        print(f'"{game.get_game_name()}" require {game.get_players_required()} players')

games_players_requirement(games)



"""
Game class now enforces get_players_required function which needs to be implemented by different games class.

Every different game class now make game specific implementation, hence base class is closed for modification while 
child class is open for new games.

"""


