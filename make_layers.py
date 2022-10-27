import pygame
from load import image
import json

# TODO add order thing in return dat


def make(img_path, data_path):

    # get data
    with open(data_path, "r") as file:
        data = json.load(file)
    total_size = data["meta"]["size"]
    total_size = (total_size["w"], total_size["h"])
    frames = data["frames"]

    # load sprite sheet
    surf = image.get_image(img_path, unalt=True)
    cur_y = 0

    layers = {}
    for index, i in enumerate(frames):
        frame = frames[i]
        size = frame["spriteSourceSize"]
        section = surf.subsurface((0, cur_y, size["w"], size["h"]))
        layers[i] = section
        cur_y += size["h"]

    return layers, (size["w"], size["h"])


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.HIDDEN)
    img, size = make(
        "./assests/healthbar/healthbar.png", "./assests/healthbar/healthbar.json"
    )
