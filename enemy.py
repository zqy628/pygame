#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import random
class Enemy(object):
    def __init__(self):
        self.restart()
        self.image = pygame.image.load('enemy.png')

    def move(self):
        if self.y > 900:
            self.restart()
        else:
            self.y += self.speed

    def restart(self):
        self.x = random.randrange(0,400)
        self.y = random.randrange(-200,-50)
        self.speed = random.random() + 0.4