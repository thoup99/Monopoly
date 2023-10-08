from player import Player

class TaxTile:
    def __init__(self, tax_name, tax_amount) -> None:
        self.tax_name = tax_name
        self.tax_amount = tax_amount

    def chargeTax(self, player: Player):
        player.money -= self.tax_amount


    