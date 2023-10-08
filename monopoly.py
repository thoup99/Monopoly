from dice import Dice
from ownable_tile import OwnableTile
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
            None,
            OwnableTile("Mediterranean Avenue", "Brown", 60, [2, 10, 30, 90, 160, 250], 50, 30),
            None,
            OwnableTile("Baltic Avenue", "Brown", 60, [4, 20, 60, 180, 320, 450], 50, 30),
            None,
            OwnableTile("Reading Railroad", "Railroad", 200, [25, 50, 100, 200], -1, 100, is_standard_property = False),
            OwnableTile("Oriental Avenue", "Light Blue", 100, [6, 30, 90, 270, 400, 550], 50, 50),
            None,
            OwnableTile("Vermont Avenue", "Light Blue", 100, [6, 30, 90, 270, 400, 550], 50, 50),
            OwnableTile("Oriental Avenue", "Light Blue", 120, [4, 100, 300, 450, 600], 50, 60),
            None,
            OwnableTile("St. Charles Place", "Pink", 140, [10, 50, 150, 450, 625, 750], 100, 70),
            OwnableTile("Electric Company", "Utility", 150, [], -1, 75, is_standard_property = False),
            OwnableTile("States Avenue", "Pink", 140, [10, 50, 150, 450, 625, 750], 100, 70),
            OwnableTile("Virginia Avenue", "Pink", 160, [12, 60, 180, 500, 700, 900], 100, 80),
            OwnableTile("Pennsylvania Railroad", "Railroad", 200, [25, 50, 100, 200], -1, 100, is_standard_property = False),
            OwnableTile("St. James Place", "Orange", 180, [14, 70, 200, 550, 750, 950], 100, 90),
            None,
            OwnableTile("Tennessee Avenue", "Orange", 180, [14, 70, 200, 550, 750, 950], 100, 90),
            OwnableTile("New York Avenue", "Orange", 200, [16, 80, 220, 600, 800, 1000], 100, 100),
            None,
            OwnableTile("Kentucky Avenue", "Red",  220, [18, 36, 90, 250, 700, 875, 1050], 150, 110),
            None,
            OwnableTile("Indiana Avenue", "Red", 220, [18, 90, 250, 700, 875, 1050], 150, 110),
            OwnableTile("Illinois Avenue", "Red",  240, [20, 100, 300, 750, 925, 1100], 150, 120),
            OwnableTile("B. &. O. Railroad", "Railroad", 200, [25, 50, 100, 200], -1, 100, is_standard_property = False),
            OwnableTile("Atlantic Avenue", "Yellow",  260, [22, 110, 330, 800, 975, 1150], 150, 130),
            OwnableTile("Ventnor Avenue", "Yellow",  260, [22, 110, 330, 800, 975, 1150],  150, 130),
            OwnableTile("Water Works", "Utility", 60, [], -1, 30, is_standard_property = False),
            OwnableTile("Marvin Gardens", "Yellow",  280, [24, 120, 360, 850, 1025, 1200], 150, 140),
            None,
            OwnableTile("Pacific Avenue", "Green", 300, [26, 130, 390, 900, 1100, 1275], 200, 150),
            OwnableTile("North Carolina Avenue", "Green", 300, [26, 130, 390, 900, 1100, 1275], 200, 150),
            None,
            OwnableTile("Pennsylvania Avenue", "Green", 320, [28, 150, 450, 1000, 1200, 1400], 200, 160),
            OwnableTile("Short Line", "Railroad", 200, [25, 50, 100, 200], -1, 100, is_standard_property = False),
            None,
            OwnableTile("Park Place", "Dark Blue", 350, [35, 175, 500, 1100, 1300, 1500], 200, 175),
            None,
            OwnableTile("Boardwalk", "Dark Blue", 400, [50, 200, 600, 1400, 1700, 2000], 200, 200)
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

    def jailPlayer(self, player: Player):
        player.position = 10
        player.is_jailed = True
        player.turns_jailed = 0

    def freePlayer(self, player: Player):
        player.is_jailed = False

    def movePlayer(self, player: Player, amount):
        player.position += amount

        #Checks for passing go and awards money
        if player.position >= 40:
            player.position -= 40
            player.money += 200

    def checkPositionOnBoard(self, player: Player):
        pass

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

                #Frees player if jailed
                if player.is_jailed:
                    self.freePlayer(current_player)

                #Jails player if they roll 3 doubles in one turn
                if doubles_rolled == 3:
                    self.jailPlayer(current_player)
                    break

            #Since after each double you are allowed to purchase property all logic for that must remain inside this loop
            self.movePlayer(current_player, self.dice_1.value + self.dice_2.value)

            self.checkPositionOnBoard(current_player)