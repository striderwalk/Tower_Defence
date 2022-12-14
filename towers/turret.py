import math
from shots import Bullet
import pygame
from load import image
import image_utils


class Turret(object):

    base_image = "./assets/gun.png"

    def __init__(self, pos):
        self.size = 145
        self.pos = pos[0] - self.size / 2, pos[1] - self.size / 2
        self.time = 0
        self.fire_speed = 45

        self.angle = 90
        self.base_angle = 90
        self.next_angle = self.angle

        self.base_image = image.get_image("./assets/gun.png", self.size)
        self.image = self.base_image
        self.img_surf = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)

    @property
    def center(self):
        x, y = self.image.get_rect().center
        x += self.pos[0]
        y += self.pos[1]
        return (x, y)

    @property
    def real_angle(self):
        return self.angle + self.base_angle

    def update_image(self):
        self.angle += self.next_angle
        surf = self.img_surf.copy()
        self.image = image_utils.rot_center(surf, self.base_image, self.real_angle)

    def update(self, enemys):
        self.time += 1

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

            self.next_angle = (math.degrees(angle) - self.angle) / 2

            if self.time % self.fire_speed != 0:
                return

            angle = math.radians(self.angle)  # +self.base_angle)
            return Bullet(self.center, angle, 5)

    def draw(self, win):
        self.update_image()
        x, y = self.pos
        # x -= self.size
        # y -= self.size/2
        win.blit(self.image, (x, y))
