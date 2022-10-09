import pygame
import pygame.gfxdraw 
from conts import WIDTH, HEIGHT
import math
import numpy as np
raidus = 150
x = range(0,101)
y = np.linspace(np.pi,np.pi/2, 101)
xvals = x
yinterp = np.interp(xvals, x, y)


def arc(win, colour, center,raidus, angle1, angle2,width=1):
    angles = np.linspace(angle1,angle2, 1000)


    # outer section
    points = []
    for i in angles:
        x = center[0] + raidus * math.cos(i)
        y = center[1] + raidus * -math.sin(i)
        points.append((x,y))

    raidus -= width
    for i in angles[::-1]:
        x = center[0] + raidus * math.cos(i)
        y = center[1] + raidus * -math.sin(i)
        points.append((x,y))



    pygame.draw.polygon(win, colour, points)



def draw(win, health):
    pygame.draw.circle(win, (34, 32, 54), (WIDTH, HEIGHT), raidus)

    ## maybe rotate img??

    start_anlge = yinterp[health]
    arc(win, (124, 32, 54), (WIDTH,HEIGHT),raidus-3, start_anlge,math.pi, 30)
