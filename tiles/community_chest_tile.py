from player import Player
import random

class CommunityChestTile:
    def __init__(self) -> None:
        pass

    def grabRandomCard(self, player: Player):
        card = random.randint(0, 12)

        match (card):
            case 0:
                player.position = 0
                player.money += 200
                return "Advance to Go and collect $200."
            
            case 1:
                player.money += 200
                return "Bank error in your favor. Collect $200."
            
            case 2:
                player.money -= 50
                return "Doctor's fee. Pay $50."
            
            case 3:
                player.money += 50
                return "From sale of stock you get $50."
            
            case 4:
                player.get_out_of_jail_free = True
                return "You pulled a Get out of Jail Free Card!"
            
            case 5:
                player.money += 100
                return "Holiday fund matures. Receive $100."
            
            case 6:
                player.money += 20
                return "Income tax refund. Collect $20."
            
            case 7:
                player.money += 100
                return "Life insurance matures. Collect $100"
            
            case 8:
                player.money -= 100
                return "Pay hospital fees of $100."
            
            case 9:
                player.money -= 50
                return "Pay school fees of $50."
            
            case 10:
                player.money -= 25
                return "Receive $25 consultancy fee."
            
            case 11:
                player.money += 10
                return "You have won second prize in a beauty contest. Collect $10."
            
            case 12:
                player.money += 100
                return "You inherit $100."
            
            case _:
                return f"Invalid Community Chest card pulled '{card}'."