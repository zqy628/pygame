#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from sys import exit
# from bullet import Bullet
# from enemy import Enemy
# from plane import Plane
import random
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

pygame.init() #初始化
screen = pygame.display.set_mode((540,960))  #分辨率参数是一对表示宽度和高度的数字。flags参数是其他选项的集合。深度参数表示用于颜色的位数。
pygame.display.set_caption('Thunder!')  #设置窗口标题
backgroud = pygame.image.load('backgroud.png').convert()  #加载并转换图像
# plane = pygame.image.load('plane.png').convert_alpha()  # 加载并转换图像
# bullet = pygame.image.load('bullet.png').convert_alpha()
# a = 0;b = -1
enemy = Enemy()
bullets = []
enemys = []
for i in range(5):
    bullets.append(Bullet())
    enemys.append(Enemy())
shotBullet = 0 #激活的子弹编号
interval = 0 #发射时间间隔
plane = Plane()
gameover = False
score = 0 #显示分数
font = pygame.font.Font(None,32)

def checkHit(enemy,bullet):
    if ((enemy.x < bullet.a < enemy.x+enemy.image.get_width()) and (enemy.y < bullet.b < enemy.y+enemy.image.get_height())):
        enemy.restart()
        bullet.active = False
        return True
    else:
        return False

def checkCrash(enemy,plane):
    if (plane.x1 + 0.7 * plane.image.get_width() > enemy.x) and (
            plane.x1 + 0.3 * plane.image.get_width() < enemy.x + enemy.image.get_width()) and (
            plane.y1 + 0.7 * plane.image.get_height() > enemy.y) and (
            plane.y1 + 0.3 * plane.image.get_height() < enemy.y + enemy.image.get_height()):
        return True
    else:
        return False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if not gameover:
        screen.blit(backgroud,(0,0))
        interval -= 1
        if interval < 0:
            bullets[shotBullet].restart()
            interval = 80
            shotBullet = (shotBullet+1) % 5
        for enemy in enemys:
            enemy.move()
            screen.blit(enemy.image,(enemy.x,enemy.y))
            if checkCrash(enemy,plane):
                 gameover = True
            for bullet in bullets:
                if bullet.active:
                    if checkHit(enemy,bullet):
                        score += 100
                    bullet.move()
                    screen.blit(bullet.image,(bullet.a,bullet.b))
        plane.move()
        screen.blit(plane.image,(plane.x1,plane.y1))
        text = font.render("Score:%d"%score,1,(0,0,0))
        screen.blit(text,(0,0))
        # screen.blit(backgroud, (0, 0))
        pygame.display.flip()   #刷新一下画面
    elif gameover and event.type == pygame.MOUSEBUTTONUP:
        gameover = False
        plane.restart()
        for enemy in enemys:
            enemy.restart()
        for bullet in bullets:
            bullet.active = False
        score = 0
    else:
        text1 = font.render("GAMEOVER",1,(0,0,0))
        screen.blit(text1,(190,400))
        pygame.display.flip()  # 刷新一下画面

raw_input('press any key to exit...')




