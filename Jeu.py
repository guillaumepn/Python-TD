import pygame
import sys
import time
from pygame.locals import *
from Monster import *
from Tower import *
from Player import *
from random import *

print(sys.version)

pygame.init()

SCR_WIDTH = 960
SCR_HEIGHT = 640

# Creation of the window
surface = pygame.display.set_mode(
    (SCR_WIDTH, SCR_HEIGHT),
    DOUBLEBUF |
    SRCALPHA
)

surface.fill((255, 255, 255))
pygame.display.set_caption("Python TD")
clock = pygame.time.Clock()

# img_wall = pygame.image.load('wall.png').convert()
# img_grass = pygame.image.load('grass.png').convert()
# img_path = pygame.image.load('path.png').convert()

# Read through map.txt file to draw the map
with open('assets/map01.txt') as file:
    lines = file.readlines()

lines = [x.strip() for x in lines]

# def score(compte):
#     font = pygame.font.Font('BradBunR.ttf', 16)
#     text = font.render("score : " + str(compte), True, white)
#     surface.blit(text, (10, 10))

def drawText(text, posX, posY, color=(255, 255, 255)):
    font = pygame.font.Font('assets/fonts/ShareTech.ttf', 16)
    text = font.render(str(text), True, color)
    surface.blit(text, (posX, posY))

def replayOrQuit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYUP:
            continue
        return event.key
    return None

# def creaText(msg, font):
    # textSurface = font.render(msg, True, white)
    # return textSurface, textSurface.get_rect()

# def message(msg):
#     GOText = pygame.font.Font('BradBunR.ttf', 150)
#     smallText = pygame.font.Font('BradBunR.ttf', 20)
#
#     GOTextSurface, GOTextRect = creaText(msg, GOText)
#     GOTextRect.center = SCR_WIDTH/2, ((SCR_HEIGHT/2)-50)
#     surface.blit(GOTextSurface, GOTextRect)
#
#     smallTextSurface, smallTextRect = creaText("Appuyez sur une touche pour continuer", smallText)
#     smallTextRect.center = SCR_WIDTH / 2, ((SCR_HEIGHT / 2) + 50)
#     surface.blit(smallTextSurface, smallTextRect)
#
#     pygame.display.update()
#     time.sleep(2)
#
#     while replayOrQuit() == None:
#         clock.tick()
#
#     main()

# def gameOver():
#     message("Boom!")
#
# def ballon(x, y, img):
#     surface.blit(img, (x, y))

def isOn(mouse_pos):
    i = 0
    j = 0
    type = 0
    if mouse_pos[0] >= 0 and mouse_pos[0] < 800 and mouse_pos[1] >= 0 and mouse_pos[1] < 640:
        i = int((mouse_pos[0]) / 32)
        j = int((mouse_pos[1]) / 32)
        type = int(lines[j][i])
        # print("Cursor", i, j)
    for tower in Tower.tower_list:
        if int(tower.posX / 32) == i and int(tower.posY / 32) == j:
            type = tower.type
    return (i, j, type)

def main():
    # Background :
    background = pygame.image.load('assets/map01.png').convert()
    # GUI buttons and panel :
    play = pygame.image.load('assets/play.png').convert_alpha()
    pause = pygame.image.load('assets/pause.png').convert_alpha()
    playPause = play
    guipanel = pygame.image.load('assets/gui-panel.png').convert()
    # The player :
    player = Player(20, 100)

    # Towers :
    tower01 = pygame.image.load('assets/tower01.png').convert_alpha()
    tower02 = pygame.image.load('assets/tower02.png').convert_alpha()

    guipanel = pygame.image.load('assets/gui-panel.png').convert()
    # Creation of snakes (appended to Monster.monster_list)
    for i in range(0, 5):
        snake = Monster(surface, 10, (-i * 20), 96, 'snake.png', lines)

    # surface.blit(background, (0, 0))

    imap = 0
    jmap = 0
    mouse_pos = 0
    paused = True
    canBuild = False
    squareX = 0
    squareY = 0
    towerType = 1


    game_over = False
    map_generated = False

    while not game_over:
        surface.blit(background, (0, 0))

        # GUI:
        surface.blit(guipanel, (800, 0))
        btn_playPause = surface.blit(playPause, (832, 32))
        # Gold:
        surface.blit(player.image_gold, (880, 48))
        drawText(player.gold, 880, 24)
        # Health:
        surface.blit(player.image_health, (912, 48))
        drawText(player.health, 916, 24)

        # Towers:
        btn_tower01 = surface.blit(tower01, (832, 96))
        btn_tower02 = surface.blit(tower02, (864, 96))

        # Events and controls :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                # Highlight squares with mouse hover :
                squareX = isOn(mouse_pos)[0]*32
                squareY = isOn(mouse_pos)[1]*32
                if isOn(mouse_pos)[2] == 9: # Can put a tower (cursor on grass tile)
                    pygame.draw.rect(surface, (255, 255, 255), (squareX, squareY, 31, 31), 1)
                    canBuild = True
                elif isOn(mouse_pos)[2] == 1: #Detect type of tower and get range #TODO NOT FINISHED
                    pygame.draw.circle(surface, (255, 255, 255, 0), (squareX, squareY), 20, 20)
                else:
                    pygame.draw.rect(surface, (255, 0, 0), (isOn(mouse_pos)[0]*32, isOn(mouse_pos)[1]*32, 31, 31), 1)
                    canBuild = False


            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if canBuild and player.gold >= 20:
                    player.gold -= 20
                    tower = Tower(squareX, squareY, towerType)
                    # mouse_pos[2] = towerType
                if btn_playPause.collidepoint(mouse_pos):
                    paused = not paused
                    if paused:
                        playPause = play
                        print("pause!")
                    else:
                        playPause = pause
                        print("play!")

                if btn_tower01.collidepoint(mouse_pos):
                    towerType = 1

                if btn_tower02.collidepoint(mouse_pos):
                    towerType = 2

        # Draw and update monsters :
        for monster in Monster.monster_list:
            if paused == False:
                monster.move()
            if monster.direction == "end":
                player.health -= 1
            surface.blit(monster.image, (monster.posX, monster.posY))

        # Draw towers :
        for tower in Tower.tower_list:
            surface.blit(tower.image, (tower.posX, tower.posY))

        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()
quit()
