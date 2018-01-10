import pygame
import time
import random
import sys
import os

# Display #

display_width = 800
display_height = 600
WINDOW = pygame.display.set_mode((display_width, display_height))

clock = pygame.time.Clock()

# game icon #
pygame.display.set_icon(cbImg)

# pause and Crash #
pause = False

class DodgeExes:
    def __init__(self, surface):
        self.game_name = "Dodge the Exes"
        self.author = "Charone Monteiro Tavares"
        self.gameDisplay = surface
        self.cb = player(display_width * 0.45, display_height * 0.9, 43, 55)
        self.fan4 = enemy4(random.randrange(0, display_width), -500, 196, 57, 3 )
        self.fan3 = enemy3(random.randrange(0, display_width), -300, 140, 57, 3)
        self.fan2 = enemy2(random.randrange(0, display_width), -700, 92, 57, 3)
        self.fanri = enemyri(random.randrange(0, display_width), -100, 45, 57, 3)





    def load(self, surface):
        # Colors #
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        self.red = (150, 0, 0)
        self.bright_red = (255, 0, 0)

        self.oranje = (220, 200, 0)

        self.green = (0, 150, 0)
        self.bright_green = (0, 255, 0)

        self.blue = (0, 0, 255)
        self.baby_blue = (0, 120, 255)

    def update(self, surface):
        # background #
        self.background = pygame.image.load('achtergrondfoto.png')
        self.background_rect = self.background.get_rect()



    def mousebutton_down(self, surface, event):
        # If you need to do an action on mouse button while it's in the down position then use this
        pass

    def mousebutton_up(self, surface, event):
        # If you need to do an action on mouse button while it's in the up position (after a down) then use this
        pass

    def key_input(self, key):
        # If you need to do an action on key inputs use this access key codes, check DRON.py for examples
        # For example: key A = keycode 97 so to check this do 'if key == 97'
        pass

    def stop_game(self):
        pass

class player():
    def __init__(self, x, y, cb_width, cb_height, surface):
        self.font = pygame.font.SysFont('freesansbold.ttf', 25)
        self.cbImg = pygame.image.load('cbCHARACTER.png')
        self.cb_width = 43
        self.cb_height = 55

    def cb(x, y, cb_width, cb_height):
        self.gameDisplay.blit(cbImg, (x, y, cb_width, cb_height))

    def cb_dodged(self, count):
        text = self.font.render("Dodged: " + str(count), True, white)
        gameDisplay.blit(text, (0, 0))




class enemy4():
    def __init__(self, fan4_x, fan4_y, fan4_width, fan4_height, surface):
        # fan 4 #
        self.fan4_width = 196
        self.fan4_height = 57
        self.fan4_x = random.randrange(0, display_width)
        self.fan4_y = -500
        self.fan4_speed = 3

    def fangirl4(fan4_x, fan4_y, fan4_width, fan4_height):
        self.gameDisplay.blit(fan4Img, (fan4_x, fan4_y, fan4_width, fan4_height))

class enemy3():
    def __init__(self, fan3_x,fan3_y,fan3_width,fan3_height, surface):
        # fan 3 #
        self.fan3_width = 140
        self.fan3_height = 57
        self.fan3_x = random.randrange(0, display_width)
        self.fan3_y = -300
        self.fan3_speed = 3

    def fangirl3(fan3_x,fan3_y,fan3_width,fan3_height):
        self.gameDisplay.blit(fan3Img,(fan3_x,fan3_y,fan3_width,fan3_height))

class enemy2():
    def __init__(self, fan2_x, fan2_y, fan2_width, fan2_height, surface):
        # fan 2 #
        self.fan2_width = 92
        self.fan2_height = 57
        self.fan2_y = -700
        self.fan2_speed = 3


    def fangirl2(fan2_x, fan2_y, fan2_width, fan2_height):
        self.gameDisplay.blit(fan2Img, (fan2_x, fan2_y, fan2_width, fan2_height))

class enemyri():
    def __init__(self, fanri_x,fanri_y,fanri_width,fanri_height, surface):
        # fan 4 #
        self.fanri_width = 45
        self.fanri_height = 57
        self.fanri_x = random.randrange(0, display_width)
        self.fanri_y = -100
        self.fanri_speed = 3

    def fangirlri(fanri_x,fanri_y,fanri_width,fanri_height):
        self.gameDisplay.blit(fanriImg,(fanri_x,fanri_y,fanri_width,fanri_height))

