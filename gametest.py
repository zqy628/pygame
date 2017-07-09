#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, pygame
pygame.init()
from random import randint

size = width, height = 1440, 996
speed = [1, 1]
black = 240,248,255
print type(black)

screen = pygame.display.set_mode(size)

# ball = pygame.image.load("intro_ball.gif").convert()
screen.fill(black)
ball = pygame.draw.rect(screen,(0,0,0),(0,0,1,1),0)
# ballrect = ball.get_rect()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ball = ball.move(speed)
    if ball.left < 0 or ball.right > width:
        speed[0] = -speed[0]
        # ballrect.right = 0
    if ball.top < 0 or ball.bottom > height:
        speed[1] = -speed[1]
        # ballrect.bottom = 0
    # black = (randint(0,10),randint(0,10),randint(0,10))
    pygame.draw.rect(screen, (0, 0, 0), (ball.left, ball.top, 1, 1), 0)
    # screen.blit(ball, ball)
    pygame.display.flip()