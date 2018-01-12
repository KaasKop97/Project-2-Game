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
        self.rect.centerx   = WINDOW.get_width() / 2
        self.rect.bottom    = HEIGHT - 20
        self.radius         = int(self.rect.width / 3)
        self.speedx         = 0
        self.added_speed    = 8.5
        self.shoot_delay    = 360
        self.last_shot      = pygame.time.get_ticks()



    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.image  = player.image_2
            self.speedx =- self.added_speed
        if keystate[pygame.K_RIGHT]:
            self.image  = player.image_2
            self.speedx =+ self.added_speed
            if keystate[pygame.K_a]:
                self.image = player.image_2
                self.speedx =- self.added_speed
            if keystate[pygame.K_d]:
                self.image = player.image_2
                self.speedx =+ self.added_speed
        if keystate[pygame.K_SPACE]:
            self.shoot()
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
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