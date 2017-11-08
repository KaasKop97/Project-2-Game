import pygame
import os
import sys


class MenuHelper:
    def __init__(self):
        self.menu_items = ["PLAY", "ABOUT", "CREDITS"]
        self.menu_items_coord = []
        self.font = pygame.font.init()
        self.font = pygame.font.SysFont('Verdana', 15)

    def make_button(self, surface, text_colour, x, y, width, height, text, colour=(66, 66, 66)):
        pygame.draw.rect(surface, colour, (x, y, width, height))

        label = self.font.render(text, 1, text_colour)
        surface.blit(label, (x + 2, y)) # Renders the label just above the bottom of the button

    # def button_clicked(self, position, ):
