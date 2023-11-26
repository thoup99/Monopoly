import random

class Dice:
    all_dice = []
    total = -1

    def __init__(self, sides) -> None:
        Dice.all_dice.append(self)
        self.sides = sides
        self.value = 0

    def roll(self) -> int:
        self.value = random.randint(1, self.sides)
        return self.value
    
    def roll_all():
        Dice.total = 0
        for dice in Dice.all_dice:
            dice.roll()
            Dice.total += dice.value
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Dice):
            return self.value == other.value
