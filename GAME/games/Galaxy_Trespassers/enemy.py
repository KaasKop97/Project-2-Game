import pygame
import os
import random
from helpers import misc_helper
from handlers import config_handler


# ..................................ENEMY CLASSES..................................#


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.misc = misc_helper.MiscHelper()
        self.conf = config_handler.ConfigHandler()

        self.game_width = int(self.conf.get_value("game", "width"))
        self.game_height = int(self.conf.get_value("game", "height"))
        self.image, self.rect = self.misc.load_image(image)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        self.radius = int(self.rect.width / 3)
        self.rect.x = random.randrange(0, self.game_width - self.rect.width)
        self.rect.y = random.randrange(-600, -100)
        self.speedy = 2
        Enemy.score = 50

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > self.game_height + 10:
            self.reset_position()

    def reset_position(self):
        self.rect.x = random.randrange(0, self.game_width - self.rect.width)
        self.rect.y = random.randrange(-600, -100)
