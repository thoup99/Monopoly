from dice import Dice
from player import Player

class Monopoly:
    def __init__(self, num_players) -> None:
        self.game_over = False
        self.winner = None

        self.players = self.getPlayerNames(num_players)
        self.current_player_index = 0

        self.num_players = num_players
        self.num_backrupt = 0

        self.dice_1 = Dice(6)
        self.dice_2 = Dice(6)

        self.board = [

        ]

    def getPlayerNames(self, num) -> list[Player]:
        players = []
        for x in range(num):
            players.append(Player(input(f"Enter player {x + 1}'s name: ")))
        return players

    def incrementCurrentPlayer(self):
        self.current_player_index += 1
        if self.current_player_index == self.num_players:
            self.current_player_index = 0

    def movePlayer(self, player: Player, amount):
        player.position += amount

        #Checks for passing go and awards money
        if player.position >= 40:
            player.position -= 40
            player.money += 200

    def doOneTurn(self):
        #Check for gameover
        if self.num_players - self.num_backrupt == 1:
            for player in self.players:
                if not player.is_bankrupt:
                    self.winner = player
                    self.game_over = True
                    return
                
        #If the current player is bankrupt go to the next one
        current_player = self.players[self.current_player_index]
        while current_player.is_bankrupt == True:
            self.incrementCurrentPlayer()
            current_player = self.players[self.current_player_index]

        doubles_rolled = 0
        loop_again = True

        #Loops while player rolls doubles
        while loop_again:
            loop_again = False
            Dice.roll_all()

            # Handles doubles
            if self.dice_1 == self.dice_2:
                loop_again = True
                doubles_rolled += 1

                #Jails player if they roll 3 doubles in one turn
                if doubles_rolled == 3:
                    current_player.is_jailed = True
                    break

            #Since after each double you are allowed to purchase property all logic for that must remain inside this loop
            self.movePlayer(current_player, self.dice_1.value + self.dice_2.value)