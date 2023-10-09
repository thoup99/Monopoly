

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.money = 1500
        self.propery = []
        self.position = 0
        self.is_jailed = False
        self.get_out_of_jail_free = False
        self.turns_jailed = 0
        self.is_bankrupt = False