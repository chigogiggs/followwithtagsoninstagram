import pygame,random
from pygame.locals import *


grid = [ [1]*8 for n in range(8)]

w = 400
h = 400

rectw = 100

tiles_loc = []

pygame.init()

screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
pygame.display.set_caption('2048')

i = [n for n in range(0, 400) if n % 100 == 0]
myx = random.choice(i)
myY = random.choice(i)
numtoassign = random.choice([2,4])
class Board:
    def __init__(self, x,y,name=None):
        self.name = name
        self.x = x
        self.y = y
        self.myfont = pygame.font.SysFont('monospace', 35)
        self.final = []
        self.ylistup = []
        self.xcurentlist = []

    def draw(self):
        for row in grid:
            for col in row:

                if col == -1:
                    pygame.draw.rect(screen,(255,0,0),(self.x,self.y,rectw,rectw),2)
                else:

                    pygame.draw.rect(screen,(255,255,255),(self.x,self.y,rectw,rectw),2)
                pygame.draw.line(screen, (0,0,0), (self.x,0), (self.x,400),2)
                self.x += rectw

            pygame.draw.line(screen, (0, 0, 0), (0, self.y), (400, self.y), 2)
            self.y += rectw
            self.x = 0
    def createrect(self):
        pygame.draw.rect(screen, (random.randint(10,255), random.randint(10,255), random.randint(10,255)), (self.x, self.y, rectw, rectw))
        # self.assignnumber(numtoassign,(self.x+ (rectw/2)-10,myY+20))
    def assignnumber(self,num,pos):
        self.text = self.myfont.render(str(num),1,(0,0,0))
        screen.blit(self.text,(pos))


    def swipe(self,direction):
        if direction == 'up':
            print('starting pos for',self.name,self.y, self.x)

            try:
                self.ylistup[:] = [n for n in range(0,self.y) if n%100 == 0]
                for x in self.ylistup:
                    self.xcurentlist.append(self.x)
                self.final[:] = list(zip(self.ylistup,self.xcurentlist))
                self.final.sort(reverse=True)
                print(self.final)
                for loc in self.final:
                    if loc in tiles_loc:
                        self.final.remove(loc)
                        tiles_loc.remove(loc)

                print('newlist is ',self.final)
                print('tilesloc is ',tiles_loc)

                self.x = self.final[-1][1]
                self.y = self.final[-1][0]
                tiles_loc.append((self.y,self.x))

            except Exception as e:
                print(e)

            print('\n\n\n\n\n\n\n\n\n\n')

        elif direction == 'down':pass
        elif direction == 'right':pass

        elif direction == 'left':pass


newx = random.choice(i)
newy = random.choice(i)

newex = random.choice(i)
newey = random.choice(i)
tilelist = []
tilelist.append(Board(newex,newey,'apkan'))
tilelist.append(Board(newex,newy,'okon'))

tiles_loc.append((newey,newex))
tiles_loc.append((newy,newex))

# print(tiles_loc)
while True:
    screen.fill((0,0,0))
    Board(0,0).draw()
    for til in tilelist:
        til.createrect()
    mouse_clicked = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    if mouse_clicked[0] == 1:
        intmouseX = int(mouse_pos[0]/rectw)
        intmouseY = int(mouse_pos[1]/rectw)

        grid[intmouseY][intmouseX] = -1
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                newx = random.choice(i)
                newy = random.choice(i)
                # tilelist.append(Board(newx,newy))
                # tiles_loc.append((newy,newx))
                for tiles in tilelist:
                    tiles.swipe('up')
            if event.key == K_DOWN:
                newx = random.choice(i)
                newy = random.choice(i)
                # tilelist.append(Board(newx,newy))
                tiles_loc.append((newy,newx))
                for tiles in tilelist:
                    tiles.swipe('down')
            if event.key == K_RIGHT:
                newx = random.choice(i)
                newy = random.choice(i)
                # tilelist.append(Board(newx,newy))
                tiles_loc.append((newy,newx))
                for tiles in tilelist:
                    tiles.swipe('right')
            if event.key == K_LEFT:
                newx = random.choice(i)
                newy = random.choice(i)
                # tilelist.append(Board(newx,newy))
                tiles_loc.append((newy,newx))
                for tiles in tilelist:
                    tiles.swipe('left')

    pygame.display.update()