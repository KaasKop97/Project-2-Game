                                # # Installations # #
import pygame
import random
from handlers import config_handler

                                # # Class Truck # #

class Truck(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, img, score):
        pygame.sprite.Sprite.__init__(self)

        self.X                      = x
        self.Y                      = y
        self.W                      = w
        self.H                      = h
        self.speed                  = 7
        self.score                  = score
        self.image                  = pygame.image.load(img)
        self.rect                   = self.image.get_rect()
        self.rect.x                 = self.X
        self.rect.y                 = self.Y
        self.conf                   = config_handler.ConfigHandler()
        self.game_width             = int(self.conf.get_value("game", "width"))
        self.game_height            = int(self.conf.get_value("game", "height"))
        self.dodge_count = 0

    def update(self):
        self.rect.move_ip(0, self.speed)

        if self.rect.y > self.game_height + 10:
            self.rect.x = random.randrange(0, self.game_width)
            self.rect.y = -30
            self.speed += 0.2
            self.dodge_count += 1

