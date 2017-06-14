import pygame
import sys
import time
from Monster import *
from random import *

print(sys.version)

pygame.init()

surfaceW = 320
surfaceH = 160

# Creation of the window
surface = pygame.display.set_mode((surfaceW, surfaceH))
pygame.display.set_caption("Python TD")
clock = pygame.time.Clock()

img_wall = pygame.image.load('wall.png')
img_grass = pygame.image.load('grass.png')
img_path = pygame.image.load('path.png')

# Creation of snakes (appended to Monster.monster_list)
for i in range(0, 5):
    snake = Monster(surface, 10, (-i*20), 80, 'snake.png')

# Read through map.txt file to draw the map
with open('map.txt') as file:
    lines = file.readlines()

lines = [x.strip() for x in lines]

def score(compte):
    font = pygame.font.Font('BradBunR.ttf', 16)
    text = font.render("score : " + str(compte), True, white)
    surface.blit(text, (10, 10))


def replayOrQuit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYUP:
            continue
        return event.key
    return None

def creaText(msg, font):
    textSurface = font.render(msg, True, white)
    return textSurface, textSurface.get_rect()

def message(msg):
    GOText = pygame.font.Font('BradBunR.ttf', 150)
    smallText = pygame.font.Font('BradBunR.ttf', 20)

    GOTextSurface, GOTextRect = creaText(msg, GOText)
    GOTextRect.center = surfaceW/2, ((surfaceH/2)-50)
    surface.blit(GOTextSurface, GOTextRect)

    smallTextSurface, smallTextRect = creaText("Appuyez sur une touche pour continuer", smallText)
    smallTextRect.center = surfaceW / 2, ((surfaceH / 2) + 50)
    surface.blit(smallTextSurface, smallTextRect)

    pygame.display.update()
    time.sleep(2)

    while replayOrQuit() == None:
        clock.tick()

    main()

def gameOver():
    message("Boom!")

def ballon(x, y, img):
    surface.blit(img, (x, y))

def main():
    imap = 0
    jmap = 0
    game_over = False
    map_generated = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        if map_generated == False:
            for line in lines:
                for c in line:
                    if c == '0':
                        surface.blit(img_wall, (32*jmap, 32*imap))
                    if c == '1':
                        surface.blit(img_path, (32*jmap, 32*imap))
                    if c == '2':
                        surface.blit(img_path, (32*jmap, 32*imap))
                    if c == '3':
                        surface.blit(img_path, (32*jmap, 32*imap))
                    if c == '4':
                        surface.blit(img_path, (32*jmap, 32*imap))
                    if c == '9':
                        surface.blit(img_grass, (32*jmap, 32*imap))
                    print(str(jmap) + " " + str(imap))
                    jmap += 1
                jmap = 0
                imap += 1
            map_generated = True
        for monster in Monster.monster_list:
            monster.paint()
        pygame.display.update()
        clock.tick(30)

main()
pygame.quit()
quit()