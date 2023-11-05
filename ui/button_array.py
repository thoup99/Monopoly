import pygame
from renderer import Renderer
from ui.button import Button

class ButtonArray:
    font = pygame.font.SysFont('Arial', 60)

    def __init__(self, text: str, options: list[str], callback) -> None:
        self.callback = callback
        
        self.background_surface = pygame.Surface((1200, 800))
        self.background_surface.set_alpha(128)
        self.background_surface.fill((0,0,0))

        self.text_surface = ButtonArray.font.render(text, True, (255,255,255))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (600, 200)

        self.buttons = []

        Renderer.elements.append(self)

        num_options = len(options)
        centerx = 600
        width = 192
        white_space = 40
        if num_options % 2 == 0:
            far_left = centerx - ((width + white_space) / 2) * (num_options // 2)            
        else:
            far_left = centerx - (width + white_space) * (num_options // 2)
        
        for num, option in enumerate(options):
            self.buttons.append(Button(option, far_left + (width + white_space) * num, 450, num, self.do_callback))

    def __del__(self):
        try:
            Renderer.elements.remove(self)
            for button in self.buttons:
                button.__del__()
        except ValueError:
            pass
        

    def do_callback(self, id):
        self.callback(id)
        print(id)
        self.__del__()

    def render(self, screen: pygame.surface.Surface):
        screen.blit(self.background_surface, (0,0))
        screen.blit(self.text_surface, self.text_rect)

