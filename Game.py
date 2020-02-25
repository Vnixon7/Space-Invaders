import pygame, random, time

pygame.init ()
pygame.font.init ()

clock = pygame.time.Clock ()
win_h = 500
win_w = 500
win = pygame.display.set_mode ((win_w, win_h))
font = pygame.font.SysFont ('comicansms', 30)
barrier_img = pygame.image.load ('barrier_SI.png')
enemy_img = pygame.image.load ('Enemy_1.jpeg')
enemy_projectile_img = pygame.image.load ('impact.png')
highScore = 0
lives = 3
score = 0


class Player (object):
    def __init__(self):
        self.x = 215
        self.y = 460
        self.height = 35
        self.width = 35
        self.vel = 10
        self.score = 0
        self.lives = 3

    def draw(self):
        char_img = pygame.image.load ('Main_SpaceIn.png')
        char_img = pygame.transform.scale (char_img, (self.width, self.height))
        win.blit (char_img, (self.x, self.y))

    def getRect(self):
        return pygame.Rect (self.x, self.y, self.width, self.height)

    def scoring(self, a, e):
        if a.getRect ().colliderect (e.getRect ()):
            self.score += 10

    def enemyCollide(self, a, b, c):
        if self.getRect ().colliderect (a.getRect ()):
            self.lives -= 1
            Enemyammo1.pop (Enemyammo1.index (a))
        if self.getRect ().colliderect (b.getRect ()):
            self.lives -= 1
            Enemyammo3.pop (Enemyammo3.index (b))
        if self.getRect ().colliderect (c.getRect ()):
            self.lives -= 1
            Enemyammo5.pop (Enemyammo5.index (c))


class Projectile (object):
    def __init__(self):
        self.vel = 10
        self.x = round (char.x + char.width // 2)
        self.y = round (char.y + char.height // 2) - 20
        self.width = 1
        self.height = 10

    def draw(self):
        pygame.draw.rect (win, (225, 225, 225), (self.x, self.y, self.width, self.height))

    def getRect(self):
        return pygame.Rect (self.x, self.y, self.width, self.height)


class EnemyProjectile (object):
    def __init__(self, x, y):
        self.vel = 10
        self.width = 1
        self.height = 10
        self.timer = 0
        self.x = x
        self.y = y
        self.impact = pygame.transform.scale (enemy_projectile_img, (25, 25))

    def draw(self):
        if self.getRect ().colliderect (char.getRect ()):
            win.blit (self.impact, (self.x, self.y))
        else:
            pygame.draw.rect (win, (225, 225, 225), (self.x, self.y, self.width, self.height))

    def getRect(self):
        return pygame.Rect (self.x, self.y, self.width, self.height)


class Barrier (object):

    def __init__(self, x):
        self.x = x
        self.y = 300
        self.height = 50
        self.width = 50
        self.img = pygame.transform.scale (barrier_img, (self.width, self.height))
        self.hitCount = 0

    def draw(self):
        win.blit (self.img, (self.x, self.y))

    def getRect(self):
        return pygame.Rect (self.x, self.y, self.width, self.height)

    def bulletCollide(self, a):

        if self.getRect ().colliderect (a.getRect ()) and self.hitCount == 0:
            barrier_img = pygame.image.load ('player_shot1.png')
            self.img = pygame.transform.scale (barrier_img, (self.width, self.height))
            self.hitCount = 1
            ammo.pop (ammo.index (a))

        elif self.getRect ().colliderect (a.getRect ()) and self.hitCount == 1:
            barrier_img = pygame.image.load ('player_shot2.png')
            self.img = pygame.transform.scale (barrier_img, (self.width, self.height))
            self.hitCount = 2
            ammo.pop (ammo.index (a))

        elif self.getRect ().colliderect (a.getRect ()) and self.hitCount == 2:
            barrier_img = pygame.image.load ('player_shot3.png')
            self.img = pygame.transform.scale (barrier_img, (self.width, self.height))
            self.hitCount = 3
            ammo.pop (ammo.index (a))

        elif self.getRect ().colliderect (a.getRect ()) and self.hitCount == 3:
            barrier_img = pygame.image.load ('player_shot4.png')
            self.img = pygame.transform.scale (barrier_img, (self.width, self.height))
            self.hitCount = 4
            ammo.pop (ammo.index (a))

        elif self.getRect ().colliderect (a.getRect ()) and self.hitCount == 4:
            barrier_img = pygame.image.load ('player_shot5.png')
            self.img = pygame.transform.scale (barrier_img, (self.width, self.height))
            self.hitCount = 5
            ammo.pop (ammo.index (a))

        elif self.getRect ().colliderect (a.getRect ()) and self.hitCount == 5:
            barrier_img = pygame.image.load ('player_shot6.png')
            self.img = pygame.transform.scale (barrier_img, (self.width, self.height))
            self.hitCount = 6
            ammo.pop (ammo.index (a))

        elif self.getRect ().colliderect (a.getRect ()) and self.hitCount == 6:
            barrier_img = pygame.image.load ('player_shot7.png')
            self.img = pygame.transform.scale (barrier_img, (self.width, self.height))
            self.hitCount = 7
            ammo.pop (ammo.index (a))

        elif self.getRect ().colliderect (a.getRect ()) and self.hitCount == 7:
            barrier_img = pygame.image.load ('player_shot8.png')
            self.img = pygame.transform.scale (barrier_img, (self.width, self.height))
            self.hitCount = 8
            ammo.pop (ammo.index (a))

    def enemyBulletCollide(self, a, b, c):
        if self.getRect ().colliderect (a.getRect ()):
            Enemyammo1.pop (Enemyammo1.index (a))
        if self.getRect ().colliderect (b.getRect ()):
            Enemyammo3.pop (Enemyammo3.index (b))
        if self.getRect ().colliderect (c.getRect ()):
            Enemyammo5.pop (Enemyammo5.index (c))


class Enemy (object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.vel = 10
        self.img = pygame.transform.scale (enemy_img, (self.width, self.height))
        self.hitCount = 0
        self.moveCount = 0
        self.EnemyAmmo = []

    def draw(self):
        win.blit (self.img, (self.x, self.y))

    def getRect(self):
        return pygame.Rect (self.x, self.y, self.width, self.height)

    def move(self):

        pass

    def bulletCollide(self, a, e, score):
        if self.getRect ().colliderect (a.getRect ()):
            self.hitCount += 1
            score += 1
            ammo.pop (ammo.index (a))
        if self.hitCount == 3:
            enemies.pop (enemies.index (e))


def draw_window(score):
    win.fill ((0, 0, 0))
    score_num = font.render ((str (char.score)), 1, (255, 255, 255))
    score_font = font.render ("SCORE", 1, (225, 225, 225))
    # high_score = font.render ('HIGH-SCORE', 1, (255, 255, 255))
    # high_score_num = font.render ((str (highScore)), 1, (255, 255, 255))
    lives_font = font.render ("LIVES", 1, (225, 225, 225))
    lives_num = font.render (str (char.lives), 1, (255, 255, 255))
    win.blit (lives_num, (435, 17))
    win.blit (lives_font, (420, 0))
    # win.blit (high_score_num, (225, 17))
    # win.blit (high_score, (180, 0))
    win.blit (score_font, (0, 0))
    win.blit (score_num, (15, 17))

    # Scoring
    for a in ammo:
        for e in enemies:
            char.scoring (a, e)
    # enemy shooting
    for a in Enemyammo1:
        a.draw ()

    for a in Enemyammo3:
        a.draw ()

    for a in Enemyammo5:
        a.draw ()

    # main character
    char.draw ()

    # Barriers
    for b in barriers:
        b.draw ()

    # enemies
    for e in enemies:
        e.draw ()
        # e.move ()

    # main character shooting
    for a in ammo:
        a.draw ()
    # collision main character ammo and barriers
    for b in barriers:
        for a in ammo:
            b.bulletCollide (a)
    # collision main character ammo and enemies
    for e in enemies:
        for a in ammo:
            e.bulletCollide (a, e, score)

    # collision main character shot by enemy
    for a in Enemyammo1:
        for b in Enemyammo3:
            for c in Enemyammo5:
                char.enemyCollide (a, b, c)
    for d in barriers:
        for a in Enemyammo1:
            for b in Enemyammo3:
                for c in Enemyammo5:
                    d.enemyBulletCollide (a, b, c)

    pygame.display.update ()


char = Player ()
E1 = Enemy (25, 150)
E2 = Enemy (100, 150)
E3 = Enemy (180, 150)
E4 = Enemy (260, 150)
E5 = Enemy (340, 150)
E6 = Enemy (420, 150)

enemies = [E1, E2, E3, E4, E5, E6]
barrier1 = Barrier (25)
barrier2 = Barrier (150)
barrier3 = Barrier (275)
barrier4 = Barrier (400)
barriers = [barrier1, barrier2, barrier3, barrier4]
ammo = []
Enemyammo1 = []
Enemyammo3 = []
Enemyammo5 = []
timer1 = 0
timer3 = 0
timer5 = 0
run = True
while run:

    # Enemy shoot timer
    timer1 += 1
    timer3 += 1
    timer5 += 1

    clock.tick (36)
    keys = pygame.key.get_pressed ()
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit ()
            quit ()

    # Enemy 1 shooting
    if len (Enemyammo1) < 1 and timer1 > 5 and E1.hitCount != 3:
        x = (E1.x + E1.width // 2)
        y = (E1.y + E1.height // 2) - 20
        Enemyammo1.append (EnemyProjectile (x, y))

    for a in Enemyammo1:

        if 500 > a.y > 0:
            a.y += a.vel

        else:
            Enemyammo1.pop (Enemyammo1.index (a))
            timer1 = 0

    # Enemy 3 shooting
    if len (Enemyammo3) < 1 and timer3 > 8 and E3.hitCount != 3:
        x = (E3.x + E3.width // 2)
        y = (E3.y + E3.height // 2) - 20
        Enemyammo3.append (EnemyProjectile (x, y))

    for a in Enemyammo3:

        if 500 > a.y > 0:
            a.y += a.vel

        else:
            timer3 = 0
            Enemyammo3.pop (Enemyammo3.index (a))

    # Enemy 5 shooting
    if len (Enemyammo5) < 1 and timer5 > 11 and E5.hitCount != 3:
        x = (E5.x + E5.width // 2)
        y = (E5.y + E5.height // 2) - 20
        Enemyammo5.append (EnemyProjectile (x, y))

    for a in Enemyammo5:

        if 500 > a.y > 0:
            a.y += a.vel

        else:
            timer5 = 0
            Enemyammo5.pop (Enemyammo5.index (a))

    # Main character shooting
    for a in ammo:
        if 500 > a.y > 0:
            a.y -= a.vel
        else:
            ammo.pop (ammo.index (a))
    # Enemy movement
    for e in enemies:
        if e.moveCount == 0:
            e.x -= 1
        if e.x == 0 - e.width:
            e.moveCount += 1
        if e.moveCount == 1:
            e.x += 1
        if e.x == 490 + e.width:
            e.moveCount = 0

    if keys[pygame.K_LEFT] and char.x > 0:
        char.x -= char.vel

    if keys[pygame.K_RIGHT] and char.x < win_w - char.width:
        char.x += char.vel

    if keys[pygame.K_SPACE]:
        if len (ammo) < 1:
            ammo.append (Projectile ())

    draw_window (score)
