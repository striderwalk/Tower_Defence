import pygame
import glob
import os
from conts import TILE_SIZE

DEFULT_SIZE = (TILE_SIZE, TILE_SIZE)


def get_image(path, size=DEFULT_SIZE, rotate=0, unalt=False):
    if type(size) in [float, int]:
        size = (size, size)
    if not os.path.exists(path):
        print("ERROR: image path not found")
        print(path)
        path = "./assets/fail.png"
    image = pygame.image.load(path)
    pygame.Surface.convert_alpha(image)
    if unalt:
        return image
    image = pygame.transform.scale(image, size)
    if rotate != 0:
        image = pygame.transform.rotozoom(image, rotate, 1)

    return image


def get_images(dir, size=DEFULT_SIZE):

    for path in glob.glob(f"{dir}/*.png"):
        yield get_image(path, size)
