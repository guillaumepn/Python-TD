import pygame, sys, random, time

check_errors = pygame.init()

if check_errors[1] > 0:
    print("(!) Had {0} initializing errors".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized")

#Play surface
playSurface = pygame.display.set_mode((720, 460))
pigame.display.set_caption('Tower Defense')

#Colors
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(165, 42, 42)

#FPS controller
fpsController = pygame.time.Clock()

#TO DELET
snakePos = [100, 50]
# snakeBody = [[100,50][90,50][80,5koreus0]]

time.sleep(5)
