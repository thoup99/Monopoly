import random

class Dice:
    def __init__(self, sides) -> None:
        self.sides = sides
        self.value = 1

    def roll(self) -> int:
        self.value = random.randint(1, self.sides)
        return self.value
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Dice):
            return self.value == other.value
