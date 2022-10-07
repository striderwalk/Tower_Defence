import numpy as np
import math
from conts import WIDTH, HEIGHT, TILE_SIZE
from shots import Mine
from random import random
import pygame


class Mine_Shooter(object):
    def __init__(self, pos, points):
        self.pos = pos
        self.time = -1
        self.fire_speed = 200
        self.size = 20
        self.path_points = points

    def update(self, path_points):
        self.time += 1
        if self.time % self.fire_speed != 0:
            return

        min_dis = 1_000_0000_000_000
        closet_point = None
        for i in self.path_points:
            dis = math.hypot(i[0] - self.pos[0], i[1] - self.pos[1])
            if dis < min_dis:
                min_dis = dis
                closet_point = i

        if closet_point is not None:
            x = closet_point[0] + (random() - 0.5) * TILE_SIZE * 0.9
            y = closet_point[0] + (random() - 0.5) * TILE_SIZE * 0.9
            return Mine((x, y))

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), self.pos, self.size)

    #     x, y = self.move()
    #     x -= self.image.get_size()[0]/2
    #     y -= self.image.get_size()[1]/2
    #     win.blit(self.image, (x, y))
