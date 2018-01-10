                                # # Installations # #
import pygame
pygame.init()


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
        self.game_heigth            = int(self.conf.get_value("game", "heigth"))

    def update(self):
        print(self.rect.y)
        self.rect.move_ip(0, self.speed)
        