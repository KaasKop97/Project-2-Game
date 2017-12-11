import  pygame, sys, turtle, math
from Colors import colors
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,770))

pygame.mouse.set_visible(0)

#       PLAYER      #
ship = pygame.image.load('aircraft zone trespassers.png')
ship_top = screen.get_height() - ship.get_height()
ship_mid = screen.get_width()/2 - ship.get_width()/2
screen.blit(ship, (ship_mid,ship_top))
shot = pygame.image.load('bullet.png')

#       ENEMY       #
class Enemy(pygame.sprite.Sprite)

    def __init__(self, row, collumn):
        pygame.sprite.Sprite.__init__(self)
        self.width = enemy.get_width()
        self.height = enemy.get_height()
        self.row
enemy = pygame.image.load('enemy ship.png')
enemy_top = screen.get_height() - enemy.get_height()
enemy_mid = screen.get_width()/2 - enemy.get_width()/2
screen.blit(enemy, (enemy_mid,enemy_top ))
ENEMYGAP = 20
ARRAYWIDTH = 10
ARRAYHEIGHT = 4
MOVETIME = 1000
MOVEX = 10
MOVEY = enemy.get_height
TIMEOFFSET = 300




shoot_y = 0
x_change = 0






while True:
    clock.tick(60)
    screen.fill((255,102,102))
    screen.blit(enemy, (enemy_mid, enemy_top))
    screen.blit(ship, (ship_mid, ship_top))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT):
                ship = pygame.image.load('aircraft (flying) zone trespassers.png')
                x_change = - 1
            elif (event.key == pygame.K_RIGHT):
                ship = pygame.image.load('aircraft (flying) zone trespassers.png')
                x_change = + 1
            elif (event.key == pygame.K_SPACE):
                shoot_y = (screen.get_height() - (ship.get_height()/0.99))
                shoot_x = ship_mid + ship.get_width()/2
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
                ship = pygame.image.load('aircraft zone trespassers.png')



    if shoot_y > 0:
        screen.blit(shot, (shoot_x, shoot_y))
        shoot_y -= 10
    pygame.display.update()
    ship_mid = ship_mid + x_change