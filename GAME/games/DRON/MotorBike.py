import pygame
import os

from helpers import misc_helper


class MotorBike(pygame.sprite.Sprite):
    def __init__(self, init_position, init_direction, bike_colour, surface):
        pygame.sprite.Sprite.__init__(self)
        self.misc = misc_helper.MiscHelper()
        self.surface = surface

        self.image, self.rect = self.misc.load_image(os.path.join(os.getcwd(), "games/DRON/data/motorbike.png"))
        self.rect.x = init_position[0]
        self.rect.y = init_position[1]

        self.rotation_done_for = init_direction
        self.direction = init_direction
        self.speed = 4
        self.colour = bike_colour
        self.dead = False
        self.line = []

        self.rotate(0, init_direction)

    def update(self):
        if not self.rotation_done_for == self.direction:
            self.rotate(self.rotation_done_for, self.direction)

        if self.misc.is_out_of_bounds(self.rect):
            self.dead = True

        if self.direction == 0:
            self.rect.move_ip(0, -self.speed)
        elif self.direction == 1:
            self.rect.move_ip(+self.speed, 0)
        elif self.direction == 2:
            self.rect.move_ip(0, +self.speed)
        elif self.direction == 3:
            self.rect.move_ip(-self.speed, 0)
        elif self.direction == 4:
            self.rect.move_ip(0, 0)

        self.handle_line()

    def rotate(self, old_direction, new_direction):
        old_location = (self.rect.x, self.rect.y)
        rotation = (old_direction - new_direction) * 90
        self.image = pygame.transform.rotate(self.image, rotation)
        self.rotation_done_for = new_direction
        self.rect = self.image.get_rect()

        self.rect.x = old_location[0]
        self.rect.y = old_location[1]

    def handle_line(self):
        self.line.append((self.rect.x, self.rect.y))
        # if self.direction == 0:
        #     self.line.append(self.rect.midbottom)
        # elif self.direction == 1:
        #     self.line.append(self.rect.midleft)
        # elif self.direction == 2:
        #     self.line.append(self.rect.midtop)
        # elif self.direction == 3:
        #     self.line.append(self.rect.midright)

        for x in range(len(self.line)):
            pygame.draw.rect(self.surface, self.colour, (self.line[x][0], self.line[x][1], 10, 10))
