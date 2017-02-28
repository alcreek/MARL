import pygame
import random
from random import randint
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pygame.init()
screen = pygame.display.set_mode((700, 700),pygame.DOUBLEBUF)



done = False

def getState(cx,cy):
    state =0
    if cx<100 or cx>600 or cy<100 or cy>600:
        state = 26
    elif cy>100 and cy< 200:
        if cx>100 and cx<200:
            state =1
        elif cx>200 and cx<300:
            state =2
        elif cx>300 and cx<400:
            state =3
        elif cx>400 and cx<500:
            state =4
        elif cx>500 and cx<600:
            state =5
    elif cy>200 and cy< 300:
        if cx>100 and cx<200:
            state =6
        elif cx>200 and cx<300:
            state =7
        elif cx>300 and cx<400:
            state =8
        elif cx>400 and cx<500:
            state =9
        elif cx>500 and cx<600:
            state =10
    elif cy>300 and cy< 400:
        if cx>100 and cx<200:
            state =11
        elif cx>200 and cx<300:
            state =12
        elif cx>300 and cx<400:
            state =13
        elif cx>400 and cx<500:
            state =14
        elif cx>500 and cx<600:
            state =15
    elif cy>400 and cy< 500:
        if cx>100 and cx<200:
            state =16
        elif cx>200 and cx<300:
            state =17
        elif cx>300 and cx<400:
            state =18
        elif cx>400 and cx<500:
            state =19
        elif cx>500 and cx<600:
            state =20
    elif cy>500 and cy< 600:
        if cx>100 and cx<200:
            state =21
        elif cx>200 and cx<300:
            state =22
        elif cx>300 and cx<400:
            state =23
        elif cx>400 and cx<500:
            state =24
        elif cx>500 and cx<600:
            state =25

    return state

    return 0
def moveSwimmer(cx,cy):
    return 0

def gridWorld(cx1,cy1,cx2,cy2):
    out = (15,13,40)#color out region
    #region out
    pygame.draw.rect(screen, out, pygame.Rect(0, 0,100, 700))
    pygame.draw.rect(screen, out, pygame.Rect(600, 0,100, 700))
    pygame.draw.rect(screen, out, pygame.Rect(0, 0, 700, 100))
    pygame.draw.rect(screen, out, pygame.Rect(0, 600,700, 100))

    color =(239,178,12)#color grid
    #gridworld
    pygame.draw.rect(screen, color, pygame.Rect(0, 0, 0, 700))
    pygame.draw.rect(screen, color, pygame.Rect(100, 0, 0, 700))
    pygame.draw.rect(screen, color, pygame.Rect(200, 0, 0, 700))
    pygame.draw.rect(screen, color, pygame.Rect(300, 0, 0, 700))
    pygame.draw.rect(screen, color, pygame.Rect(400, 0, 0, 700))
    pygame.draw.rect(screen, color, pygame.Rect(500, 0, 0, 700))
    pygame.draw.rect(screen, color, pygame.Rect(600, 0, 0, 700))
    pygame.draw.rect(screen, color, pygame.Rect(700, 0, 0, 700))

    pygame.draw.rect(screen, color, pygame.Rect(0, 0,700, 0))
    pygame.draw.rect(screen, color, pygame.Rect(0, 100,700, 0))
    pygame.draw.rect(screen, color, pygame.Rect(0, 200,700, 0))
    pygame.draw.rect(screen, color, pygame.Rect(0, 300,700, 0))
    pygame.draw.rect(screen, color, pygame.Rect(0, 400,700, 0))
    pygame.draw.rect(screen, color, pygame.Rect(0, 500,700, 0))
    pygame.draw.rect(screen, color, pygame.Rect(0, 600,700, 0))
    pygame.draw.rect(screen, color, pygame.Rect(0, 100,700, 0))

    #absorption state
    abscolor = (31,195,13)#color a.e.
    pygame.draw.rect(screen, abscolor, pygame.Rect(505, 105,90, 90))
    pygame.display.update()
    ###############################



    swimColor = (45,196,233) #color swimmers
    pygame.draw.circle(screen, swimColor, (cx1, cy1), 30, 0) # swimmer1
    pygame.draw.circle(screen, swimColor, (cx2, cy2), 30, 0) # swimmer2

def coords():
    c =random.randint(100,600)
    BUZZ =1.2
    dif = random.gauss(0, BUZZ)
    #c = c+dif
    return c

def getaction():
    action = random.randint(1,4)
    return action

def move(cxin,cyin,action):
    speed =5
    dx = 10

    if action ==1 and cyin<50:
        speed =speed*(-1)
        ncx = cxin
        ncy = cyin - dx*speed
    elif action ==1 and cyin>50:
        ncx = cxin
        ncy = cyin - dx*speed
    elif action ==2 and cyin>600:
        speed =speed*(-1)
        ncx = cxin
        ncy = cyin + dx*speed
    elif action ==2 and cyin<600:
        ncx = cxin
        ncy = cyin + dx*speed

    elif action ==3 and cxin<50:
        speed =speed*(-1)
        ncx = cxin - dx*speed
        ncy = cyin
    elif action ==3 and cxin>50 :
        ncx = cxin - dx*speed
        ncy = cyin
    elif action ==4 and cxin>600:
        speed =speed*(-1)
        ncx = cxin + dx*speed
        ncy = cyin
    elif action ==4 and cxin<600:
        ncx = cxin + dx*speed
        ncy = cyin
    else:
        ncx = cxin
        ncy = cyin


    return ncx,ncy

global cx1
global cx2
cx1 = coords()
cx2= coords()
global cy1
global cy2
cy1 =coords()
cy2= coords()

gridWorld(cx1,cy1,cx2,cy2)

while not done:

        pygame.display.update()

        #iterations =5

        action1 = getaction()
        (ncx1,ncy1) = move(cx1,cy1,action1)
        action2 = getaction()
        (ncx2,ncy2) = move(cx2,cy2,action2)

        screen.fill((0,0,0))
        cx1 = ncx1
        cy1 = ncy1
        cx2 = ncx2
        cy2 = ncy2

        gridWorld(ncx1,ncy1,ncx2,ncy2)


        pygame.display.update()

        pygame.time.wait(10)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_blue = not is_blue

        pygame.display.flip()
