                                    # # Installations # #
import pygame
pygame.init()


                                    # # Class Player # #

class Player (pygame.sprite.Sprite):
    def __init__(self, x, y, q, h, img):
        pygame.sprite.Sprite.__init__(self)

        self.X                  =       x
        self.Y                  =       y
        self.W                  =       w
        self.H                  =       h
        self.image              =       pygame.image.load(img)
        self.rect               =       self.image.get_rect()
        self.rect.x             =       self.X
        self.rect.y             =       self.Y
        self.conf               =       config_handler.CongigHandler()
        self.game_width         =       int(self.conf.get_value("game", "width"))
        self.game_height        =       int(self.conf.get_value("game", "height"))
        self.changeX            =       0

    def update(self):

        self.rect.move_ip(self.changeX, 0)