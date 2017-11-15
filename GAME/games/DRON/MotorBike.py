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
        self.x = 0
        self.y = 0
        self.oldx = None
        self.oldy = None
        self.speed = 3
        self.dead = 0
        self.direction = ""

    def move(self):
        self.oldx = self.x
        self.oldy = self.y
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

    def draw(self, surface):
        surface.fill((255, 255, 255))
        surface.blit(self.image, (self.x, self.y))

    def hit_line(self):
        pass

    def out_of_bounds(self):
        pass
