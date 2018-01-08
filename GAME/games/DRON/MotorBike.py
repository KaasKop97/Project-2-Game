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

        self.direction_changed = 0

        self.line = [(self.rect.x, self.rect.y, 10, 10)]
        # Because the original direction is 1 we need to append 15 so that the player doesnt die in 1sec kek
        self.hitbox = (self.rect.x + 15, self.rect.y, 2, 2)
        self.rotate(0, init_direction)

    def update(self):
        if self.misc.is_out_of_bounds(self.rect):
            self.dead = True

        if self.direction == 0 and not self.direction_changed == 2:
            self.rect.move_ip(0, -self.speed)
            self.direction_changed = 0
        elif self.direction == 1 and not self.direction_changed == 3:
            self.rect.move_ip(+self.speed, 0)
            self.direction_changed = 1
        elif self.direction == 2 and not self.direction_changed == 0:
            self.rect.move_ip(0, +self.speed)
            self.direction_changed = 2
        elif self.direction == 3 and not self.direction_changed == 1:
            self.rect.move_ip(-self.speed, 0)
            self.direction_changed = 3
        elif self.direction == 4:
            # direction 4 is to stop the vehicle
            self.rect.move_ip(0, 0)
        else:
            self.direction = self.direction_changed
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
        if not self.line[-1] == self.rect:
            self.line.append((self.rect.x, self.rect.y, 10, 10))
            
            if self.direction == 0:
                self.hitbox = (self.rect.x, self.rect.y - self.rect.height // 2, 10, 2)
            elif self.direction == 1:
                self.hitbox = (self.rect.x + self.rect.width + 5, self.rect.y, 2, 10)
            elif self.direction == 2:
                self.hitbox = (self.rect.x, self.rect.y + 15, 10, 2)
            elif self.direction == 3:
                self.hitbox = (self.rect.x - 5, self.rect.y, 2, 10)

        for x in range(len(self.line)):
            pygame.draw.rect(self.surface, self.colour, (self.line[x][0], self.line[x][1], self.line[x][2], self.line[x][3]))