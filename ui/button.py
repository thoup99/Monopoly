import pygame
from renderer import Renderer
from input import Input


#NEEDS TESTED
class Button:
    font = pygame.font.SysFont('Arial', 30)

    def __init__(self, text, center_x, center_y, id_num, callback) -> None:
        self.is_active = True
        self.callback = callback
        self.id = id_num

        self.image = pygame.image.load("./images/button.png")
        self.image_rect = self.image.get_rect()

        self.image_rect.centerx = center_x
        self.image_rect.centery = center_y

        self.text_surface = Button.font.render(text, True, (255,255,255))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.centerx, self.text_rect.centery = self.image_rect.center

        Renderer.elements.append(self)
        Input.subscribe(pygame.MOUSEBUTTONDOWN, self.check_click)

    def check_mouse_in(self, position): ##NEEDS UPDATED
        return self.image_rect.collidepoint(position[0], position[1])

    def check_click(self, button, position):
        if self.is_active and button == 1 and self.check_mouse_in(position):
            self.callback(self.id)

    def render(self, screen: pygame.surface.Surface):
        screen.blit(self.image, self.image_rect)
        screen.blit(self.text_surface, self.text_rect)