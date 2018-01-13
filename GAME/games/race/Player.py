                                    # # Installations # #
import pygame
from handlers import config_handler

                                    # # Class Player # #

class Player (pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, img):
        pygame.sprite.Sprite.__init__(self)

        self.X                  =       x
        self.Y                  =       y
        self.W                  =       w
        self.H                  =       h
        self.image              =       pygame.image.load(img)
        self.rect               =       self.image.get_rect()
        self.rect.x             =       self.X
        self.rect.y             =       self.Y
        self.conf               =       config_handler.ConfigHandler()
        self.game_width         =       int(self.conf.get_value("game", "width"))
        self.game_height        =       int(self.conf.get_value("game", "height"))
        self.changeX            =       0
        self.dead               =       False
<<<<<<< HEAD
        self.dodge_count        =       self.truck.dodged
=======
<<<<<<< HEAD
        # self.dodge_count        =       self.Truck.dodged
=======
        #self.dodge_count        =       self.truck.dodged
>>>>>>> 2b0ee0e411bd7ad65d7e7832f1953d27bf57ae28
>>>>>>> 0613ffd070f5a426a758fab9bdc2cc7fa0aebd19

    def update(self):

        self.dead = True
        self.rect.move_ip(self.changeX, 0)
