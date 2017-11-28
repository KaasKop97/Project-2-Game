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
        self.direction = 1
        self.rotation_done_for = 1

    def update(self):
        if self.misc.is_out_of_bounds(self.rect):
            self.dead = True
            self.direction = "none"
            self.stop_moving()
            self.misc.stop_music()
        if self.direction == 3:
            self.move_left()
        elif self.direction == 0:
            self.move_up()
        elif self.direction == 2:
            self.move_down()
        elif self.direction == 1:
            self.move_right()
        self.log.write_log("DEBUG", "Moving... new values: " + str(self.rect.x) + ", " + str(self.rect.y))

    def move_left(self):
        self.rotate(self.rotation_done_for, 3)
        self.rotation_done_for = 3
        self.rect.move_ip(-self.speed, 0)

    def move_up(self):
        self.rotate(self.rotation_done_for, 0)
        self.rotation_done_for = 0
        self.rect.move_ip(0, -self.speed)

    def move_down(self):
        self.rotate(self.rotation_done_for, 2)
        self.rotation_done_for = 2
        self.rect.move_ip(0, +self.speed)

    def move_right(self):
        self.rotate(self.rotation_done_for, 1)
        self.rotation_done_for = 1
        self.rect.move_ip(+self.speed, 0)

    def stop_moving(self):
        self.rect.move_ip(0, 0)

    def rotate(self, old_direction, new_direction):
        rotation = (old_direction - new_direction) * 90
        self.image = pygame.transform.rotate(self.image, rotation)

    def draw_line(self):
        pass

    def hit_line(self):
        pass

    def is_out_of_bounds(self):
        if self.rect[0] >= int(self.config.get_value("game", "width")) or self.rect[0] <= 0 or self.rect[1] >= int(
                self.config.get_value("game", "height")) or self.rect[1] <= 0:
            return True
