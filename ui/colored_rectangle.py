import pygame
from renderer import Renderer

class ColoredRectangle:
    def __init__(self, center, width, height, color, alpha = 255) -> None:
        self.color = color
        self.center = center
        self.alpha = alpha

        self.rectangle = pygame.Surface((width, height))
        self.rectangle.fill(color)
        self.rectangle.set_alpha(alpha)
        self.rectangle_rect = self.rectangle.get_rect()
        self.rectangle_rect.center = center

        Renderer.addElement(self)

    def __del__(self):
        print("Deleting Colored Rectangle")

    def destroy(self):
        Renderer.removeElement(self)

    def setHeight(self, new_height):
        self.createNewRectangle(self.rectangle_rect.width, new_height)

    def setWidth(self, new_width):
        self.createNewRectangle(new_width, self.rectangle_rect.height)

    def setColor(self, new_color):
        self.color = new_color
        self.createNewRectangle(self.rectangle_rect.width, self.rectangle_rect.height)

    def setAlpha(self, new_alpha):
        self.alpha = new_alpha
        self.createNewRectangle(self.rectangle_rect.width, self.rectangle_rect.height)

    def createNewRectangle(self, width, height):
        self.rectangle = pygame.Surface((width, height))
        self.rectangle.fill(self.color)
        self.rectangle.set_alpha(self.alpha)
        self.rectangle_rect = self.rectangle.get_rect()
        self.rectangle_rect.center = self.center

    def render(self, screen: pygame.surface.Surface):
        screen.blit(self.rectangle, self.rectangle_rect)