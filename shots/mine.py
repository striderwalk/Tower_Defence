import math
import pygame
import glob
from conts import FPS, TILE_SIZE
from load import image


class Mine:
    def __init__(self, pos):

        self.size = 45
        self.pos = pos
        self.images = [image.get_image("./assests/mine.png", self.size)]
        self.life_left = True
        self.dead = False
        self.img_index = 0
        self.img_time = 0
        self.img_fps = 5

    @property
    def image(self):
        if len(self.images) == 1:
            return self.images[-1]
        self.img_time += self.img_fps
        if self.img_time % FPS == 0:
            self.img_index += 1
            if self.img_index >= len(self.images):
                self.img_index -= 1
                self.die()

        return self.images[self.img_index]
    @property
    def body(self):
        return (
                self.pos[0] - self.size,
                self.pos[1] - self.size / 2,
                self.size*2,
                self.size,
            )

    def update(self, enemys):
        if self.life_left is True:
            pass
        elif self.life_left == 0:
            self.img = None
            self.die()
            return "die"

        else:
            self.life_left -= 1
        hit = False
        for enemy in enemys:
            if enemy.dead:
                continue
            if math.hypot(enemy.pos[0] - self.pos[0], enemy.pos[1] - self.pos[1]) < TILE_SIZE:
                hit = True
            # print(math.hypot(enemy.pos[0] - self.pos[0], enemy.pos[1] - self.pos[1]), hit)

        if not hit:
            return

        if hit:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play(loops=0)
            self.images = image.get_images("./assests/explotion", self.size * 2)
            self.img_time = 0
            self.life_left = 900

        for i in enemys:
            if i.dead:
                continue
            if math.hypot(enemy.pos[0] - self.pos[0], enemy.pos[1] - self.pos[1]) < TILE_SIZE:
                i.die()
    def die(self):
        self.dead = True

    def draw(self, win):
        # pygame.draw.rect(win, (255,255,0),self.body)
        x, y = self.pos
        x -= self.image.get_size()[0] / 2
        y -= self.image.get_size()[1] / 2
        win.blit(self.image, (x,y))
        # pygame.draw.circle(win, (255,0,255), self.pos, 3)
        # pygame.draw.circle(win, (255,0,255), self.pos, TILE_SIZE*1,width=1)


    def __repr__(self):
        return "mine"
