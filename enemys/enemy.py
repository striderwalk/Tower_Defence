import numpy as np
import math
import json
from conts import WIDTH, HEIGHT, TILE_SIZE
import pygame
from load import path


def get_img(size):
    # img = pygame.image.load("./assests/enemy.png")
    img = pygame.image.load("./assests/New_Project_2.png")
    img = pygame.transform.scale(img, (size, size))
    return img


class Enemy(object):
    """docstring for Enemy"""

    path_points = path.get_points()

    def make_path(self):
        path = []
        for i in range(len(Enemy.path_points) - 1):
            p1 = Enemy.path_points[i]
            p2 = Enemy.path_points[i + 1]
            dis = int(math.hypot(p1[0] - p2[0], p1[1] - p2[1]))
            path.extend(np.linspace(p1, p2, dis))

        return path

    def __init__(self):
        self.path = self.make_path()
        self.count = -1
        self.speed = 5
        self.dead = False
        self.size = 90
        self.health = 100

        self.image = get_img(self.size)

    @property
    def pos(self):
        if math.isinf(self.count):
            return self.path[-1]
        return self.path[int(self.count)]

    @property
    def body(self):
        return pygame.Rect(
            (
                self.pos[0] - self.size / 2,
                self.pos[1] - self.size / 2,
                self.size,
                self.size,
            )
        )

    def move(self):
        if self.health <= 0 or math.isinf(self.count):
            self.die()
            return {"type": "die"}

        self.count += self.speed

        if self.count >= len(self.path) - 1:
            self.die(move=False)
            self.count -= self.speed
            return {"type": "win", "value": self.pos}

        return {"type": "move", "value": self.pos}

    def die(self, move=True):
        if move:
            self.count = float("inf")
        self.dead = True

    def hit(self, dmg=10):
        self.health -= dmg

    def draw(self, win):
        pos = self.move()
        if pos["type"] == "die":
            return "die"
        x, y = pos["value"]
        x -= self.image.get_size()[0] / 2
        y -= self.image.get_size()[1] / 2
        win.blit(self.image, (x, y))
        if pos["type"] == "win":
            return "win"
        # pygame.draw.circle(win, (255,255,0), self.pos, 15)

    def __repr__(self):
        return f"enemy at {self.pos}"
