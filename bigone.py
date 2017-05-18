import pygame
import math
from pygame.locals import *
import sidetestfile
import my_algorithm
pygame.init()

screen = pygame.display.set_mode((1300,800))
w = 10
grid = [ [1]*80 for n in range(80)]

lastmouseclick = []

def path(first_input):
    moveslist = []

    # insert them into to a list
    list = []
    list.append(first_input)

    # create second list to furthr down list's list with a loop
    list2 = []

    for every_thing in list:
        for every_atom in every_thing:
            list2.append(every_atom)
    size_of_list2 = len(list2)
    sqrrt = math.sqrt(size_of_list2)
    # creat a list to match every atom in list2 with  number
    number_match_list = []
    i = 0

    try:
        for _ in list2:
            i += 1
            number_match_list.append(i)
        p_index = list2.index('p')
        m_index = list2.index('m')
        kmr = (list2.index('m') // sqrrt) + 1
        kpr = (list2.index('p') // sqrrt) + 1

        temp = 0
        tt = list2.index('m')
        kttr = (tt // sqrrt) + 1

        if kpr * sqrrt != p_index:
            kpc = sqrrt - ((kpr * sqrrt) - p_index)

        else:
            kpc = sqrrt * kpr
        if kmr * sqrrt != p_index:
            kmc = sqrrt - ((kmr * sqrrt) - m_index)

        else:
            kmc = sqrrt * kmr

        if kmc == kpc: #if on the same horizontal line
            if kmr > kpr:
                print('up by', kmr - kpr, 'steps ')
                [moveslist.append("up") for _ in range(int(kmr - kpr))]
                return

            elif kpr > kmr:
                print('down by', kpr - kmr, 'stepshere1')
                [moveslist.append("down") for _ in range(int(kpr - kmr))]
                print("movelist thooo is " , moveslist, kpr - kmr)
        else:

            if kmr > kpr:
                print('up by', kmr - kpr, 'steps ')
                [moveslist.append("up") for _ in range(int(kmr - kpr))]
                return

            elif kmr < kpr:

                print('down by', kpr - kmr, 'stepshere 2')
                [moveslist.append("down") for _ in range(int(kpr - kmr))]

            if m_index > p_index:
                print("kpc in here1 is ", kpc, "\n and m_index is ", m_index)
                print('left by', kmc - kpc, 'steps')

                [moveslist.append("left") for _ in range(int(kmc - kpc))]

                # print(moveslist,"here1")
                # ini()
                return moveslist

            elif m_index < p_index:
                print('right by', kpc - kmc, 'steps')
                [moveslist.append("right") for _ in range(int(kpc - kmc))]

                print(moveslist)
                # ini()
                return moveslist

        if kpr == kmr:
            if m_index > p_index:
                # print('left by', m_index - p_index, 'steps')

                [moveslist.append("left") for _ in range(int(m_index - p_index))]

                # print(moveslist,"here122")
                # ini()
                return moveslist

            elif m_index < p_index:
                print('right by', p_index - m_index, 'steps')
                [moveslist.append("right") for _ in range(int(p_index - m_index))]

                print(moveslist)
                # ini()
                return moveslist





        print(moveslist)

    except ValueError:
        print('Value Error guy!')
        # ini(
        return moveslist

def turnToStringCode(row,col,numofboxes = 64):
    pass




class person:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def createperson(self, col = (255, 0, 0)):

        pygame.draw.rect(screen,col,(self.x,self.y,w,w))



badpersonX = 0
badpersonY = 7
goodpersonX = 0
goodpersonY = 0
badpersonyvar = 0
badpersonxvar = 0
timer = 0
def changecellColor(row,col):
    grid[col][row] *= -1
while True:
    timer += 1
    pygame.time.Clock().tick(60)
    grid2 = []
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0,0,0), (0, 0, w*80, w*80), 2)
    x = 0

    y = 0
    for row in grid:
        for col in row:
            # grid2.append(col)
            if col == -1:
                color = (255,0,0)
            else:
                color = (0, 0, 0)
            pygame.draw.rect(screen, color, (x, y, w, w), 9)

            x += w
        y += w
        x = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    mouseclicked = pygame.mouse.get_pressed()
    mousepos = pygame.mouse.get_pos()

    if mouseclicked[0] == 1:
        lastmouseclick [:] = []
        grid2[:] = []
        gridtemp =  [ [1]*80 for n in range(80)]
        cellx = mousepos[0]//w
        celly = mousepos[1]//w
        # changecellColor(cellx,celly)
        goodpersonX = cellx
        goodpersonY = celly
        lastmouseclick.append(cellx)
        lastmouseclick.append(celly)
        print(cellx, celly)

        if celly in range(80) and cellx in range(80):
            string = ["-" for _ in range(6400)]
            print('String is ' ,string)
            #reset all back to 1's in list

            # print("\n\n\n gridtemp is ", gridtemp)
            gridtemp[goodpersonY][goodpersonX] = -1

            # print("\n\n\n gridtemp after changed is ", gridtemp)
            gridtemp[badpersonY][badpersonX] = -2

            # print("\n\n\n gridtemp two  is ", grid2)
            for row in gridtemp:
                for col in row:
                    grid2.append(col)


            # print("\n\n\n second grid two  is ", grid2)
            sqrroot = math.sqrt(6400)
            string[grid2.index(-1)] = "m"
            string[grid2.index(-2)] = "p"
            finalstring = ''

            # print("\n\n\n string two  is ", string)
            for letter in string:
                finalstring += letter
            print("final strng is ", finalstring)
            movelist = sidetestfile.ini(finalstring)#path(string)

            print(movelist)
            u = 0
            ulist = []
            uvar =''
            for i in string:
                u += 1
                uvar += i
                if u == 80:
                    u = 0
                    ulist.append(uvar)
                    uvar = ''

            print(ulist,"\n\n\n\n\n\n")
            if movelist != None :
                up = movelist.count("up")
                down = movelist.count("down")
                left = movelist.count("left")
                right = movelist.count("right")
                print("up:", up, "down : ", down, "left: ", left, "right: ", right)
                if down > 0:
                    badpersonyvar = down * -1
                if up > 0:
                    badpersonyvar = up
                if left > 0:
                    badpersonxvar = left * -1
                if right > 0:
                    badpersonxvar = right
            # except AttributeError as e:
            #     print(e)

    # if goodpersonxvar > 0 :
    #     goodpersonxvar -= 1
    # if goodpersonyvar > 0:
    #     goodpersonyvar -= 1
    if timer % 90 == 0:
        pass
    if badpersonxvar > 0:
        if timer % 1 == 0:
            badpersonX -= 1
            badpersonxvar -= 1
    if badpersonyvar > 0:
        if timer % 1 == 0:
            badpersonY += 1
            badpersonyvar -= 1

    if badpersonyvar < 0:
        if timer % 1 == 0:
            print("lololol")
            badpersonY -= 1
            badpersonyvar += 1
    if badpersonxvar < 0:
        if timer % 1 == 0:
            print("lololol")
            badpersonX += 1
            badpersonxvar += 1
    if badpersonxvar == 0 and badpersonyvar == 0:
        try:
            grid2[:] = []
            gridtemp =  [ [1]*80 for n in range(80)]
            cellx = lastmouseclick[0]
            celly = lastmouseclick[1]
            # changecellColor(cellx,celly)
            goodpersonX = cellx
            goodpersonY = celly
            print(cellx, celly)

            if celly in range(80) and cellx in range(80):
                string = ["-" for _ in range(6400)]
                print('String is ' ,string)
                #reset all back to 1's in list

                # print("\n\n\n gridtemp is ", gridtemp)
                gridtemp[goodpersonY][goodpersonX] = -1

                # print("\n\n\n gridtemp after changed is ", gridtemp)
                gridtemp[badpersonY][badpersonX] = -2

                # print("\n\n\n gridtemp two  is ", grid2)
                for row in gridtemp:
                    for col in row:
                        grid2.append(col)


                # print("\n\n\n second grid two  is ", grid2)
                sqrroot = math.sqrt(6400)
                string[grid2.index(-1)] = "m"
                string[grid2.index(-2)] = "p"
                finalstring = ''

                # print("\n\n\n string two  is ", string)
                for letter in string:
                    finalstring += letter
                print("final strng is ", finalstring)
                movelist = sidetestfile.ini(finalstring)#path(string)

                print(movelist)
                u = 0
                ulist = []
                uvar =''
                for i in string:
                    u += 1
                    uvar += i
                    if u == 80:
                        u = 0
                        ulist.append(uvar)
                        uvar = ''

                print(ulist,"\n\n\n\n\n\n")
                if movelist != None :
                    up = movelist.count("up")
                    down = movelist.count("down")
                    left = movelist.count("left")
                    right = movelist.count("right")
                    print("up:", up, "down : ", down, "left: ", left, "right: ", right)
                    if down > 0:
                        badpersonyvar = down * -1
                    if up > 0:
                        badpersonyvar = up
                    if left > 0:
                        badpersonxvar = left * -1
                    if right > 0:
                        badpersonxvar = right
        except:
            pass
    # badpersonY += badpersonyvar
    # badpersonX += badpersonxvar
    goodperson = person(int(w * goodpersonX), int(w * goodpersonY))
    goodperson.createperson(col=(0, 255, 0))
    badperson = person(int(w*badpersonX),int(w*badpersonY))
    badperson.createperson()




    pygame.display.update()

