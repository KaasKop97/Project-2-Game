import pygame
import os
from helpers import misc_helper
from handlers import config_handler
from games.Galaxy_Trespassers.bullet import Bullet


# ..................................PLAYER CLASS..................................#


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.misc = misc_helper.MiscHelper()
        self.conf = config_handler.ConfigHandler()
        self.game_width = int(self.conf.get_value("game", "width"))
        self.game_height = int(self.conf.get_value("game", "height"))

        self.image_stationary, self.rect =  self.misc.load_image(os.path.join("games", "Galaxy_Trespassers", "data",
                                                 "player_flying.png"))
        self.image_flying, self.rect =  self.misc.load_image(os.path.join("games", "Galaxy_Trespassers", "data",
                                                 "player_flying.png"))

        self.image = self.image_flying
        self.rect.centerx = self.game_width / 2
        self.rect.bottom = self.game_height - 20
        self.radius = int(self.rect.width / 3)
        self.speedx = 0
        self.added_speed = 8.5
        self.shoot_delay = 360
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right > self.game_width:
            self.rect.right = self.game_width
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)

            # all_sprites.add(bullet)
            # bullets.add(bullet)
            # random.choice(lazer_sounds).play()
