from player import Player
import random

class ChanceTile:
    def __init__(self) -> None:
        pass

    def grabRandomCard(self, player: Player):
        card = random.randint(0, 7)

        match (card):
            case 0:
                player.position = 39
                return "Go to Board walk!"
            
            case 1:
                player.position = 0
                player.money += 200
                return "Pass Go (Collect $200)"
            
            case 2:
                if player.position > 23:
                    player.money += 200

                player.position = 23
                return "Advance to Illinois Avenue."
            
            case 3:
                if player.position > 11:
                    player.money += 200

                player.position = 11
                return "Advance to St. Charles Place."
            
            case 4:
                player.money += 50
                return "Bank pays you dividend of $50."
            
            case 5:
                player.get_out_of_jail_free = True
                return "You pulled a Get out of Jail Free Card!"
            
            case 6:
                player.position -= 3
                return "Go back 3 spaces."
            
            case 7:
                player.position = 10
                player.is_jailed = True
                player.turns_jailed = 0
                return "Go to jail. Do not pass Go."
            
            case _:
                return f"Invalid Chance card pulled '{card}'."
        