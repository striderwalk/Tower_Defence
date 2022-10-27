import math
import pygame
from conts import RED, WIDTH, HEIGHT


class Bullet:
    def __init__(self, pos, angle, speed):
        self.pos = pos
        self.angle = angle  # radients
        self.speed = speed
        self.dead = False

    def move(self):
        new_x = self.pos[0] + self.speed * math.sin(self.angle)
        new_y = self.pos[1] + self.speed * math.cos(self.angle)

        self.pos = (new_x, new_y)

        return self.pos

    def update(self, enemys):   
        # check if in bounds
        invaild_x = self.pos[0] < 0 or self.pos[0] > WIDTH
        invaild_y = self.pos[1] < 0 or self.pos[1] > HEIGHT
        if invaild_x or invaild_y:
            self.die()

        hits = []
        for enemy in enemys:
            if enemy.dead:
                continue
            if enemy.body.collidepoint(self.pos):
                hits.append(enemy)

        if hits is []:
            return
        min_dis = 1_000_0000_000_000
        min_index = None

        for index, i in enumerate(hits):
            dis = math.hypot(enemy.pos[0] - self.pos[0], enemy.pos[1] - self.pos[1])
            if dis < min_dis:
                min_dis = dis
                min_index = index

        if min_index is not None:
            hits[min_index].hit()
            return "die"

    def die(self):
        self.death = True

    def draw(self, win):
        pygame.draw.circle(win, (RED), self.move(), 5)
