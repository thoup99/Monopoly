import pygame
from ui.colored_rectangle import ColoredRectangle
from tiles.ownable_tile import OwnableTile

class TileOwner:
    def __init__(self, ownable_tile: OwnableTile, position) -> None:
        self.tile = ownable_tile

        self.background = ColoredRectangle(position, 24, 24, (0, 0, 0))

        if self.tile.owned:
            self.foreground = ColoredRectangle(position, 20, 20, self.tile.owner.color)
        else:
            self.foreground = ColoredRectangle(position, 20, 20, (255, 255, 255))

