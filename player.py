

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.money = 0
        self.propery = []
        self.position = 0
        self.is_jailed = False
        self.turns_jailed = 0
        self.is_bankrupt = False