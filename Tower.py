import pygame

class Tower():
    tower_count = 0
    tower_list = []
    def __init__(self, posX, posY, type = 1):
        self.posX = posX
        self.posY = posY
        self.type = type
        if self.type == 1:
            self.image = pygame.image.load('assets/tower01.png').convert_alpha()
            self.cost = 20
        Tower.tower_count += 1
        Tower.tower_list.append(self)