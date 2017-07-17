import pygame
from Bullet import *
from Monster import *

class Tower():
    tower_count = 0
    tower_list = []
    def __init__(self, posX, posY, type = 1, range = 50):
        self.posX = posX
        self.posY = posY
        self.type = type
        self.range = range
        self.target = None
        self.bullet_shot = False
        if self.type == 1:
            self.image = pygame.image.load('assets/tower01.png').convert_alpha()
            self.range = 80
            self.damage = 1
            self.bullet_image = pygame.image.load('assets/bullet01.png').convert_alpha()

        if self.type == 2:
            self.image = pygame.image.load('assets/tower02.png').convert_alpha()
            self.range = 100
            self.damage = 3
            self.bullet_image = pygame.image.load('assets/bullet02.png').convert_alpha()

        if self.type == 3:
            self.image = pygame.image.load('assets/tower03.png').convert_alpha()
            self.range = 50
            self.damage = 2
            self.bullet_image = pygame.image.load('assets/bullet03.png').convert_alpha()

        Tower.tower_count += 1
        Tower.tower_list.append(self)

    def shoot(self, destX, destY):
        if not self.bullet_shot:
            print("bullet shot!")
            bullet = Bullet(self.posX, self.posY, destX, destY, self.bullet_image)
            self.bullet_shot = True
            bullet.move()
            print("bullet arrived")
            self.target.health -= self.damage
            self.bullet_shot = False
