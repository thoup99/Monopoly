import random

class Dice:
    all_dice = []

    def __init__(self, sides) -> None:
        Dice.all_dice.append(self)
        self.sides = sides
        self.value = 1

    def roll(self) -> int:
        self.value = random.randint(1, self.sides)
        return self.value
    
    def roll_all():
        for dice in Dice.all_dice:
            dice.roll()
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Dice):
            return self.value == other.value
