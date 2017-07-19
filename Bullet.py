import pygame
from Player import *
from threading import Timer

class Bullet():
    bullet_count = 0
    bullet_list = []

    def __init__(self, tower, target, image):
        self.tower = tower
        self.posX = tower.posX
        self.posY = tower.posY
        self.destX = target.posX
        self.destY = target.posY
        self.diffX = (self.destX - self.posX)
        self.diffY = (self.destY - self.posY)
        self.image = image
        Bullet.bullet_count += 1
        Bullet.bullet_list.append(self)

    def move(self):
        self.posX += self.diffX / 3
        self.posY += self.diffY / 3
        print("posx: " + str(self.posX ) + " , posy: " + str(self.posY ) + " , destx: " + str(self.destX ) + " , desty: " + str(self.destY) )

        t = Timer(1/30, self.move)

        # If bullet gets beyond map's borders :
        if self.posX < 0 or self.posY < 0 or self.posX > 800 or self.posY > 640:
            self.tower.bullet_shot = False
            Bullet.bullet_list.remove(self)
        # Else, if bullet has not reached target :
        elif int(self.posX) != int(self.destX) and int(self.posY) != int(self.destY):
            t.start()
        # Else, it reached target !
        else:
            self.tower.target.health -= self.tower.damage
            self.tower.bullet_shot = False
            print("bullet arrived")
            Bullet.bullet_list.remove(self)
