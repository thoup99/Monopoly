import pygame
from renderer import Renderer

class Label:
    def __init__(self, text, center_x, center_y, font_size = 30, color = (255, 255, 255)) -> None:

        self.font = pygame.font.SysFont('Arial', font_size)

        self.text = text
        self.color = color

        self.center_x = center_x
        self.center_y = center_y
        
        self.text_surface = self.font.render(text, True, self.color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.centerx, self.text_rect.centery = center_x, center_y

        Renderer.addElement(self)

    def setText(self, newText):
        self.text = newText
        self.rerenderText()
    
    def setColor(self, newColor):
        self.color = newColor
        self.rerenderText()

    def rerenderText(self):
        self.text_surface = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.centerx, self.text_rect.centery = self.center_x, self.center_y

    def getWidth(self):
        return self.text_rect.width

    def getHeight(self):
        return self.text_rect.height

    def __del__(self):
        print("Deleting Label")

    def destroy(self):
        Renderer.removeElement(self)

    def render(self, screen: pygame.surface.Surface):
        screen.blit(self.text_surface, self.text_rect)