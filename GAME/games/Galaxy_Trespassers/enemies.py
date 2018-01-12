import pygame


#..................................ENEMY CLASSES..................................#


class Enemy00(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image  = os.path.join("games", "Galaxy_Trespassers", "data", "enemy ship flying.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect   = self.image.get_rect()
        self.radius = int(self.rect.width / 3)
        self.rect.x = random.randrange(0, game_width - self.rect.width)
        self.rect.y = random.randrange(-600, -100)
        self.speedy = 1
        Enemy.score = 50

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > game_height + 10:
            self.rect.x = random.randrange(0, game_width - self.rect.width)
            self.rect.y = random.randrange(-600, -100)
            self.speedy = 1


    #   class enemy1
class Enemy01(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image  = os.path.join("games", "Galaxy_Trespassers", "data", "enemy ship flying 2.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect   = self.image.get_rect()
        self.radius = int(self.rect.width / 3)
        self.rect.x = random.randrange(0, game_width - self.rect.width)
        self.rect.y = random.randrange(-800, -150)
        self.speedy = 2
        Enemy1.value  = 100

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > game_height + 10:
            self.rect.x = random.randrange(0, game_width - self.rect.width)
            self.rect.y = random.randrange(-800, -150)
            self.speedy = 2

    #   class enemy2
class Enemy02(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image      = os.path.join("games", "Galaxy_Trespassers", "data", "enemy ship flying 3.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect       = self.image.get_rect()
        self.radius = int(self.rect.width / 3)
        self.rect.x = random.randrange(0, game_width - self.rect.width)
        self.rect.y = random.randrange(-900, -300)
        self.speedy = 3
        Enemy2.value = 150

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > game_height + 10:
            self.rect.x = random.randrange(0, game_width - self.rect.width)
            self.rect.y = random.randrange(-900, -300)
            self.speedy = 3


    #   class enemy 3
class Enemy03(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = os.path.join("games", "Galaxy_Trespassers", "data", "enemy ship flying 4.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width / 3)
        self.rect.x = random.randrange(0, game_width - self.rect.width)
        self.rect.y = random.randrange(-2000, -800)
        self.speedy = 4
        Enemy3.value = 500

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > game_height + 10:
            self.rect.x = random.randrange(0, game_width - self.rect.width)
            self.rect.y = random.randrange(-2000, -800)
            self.speedy = 4