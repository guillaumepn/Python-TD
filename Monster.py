import pygame
import Player

class Monster():
    monster_count = 0
    monster_list = []

    def __init__(self, surface, hp, posX, posY, image, grid):
        self.surface = surface
        self.hp = hp
        self.posX = posX
        self.posY = posY
        self.direction = "right"
        self.image = pygame.image.load(image).convert_alpha()
        self.grid = grid
        Monster.monster_count += 1
        Monster.monster_list.append(self)

    # def draw(self, surface):
    #     surface.blit(self.image, (self.posX, self.posY))

    def move(self):
        self.getDirection()
        # print(str(self.posY) + " " + self.direction)
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
        # if self.isOn() == 7: # End of path
            # Player.hp -= 1
            # Monster.monster_list.remove(self)

    def isOn(self):
        diffX = 0
        diffY = 0
        if self.direction == "left": diffX = 31
        if self.direction == "up": diffY = 31
        i = int((self.posY + diffY) / 32)
        j = int((self.posX + diffX) / 32)
        # print(self.grid[i][j])
        return int(self.grid[i][j])