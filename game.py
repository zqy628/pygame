#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from sys import exit
import random
pygame.init() #初始化
screen = pygame.display.set_mode((600,300),pygame.RESIZABLE,0)  #分辨率参数是一对表示宽度和高度的数字。flags参数是其他选项的集合。深度参数表示用于颜色的位数。
pygame.display.set_caption('Hello,world!')  #设置窗口标题
backgroud1 = pygame.image.load('0.jpg').convert()  #加载并转换图像
backgroud2 = pygame.image.load('1.jpg').convert()  # 加载并转换图像

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.blit(random.choice([backgroud1,backgroud2]),(0,0))  #将背景图画上去
        pygame.display.update()   #刷新一下画面