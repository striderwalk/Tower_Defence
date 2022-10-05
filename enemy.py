import numpy as np
import math
import json
from conts import WIDTH, HEIGHT
import pygame

def get_points():
    with open("./path.json") as file:
        points = json.load(file)
    return points

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
        self.speed = 1
        self.dead = False
        self.size = 45

    @property   
    def pos(self):
        return self.path[int(self.count)]
    @property
    def body(self):
        return pygame.Rect((self.pos[0]-self.size/2, self.pos[1]-self.size/2, self.size, self.size))
    def move(self):
        self.count += self.speed
        
        if self.count >= len(self.path) -1:
            self.die()
            self.count -= self.speed  
            return self.pos
            

        return self.pos

    def die(self):
        self.count = float("inf")
        self.dead = True

