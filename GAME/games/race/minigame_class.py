import pygame

import random

import pygame.mixer

#import os

import time

pygame.init()

#display
width =     800
height =    600

x =         (display_width * 0.45)
y =         (display_height * 0.8)

#RGB codes
black =             (0, 0, 0)
white =             (255, 255, 255)
red =               (255, 0, 0)
green =             (0, 255, 0)
ocean_blue =        (0, 153, 153)
zilver =            (192,192,192)

#background_image = pygame.image.load("BGgame.png").convert()
#pygame.mixer.music.load("RDsound.wav")
carImg = pygame.image.load("car.png")
Truckobstacle = pygame.image.load("Truckobstacle.png")
#truckobstacle2 = pygame.image.load("Truckobstacle2.png")

car_width =         153

truckobstacle_width =   57
truckobstacle_heigth =  129
truckobstacle_speed =   0

truckobstacle_x =       random.randrange(0, display_width) #ipv rect truckobstacle_x
truckobstacle_y =       -600

                                                 #---FUNTIONS---#

class gameDisplay (pygame.sprite.Sprite):

    def __init__(self):
        self.width =    width
        self.height =   heigth
        self.display =  pygame.display.set_mode

    def background_display (self):
        self.gameDisplay.fill(zilver)


class player (pygame.sprit.Sprite):     #this class will represent the player, the car

    def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image =        carImg
    self.image.load =   pygame.image.load("car.png")
    self.image.width =  153
    self.image.blit =   gameDisplay.blit()

    def get_keys(self):
    pygame.sprite.Sprite.__init__(self)
    self.x_change = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()

            # Did someone putt the keydown?
            if event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_LEFT:
                    x_change = -5
                    print(event.key)

                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                    print(event.key)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key - -pygame.K_RIGHT:
                    x_change = 0
                    print(event.key)

    def update(self): #location of the player
        x = (width * 0.45)
        y = (height * 0.8)

        carImg(x,y)

class truckobtacle (pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect =         self.image.get_rect()
        self.rect.width =   57
        self.rect.heigth =  129
        self.image =        random.choice("Truckobstacle.png")
        self.speed =        4

    def move(self):
        self.rect.move_ip(0, self.speed)

    def update(self):
        self.rect.x =               random.randrang(0, display_width - self.rect.width)
        self.rect.y =               random.randrange(-600, 0)
        self.rect.speed =           0
        self.rect.added.speed +=    1

        if y < self.rect.x + self.rect.heigth:
            print ("y4 crossover")

            if x > self.rect.x and x < self.rect.x + self.rect.width or x + car_width > self.rect.x and x + car_width < self.rect.x + sel.rect.width:
                print("x4 crossover")
                crash()

        self.move ()

class message_display (pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font =             pygame.font.Font("freesanbold.ttf", 100)
        self.text =             font.render("You are DEAD", True, red)
        self.TextRect.center =   ((width/2),(heigth/2))

    def update (self):
        self.message_display =  gameDisplay.blitt(self.text)
        time.sleep(0.1)

class score_display (pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font =     pygame.font.sysFont("freesanbold.ttf",21)
        self.text =     font.render(message_fortmat % count, True, red)

    def update (self):
        self.gameDisplay.dodged=            (dodged,5,25)
        self.gameDisplay.added.speed =      (self.rect.added.speed * 15, 5, 50)
        self.gameDisplay.score =            (5, 5, "final Score: %d km")

        self.gameDisplay.blitt(self.gameDisplay.dodged, self.gameDisplay.added.speed, self.gameDisplay.score)

class crash (pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font =                 pygame.font.Font("freesansbold.ttf", 50)
        self.text =                 font.render("DEAD", largeText)
        self.TextRect.center =      ((display_width / 2), (display_height / 4))

    def update (self):

        self.message_display = gameDisplay.blit(TextSurf, TextRect)

        if x > width - car_width or not x < display_width - car_width or not x > 0:
            print ("out of boundaries")
            crash()

class button (pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.mouse =                pygame.mouse.get_pos()
        self.click =                pygame.mouse.get_pressed()
        self.font =                 pygame.font.Font("freesansbold.ttf", 18)
        self.TextRect.center =      ((x + (w / 2), y + (h / 2)))

    def update (self):

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                action()
        else:

            pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font("freesansbold.ttf", 18)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x + (w / 2), y + (h / 2)))
        gameDisplay.blit(textSurf, textRect)

class pause (pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font =                 pygame.font.Font("freesansbold.ttf", 70)
        self.text =                 text_objects("Pause", largeText)
        self.TextRect.center =     ((display_width / 2), (display_height / 4))

    def update (self):

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

class game_intro (pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.display =          gameDisplay.fill(ocean_blue)
        self.font =             pygame.font.Font("freesansbold.ttf", 50)
        self.text =             text_objects("let's drive", largeText)
        self.TextRect.center =  ((display_width / 2), (display_height / 10))

    def update (self)

        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        #blit?

class unpause (pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pause = False

    def update (self):
        global pause



        pygame.display.update()
        clock.tick(60)

#def main():
#game_Intro()
game_loop()
pygame.quit()
quit()









