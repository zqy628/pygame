#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, pygame
pygame.init()

screen = pygame.display.set_mode((1440,960))
player = pygame.image.load("intro_ball.gif")
background = pygame.image.load('1.jpg').convert()
screen.blit(background, (0, 0))        #draw the background
position = player.get_rect()
screen.blit(player, position)          #draw the player
pygame.display.update()                #and show it all
for x in range(500):                   #animate 100 frames
    screen.blit(background, position, position) #erase
    position = position.move(2, 0)     #move player
    screen.blit(player, position)      #draw new player
    pygame.display.update()            #and show it all
    pygame.time.delay(40)             #stop the program for 1/10 secon