import pygame
from ui.image import Image

class Sprite:

    def __init__(self, center_x, center_y, paths: list[str]) -> None:
        self.images = []

        for path in paths:
            self.images.append(pygame.image.load(path))

        self.image = Image(paths[0], center_x, center_y)

    def setIndex(self, i):
        self.image.setImage(self.images[i])