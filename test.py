# 1 - Import library
import numpy as np
import pygame
from pygame.locals import *
from math import sqrt

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

# 3 - Load images
player = pygame.image.load("./resources/images/aim.png")
evil = pygame.image.load("./resources/images/evil_dude.png")
good = pygame.image.load("./resources/images/good_dude.png")

good_x = 100
good_y = 200

evil_x = 0
evil_y = 300

evil_v = 3

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    ax, ay = pygame.mouse.get_pos()
    ax -= 150
    ay -= 150
    screen.blit(player, (ax,ay))
    screen.blit(evil, (evil_x, evil_y))
    screen.blit(good, (good_x,good_y))
    good_x += 0.09
    if good_x > 640:
        good_x = 50

    ev_x = (good_x - evil_x)
    ev_y = (good_y - evil_y)
    ev_rho = sqrt(ev_x**2 + ev_y**2)
    evil_x += 0.05*evil_v * ev_x / ev_rho
    evil_y += 0.05*evil_v * ev_y / ev_rho

    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            print("Выстрелил!")
            rect = evil.get_rect()
            rect.left = evil_x
            rect.top = evil_y
            if pygame.Rect.collidepoint(rect, event.pos):
                print("Попал!!!")
                evil_x = 0
                evil_y = np.random.randint(50, 400)
                evil_v = np.random.randint(1, 7)
