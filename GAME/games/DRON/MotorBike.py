import pygame
import os
from helpers import log_helper, misc_helper
from handlers import config_handler


class MotorBike(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.config = config_handler.ConfigHandler()
        self.log = log_helper.LogHelper()
        self.misc = misc_helper.MiscHelper()
        self.image, self.rect = self.misc.load_image(os.path.join(os.getcwd(), "games/DRON/data/motorbike.png"))
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect.x += 5
        self.rect.y += 5
        self.speed = 5
        self.dead = False
        self.direction = "right"
        self.rotation_done_for = ""

    def update(self):
        if self.misc.is_out_of_bounds(self.rect):
            self.dead = True
        if self.direction == "left":
            self.move_left()
        elif self.direction == "up":
            self.move_up()
        elif self.direction == "down":
            self.move_down()
        else:
            self.move_right()
        self.log.write_log("DEBUG", "Moving... new values: " + str(self.rect.x) + ", " + str(self.rect.y))

    def move_left(self):
        if self.rotation_done_for == "right":
            self.image = pygame.transform.rotate(self.image, 180)
        elif not self.rotation_done_for == "left":
            self.image = pygame.transform.rotate(self.image, -90)

        self.rotation_done_for = "left"
        self.rect.move_ip(-self.speed, 0)

    def move_up(self):
        if self.rotation_done_for == "down":
            self.image = pygame.transform.rotate(self.image, 180)
        elif not self.rotation_done_for == "up":
            self.image = pygame.transform.rotate(self.image, -90)

        self.rotation_done_for = "up"
        self.rect.move_ip(0, -self.speed)

    def move_down(self):
        if self.rotation_done_for == "up":
            self.image = pygame.transform.rotate(self.image, 180)
        elif not self.rotation_done_for == "down":
            self.image = pygame.transform.rotate(self.image, -90)

        self.rotation_done_for = "down"
        self.rect.move_ip(0, +self.speed)

    def move_right(self):
        # Because this is the default we need to check if it's empty or not
        if self.rotation_done_for == "left":
            self.image = pygame.transform.rotate(self.image, 180)
        elif not self.rotation_done_for == "right":
            self.image = pygame.transform.rotate(self.image, -90)

        self.rotation_done_for = "right"
        self.rect.move_ip(+self.speed, 0)

    def draw_line(self):
        pass

    def hit_line(self):
        pass

    def is_out_of_bounds(self):
        if self.rect[0] >= int(self.config.get_value("game", "width")) or self.rect[0] <= 0 or self.rect[1] >= int(
                self.config.get_value("game", "height")) or self.rect[1] <= 0:
            return True
