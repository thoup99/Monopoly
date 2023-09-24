from dice import Dice
from player import Player

class Monopoly:
    def __init__(self, num_players) -> None:
        self.game_over = False
        self.players = self.getPlayerNames(num_players)

        self.dice_1 = Dice(6)
        self.dice_2 = Dice(6)

    def getPlayerNames(self, num):
        players = []
        for x in range(num):
            players.append(Player(input(f"Enter player {x + 1}'s name: ")))


    def doOneTurn(self):
        pass