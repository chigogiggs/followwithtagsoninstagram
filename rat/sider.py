import pygame,os
import sys, random
from pygame.locals import *
from threading import _start_new_thread
import threading
import math

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'

bg = pygame.image.load('../rat/bg1.jpg')
clock  = pygame.time.Clock()

timer = 0
bomb = pygame.image.load('../rat/bomb.png')
bomb = pygame.transform.scale(bomb, (70,70))
w = 1000
h= 500
screen = pygame.display.set_mode((w,h))

bgposlist = [(0,0),(0,0)]
class Bomb:
    def __init__(self,x,y,width,height):
        self.bgx = 0
        self.rectlist = []
        self.bgy = 0
        self.bgxonoffvar = 0
        self.x = x
        self.y = y
        self.w =width
        self.h = height
        self.list = []
        self.list.append(self.y-200)
        self.force = 5
        self.updowncheck = 0
        self.shakelooptime = 60
        self.maxforce = 20
        self.uo = 3


    def throwbomb(self):
        def initials():

            if self.uo == 0:
                self.y = 429
            if int(self.maxforce) == 0:
                self.uo =0
            if self.y < 430:
                self.y += self.force
                self.x += self.uo
                if self.force < self.maxforce:
                    self.force += 1
            elif self.y > 430 or self.y == 430:
                self.y = 429
                self.force = self.force*-1
                self.maxforce = self.maxforce/2

        initials()


        def lights():
            if self.uo == 0:
                print(self.y)
                if self.y == 429 or self.y == 430:
                    print('got here')
                    for i in range(0,20):
                        self.linevar = random.choice([-20,-40,-60,-80,-100,-120,-140,-160,-180,-200,20,40,60,70,80,90,100,120,140,160,180,200])
                        pygame.draw.line(screen,(255,255,255),(self.x  +self.linevar, self.y - 400),(self.x+25,self.y+35))

                    if self.shakelooptime == 0:
                        bgposlist.append((0,0))
                        bgposlist.append((0,0))
                    if self.shakelooptime > 0:
                        self.shakelooptime -= 1
                        for huh in range(0,25):
                            if self.bgxonoffvar == 0:

                                if self.bgx < 100:
                                    print('true1')
                                    self.bgx += 10
                                    self.bgy -= 5
                                    print('my bgx is',self.bgx)
                                    bgposlist.append((self.bgx,self.bgy))
                                if self.bgx == 100:
                                    self.bgxonoffvar = 1

                            if self.bgxonoffvar == 1:
                                if self.bgx > -100:
                                    self.bgx -= 10
                                    self.bgy += 5
                                    bgposlist.append((self.bgx,self.bgy))
                                if self.bgx == -100:
                                    self.bgxonoffvar = 0

        lights()

        screen.blit(bomb,(self.x,self.y))
    def effectone(self):
        strtX = self.x - 200
        for ix in range(0,100):
            self.rectlist.append(strtX)
            strtX += 40

        for rectx in self.rectlist:
            pygame.draw.rect(screen,(0,0,0),(rectx,self.y,20,100))



    def soldier(self):
        pygame.draw.rect(screen,(255,0,0),(self.x,self.y,self.w,self.h))


x = 100
y = 100
var = 0
vary = 0
bomblist = []
while True:

    screen.fill((0,0,0))
    screen.blit(bg,bgposlist[-2])
    clock.tick(60)
    warrior = Bomb(x,y,40,40)
    warrior.soldier()
    mousepos= pygame.mouse.get_pos()
    x = mousepos[0]-20
    y = mousepos[1]-20
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == KEYUP:
            var = 0
            vary = 0
        if event.type== KEYDOWN:
            if event.key == K_RIGHT:
                var = 5
            if event.key == K_LEFT:
                var = -5
            if event.key == K_UP:
                vary = -5
            if event.key == K_DOWN:
                vary= +5
            if event.key == K_SPACE:
                bomblist.append(Bomb(x+30,y-5,0,0))

    for bommb in bomblist:
        bommb.throwbomb()
    x += var
    y +=vary


    pygame.display.update()