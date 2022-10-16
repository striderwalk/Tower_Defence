import pygame
import pygame.gfxdraw
from conts import WIDTH, HEIGHT
import math
import numpy as np
import make_layers


def get(health):
    img = make_layers.make(
        "./assests/healthbar/healthbar.png",
        "./assests/healthbar/healthbar.json",
        1,
        (health, 100),
    )
    img.convert()
    img.set_alpha(255)
    img.set_colorkey((0, 0, 0, 255))
    return img
