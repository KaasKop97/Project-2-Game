import pygame
import pygame.gfxdraw
import random


# This is where all the logic of the game should come to, you can have as many sub files and directories as you want
# Just remember that this is the only class that is called by thw while loop in main.py

class Memes:
    def __init__(self):
        self.game_name = "Clicker"
        self.game_author = "Mitchel van Hamburg"
        self.font = pygame.font.init()
        self.font = pygame.font.SysFont('Verdana', 15)

    def main(self, surface):
        pygame.draw.circle(surface, (0, 0, 0), (500, 500), 100)

    def mousebutton_down(self, surface, position):
        pygame.draw.rect(surface, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)), (position[0], position[1], 50, 50))

    def startup(self):
        self.font.render("Welcome to the clicker game!", 1, (0, 0, 0))
