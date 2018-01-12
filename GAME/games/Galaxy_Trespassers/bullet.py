import pygame
import os
from helpers import misc_helper
from handlers import config_handler


# ......................................BULLET.....................................#


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.misc = misc_helper.MiscHelper()
        self.conf = config_handler.ConfigHandler()
        self.game_width = int(self.conf.get_value("game", "width"))
        self.game_height = int(self.conf.get_value("game", "height"))
        self.image, self.rect = self.misc.load_image(os.path.join("games", "Galaxy_Trespassers", "data", "bullet.png"))
        self.image.set_colorkey((0, 0, 0))

        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            print("BOOM BITCH")

    def explode(self):
        pass
