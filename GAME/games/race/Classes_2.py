                        #Author/developer:    Amanpreet Singh
                        #Project:             minigame

                        #import the installations
import pygame
import random
import pygame.mixer
import os               #no need
import time
pygame.init()

                             # # display # #
width               =           800
height              =           600
GameDisplay         =           pygame.display.set_mode((width, height))
title_game          =           "Insane Driver!"

                    # # Location of the player, car # #

X                   =           (width * 0.45)
Y                   =           (height * 0.8)

                     # # Title & background of the game # #
pygame.display.set_caption       ("Insane Driver!")
background          =            pygame.image.load("road2.png").convert()
background_rect     =            background.get_rect()

                         # # Game Music # #
pygame.mixer.music.load          ("RDsound.wav")
pygame.mixer.music.play          (-1)               #the music will be played non-stop

                       # # R.G.B. color codes # #
black               =            (0, 0, 0)
white               =            (255, 255, 255)
red                 =            (255, 0, 0)
green               =            (0, 255, 0)
ocean_blue          =            (0, 153, 153)
zilver              =            (192,192,192)

                     # # Player in the Game # #

car                 =            pygame.image.load("car__.png") #new car image added
#car_width          =            147                            #moet veranderd worden
car_T               =            GameDisplay.get_height() - car.get.height()
car_M               =            GameDisplay.get_width() / 2 - car.get_width() / 2
x_change            =            0

                    # #  Obstacle in the Game # #

Truckobstacle               =            pygame.image.load("Truckobstacle.png")
truckobstacle_width         =            57
truckobstacle_heigth        =            129
truckobstacle_speed         =            0
truckobstacle_X             =            random.randrange(0, width)
truckobstacle_Y             =            -600

                          # # the score # #
score                       =         (count, X, Y, size = 'Dodged:%d')
font                        =         (font.render, (size % count, True, black))
dodged                      =          0

                         # # font_style # #

font_style              =        pygame.font.Font("freesanbold.ttf")

def design_text(surf, text, size, X, Y):
    font                =        pygame.font.Font(font_style, size)
    text_surface        =        font.render(text, True, black)
    text_rect           =        text_surface.get_rect()
    text_rect.midtop    =        (X, Y)
    surf.blit                    (text_surface, text_rect)

                        # # Classes for the game # #

class player (pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image          =                         pygame.image.load("car.png") #image needs to be changed
        self.rect           =                         self.image.get_rect()
        self.width          =                         147
        self.rect.centerX   =                         GameDisplay.width() / 2
        self.rect.buttom    =                         height - 20
        self.speed          =                         0

    def update (self):
    x_change                = 0

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

    GameDisplay.blit()

class game_score (pygame.sprite.Sprite):  ##check

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.score =            GameDisplay (truckobstacle_speed * 15, 5, 50, "Spd: %d km")
        self.score2 =           GameDisplay( score, 5, 5, "Final Score: %d")

    def update (self):
        GameDisplay.blit(score)

class truckobstacle (pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image          =                       random.choice("Truckobstacle.png")  # needs to be changed as well
        self.rect           =                       self.image.get_rect()
        self.rect.width     =                       truckobstacle_width                 #57
        self.rect.height    =                       truckobstacle_heigth                #129
        self.speed          =                       4

    def update (self):

        self.rect.x              =                               random.randrang(0, width - self.rect.width)
        self.rect.y              =                               random.randrange(-600, 0)
        self.rect.speed          =                               0
        self.rect.added.speed   +=                               1

        if y < self.rect.x + self.rect.heigth: #Y , X
            print ("y4 crossover")

            if x > self.rect.x and x < self.rect.x + self.rect.width or x + car_width > self.rect.x and x + car_width < self.rect.x + sel.rect.width:
                print("x4 crossover")
                crash()

        self.move ()

                            # # definition of the intro # #
def game_intro():
    GameDisplay.blit                (background, background_rect)                           #background
    design_text                     (GameDisplay, "Insane Driver!", 70, width / 2, height / 6)
    design_text                     (GameDisplay,"press any key to continue!", 35, width / 2, height / 3)
    design_text                     (GameDisplay, "GOAL: dodge as many trucks as you can!", 23, width / 2, height / 2)
    design_text                     (GameDisplay, "to quit the game press esc!", 23, width / 2, height / 1.8)
    pygame.display.update()

    wait = True
    while wait:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K.ESCAPE:
                    pygame.quit()
            elif event.type == pygame.KEYUP:
                wait = False

                                        # # Crash # #
def crash ():
    GameDisplay.blit(background, background_rect)
    design_text(GameDisplay, "DEAD", 50, width / 2, height / 4)
    pygame.display.update()
    time.sleep(0.1)
    pygame.display.update()

#message display, klopt nog niet
        self.font_messagedisplay =           pygame.font.Font("freesanbold.ttf", 100)
        self.text =                          font.render("You are DEAD", True, red)
        self.TextRect.center =               ((width/2),(height/2))


    GameDisplay.fill(white)
    GameDisplay.blit(background, background_rect)
    pygame.display.update()
    clock.tick(60)

#def main():
#game_Intro()
game_loop()
pygame.quit()
quit()















#x_change = 0 zetten
