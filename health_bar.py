import pygame
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
