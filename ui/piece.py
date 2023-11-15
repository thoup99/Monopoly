import pygame
from player import Player
from renderer import Renderer

class BoardPiece:
    def __init__(self, player: Player) -> None:

        self.player = player

        #Create a list with all the center positions of tiles on the board
        base_positions = [(913, 712), (835, 722), (774, 720), (717, 724), (658, 715), (599, 716), (538, 720), (483, 716), (422, 722), (364, 726), (297, 699), (279, 635), (281, 575), (278, 518), (277, 459), (283, 396), (281, 340), (281, 282), (282, 224), (282, 164), (281, 87), (363, 73), (421, 75), (481, 72), (540, 71), (599, 76), (658, 73), (715, 73), (778, 75), (837, 71), (915, 79), (922, 162), (921, 219), (919, 277), (922, 339), (921, 398), (919, 458), (924, 517), (920, 577), (923, 637)]

        self.positions = []   

        #Modify the positions based on the player number
        width_change = -10 if (player.number) % 2 == 0 else 10
        height_change = -10 if (player.number) <= 1 else 10

        for position in base_positions:
            self.positions.append((position[0] + width_change, position[1] + height_change))

        #Position the player will occupy if they are jailed
        not_jail_positions = [(248, 688), (248, 720), (274, 746), (310, 746)]
        self.not_jail_position = not_jail_positions[self.player.number]

        self.square = pygame.Surface((20, 20))
        self.square.fill(player.color)
        self.square_rect = self.square.get_rect()

        Renderer.addElement(self)

    def __del__(self):
        print("Deleting BoardPiece")

    def destroy(self):
        Renderer.removeElement(self)

    def render(self, screen: pygame.surface.Surface):
        if not self.player.is_jailed:
            if self.player.position == 10:
                self.square_rect.center = self.not_jail_position
            else:
                self.square_rect.center = self.positions[self.player.position]
        else:
            self.square_rect.center = self.positions[self.player.position]

        screen.blit(self.square, self.square_rect)