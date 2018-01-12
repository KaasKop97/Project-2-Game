import pygame
import os
from helpers import misc_helper
from handlers import config_handler


# .................................EXPLOSION CLASS.................................#


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.misc = misc_helper.MiscHelper()
        self.conf = config_handler.ConfigHandler()
        self.game_width = int(self.conf.get_value("game", "width"))
        self.game_height = int(self.conf.get_value("game", "height"))

        self.image, self.rect = self.misc.load_image(os.path.join("games", "Galaxy_Trespassers", "data", "explosion.png"))
        self.image.set_colorkey((0, 0, 0))

        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 60

    def update(self):
        pass
        # now = pygame.time.get_ticks()
        # if now - self.last_update > self.frame_rate:
        #     self.last_update = now
        #     self.frame += 1
        #     self.kill()
