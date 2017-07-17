import pygame
from Player import *

class Bullet():
    bullet_count = 0
    bullet_list = []

    def __init__(self, surface, posX, posY, destX, destY, image):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.destX = destX
        self.destY = destY
        self.image = pygame.image.load(image).convert_alpha()
        Bullet.bullet_count += 1
        Bullet.bullet_list.append(self)

    def move(self):
        diffX = (self.destX - self.posX)
        diffY = (self.destY - self.posY)
        stepX = diffX / 60
        stepY = diffY / 60
        self.posX += stepX
        self.posY += stepY