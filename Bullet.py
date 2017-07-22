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
        self.step = 1
        Bullet.bullet_count += 1
        Bullet.bullet_list.append(self)
        # Sounds :
        if self.tower.type == 1:
            self.shoot = pygame.mixer.Sound('assets/sounds/shoot02.wav')
        if self.tower.type == 2:
            self.shoot = pygame.mixer.Sound('assets/sounds/shoot01.wav')
        if self.tower.type == 3:
            self.shoot = pygame.mixer.Sound('assets/sounds/shoot04.wav')

    def move(self):
        self.posX += self.diffX / 3
        self.posY += self.diffY / 3
        if self.step == 1:
            self.shoot.play()
        self.step += 1
        print("posx: " + str(self.posX ) + " , posy: " + str(self.posY ) + " , destx: " + str(self.destX ) + " , desty: " + str(self.destY) )

        t = Timer(1/30, self.move)

        if self.step >= 3:
            self.posX = self.destX
            self.posY = self.destY
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
