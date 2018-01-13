import pygame
import os
from helpers import misc_helper
from handlers import config_handler


# .......................................WALL.......................................#


class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.misc = misc_helper.MiscHelper()
        self.conf = config_handler.ConfigHandler()
        self.game_width = int(self.conf.get_value("game", "width"))
        self.game_height = int(self.conf.get_value("game", "height"))

        self.image, self.rect = self.misc.load_image(os.path.join("games", "Galaxy_Trespassers", "data", "wall.png"))
        self.image.set_colorkey((0, 0, 0))
        self.rect.centerx = self.game_width / 2
        self.rect.bottom = self.game_height
