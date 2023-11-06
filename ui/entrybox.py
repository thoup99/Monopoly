import pygame
from renderer import Renderer
from input import Input


class EntryBox:
    big_font = pygame.font.SysFont('Arial', 60)
    font = pygame.font.SysFont('Arial', 50)

    def __init__(self, text: str, callback) -> None:
        self.is_active = True
        self.callback = callback
        self.entered_text = ""

        self.background_surface = pygame.Surface((1200, 800))
        self.background_surface.set_alpha(128)
        self.background_surface.fill((0,0,0))

        self.text_surface = EntryBox.big_font.render(text, True, (255,255,255))
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (600, 400 - 30)

        self.entry_surface = EntryBox.font.render(self.entered_text, True, (255,255,255))
        self.entry_rect = self.entry_surface.get_rect()
        self.entry_rect.center = (600, 400 + 30)

        Renderer.addElement(self)
        Input.subscribe(pygame.KEYDOWN, self.handleInput)

    def __del__(self):
        print("Deleting Entry Box")


    def destroy(self):
        Renderer.removeElement(self)
        Input.unsubscribe(pygame.KEYDOWN, self.handleInput)

    def handleInput(self, key, unicode: str):
        if key == pygame.K_RETURN and len(self.entered_text) > 0:
            self.callback(self.entered_text)
            self.destroy()

        elif key == pygame.K_BACKSPACE and len(self.entered_text) > 0:
            self.entered_text = self.entered_text[:-1]
            self.rerenderText()

        elif (unicode.isalpha() or unicode == " ") and len(self.entered_text) < 16:
            self.entered_text += unicode
            self.rerenderText()


    def rerenderText(self):
        self.entry_surface = EntryBox.font.render(self.entered_text, True, (255,255,255))
        self.entry_rect = self.entry_surface.get_rect()
        self.entry_rect.center = (600, 400 + 30)


    def render(self, screen: pygame.surface.Surface):
        screen.blit(self.background_surface, (0,0))
        screen.blit(self.text_surface, self.text_rect)
        screen.blit(self.entry_surface, self.entry_rect)