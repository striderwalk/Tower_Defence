import numpy as np
import math
import json
from conts import WIDTH, HEIGHT, TILE_SIZE
import pygame

def get_points():
    with open("./path.json") as file:
        points = json.load(file)
    return points

def get_img(size):
    # img = pygame.image.load("./assests/enemy.png")
    img = pygame.image.load("./assests/New_Project_2.png")
    img = pygame.transform.scale(img, (size, size))
    return img

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
        self.speed = 3
        self.dead = False
        self.size = 90

        self.image = get_img(self.size)

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


    def draw(self, win):
        x, y = self.move()
        x -= self.image.get_size()[0]/2
        y -= self.image.get_size()[1]/2
        win.blit(self.image, (x, y))
