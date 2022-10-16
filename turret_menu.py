import pygame
import towers

### make a get all func ###
tower_list = [towers.Turret, towers.Mine_Shooter]

from load import image
from conts import WIDTH, HEIGHT, SIDEBAR_WIDTH
import mouse


class Button:
    size = (70, 70)
    base_image = "./assests/base_tile.png"

    @classmethod
    def make_image(cls, path, size):
        dis_img = image.get_image(path, (size[0] * 0.8, size[1] * 0.8))
        logo_image = image.get_image(Button.base_image, size)
        logo_image.blit(dis_img, (size[0] * 0.1, size[1] * 0.1))

        return logo_image

    def __init__(self, pos, path, size=size):
        self.pos = pos
        self.size = size
        self.image = Button.make_image(path, size)
        self.rect = pygame.Rect(pos, size)
        self.clicked = False

    def draw(self, win):

        if self.clicked:  # show selection
            x, y = self.pos
            x -= self.size[0] * 0.1  
            y -= self.size[1] * 0.1
            w = self.size[0] * 1.2
            h = self.size[1] * 1.2

            pygame.draw.rect(win, (255, 0, 0), (x, y, w, h), border_radius=3)

        # draw image
        x, y = self.pos
        win.blit(self.image, (x, y))

    def check(self, pos) -> bool:
        return self.rect.collidepoint(pos)


class Menu:
    size = (SIDEBAR_WIDTH, HEIGHT)

    def __init__(self):
        self.surf = pygame.Surface(Menu.size, pygame.SRCALPHA)
        self.surf.fill((34, 32, 52))
        self.buttons = []
        self.turrets = tower_list
        self.selection = 0
        gap = int(Menu.size[1] * 0.8 // len(tower_list))

        max_y = int(Menu.size[1] * 0.80)
        base_y = Menu.size[1] * 0.20
        x = Menu.size[0] * 0.20
        for turret, y in zip(tower_list, range(0, max_y, gap)):

            y += base_y
            self.buttons.append(Button((x, y), turret.base_image))

        self.buttons[0].clicked = True

    def update(self, win):
        win.blit(self.surf, (0, 0))
        for i in self.buttons:
            i.draw(win)

        if not mouse.is_clicked(0):
            return

        mouse_upadate = mouse.get_pos()
        if mouse_upadate["zone"] != "SIDEBAR": # check for mouse pos
            return

        pos = mouse_upadate["value"]

        for index, i in enumerate(self.buttons):
            i.clicked = False

            if i.check(pos):
                self.selection = index

        self.buttons[self.selection].clicked = True
