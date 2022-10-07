import numpy as np
import math
from conts import WIDTH, HEIGHT
from shots import Bullet
import pygame


class Turret(object):
    def __init__(self, pos):
        self.pos = pos
        self.time = 0
        self.fire_speed = 200
        self.size = 20

    def update(self, enemys):
        self.time += 1
        if self.time % self.fire_speed != 0:
            return
        min_dis = 1000000000
        close_enemy = None
        for enemy in enemys:
            dis = math.hypot(enemy.pos[0] - self.pos[0], enemy.pos[1] - self.pos[1])
            if dis < min_dis:
                min_dis = dis
                close_enemy = enemy

        if close_enemy is not None:
            enemy = close_enemy
            angle = math.atan2(enemy.pos[0] - self.pos[0], enemy.pos[1] - self.pos[1])
            return Bullet(self.pos, angle, 5)

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), self.pos, self.size)
