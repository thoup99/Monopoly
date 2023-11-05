import pygame

class Renderer:
    elements = []

    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.screen = screen
        self.color = (32, 150, 65)

    def addElement(element):
        Renderer.elements.append(element)

    def removeElement(element):
        Renderer.elements.remove(element)

    def renderAll(self):
        self.screen.fill(self.color)

        for element in Renderer.elements:
            element.render(self.screen)

        pygame.display.update()