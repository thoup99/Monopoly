from dice import Dice
from player import Player

class Monopoly:
    def __init__(self, num_players) -> None:
        self.game_over = False
        self.winner = None

        self.players = self.getPlayerNames(num_players)
        self.current_player = 0

        self.num_players = num_players
        self.num_backrupt = 0

        self.dice_1 = Dice(6)
        self.dice_2 = Dice(6)

    def getPlayerNames(self, num) -> [Player]:
        players = []
        for x in range(num):
            players.append(Player(input(f"Enter player {x + 1}'s name: ")))

    def incrementCurrentPlayer(self):
        self.current_player += 1
        if self.current_player == self.num_players:
            self.current_player = 0


    def doOneTurn(self):
        #Check for gameover
        if self.num_players - self.num_backrupt == 1:
            for player in self.players:
                if not player.is_bankrupt:
                    self.winner = player
                    self.game_over = True
                    return
                
        #If the current player is bankrupt go to the next one
        while self.players[self.current_player].is_bankrupt == True:
            self.incrementCurrentPlayer()

        
        

