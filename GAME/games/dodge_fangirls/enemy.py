import pygame
from handlers import config_handler

class Enemys(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, img, score):
        pygame.sprite.Sprite.__init__(self)

        self.X = x
        self.Y = y
        self.W = w
        self.H = h
        self.speed = 7.5
        self.score = score
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = self.X
        self.rect.y = self.Y
        self.conf = config_handler.ConfigHandler()
        self.game_width = int(self.conf.get_value("game", "width"))
        self.game_height = int(self.conf.get_value("game", "height"))

    def update(self):
        self.rect.move_ip(0, self.speed)


        if self.rect.top > self.game_height + 10:
            self.rect.x = self.X
            self.rect.y = self.Y
            self.speed += 0.2

        # if self.Y > self.game_height:
        #     self.Y = 0
        #     Self.X = random.randrange(0,display_width)
        #     self.dodged += self.score




