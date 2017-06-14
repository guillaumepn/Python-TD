import pygame
import time

class Monster():
    monster_count = 0
    monster_list = []

    def __init__(self, surface, hp, posX, posY, image):
        self.surface = surface
        self.hp = hp
        self.posX = posX
        self.posY = posY
        self.image = pygame.image.load(image)
        Monster.monster_count += 1
        Monster.monster_list.append(self)

    def paint(self):
        self.move()
        self.surface.blit(self.image, (self.posX, self.posY))

    def move(self):
        self.posX += 1
