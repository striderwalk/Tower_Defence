from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame  # import after disabling prompt
from conts import *


tile_map = {
    "b": "./assests/base_tile.png",
    "r": "./assests/right_arrow.png",
    "l": "./assests/left_arrow.png",
    "u": "./assests/up_arrow.png",
    "d" : "./assests/down_arrow.png",
    "lt": "./assests/left_turn.png",
    "rt": "./assests/right_turn.png",
}


def make(level):
    # set up pygame
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    keys = tile_map.keys()
    for y, row in enumerate(level):
        for x, i in enumerate(row):
            if "t" in i:
                angle = 0
                if x > 0 and level[y][x-1] == "r":
                    angle = 270
                if x < len(row)-1 and level[y][x+1] == "l":
                    angle = 90
                if y > 0 and level[y-1][x] == "d":
                    angle = 180
                if y < len(row)-1 and level[y+1][x] == "u":
                    angle = 0

                img = pygame.image.load(tile_map[i])
                img = pygame.transform.rotate(img, angle)


            elif i in keys:
                img = pygame.image.load(tile_map[i])
            else:
                img = pygame.image.load(tile_map["b"])

            img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
            win.blit(img, (x*TILE_SIZE,y*TILE_SIZE))



    run = True
    while run:

        # update screen
        pygame.display.flip()
        # win.fill(WHITE)

        # check for input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        clock.tick(60)

    exit()


if __name__ == '__main__':

    make([
["b", "b", "b", "b", "b", "b", "b","b"], 
["b", "rt", "r", "rt", "b", "rt", "r","r"], 
["b", "u", "b", "d", "b", "u", "b","b"], 
["b", "u", "b", "d", "b", "u", "b","b"], 
["b", "u", "b", "lt", "r", "lt", "b","b"],
["b", "u", "b", "b", "b", "b", "b","b"],] )
