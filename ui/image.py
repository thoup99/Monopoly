import pygame
from renderer import Renderer

class Image:
    def __init__(self, path, center_x, center_y) -> None:
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()

        self.rect.centerx = center_x
        self.rect.centery = center_y

        Renderer.elements.append(self)

    def loadNewImage(self, path):
        self.image = pygame.image.load(path)

    def render(self, screen: pygame.surface.Surface):
        screen.blit(self.image, self.rect)