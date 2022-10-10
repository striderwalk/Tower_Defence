import pygame
import glob, os
from conts import TILE_SIZE

DEFULT_SIZE = (TILE_SIZE, TILE_SIZE)

def get_image(path, size=DEFULT_SIZE):
    if type(size) in [float, int]:
        size = (size, size)
    if not os.path.exists(path):
        print("ERROR: image path not found")
        print(path)
        path = "./assests/fail.png"
    image = pygame.image.load(path)
    image = pygame.transform.scale(image, size)
    pygame.Surface.convert_alpha(image)
        
    return image


def get_images(dir, size=DEFULT_SIZE):

    for path in glob.glob(f"{dir}/*.png"):
        yield get_image(path, size)

