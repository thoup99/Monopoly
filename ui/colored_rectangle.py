import pygame
from renderer import Renderer

class ColoredRectangle:
    def __init__(self, center, width, height, color) -> None:
        self.rectangle = pygame.Surface((width, height))
        self.rectangle.fill(color)
        self.rectangle_rect = self.rectangle.get_rect()
        self.rectangle_rect.center = center

        Renderer.addElement(self)

    def __del__(self):
        print("Deleting Colored Rectangle")

    def destroy(self):
        Renderer.removeElement(self)

    def render(self, screen: pygame.surface.Surface):
        screen.blit(self.rectangle, self.rectangle_rect)