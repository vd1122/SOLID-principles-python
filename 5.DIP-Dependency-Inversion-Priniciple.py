
"""
DIP --> Dependeny Inversion Principle

Depends on 2 principles -

1. High level modules should not depend on low level modules; both should depend on abstractions"
2. Abstractions should not depend on details. Details should depend upon abstraction"

High level modules are the part of our application that bring real value. They are the modules written to solve real
problems and use cases.

Low level modules are implementation details that are required to execute the business policies.

"""

"""
Example of DI principle violation
"""

'''
We are directly using team_players_list.team_players. In our high level class TeamPlayersList and we are using the 
implementation of this list directly in high level class. As of now this is fine but imagine a situation in which 
we need to change this implementation from list to something else. In that case our high-level class TeamPlayersList 
would break as it is dependent on implementation details of Low level class TeamPlayers.
'''

from enum import Enum

class Teams(Enum):
    AUS_TEAM = 1
    ENG_TEAM = 2
    IND_TEAM = 3

class Player:
    def __init__(self, player_name):
        self.player_name = player_name

class TeamPlayers():
    def __init__(self):
        self.team_players = []

    def add_team_players(self, player, team):
        self.team_players.append((player, team))

class TeamPlayersList():
    def __init__(self, team_players):
        players = team_players.team_players
        for player in players:
            if player[1] == Teams.AUS_TEAM:
                print(f'{player[0].player_name} is in AUS team')

            if player[1] == Teams.ENG_TEAM:
                print(f'{player[0].player_name} is in ENG team')

            if player[1] == Teams.IND_TEAM:
                print(f'{player[0].player_name} is in IND team')


player1 = Player('Ricky')
player2 = Player('Kevin')
player3 = Player('Virat')

team_players = TeamPlayers()
team_players.add_team_players(player1, Teams.IND_TEAM)
team_players.add_team_players(player2, Teams.AUS_TEAM)
team_players.add_team_players(player3, Teams.ENG_TEAM)

TeamPlayersList(team_players)


'''
To comply to Dependency Inversion Principle, we need to ensure that high level class TeamPlayersList should not depend 
on concrete implementation of low level class TeamPlayers. Instead it should depend on some abstraction.
'''
from enum import Enum
from abc import ABCMeta, abstractmethod

class Teams(Enum):
    AUS_TEAM = 1
    ENG_TEAM = 2
    IND_TEAM = 3

class TeamPlayerLookup(metaclass=ABCMeta):
  @abstractmethod
  def players_of_team(self, team):
    pass

class Player:
    def __init__(self, player_name):
        self.player_name = player_name

class TeamPlayers(TeamPlayerLookup):
  def __init__(self):
    self.team_players = []

  def add_team_players(self, student, team):
    self.team_players.append((student, team))

  def players_of_team(self, team):
    for player in self.team_players:
      if player[1] == team:
        return player[0].player_name,

class TeamPlayersList():
  def __init__(self, team_player_lookup):
    for player in team_player_lookup.players_of_team(Teams.AUS_TEAM):
      print(f'{player} is in AUS team.')

    for player in team_player_lookup.players_of_team(Teams.ENG_TEAM):
      print(f'{player} is in ENG team.')

    for player in team_player_lookup.players_of_team(Teams.IND_TEAM):
      print(f'{player} is in IND team.')


player1 = Player('Ricky')
player2 = Player('Kevin')
player3 = Player('Virat')

team_players = TeamPlayers()
team_players.add_team_players(player1, Teams.AUS_TEAM)
team_players.add_team_players(player2, Teams.ENG_TEAM)
team_players.add_team_players(player3, Teams.IND_TEAM)

TeamPlayersList(team_players)
