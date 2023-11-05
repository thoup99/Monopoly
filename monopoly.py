from dice import Dice
from tiles.chance_tile import ChanceTile
from tiles.community_chest_tile import CommunityChestTile
from tiles.ownable_tile import OwnableTile
from tiles.tax_tile import TaxTile


from player import Player

class Monopoly:
    MAKE_PLAYER_COUNT = 0
    PLAYER_COUNT = 1
    MAKE_NAME_SELECTION = 2
    NAME_SELCTION = 3
    CREATE_PLAYER_CARDS = 4
    ROLLING_DICE = 5
    BUYING = 6

    def __init__(self) -> None:
        self.game_over = False
        self.winner = None

        self.player_names = []

        self.state = Monopoly.MAKE_PLAYER_COUNT

        self.players = []
        self.current_player_index = 0

        self.num_players = -1
        self.num_bankrupt = 0

        self.dice_1 = Dice(6)
        self.dice_2 = Dice(6)

        self.board = [
            None,
            OwnableTile("Mediterranean Avenue", "Brown", 60, [2, 10, 30, 90, 160, 250], 50, 30),
            CommunityChestTile(),
            OwnableTile("Baltic Avenue", "Brown", 60, [4, 20, 60, 180, 320, 450], 50, 30),
            TaxTile("Income Tax", 200),
            OwnableTile("Reading Railroad", "Railroad", 200, [25, 50, 100, 200], -1, 100, is_standard_property = False),
            OwnableTile("Oriental Avenue", "Light Blue", 100, [6, 30, 90, 270, 400, 550], 50, 50),
            ChanceTile(),
            OwnableTile("Vermont Avenue", "Light Blue", 100, [6, 30, 90, 270, 400, 550], 50, 50),
            OwnableTile("Oriental Avenue", "Light Blue", 120, [4, 100, 300, 450, 600], 50, 60),
            None,
            OwnableTile("St. Charles Place", "Pink", 140, [10, 50, 150, 450, 625, 750], 100, 70),
            OwnableTile("Electric Company", "Utility", 150, [], -1, 75, is_standard_property = False),
            OwnableTile("States Avenue", "Pink", 140, [10, 50, 150, 450, 625, 750], 100, 70),
            OwnableTile("Virginia Avenue", "Pink", 160, [12, 60, 180, 500, 700, 900], 100, 80),
            OwnableTile("Pennsylvania Railroad", "Railroad", 200, [25, 50, 100, 200], -1, 100, is_standard_property = False),
            OwnableTile("St. James Place", "Orange", 180, [14, 70, 200, 550, 750, 950], 100, 90),
            CommunityChestTile(),
            OwnableTile("Tennessee Avenue", "Orange", 180, [14, 70, 200, 550, 750, 950], 100, 90),
            OwnableTile("New York Avenue", "Orange", 200, [16, 80, 220, 600, 800, 1000], 100, 100),
            None,
            OwnableTile("Kentucky Avenue", "Red",  220, [18, 36, 90, 250, 700, 875, 1050], 150, 110),
            ChanceTile(),
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
            CommunityChestTile(),
            OwnableTile("Pennsylvania Avenue", "Green", 320, [28, 150, 450, 1000, 1200, 1400], 200, 160),
            OwnableTile("Short Line", "Railroad", 200, [25, 50, 100, 200], -1, 100, is_standard_property = False),
            ChanceTile(),
            OwnableTile("Park Place", "Dark Blue", 350, [35, 175, 500, 1100, 1300, 1500], 200, 175),
            TaxTile("Luxury Tax", 100),
            OwnableTile("Boardwalk", "Dark Blue", 400, [50, 200, 600, 1400, 1700, 2000], 200, 200)
        ]
    
    def setState(self, state):
        self.state = state

    def setPlayerNumber(self, num):
        self.num_players = num + 1
        self.setState(Monopoly.MAKE_NAME_SELECTION)

    def appendPlayerName(self, name):
        self.player_names.append(name)

        if len(self.player_names) != self.num_players:
            self.setState(Monopoly.MAKE_NAME_SELECTION)
        else:
            self.setState(Monopoly.CREATE_PLAYER_CARDS)

    def createPlayers(self):
        for name in self.player_names:
           self.players.append(Player(name))

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

    def transferPlayerBelongings(self, player: Player):
        tile = self.board[player.position]
        if isinstance(tile, OwnableTile):
            #Transfers all property
            for property in player.propery:
                property.setOwner(player)

    def checkIfPlayerBankrupt(self, player: Player):
        if player.money < 0:
            print("less than 0")
            player.is_bankrupt = True
            self.num_bankrupt
            self.transferPlayerBelongings(player)
            return True
        return False

    def checkPositionOnBoard(self, player: Player):
        tile = self.board[player.position]
        if isinstance(tile, OwnableTile):

            #Tile has no owner
            if tile.isOwned() == False:
                if player.money > tile.cost:
                    answer = input(f"Would you like to purchase {tile.name} for {tile.cost}?")
                    if answer == "y":
                        tile.setOwner(player)
                        player.money -= tile.cost
                    else:
                        print(f"You gave up on purchasing {tile.name}")
                else:
                    print(f"{player.name} Can not afford to purchase {tile.name} for {tile.cost}")
            
            #Tile has an owner
            elif tile.owner != player:
                #Does not account for the player going into negatives while paying
                rent = tile.determineRent()
                print("Pay rent monkey boy")
                print(f"{player} paid {tile.owner} ${rent} in rent for landing on {tile.name}.")
                tile.owner.money += rent
                player.money -= rent

        elif isinstance(tile, ChanceTile):
            tile.grabRandomCard(player)

        elif isinstance(tile, CommunityChestTile):
            tile.grabRandomCard(player)

        elif isinstance(tile, TaxTile):
            tile.chargeTax(player)

        else:
            print("Corner Tile")

    def doOneTurn(self):
        #Check for gameover
        if self.num_players - self.num_bankrupt == 1:
            for player in self.players:
                if not player.is_bankrupt:
                    self.winner = player
                    self.game_over = True
                    print(f"{self.winner} Won the Game!")
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
            print(f"{current_player.name} rolled a {Dice.total}!")

            # Handles doubles
            if self.dice_1 == self.dice_2:
                loop_again = True
                doubles_rolled += 1

                #Frees player if jailed
                if current_player.is_jailed:
                    self.freePlayer(current_player)

                #Jails player if they roll 3 doubles in one turn
                if doubles_rolled == 3:
                    self.jailPlayer(current_player)
                    break

            #Since after each double you are allowed to purchase property all logic for that must remain inside this loop
            print("Moving player")
            self.movePlayer(current_player, self.dice_1.value + self.dice_2.value)

            print("checking position")
            self.checkPositionOnBoard(current_player)

            print("checking for bankrupt")
            print(f"{current_player.name}: {current_player.money}")
            if self.checkIfPlayerBankrupt(current_player):
                print(f"{current_player.name} has gone bankrupt!")
                break
            print("Done")
        self.incrementCurrentPlayer()