import pygame
from Player import *

class Monster():
    monster_count = 0
    monster_list = []

    def __init__(self, surface, health, posX, posY, image, grid):
        self.surface = surface
        self.health = health
        self.posX = posX
        self.posY = posY
        self.direction = "right"
        self.image = pygame.image.load(image).convert_alpha()
        self.grid = grid
        Monster.monster_count += 1
        Monster.monster_list.append(self)

    def move(self):
        self.getDirection()
        if self.direction == "right":
            self.posX += 1

        elif self.direction == "left":
            self.posX -= 1

        elif self.direction == "down":
            self.posY += 1

        elif self.direction == "up":
            self.posY -= 1

    def getDirection(self):
        if self.isOn() == 3:
            self.direction = "up"
        elif self.isOn() == 4:
            self.direction = "right"
        elif self.isOn() == 5:
            self.direction = "down"
        elif self.isOn() == 6:
            self.direction = "left"
        elif self.isOn() == 7: # End of path
            self.direction = "end"
            Monster.monster_list.remove(self)

    def isOn(self):
        diffX = 0
        diffY = 0
        if self.posX < 0:
            x = 0
        else:
            x = self.posX
        if self.posY < 0:
            y = 0
        elif self.posY > 640:
            y = 600
        else:
            y = self.posY

        if self.direction == "left": diffX = 31
        if self.direction == "up": diffY = 31
        i = int((y + diffY) / 32)
        j = int((x + diffX) / 32)
        return int(self.grid[i][j])
