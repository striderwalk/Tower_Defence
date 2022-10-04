import numpy as np
import math
from conts import WIDTH, HEIGHT
import pygame

def get_points():
    min_x = WIDTH*0.1
    min_y = HEIGHT*0.1
    path = [(0,0), (1, 0), (1, 0.5), (0, 0.5), (0,1),(1,1)]

    path = [ (WIDTH * i[0], HEIGHT * i[1]) for i in path]
    path = [ ((i[0]*0.8)+min_x,(i[1]*0.8)+min_y) for i in path]

    return path


class Enemy(object):
    """docstring for Enemy"""
    path_points = get_points()

    def make_path(self):
        path = []
        for i in range(len(Enemy.path_points)-1):
            p1 = Enemy.path_points[i]
            p2 = Enemy.path_points[i+1]
            dis = int(math.hypot(p1[0]-p2[0],p1[1]-p2[1]))
            path.extend(np.linspace(p1, p2, dis))

        return path

    def __init__(self):
        self.path = self.make_path()
        self.count = -1
        self.speed = 5
        self.dead = False

    @property   
    def pos(self):
        return self.path[int(self.count)]
    @property
    def body(self):
        return pygame.Rect((*self.pos, 10,10))
    def move(self):
        self.count += self.speed
        
        if self.count >= len(self.path) -1:
            self.die()
            self.count -= self.speed  
            return self.pos
            

        return self.pos

    def die(self):
        self.dead = True

