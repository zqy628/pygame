#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
class Plane(object):
    def __init__(self):
        self.image = pygame.image.load('plane.png').convert_alpha()
        self.restart()

    def move(self):
        x, y = pygame.mouse.get_pos()
        self.x1 = x - self.image.get_width() / 2
        self.y1 = y - self.image.get_height() / 2

    def restart(self):
        self.x1 = 200
        self.y1 = 600