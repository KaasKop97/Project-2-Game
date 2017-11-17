import pygame
import os
from helpers import log_helper
from handlers import config_handler


class MotorBike(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.config = config_handler.ConfigHandler()
        self.log = log_helper.LogHelper()
        self.image = pygame.image.load(os.path.join(os.getcwd(), "games/DRON/data/motorbike.png"))
        self.rect = self.image.get_rect()
        self.x = 5
        self.y = 5
        self.speed = 7
        self.dead = False
        self.direction = ""

    def move(self):
        if self.direction == "left":
            self.move_left()
        elif self.direction == "up":
            self.move_up()
        elif self.direction == "down":
            self.move_down()
        else:
            self.move_right()
        self.log.write_log("DEBUG", "Moving... new values: " + str(self.x) + ", " + str(self.y))

    def move_left(self):
        self.x -= self.speed

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed

    def move_right(self):
        self.x += self.speed

    def draw_line(self):
        pass

    def draw(self, surface):
        surface.fill((0, 0, 0))
        surface.blit(self.image, (self.x, self.y))

    def hit_line(self):
        pass

    def is_out_of_bounds(self):
        if self.x >= int(self.config.get_value("game", "width")) or self.x <= 0 or self.y >= int(self.config.get_value("game", "height")) or self.y <= 0:
            self.dead = True

