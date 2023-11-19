import pygame

from ui.label import Label
from ui.colored_rectangle import ColoredRectangle

class BackgroundLabel:
    def __init__(self, text, center_x, center_y, font_size = 30, fgcolor = (255, 255, 255), bgcolor = (0, 0, 0), alpha = 255) -> None:
        self.alpha = alpha

        self.rectangle = ColoredRectangle((center_x, center_y))
        self.label = Label(text, center_x, center_y, font_size, fgcolor)
        
        self.setText(text)

    def setText(self, newText):
        self.label.setText(newText)
        self.rectangle.setWidth(self.label.getWidth() + 10)
        self.rectangle.setHeight(self.label.getHeight() + 6)

        if newText == "" or newText == " ":
            self.rectangle.setAlpha(0)
        else:
            self.rectangle.setAlpha(self.alpha)