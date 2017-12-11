#   IMPORTS  #
import pygame
import time
import random
import pygame.mixer
import os
import math

#   INITIALIZATIONS  #

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()

#   DISPLAY   #
display_width = 800
display_height = 780
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Galaxy Trespassers")

#   OBJECTS   #
# objects = list()
# objects.append(aircraft_width)
# objects.append(bullet_height)
aircraft_width = 180
bullet_height = 22
enemy_height = 130
enemy_width = 165

#   RGB-COLORS  #
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
pink = (255, 102, 102)

#   CLOCK   #

clock = pygame.time.Clock()

#   PLAY MUSIC  #

pygame.mixer.music.load("Galaxy trespassers.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#   IMAGE LOADS #
aircraftNullImg = pygame.image.load('aircraft zone trespassers.png')
aircraftOneImg = pygame.image.load('aircraft (flying) zone trespassers.png')
bulletImg = pygame.image.load('bullet.png')
enemyShipNullImg = pygame.image.load('enemy ship.png')
enemyShipOneImg = pygame.image.load('enemy ship flying.png')

#   DEFINITIONS #

def aircraft(x,y):
    gameDisplay.blit(aircraftNullImg,(x,y))
    gameDisplay.blit(aircraftOneImg,(x,y))
    
def enemy(enemyx,enemyy):
    gameDisplay.blit(enemyShipNullImg,(enemyx,enemyy))
    gameDisplay.blit(enemyShipOneImg,(enemyx,enemyy))
    
def bullet(bullet1x,bullet1y):
    gameDisplay.blit(bulletImg,(bullet1x,bullet1y))
    
def bullet2(bullet2x,bullet2y):
    gameDisplay.blit(bulletImg,(bullet2x,bullet2y))

def text_objects(text,font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()  
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',70)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()

def dead():
    message_display('YOU DIED')
##    message_display('YOU DEAD BISH')

#   GAME LOOP   #
def game_loop():

#   STATICS  #
    x = (display_width * 0.35540)
    y = (display_height * 0.85)
    bullet1x = (x * 1.329)
    bullet1y = (y * 1.09)
    bullet2x = (bullet1x * 1.09)
    bullet2y = (bullet1y)
    enemy_startx = random.randrange(0, display_width)
    enemy_starty = - 200
    enemy_speed = 10


#   CHANGES #    
    x_change = 0    
    bullet1x_change = 0
    bullet1y_change = 0
    bullet2x_change = 0
    bullet2y_change = 0

    
    gameExit = False
#   WHILE GAME HASN'T BEEN EXITED, START WHILE LOOP  #
    while not gameExit:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                   x_change = 8
                   bullet1x_change = 0
                   gameDisplay.blit(aircraftOneImg,(x,y))
                elif event.key == pygame.K_LEFT:
                    x_change = -8
                    bullet1x_change = 0
                    bullet2x_change = 0
                    gameDisplay.blit(aircraftOneImg,(x,y))                    
                elif event.key == pygame.K_SPACE:
                    bullet1x_change = 0
                    bullet1y_change = -5
                    bullet2x_change = 0
                    bullet2y_change = -5
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    bullet1x_change = 0
                    bullet2x_change = 0
                    gameDisplay.blit(aircraftNullImg,(x,y))
                elif event.key == pygame.K_SPACE:
                    bullet1x_change = 0
                    bullet1y_change = -5
                    bullet2x_change = 0
                    bullet2y_change = -5
        
 #  DRAWS #
        gameDisplay.fill(pink)
        x += x_change
        bullet1x += bullet1x_change
        bullet1y += bullet1y_change
        bullet2x += bullet2x_change
        bullet2y += bullet2y_change
        enemy_starty += enemy_speed
        enemy_startx == enemy_startx
        bullet(bullet1x,bullet1y)
        bullet2(bullet2x,bullet2y)
        aircraft(x,y)
        enemy(enemy_startx,enemy_starty)
#   logic  #
        if x > display_width - aircraft_width:
            x = display_width - aircraft_width
        if x < 1:
            x = 1
        if bullet1y > display_height - bullet_height:
            bullet1y = y
        if enemy_starty > display_height:
            enemy_starty = 0 - enemy_height + 20
            enemy_startx = random.randrange(0,(display_width - enemy_width + 20))
        if enemy_starty + enemy_height > display_height:
            dead()
        if y < enemy_starty + enemy_height:
            if x > enemy_startx and x < enemy_startx + enemy_width or x + aircraft_width > enemy_startx and x + aircraft_width < enemy_startx + enemy_width:
                print('xcrossover')
                dead()
        pygame.display.update()
        clock.tick(30)
#   END  WHILE LOOP #


game_loop()
pygame.quit()
quit()
