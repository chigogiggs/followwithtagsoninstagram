import pygame
import sys, random
from pygame.locals import *
from threading import _start_new_thread
import threading
import math,os
from rat.Hythonbaner import  *
import datetime
w = 1110
h = 650
# screen = pygame.display.set_mode((w,h))



os.environ['SDL_VIDEO_CENTERED'] = '1'
w = 1110
h = 650
clock  = pygame.time.Clock()
pygame.mixer.init()
pygame.init()
intromusic = pygame.mixer.Sound('introsong.wav')

bgmusic = pygame.mixer.Sound('bgmusic1.wav')
screen = pygame.display.set_mode((w,h))

bitfilelist= ['letmeout.wav','goddamnit.wav','focus.wav','comeon1.wav']

scorefastlist = []
def genesis():
    # global scorefast
    scorefastlist[:] = []
    scorefast = 0
    slowerscore = 0
    global  screen
    bombcount = 5
    batxmovevar = 5
    buleetmovevar = 45
    ui = 0
    pygame.init()
    posture = 'soldier1.png'
    intromusic.stop()
    bgmusic.play(1000000)
    # pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize

    jet = pygame.image.load('jet.png')
    jet = pygame.transform.scale(jet, (100,200))
    bomb = pygame.image.load('bomb.png')
    bomb = pygame.transform.scale(bomb, (70,70))
    batdead = pygame.image.load('batdead.png')
    hrt = pygame.image.load('hrt.png')
    hrt = pygame.transform.scale(hrt, (30,30))
    batdead = pygame.transform.scale(batdead, (550, 250))
    pygame.mixer.init()
    pause = 0
    firesoundeffect = pygame.mixer.music
    firesoundvar = 'gunsound.wav'
    firesoundeffect.load(firesoundvar)
    deadbatsound = pygame.mixer.Sound('batdeadsound.wav')
    bulletsound = 'ffff.wav'
    ifire = pygame.mixer.Sound(bulletsound)
    firesoundeffect.play(100000)
    firesoundeffect.pause()
    bullettype = 0
    jetswitch = 0
    gamespeedvar = 50
    bats = []
    level = 1
    # soldierdiagonal = pygame.image.load('soldier2.png')
    # soldierup = pygame.image.load('soldier3.png')
    class Player:
        def __init__(self,x,y,raduis,color):
            self.x = x
            self.y = y
            self.raduis = raduis
            self.color = color
            self.bat = pygame.image.load('bat.png')
            self.bat = pygame.transform.scale(self.bat, (150, 150))
            self.fireexplode = pygame.image.load('fireexplode.png')
            self.fireexplode = pygame.transform.scale(self.fireexplode, (90, 60))
            #
            # pygame.display.update(0)

        def createplayer(self):
            soldier = pygame.image.load('images/soldiers/'+posture)
            soldier = pygame.transform.scale(soldier,(self.raduis,self.raduis))
            screen.blit(soldier,(self.x,self.y))

        def createbats(self):
            self.x -= batxmovevar
            screen.blit(self.bat,(self.x,self.y))
            if self.x < -150:
                bats.remove(self)




            return self.x,self.y

        def drawbomb(self):
            global bombcount
            myX = 20
            for bombs in [1,2,3]:
                screen.blit(bomb,(myX,570))
                myX += 70


        def printscore(self, whatnum):

            scoretoprint = str(whatnum)
            font = pygame.font.SysFont('Lucida Grande', 50)
            text = font.render(scoretoprint, 1, (255, 255, 255))
            screen.blit(text, (1000, 20))


            scoretoprint = 'level '+str(level)
            font = pygame.font.SysFont('Lucida Grande', 50)
            text = font.render(scoretoprint, 1, (255, 255, 255))
            screen.blit(text, (500, 20))
        def lifehrt(self,pos):
            screen.blit(hrt, pos)

        def firebullet(self):
            wr = pygame.rect.Rect((self. x,self.y,30,self.raduis))

            if pause != 1:
                if bullettype == 0:
                    pygame.draw.rect(screen,self.color,wr)
                elif bullettype == 1:
                    screen.blit(self.fireexplode,(self.x,self.y-10))
                if self.x > 1110:
                    bullets.remove(self)
                else:
                    self.x += buleetmovevar
            return  wr.left, wr.top

        def scared(self):pass


    lifelist = []
    lifelist.append(Player(2,3,3,4))
    lifelist.append(Player(2,3,3,4))
    lifelist.append(Player(2,3,3,4))
    lifelist.append(Player(2,3,3,4))
    lifelist.append(Player(2,3,3,4))

    bg = pygame.image.load('bg1.jpg')
    # bg = pygame.transform.scale(bg,(1400,1000))

    x,y = 20,h-450
    side = [1,2,3,4,5,6]
    clock  = pygame.time.Clock()
    players = []
    bats.append(Player(random.randint(w+10,w+10), random.randint(50,300), 150, (0, 0, 0)))

    mouseclicktimercontrol = 5
    batcreationtimercontrol = 10
    bullets  = []
    batslocationlist = []
    var  = 0
    vary = 0
    lifevar =20
    batcreationvar = 10
    while True:


        bityell = pygame.mixer.Sound(random.choice(bitfilelist))
        global jetswitch
        global bulletsound
        global firesoundvar
        clock.tick(60)
        if gamespeedvar >0:
            gamespeedvar -=1
        if gamespeedvar == 0:
            batxmovevar += 1
            gamespeedvar= 50
            print('batmovevar is ',batxmovevar)
            if batxmovevar%10 == 0:
                level += 1
                if batcreationvar >1:
                    batcreationvar-=1
                print('leveled',level)
        batslocationlist[:] = []
        screen.fill((0,0,0))
        screen.blit(bg,(0,0))
        mouse_clicked = pygame.mouse.get_pressed()
        x += var
        y += vary
        if vary == 0:
            if y < 200:
                y += 20
        if level == 6:
            buleetmovevar = 90
        if jetswitch == 1:
            screen.blit(jet,(x+80,y+150))
            screen.blit(jet,(x+150,y+150))
        if slowerscore < scorefast:
            slowerscore +=1

        Player(1,2, 150, (0, 0, 0)).drawbomb()
        Player(1,2, 150, (0, 0, 0)).printscore(slowerscore)
        lifevar = 20
        for life in lifelist:
            life.lifehrt((lifevar,20))
            lifevar += 40
        if batcreationtimercontrol > batcreationvar:
            batcreationtimercontrol = batcreationvar
        if batcreationtimercontrol < batcreationvar:
            batcreationtimercontrol += 1
        if mouseclicktimercontrol < 5:
            mouseclicktimercontrol += 1
        if mouse_clicked[0] == 0:
            firesoundeffect.pause()
        if mouse_clicked[0] == 1 and mouseclicktimercontrol == 5:
            posture = 'soldier1.png'
            if pause != 1:
                bullets.append(Player(x + 370,y+150,10,(255,0,0)))
                mouseclicktimercontrol = 0
                ifire.play()
                firesoundeffect.unpause()
        if batcreationtimercontrol == batcreationvar:
            if pause != 1:
                bats.append(Player(random.randint(w+10,w+10), random.randint(50,300), 150, (0, 0, 0)))
                batcreationtimercontrol = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                jetswitch = 0
                var = 0
                vary = 0
                posture = 'soldier1.png'
                firesoundeffect.pause()
            if event.type == KEYDOWN:
                if event.key == K_a:
                    if ui != 1:
                         var = -15
                if event.key == K_d:
                    if ui != 1:
                         var = 15
                if event.key == K_s:
                    if bullettype == 1:
                        bullettype = 0
                        bulletsound = 'ffff.wav'
                        firesoundvar = 'gunsound.mp3'
                    elif bullettype ==0:
                        bullettype = 1
                        bulletsound = 'explosion.wav'
                        firesoundvar = bulletsound
                if event.key == K_F1 and ui == 0:
                    batxmovevar = 0
                    ui = 1
                    buleetmovevar = 0
                    pause = 1
                elif event.key == K_F1 and ui == 1:
                    batxmovevar = 5
                    ui = 0
                    buleetmovevar = 45

                    pause= 0
                if event.key == K_DOWN:
                    if ui != 1:
                        pass




                if event.key == K_SPACE:
                    posture = 'soldier1.png'
                    if pause != 1:
                        bullets.append(Player(x + 370,y+150,10,(255,0,0)))
                        mouseclicktimercontrol = 0
                        ifire.play()
                        firesoundeffect.unpause()
                if event.key == K_RIGHT:
                    if ui != 1:
                        var = 15
                     # posture = 'soldier'+str(posturechangevar)+'.png'

                elif event.key == K_LEFT:
                    if ui != 1:
                         var = -15
                     # posture = 'soldier'+str(posturechangevar)+'.png'
                elif event.key == K_UP:
                    if ui != 1:
                        vary = -20
                        jetswitch = 1

                        # gunend.play()
        player = Player(x, y, 400, (0, 0, 0))
        player.createplayer()
        for bat in bats:
            batpos = bat.createbats()
            batslocationlist.append(batpos)
        if len(lifelist) ==0:
            scorefastlist.append(scorefast)
            bityell.stop()
            Gameover()
        for loca in batslocationlist:
            if x + 400 > loca[0] >x and y <loca[1] or loca[0] + 150 > x > loca[0] and y <loca[1]:
                try:
                    del lifelist[-1]
                    ndexloc = batslocationlist.index(loca)
                    bats.remove(bats[ndexloc])
                    bityell.set_volume(20)
                    bityell.play()

                except Exception as e:
                    # print(e
                    pass
        for bulet in bullets:
            bulletpos = bulet.firebullet()
            for loc in batslocationlist:
                if loc[0] + 150 > bulletpos[0] > loc[0] and loc[1] + 150 > bulletpos[1] > loc[1] or bulletpos[0] + 30 > loc[0] > bulletpos[0] and bulletpos[1] + 10 > loc[1] > bulletpos[1]:
                    try:
                        deadbatsound.set_volume(.2)
                        deadbatsound.play()
                        indexloc = batslocationlist.index(loc)
                        bats.remove(bats[indexloc])
                        batslocationlist.remove(loc)

                        bullets.remove(bulet)
                    except (ValueError,IndexError) as e:
                        print(e)
                    print('hit')
                    screen.blit(batdead,(loc[0]-200,loc[1]-100))
                    scorefast += 9


        if pause == 1:
            paused = "Paused! press f1 to unpause!"
            font = pygame.font.SysFont('Lucida Grande', 50)
            text = font.render(paused, 1, (255, 255, 255))
            screen.blit(text, (w/2-300, h/2-100))
        pygame.display.update()



def banner():
    bannertimer = datetime.datetime.now()
    rectlist = []
    switch = 'off'
    timer = 0
    class Draw:
        def __init__(self,x,y):
            self.x = x
            self.y= y
        def effectone(self):
            pygame.draw.rect(screen,(0,0,0),(self.x,self.y,20,100))

    intromusic.play(1000)
    clock.tick(60)
    while True:
        mouseclicked = pygame.mouse.get_pressed()
        if mouseclicked[0] == 1:
            genesis()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    genesis()

        scoretoprint = 'Hython Inc'
        font = pygame.font.Font('openingfont.ttf', 100)
        text = font.render(scoretoprint, 1, (255, 255, 255))
        screen.blit(text, (300, 280))

        myx = 300
        for i in range(0,30):
            rects = Draw(myx,280)
            if len(rectlist) <=30 and switch == 'off':
                rectlist.append(rects)
            elif len(rectlist) >30 or len(rectlist) == 30:
                switch= 'on'

            myx += 20
        for rect in rectlist:
            rect.effectone()
        if switch == 'on':
            timer += 1
            try:
                if timer == 11:
                    rectlist.remove(rectlist[-1])
                    timer = 0
            except IndexError:
                pass
        print(len(rectlist))
        timenow = datetime.datetime.now()
        diffintime = timenow- bannertimer
        if int(str(diffintime)[5:7]) > 10:
            genesis()
        pygame.display.update()

#5197436333


def Gameover():
    bgmusic.stop()
    intromusic.stop()
    currenttime = datetime.datetime.now()
    class Gameend:
        def __init__(self,x,y):
            self.x = x
            self.y= y
        def effectone(self):
            pygame.draw.rect(screen,(0,0,0),(self.x,self.y,20,100))

    intromusic.play(1000)
    while True:
        clock.tick(60)
        screen.fill((0,0,0))
        highscoretext = 'High Score'
        font = pygame.font.SysFont('Lucida Grande', 70)
        text = font.render(highscoretext, 1, (255, 255, 255))
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        screen.blit(text,(textpos[0],textpos[1]+200))
        pygame.draw.rect(screen,(128,128,128),(textpos[0]-100,textpos[1]+270,450,100))


        font = pygame.font.SysFont('Lucida Grande', 70)
        btext = font.render(str(scorefastlist[0]), 1, (0, 0, 0))
        textpos = btext.get_rect()
        textpos.centerx = screen.get_rect().centerx
        screen.blit(btext,(textpos[0],textpos[1]+300))
        mouseclicked = pygame.mouse.get_pressed()
        # if mouseclicked[0] == 1:
        #     genesis()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    genesis()
        pygame.display.update()
banner()