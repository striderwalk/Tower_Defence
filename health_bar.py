import pygame 
from conts import WIDTH, HEIGHT
import math
import numpy as np
raidus = 150
x = range(0,101)
y = np.linspace(np.pi,np.pi/2, 101)
xvals = x
yinterp = np.interp(xvals, x, y)
def draw(win, health):
    pygame.draw.circle(win, (34, 32, 54), (WIDTH, HEIGHT), raidus)

    ## maybe rotate img??

    start_anlge = yinterp[health]

    print(start_anlge, health)
    pygame.draw.arc(win, (124, 32, 54), (WIDTH-raidus, HEIGHT-raidus, raidus*2, raidus*2), start_anlge,math.pi, width = 30)