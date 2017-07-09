#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from sys import exit
import random
pygame.init() #初始化
screen = pygame.display.set_mode((540,960))  #分辨率参数是一对表示宽度和高度的数字。flags参数是其他选项的集合。深度参数表示用于颜色的位数。
pygame.display.set_caption('Thunder!')  #设置窗口标题
backgroud = pygame.image.load('backgroud.png').convert()  #加载并转换图像
plane = pygame.image.load('plane.png').convert_alpha()  # 加载并转换图像
bullet = pygame.image.load('bullet.png').convert_alpha()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(backgroud,(0,0))
    x,y = pygame.mouse.get_pos()
    x -= plane.get_width()/2
    y -= plane.get_height()/2
    screen.blit(plane,(x,y))
    # screen.blit(backgroud, (0, 0))
    pygame.display.flip()   #刷新一下画面