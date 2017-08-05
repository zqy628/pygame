#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

class Bullet(object):
    def __init__(self):
        self.a = 0
        self.b = -1
        self.image = pygame.image.load('bullet.png').convert_alpha()
        self.active = False

    def move(self):
        if self.b < 0:
            self.active = False
        if self.active:
            self.b -= 5

    def restart(self):
        x, y = pygame.mouse.get_pos()
        self.a = x - self.image.get_width()/2
        self.b = y - self.image.get_height()/2
        self.active = True