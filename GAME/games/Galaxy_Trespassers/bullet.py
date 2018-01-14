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
        self.bullet, self.rect_bullet = self.misc.load_image(os.path.join("games", "Galaxy_Trespassers", "data", "bullet.png"))
        self.explosion, self.rect_explosion = self.misc.load_image(os.path.join("games", "Galaxy_Trespassers", "data", "explosion.png"))

        self.image = self.bullet
        self.rect = self.rect_bullet

        self.image.set_colorkey((0, 0, 0))
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10
        self.spawn_time = pygame.time.get_ticks()
        self.hit = False

    def update(self):
        self.rect.y += self.speedy

    def explode(self, center):
        self.image = self.explosion
        self.rect = self.rect_explosion
        self.speedy = 0
        self.rect.y = 0
        self.rect.center = center
