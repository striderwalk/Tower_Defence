import math
from random import random
import itertools
from shots import Mine
from load import path, image
from conts import TILE_SIZE, FPS

PATH = path.get_path()


class Mine_Shooter(object):

    base_image = "./assests/mine_launcher/open/open1.png"

    def __init__(self, pos):
        self.pos = pos
        self.grid_pos = (math.floor(
            pos[0] / TILE_SIZE), math.floor(pos[1] / TILE_SIZE))
        self.time = -1
        self.fire_speed = 200
        self.size = 80

        self.images = image.get_images(
            "./assests/mine_launcher/open", self.size * 2)
        self.cur_image = next(self.images)
        self.img_time = 0
        self.img_fps = 5

    @property
    def image(self):
        self.img_time += self.img_fps
        if self.img_time % FPS == 0:
            try:
                self.cur_image = next(self.images)
            except StopIteration:
                self.images = itertools.cycle([self.cur_image])

        return self.cur_image

    def update(self, *args):
        self.time += 1
        if self.time % self.fire_speed != 0:
            return

        min_dis = 1_000_0000_000_000
        closet_point = None
        for i in PATH:
            dis = abs(self.grid_pos[0] - i[0]) + abs(self.grid_pos[1] - i[1])
            if dis < min_dis:
                min_dis = dis
                closet_point = i

        if closet_point is not None:
            self.images = image.get_images(
                "./assests/mine_launcher/close", self.size * 2
            )

            x = (closet_point[0] + random() - 0.5) * TILE_SIZE * 0.9
            y = (closet_point[1] + random() - 0.5) * TILE_SIZE * 0.9
            return Mine((x, y))

    def draw(self, win):
        x, y = self.pos
        x -= self.image.get_size()[0] / 2
        y -= self.image.get_size()[1] / 2
        win.blit(self.image, (x, y))

    #     x, y = self.move()
    #     x -= self.image.get_size()[0]/2
    #     y -= self.image.get_size()[1]/2
    #     win.blit(self.image, (x, y))
