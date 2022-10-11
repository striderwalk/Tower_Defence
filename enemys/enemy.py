import numpy as np
import math
import json
from conts import WIDTH, HEIGHT, TILE_SIZE
import pygame
from load import path, image




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
        self.angle = 180
        self.base_angle = 180
        self.next_angles = [self.angle]

        self.base_image = image.get_image("./assests/enemy2-export.png", self.size, rotate=self.angle)
        self.image = self.base_image       
        self.img_surf = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)

    def rot_center(self, image, angle):
        # https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame#:~:text=at%2012%3A43-,rabbid76,-188k2525%20gold%20badges109109
        """rotate a Surface, maintaining position."""
        
        surf = self.img_surf.copy()
        topleft = self.pos[0]-self.size/2, self.pos[1]-self.size/2
        rotated_image = pygame.transform.rotozoom(image, angle, 1)
        new_rect = rotated_image.get_rect(center = image.get_rect().center)

        surf.blit(rotated_image, new_rect)
        return surf

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
        if self.count < len(self.path) - 1:
            new_pos = self.path[int(self.count)+1]
            dx = new_pos[0] - self.pos[0]
            dy = new_pos[1] - self.pos[1]
            angle = math.degrees(math.atan2(dx, dy))

            if len(self.next_angles)  == 0 or self.next_angles[-1] != angle:
                self.next_angles = list(np.linspace(self.angle, angle, 10))
            


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



    def update_image(self):
        if len(self.next_angles) > 0:
            self.angle = self.next_angles.pop(0)
        self.image = self.rot_center(self.base_image, self.angle)

    def draw(self, win):
        self.update_image()

        pos = self.move()
        if pos["type"] == "die":
            return "die"
        win.blit(self.image, (self.body[:2]))
        if pos["type"] == "win":
            return "win"
        # pygame.draw.circle(win, (255,255,0), self.pos, 15)

    def __repr__(self):
        return f"enemy at {self.pos}"
