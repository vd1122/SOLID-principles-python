"""
ISP --> Interface Segregation Principle

"Clients should not be forced to depend upon interfaces that they do not use"

"""

"""
Example of IS principle violation
"""

class Game:

    def badminton_court_area(self) -> None:
        raise NotImplementedError

    def lawn_tennis_court_area(self) -> None:
        raise NotImplementedError


class LawnTennis(Game):

    def lawn_tennis_court_area(self) -> int:
        return 222

    def badminton_court_area(self) -> None:
        pass


class Badminton(Game):

    def badminton_court_area(self) -> int:
        return 111

    def lawn_tennis_court_area(self) -> None:
        pass


'''
Above example violates IS principle as Badminton game does not depend on lawn tennis court area and vice versa, so
interfaces are redundantly applied
'''

"""
Example of implemented IS principle
"""

class Game:
    def __init__(self):
        pass

class BadmintonGame(Game):
    def badminton_court_area(self) -> int:
        raise NotImplementedError

class LawnTennisGame(Game):
    def lawn_tennis_court_area(self) -> int:
        raise NotImplementedError

class Badminton(BadmintonGame):
    def badminton_court_area(self) -> int:
        return 111

class LawnTennis(LawnTennisGame):
    def lawn_tennis__court_area(self) -> int:
        return 222


'''
In the above example badminton court area function is not required for lawn tennis game and vice versa hence classed use
minimal interfaces that are directly required without redundancy
'''
