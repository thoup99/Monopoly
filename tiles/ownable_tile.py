from player import Player
from dice import Dice

class OwnableTile:
    groups = {
       "Brown": [],
       "Light Blue": [],
       "Pink": [],
       "Orange": [],
       "Red": [],
       "Yellow": [],
       "Green": [],
       "Dark Blue": [],
       "Utility": [],
       "Railroad": []
    }

    def __init__(self, name, group, cost, rent_table, house_cost, mortgage, is_standard_property = True) -> None:
        self.name = name
        self.group = group
        self.cost = cost
        self.rent_table = rent_table
        self.house_cost = house_cost
        #Buying back a mortagage is 110% the mortgage cost
        self.mortgage = mortgage
        self.owned = False
        self.owner = None
        self.is_standard_property = is_standard_property
        self.houses = 0
        self.hotels = 0

        OwnableTile.groups[group].append(self)

    def isOwned(self):
        return self.owned
    
    def setOwner(self, player : Player):
        if self.isOwned():
            self.owner.propery.remove(self)
            
        self.owner = player
        self.owned = True
        player.propery.append(self)

    def determineRent(self):
        amount_owned = 0
        for tile in OwnableTile.groups[self.group]:
            if tile.owner == self.owner:
                amount_owned += 1

        if self.group == "Railroad":
            return self.rent_table[amount_owned - 1]
        
        elif self.group == "Utility":
            match (amount_owned):
                case 1:
                    return 4 * Dice.total
                case 2:
                    return 10 * Dice.total

        elif (self.is_standard_property):
            return self.rent_table[self.houses + self.hotels]
