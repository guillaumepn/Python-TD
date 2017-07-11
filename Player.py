import pygame

class Player():

    def __init__(self, health, gold):
        self.health = health
        self.gold = gold
        self.image_gold = pygame.image.load('assets/gold.png').convert_alpha()
        self.image_health = pygame.image.load('assets/health.png').convert_alpha()