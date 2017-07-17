import pygame
from Player import *
from threading import Timer

class Bullet():
    bullet_count = 0
    bullet_list = []

    def __init__(self, posX, posY, destX, destY, image):
        self.posX = posX
        self.posY = posY
        self.destX = destX
        self.destY = destY
        self.image = image
        Bullet.bullet_count += 1
        Bullet.bullet_list.append(self)

    def move(self):
        diffX = (self.destX - self.posX)
        diffY = (self.destY - self.posY)
        stepX = diffX / 3
        stepY = diffY / 3
        self.posX += stepX
        self.posY += stepY
        print("posx: " + str(self.posX ) + " , posy: " + str(self.posY ) + " , destx: " + str(self.destX ) + " , desty: " + str(self.destY) )

        t = Timer(1/30, self.move)
        if int(self.posX) != int(self.destX) and int(self.posY) != int(self.destY):
            t.start()
            # return "continue"
        else:
            # t.cancel()
            Bullet.bullet_list.remove(self)
            return "end"
