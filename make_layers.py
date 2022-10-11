import pygame
from load import image
from PIL import Image
import json


def make(img_path, data_path, swipe_layer=-1, swipe_size=None):
    if swipe_layer != -1:
        if swipe_size is None:
            raise ValueError("No swipe_size give")
        elif type(swipe_size) not in [int, float] and len(swipe_size) != 2:
            raise ValueError("No swipe_size should be (0 <= w < 1 , 0 <= h < 1)")
    swipe_size = swipe_size[0] * 222 + 13, swipe_size[1]

    ## get data ##
    with open(data_path, "r") as file:
        data = json.load(file)
    total_size = data["meta"]["size"]
    total_size = (total_size["w"], total_size["h"])
    frames = data["frames"]
    
    # load sprite sheet
    surf = image.get_image(img_path, total_size)
    draw_surf = None
    cur_y = 0

    layers = []
    for index, i in enumerate(frames):
        frame = frames[i]
        size = frame["spriteSourceSize"]
        if draw_surf is None: ## set up surface
            draw_surf = pygame.Surface((size["w"], size["h"]))
            draw_surf.set_alpha(0)

        if swipe_layer != index:
            section = surf.subsurface((0,cur_y, size["w"], size["h"]))
        else:

            section = surf.subsurface((0,cur_y, *swipe_size))
        


        layers.append(section)
        cur_y += size["h"]

    for i in layers:
        draw_surf.blit(i, (0,0))



    return draw_surf

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_mode((0,0), pygame.HIDDEN)
    img = make("./assests/healthbar/main.png", "./assests/healthbar/main.json", 1, (100, 100))

