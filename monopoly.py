from dice import Dice

from tiles.chance_tile import ChanceTile
from tiles.community_chest_tile import CommunityChestTile
from tiles.ownable_tile import OwnableTile
from tiles.tax_tile import TaxTile

from ui.label import Label
from ui.background_label import BackgroundLabel
from ui.button_array import ButtonArray
from ui.sprite import Sprite

from ui.piece import BoardPiece
from ui.tile_owner import TileOwner

from player import Player
from timers import Timer

class Monopoly:
    MAKE_PLAYER_COUNT = 0
    PLAYER_COUNT = 1
    MAKE_NAME_SELECTION = 2
    NAME_SELCTION = 3
    CREATE_PLAYER_CARDS = 4
    PLAYING_GAME = 5
    GAME_OVER = 6

    def __init__(self) -> None:
        self.game_over = False
        self.winner = None
        self.done = False

        self.player_names = []

        self.state = Monopoly.MAKE_PLAYER_COUNT

        self.players = []
        self.current_player_index = -1
        self.current_player = Player("Null", 0)

        self.num_players = -1
        self.num_bankrupt = 0

        self.dice_1 = Dice(6)
        self.dice_2 = Dice(6)

        dice_image_paths = [
            "./images/dice0.png",
            "./images/dice1.png",
            "./images/dice2.png",
            "./images/dice3.png",
            "./images/dice4.png",
            "./images/dice5.png",
            "./images/dice6.png"
        ]

        self.dice_1_sprite = Sprite(71, 256, dice_image_paths)
        self.dice_2_sprite = Sprite(171, 256, dice_image_paths)

        self.doubles_label = Label("", 121, 316, font_size= 50)
        self.doubles_label_colors = [(237, 193, 36), (240, 111, 12), (224, 37, 20), (255, 255, 255)]

        self.move_timer = Timer(100, self.movePlayer)
        self.land_on_space_timer = Timer(500, self.checkPositionOnBoard)
        self.position_outcome_timer = Timer(2000, self.endTurnChecks)

        self.current_player_label = BackgroundLabel(" ", 599, 19, alpha= 180)
        self.position_outcome_label = BackgroundLabel(" ", 599, 126, 50, alpha= 140)
        

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
            OwnableTile("Connecticut Avenue", "Light Blue", 120, [4, 100, 300, 450, 600], 50, 60),
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

        self.tile_owners = []

        base_positions = [(913, 712), (835, 722), (774, 720), (717, 724), (658, 715), (599, 716), (538, 720), (483, 716), (422, 722), (364, 726), (297, 699), (279, 635), (281, 575), (278, 518), (277, 459), (283, 396), (281, 340), (281, 282), (282, 224), (282, 164), (281, 87), (363, 73), (421, 75), (481, 72), (540, 71), (599, 76), (658, 73), (715, 73), (778, 75), (837, 71), (915, 79), (922, 162), (921, 219), (919, 277), (922, 339), (921, 398), (919, 458), (924, 517), (920, 577), (923, 637)]
        for index, tile in enumerate(self.board):
            if isinstance(tile, OwnableTile):
                self.tile_owners.append(TileOwner(tile, base_positions[index]))
    
    def setState(self, state):
        self.state = state

    def setPlayerNumber(self, num):
        self.num_players = num
        self.setState(Monopoly.MAKE_NAME_SELECTION)

    def appendPlayerName(self, name):
        self.player_names.append(name)

        if len(self.player_names) != self.num_players:
            self.setState(Monopoly.MAKE_NAME_SELECTION)
        else:
            self.setState(Monopoly.CREATE_PLAYER_CARDS)

    def createPlayers(self):
        for x, name in enumerate(self.player_names):
           player = Player(name, x)
           self.players.append(player)
           BoardPiece(player)

    def movePlayer(self, spaces):
        player = self.players[self.current_player_index]
        player.position += 1
        spaces -= 1

        if player.position >= 40:
            player.position -= 40
            player.money += 200
        
        if spaces > 0:
            self.move_timer.setArgument(spaces)
            self.move_timer.beginTicking()
        else:
            self.land_on_space_timer.beginTicking()

    def startNextTurn(self):
        while True:
            self.current_player_index += 1

            if self.current_player_index > self.num_players - 1:
                self.current_player_index = 0

            if not self.players[self.current_player_index].is_bankrupt:
                break

        self.current_player = self.players[self.current_player_index]

        self.current_player.doubles_rolled = 0

        self.current_player_label.setText(f"{self.current_player.name}'s Turn")

        #Free a player with a get out of jail free card
        if self.current_player.is_jailed and self.current_player.get_out_of_jail_free:
            self.freePlayer(self.current_player)
            self.current_player.get_out_of_jail_free = False

        if self.game_over:
            self.createGameOverCard()

        else:
            self.rollDicePrompt()

    def rollDicePrompt(self):
        ButtonArray("Roll the Dice!", [["Roll!", None]], self.rollDiceClicked)

    def rollDiceClicked(self):
        self.rollDice()
        player = self.players[self.current_player_index]

        if self.dice_1 == self.dice_2:
            player.doubles_rolled += 1

            if player.is_jailed:
                self.freePlayer(player)

            if player.doubles_rolled == 3:
                self.jailPlayer(player)

        if player.is_jailed:
            player.turns_jailed += 1

            if player.turns_jailed == 3:
                self.freePlayer(player)

        self.updateDiceUI()
        self.movePlayer(Dice.total)

    def updateDiceUI(self):
        self.dice_1_sprite.setIndex(self.dice_1.value)
        self.dice_2_sprite.setIndex(self.dice_2.value)

        if self.dice_1 == self.dice_2:
            self.doubles_label.setText("Doubles!")
            self.doubles_label.setColor(self.doubles_label_colors[self.current_player.doubles_rolled - 1])
        else:
            self.doubles_label.setText("")

    def checkPositionOnBoard(self):
        player = self.players[self.current_player_index]

        tile = self.board[player.position]
        if isinstance(tile, OwnableTile):

            #Tile has no owner
            if tile.isOwned() == False:
                if player.money > tile.cost:
                    ButtonArray(f"Would you like to purchase {tile.name} for ${tile.cost}?", [["Yes", True], ["No", False]], self.purchaseDecision)
                else:
                    self.position_outcome_label.setText(f"{player.name} Can not afford to purchase {tile.name} for {tile.cost}")
                    self.position_outcome_timer.beginTicking()
            
            #Tile has an owner
            elif tile.owner != player:
                rent = tile.determineRent()
                player.money -= rent

                #Adjust the cost of rent if the player goes bankrupt
                if player.money < 0:
                    rent += player.money 

                tile.owner.money += rent

                self.position_outcome_label.setText(f"{player.name} paid {tile.owner.name} ${rent} in rent for landing on {tile.name}.")
                self.position_outcome_timer.beginTicking()

            elif tile.owner == player:
                self.position_outcome_label.setText(f"{player.name} landed on their own property! No rent is due.")
                self.position_outcome_timer.beginTicking()

        elif isinstance(tile, ChanceTile):
            text = tile.grabRandomCard(player)
            self.position_outcome_label.setText(text)
            self.position_outcome_timer.beginTicking()

        elif isinstance(tile, CommunityChestTile):
            text = tile.grabRandomCard(player)
            self.position_outcome_label.setText(text)
            self.position_outcome_timer.beginTicking()

        elif isinstance(tile, TaxTile):
            tile.chargeTax(player)
            self.endTurnChecks()

        elif player.position == 30:
            self.jailPlayer(player)
            self.endTurnChecks()

        else:
            self.endTurnChecks()

    def hidePositionOutcomeLabel(self):
        self.position_outcome_label.setText(" ")

    def purchaseDecision(self, is_purchasing: bool):
        player = self.players[self.current_player_index]
        tile = self.board[player.position]

        if is_purchasing:
            tile.setOwner(player)
            player.money -= tile.cost
            self.updateTileOwners()

            self.position_outcome_label.setText(f"{player.name} has purchased {tile.name}!")
            self.position_outcome_timer.beginTicking()
        else:
            self.position_outcome_label.setText(f"{player.name} decided not to purchase {tile.name}.")
            self.position_outcome_timer.beginTicking()

    def updateTileOwners(self):
        for tile_owner in self.tile_owners:
            tile_owner.update()

    def endTurnChecks(self):
        self.hidePositionOutcomeLabel()

        #Check if bankrupt
        player = self.players[self.current_player_index]
        if self.checkIfPlayerBankrupt(player):
            self.num_bankrupt += 1
            player.is_bankrupt = True

            tile = self.board[self.players[self.current_player_index].position]
            if isinstance(tile, OwnableTile):
                self.transferPlayerBelongings(player)
            else:
                self.removePlayerOwnership(player)

            self.updateTileOwners()       

        #Check for doubles
        if not player.is_bankrupt:
            if self.dice_1 == self.dice_2:
                self.rollDicePrompt()
                return
            
        self.checkForGameOver()
        
        self.startNextTurn()

    def checkForGameOver(self):
        if self.num_bankrupt == self.num_players - 1:
            self.game_over = True

    def setDoneTrue(self):
        self.done = True

    def createGameOverCard(self):
        ButtonArray(f"{self.players[self.current_player_index].name} won the game!", [["Exit", None]], self.setDoneTrue)

    #---------------------------------------------#

    def rollDice(self):
        Dice.roll_all()


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
        player.turns_jailed == 0


    def transferPlayerBelongings(self, player: Player):
        tile = self.board[player.position]
        if isinstance(tile, OwnableTile):
            #Transfers all property
            for property in player.propery:
                property.setOwner(player)

    def removePlayerOwnership(self, player: Player):
        for property in player.propery:
            property.removeOwner()

    def checkIfPlayerBankrupt(self, player: Player):
        return player.money < 0