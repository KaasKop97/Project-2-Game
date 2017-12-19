import pygame
import os
from helpers import log_helper, misc_helper
from handlers import config_handler


class MotorBike(pygame.sprite.Sprite):
    def __init__(self, init_pos, init_rot, bike_colour, init_direction, surface):
        pygame.sprite.Sprite.__init__(self)
        self.config = config_handler.ConfigHandler()
        self.log = log_helper.LogHelper()
        self.misc = misc_helper.MiscHelper()
        self.image, self.rect = self.misc.load_image(os.path.join(os.getcwd(), "games/DRON/data/motorbike.png"))
        self.rotate(3, 0)
        self.colour = bike_colour
        self.surface = surface

        self.rect.x += init_pos[0]
        self.rect.y += init_pos[1]
        self.speed = 5
        self.dead = False
        self.direction = init_direction
        self.rotation_done_for = init_direction
        self.drawn_line = []

    def update(self):
        if self.misc.is_out_of_bounds(self.rect):
            self.dead = True
            self.stop_moving()
            self.direction = self.rotation_done_for
            self.misc.stop_music()

        # Here we check what direction to go in and prevent people from going in the opposite direction
        # TODO: Going in the opposite direction stops the character in place fix et.
        if self.direction == 3 and not self.rotation_done_for == 1:
            self.move_left()
        elif self.direction == 0 and not self.rotation_done_for == 2:
            self.move_up()
        elif self.direction == 2 and not self.rotation_done_for == 0:
            self.move_down()
        elif self.direction == 1 and not self.rotation_done_for == 3:
            self.move_right()
        self.handle_line()
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
        old_values = [self.rect.x, self.rect.y]
        rotation = (old_direction - new_direction) * 90
        self.image = pygame.transform.rotate(self.image, rotation)
        self.rect = self.image.get_rect()
        self.rect.x = old_values[0]
        self.rect.y = old_values[1]

    def handle_line(self):
        if self.direction == 1:
            self.drawn_line.append((self.rect.x - self.rect.width // 2, self.rect.y, self.rect.width, self.rect.height))
        elif self.direction == 0:
            self.drawn_line.append((self.rect.x, self.rect.y + self.rect.height, self.rect.width, self.rect.height))
        elif self.direction == 2:
            self.drawn_line.append((self.rect.x, self.rect.y - self.rect.height // 2, self.rect.width, self.rect.height))
        elif self.direction == 3:
            self.drawn_line.append((self.rect.x + self.rect.width, self.rect.y, self.rect.width, self.rect.height))

        for x in range(len(self.drawn_line)):
            if self.rect.collidepoint(self.drawn_line[x][0], self.drawn_line[x][1]):
                print("Die pls.")
            if not self.drawn_line[x] == (self.rect.x, self.rect.y):
                pygame.draw.rect(self.surface, self.colour, (self.drawn_line[x][0], self.drawn_line[x][1], 25, 25))
