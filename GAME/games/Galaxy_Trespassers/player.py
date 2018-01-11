import pygame


# ..................................PLAYER CLASS..................................#


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_default  =  pygame.image.load(os.path.join(game_folder, 'aircraft zone trespassers.png')).convert()
        self.image          = pygame.image.load(os.path.join(game_folder, 'aircraft zone trespassers.png')).convert()
        self.image_2        = pygame.image.load(os.path.join(game_folder, 'aircraft (flying) zone trespassers.png')).convert()
        self.image_default.set_colorkey(BLACK)
        self.image.set_colorkey(BLACK)
        self.image_2.set_colorkey(BLACK)
        self.rect           = self.image.get_rect()
        self.rect.centerx   = gamedisplay.get_width() / 2
        self.rect.bottom    = game_height - 20
        self.radius         = int(self.rect.width / 3)
        self.speedx         = 0
        self.added_speed    = 8.5
        self.shoot_delay    = 360
        self.last_shot      = pygame.time.get_ticks()



    def update(self):
        self.speedx = 0
        self.rect.x += self.speedx
        if self.rect.right > game_width:
            self.rect.right = game_width
        if self.rect.left < 0:
            self.rect.left  = 0

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot  = now
            bullet          = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            random.choice(lazer_sounds).play()