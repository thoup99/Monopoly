import pygame
from renderer import Renderer
from input import Input


#NEEDS TESTED
class Button:
    font = pygame.font.SysFont('Arial', 50)

    def __init__(self, text, center_x, center_y, id_num, callback) -> None:
        self.is_active = True
        self.callback = callback
        self.id = id_num

        self.image = pygame.image.load("./images/button.png")
        self.image_rect = self.image.get_rect()

        self.image_rect.centerx = center_x
        self.image_rect.centery = center_y

        self.text_surface = Button.font.render(text, True, (0,0,0))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.centerx, self.text_rect.centery = self.image_rect.center

        Renderer.addElement(self)
        Input.subscribe(pygame.MOUSEBUTTONDOWN, self.checkClick)

    def __del__(self):
        print("Deleting Button")

    def destroy(self):
        Renderer.removeElement(self)
        Input.unsubscribe(pygame.MOUSEBUTTONDOWN, self.checkClick)

    def checkMouseIn(self, position):
        return self.image_rect.collidepoint(position[0], position[1])

    def checkClick(self, button, position):
        if self.is_active and button == 1 and self.checkMouseIn(position):
            self.callback(self.id)

    def render(self, screen: pygame.surface.Surface):
        screen.blit(self.image, self.image_rect)
        screen.blit(self.text_surface, self.text_rect)