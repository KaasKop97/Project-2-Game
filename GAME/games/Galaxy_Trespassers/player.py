import pygame
import os
from helpers import misc_helper
from handlers import config_handler


# ..................................PLAYER CLASS..................................#


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.misc = misc_helper.MiscHelper()
        self.conf = config_handler.ConfigHandler()
        self.game_width = int(self.conf.get_value("game", "width"))
        self.game_height = int(self.conf.get_value("game", "height"))

        self.image_stationary, self.rect_stationary = self.misc.load_image(os.path.join("games", "Galaxy_Trespassers", "data",
                                                                             "player_flying.png"))
        self.image_flying, self.rect_flying = self.misc.load_image(os.path.join("games", "Galaxy_Trespassers", "data",
                                                                         "player_flying.png"))

        self.image = self.image_stationary
        self.rect = self.rect_stationary

        self.rect.centerx = self.game_width / 2
        self.rect.bottom = self.game_height - 20
        self.speedx = 0
        self.added_speed = 8.5
        self.dead = False
        self.killed = 0

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right > self.game_width:
            self.rect.right = self.game_width
        if self.rect.left < 0:
            self.rect.left = 0
