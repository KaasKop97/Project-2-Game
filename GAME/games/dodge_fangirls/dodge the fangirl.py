import pygame
import time
import random
import sys
import os

pygame.init()

# music #
crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("loyal.mp3")

os.environ['SDL_VIDEO_CENTERED'] = '1'

# display #
display_width = 800
display_height = 600
WINDOW = pygame.display.set_mode((display_width, display_height))

background =  pygame.image.load('achtergrondfoto.png')
background_rect = background.get_rect()

black = (0,0,0)
white = (255,255,255)

red = (150,0,0)
bright_red = (255,0,0)

yellow = (220,200,0)

green = (0,150,0)
bright_green = (0,255,0)

blue = (0,0,255)
baby_blue = (0,120,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dodge the Exes')
clock = pygame.time.Clock()

#  images  #
fan4Img = pygame.image.load('OBSTACLE4.png')
fan3Img = pygame.image.load('OBSTACLE3.png')
fan2Img = pygame.image.load('OBSTACLE2.png')
fanriImg = pygame.image.load('rihannaCHARACTER.png')
cbImg = pygame.image.load('cbCHARACTER.png')



# game icon #
pygame.display.set_icon(cbImg)

# pause and Crash #
pause = False

def cb_dodged(count):
    font = pygame.font.SysFont('freesansbold.ttf', 25)
    text = font.render("Dodged: "+str(count), True, white)
    gameDisplay.blit(text,(0,0))



# Objects heights & widths #
# fan4, fan3, fan2, fanri, cb#

fan4_width = 196
fan4_height = 57

fan3_width = 140
fan3_height = 57

fan2_width = 92
fan2_height = 57

fanri_width = 45
fanri_height = 57

cb_width = 43
cb_height = 55

#               functions                 #
def fangirl4(fan4_x,fan4_y,fan4_width,fan4_height):
    gameDisplay.blit(fan4Img,(fan4_x,fan4_y,fan4_width,fan4_height))

def fangirl2(fan2_x,fan2_y,fan2_width,fan2_height):
    gameDisplay.blit(fan2Img,(fan2_x,fan2_y,fan2_width,fan2_height))

def fangirl3(fan3_x,fan3_y,fan3_width,fan3_height):
    gameDisplay.blit(fan3Img,(fan3_x,fan3_y,fan3_width,fan3_height))

def fangirlri(fanri_x,fanri_y,fanri_width,fanri_height):
    gameDisplay.blit(fanriImg,(fanri_x,fanri_y,fanri_width,fanri_height))

def cb(x,y,cb_width,cb_height):
    gameDisplay.blit(cbImg,(x,y,cb_width,cb_height))


# text on screen #
def text_objects(text, font):
    textSurface = font.render(text, True, yellow)
    return textSurface, textSurface.get_rect()

    
# crash text #
def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    
    
    largeText = pygame.font.Font("freesansbold.ttf",50)
    TextSurf, TextRect = text_objects("You bumped into an ex!", largeText)
    TextRect.center = ((display_width/2),(display_height/4))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(black)


        # menu buttons #        
        # green button #
        button("Play Again",150,300,100,50,green,bright_green,game_loop)
        # red button #
        button("Quit",550,300,100,50,red,bright_red,quitgame)
        
        
        pygame.display.update()
        clock.tick(60)

# press button #
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()               
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.Font("freesansbold.ttf",18)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2), y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
def quitgame():
    pygame.quit()
    quit()

# game pause #
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():

    pygame.mixer.music.pause()

    largeText = pygame.font.Font("freesansbold.ttf",70)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/4))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(black)


        # menu buttons #        
        # green button #
        button("Continue",150,300,100,50,green,bright_green,unpause)
        # red button #
        button("Quit",550,300,100,50,red,bright_red,quitgame)
        
        
        pygame.display.update()
        clock.tick(60)
    
    

# game menu #
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(black)
        largeText = pygame.font.Font("freesansbold.ttf",60)
        TextSurf, TextRect = text_objects("Dodge the Exes", largeText)
        TextRect.center = ((display_width/2),(display_height/10))
        gameDisplay.blit(TextSurf, TextRect)

        # menu buttons #        
        # green button #
        button("Go!",150,300,100,50,green,bright_green,game_loop)
        # red button #
        button("Quit",550,300,100,50,red,bright_red,quitgame)
        
        
        pygame.display.update()
        clock.tick(60)
    


# Game Loop #
def game_loop():
    global pause
    pygame.mixer.music.play(-1)


    x = (display_width * 0.45)
    y = (display_height * 0.9)


    x_change = 0
    
# fan start positions and speed #
    fan4_x = random.randrange(0, display_width)
    fan4_y = -500
    fan4_speed = 3

    fan2_x = random.randrange(0,display_width)
    fan2_y = -700
    fan2_speed = 3

    fan3_x = random.randrange(0, display_width)
    fan3_y = -300
    fan3_speed = 3

    fanri_x = random.randrange(0,display_width)
    fanri_y = -100
    fanri_speed = 3
    
    dodged = 0

    # game exit #
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # keybord #
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                   
        x += x_change
        WINDOW.blit(background, background_rect)

        # fangirls x,y,width and height #
        fangirl4(fan4_x, fan4_y,fan4_width,fan4_height)
        fan4_y += fan4_speed

        fangirl2(fan2_x, fan2_y,fan2_width,fan2_height)
        fan2_y += fan2_speed

        fangirl3(fan3_x, fan3_y,fan3_width,fan3_height)
        fan3_y += fan3_speed

        fangirlri(fanri_x, fanri_y,fanri_width,fanri_height)
        fanri_y += fanri_speed

        # cb x,y,width and height and dodged #
        cb(x,y,cb_width,cb_height)
        cb_dodged(dodged)

        # the speed and the dodged points Fan#
        if x > display_width - cb_width or x < 0:
            crash()

        if fan4_y > display_height:
            fan4_y = 0
            fan4_x = random.randrange(0,display_width)
            dodged += 4
            fan4_speed += 0.5

        if fan2_y > display_height:
            fan2_y = 0
            fan2_x = random.randrange(0,display_width)
            dodged += 2
            fan2_speed += 0.5

        if fan3_y > display_height:
            fan3_y = 0
            fan3_x = random.randrange(0,display_width)
            dodged += 3
            fan3_speed += 0.5

        if fanri_y > display_height:
            fanri_y = 0
            fanri_x = random.randrange(0,display_width)
            dodged += 1
            fanri_speed += 0.5

#        crash obstacles       #            
        if y < fan4_y+fan4_height:
            print('y4 crossover')
 
            if x > fan4_x and x < fan4_x + fan4_width or x+cb_width > fan4_x and x + cb_width < fan4_x+fan4_width:
                print('x4 crossover')
                crash()
                
        if y < fan3_y+fan3_height:
            print('y3 crossover')

            if x > fan3_x and x < fan3_x + fan3_width or x+cb_width > fan3_x and x + cb_width < fan3_x+fan3_width:
                print('x3 crossover')
                crash()

        if y < fan2_y+fan2_height:
            print('y2 crossover')

            if x > fan2_x and x < fan2_x + fan2_width or x+cb_width > fan2_x and x + cb_width < fan2_x+fan2_width:
                print('x2 crossover')
                crash()

        if y < fanri_y+fanri_height:
            print('y1 crossover')

            if x > fanri_x and x < fanri_x + fanri_width or x+cb_width > fanri_x and x + cb_width < fanri_x+fanri_width:
                print('x1 crossover')
                crash()
        

        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()
    
