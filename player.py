

class Player:
    def __init__(self, name, number) -> None:
        self.name = name
        self.number = number
        self.money = 1500
        self.propery = []
        self.position = 0
        self.is_jailed = False
        self.get_out_of_jail_free = False
        self.turns_jailed = 0
        self.is_bankrupt = False

        self.doubles_rolled = 0

        colors = [(199, 54, 54), (247, 106, 12), (67, 166, 40), (40, 69, 166)]
        self.color = colors[number]