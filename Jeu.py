import pygame
import sys
import time
from pygame.locals import *
from Monster import *
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

background = pygame.image.load('assets/map01.png').convert()
play = pygame.image.load('assets/play.png').convert_alpha()
pause = pygame.image.load('assets/pause.png').convert_alpha()
playPause = play
guipanel = pygame.image.load('assets/gui-panel.png').convert()

surface.blit(background, (0,0))

# Read through map.txt file to draw the map
with open('assets/map01.txt') as file:
    lines = file.readlines()

lines = [x.strip() for x in lines]

# Creation of snakes (appended to Monster.monster_list)
for i in range(0, 5):
    snake = Monster(surface, 10, (-i*20), 96, 'snake.png', lines)


# def score(compte):
#     font = pygame.font.Font('BradBunR.ttf', 16)
#     text = font.render("score : " + str(compte), True, white)
#     surface.blit(text, (10, 10))


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
    return (i, j, type)

def main():
    imap = 0
    jmap = 0

    game_over = False
    map_generated = False

    while not game_over:
        surface.blit(background, (0, 0))

        # GUI:
        surface.blit(guipanel, (800, 0))
        surface.blit(playPause, (832, 32))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                if isOn(mouse_pos)[2] == 9: # Can put a tower (cursor on grass tile)
                    pygame.draw.rect(surface, (255, 255, 255), (isOn(mouse_pos)[0]*32, isOn(mouse_pos)[1]*32, 31, 31), 1)
                else:
                    pygame.draw.rect(surface, (255, 0, 0), (isOn(mouse_pos)[0]*32, isOn(mouse_pos)[1]*32, 31, 31), 1)


        # if map_generated == False:
        #     for line in lines:
        #         for c in line:
        #             if c == '0': # wall (no tower allowed)
        #                 surface.blit(img_wall, (32*jmap, 32*imap))
        #             if c == '1': # START (path: no tower allowed)
        #                 surface.blit(img_path, (32*jmap, 32*imap))
        #             if c == '2': # move (path: no tower allowed)
        #                 surface.blit(img_path, (32*jmap, 32*imap))
        #             if c == '3': # turn up (path: no tower allowed)
        #                 surface.blit(img_path, (32*jmap, 32*imap))
        #             if c == '4': # turn right (path: no tower allowed)
        #                 surface.blit(img_path, (32*jmap, 32*imap))
        #             if c == '5': # turn down (path: no tower allowed)
        #                 surface.blit(img_path, (32*jmap, 32*imap))
        #             if c == '6': # turn left (path: no tower allowed)
        #                 surface.blit(img_path, (32*jmap, 32*imap))
        #             if c == '7': # END (path: no tower allowed)
        #                 surface.blit(img_path, (32*jmap, 32*imap))
        #             if c == '9': # grass (can put towers on it)
        #                 surface.blit(img_grass, (32*jmap, 32*imap))
        #             print(str(jmap) + " " + str(imap))
        #             jmap += 1
        #         jmap = 0
        #         imap += 1
        #     map_generated = True
        # for monster in Monster.monster_list:

        for monster in Monster.monster_list:
            monster.move()
            surface.blit(monster.image, (monster.posX, monster.posY))

        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()
quit()
