import pygame
from ui.colored_rectangle import ColoredRectangle
from tiles.ownable_tile import OwnableTile

class TileOwner:
    def __init__(self, ownable_tile: OwnableTile, position) -> None:
        self.tile = ownable_tile

        self.background = ColoredRectangle(position, 19, 19, (0, 0, 0))

        if self.tile.owned:
            self.foreground = ColoredRectangle(position, 15, 15, self.tile.owner.color)
        else:
            self.foreground = ColoredRectangle(position, 15, 15, (255, 255, 255))

