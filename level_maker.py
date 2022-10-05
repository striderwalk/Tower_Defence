import json
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

""" u
  l # r
    d
"""

def get_angle(level, point):
    x, y = point
    angle = 0
    if x > 0 and level[y][x-1] == "r":
        angle = 270
    if x < len(level[0])-1 and level[y][x+1] == "l":
        angle = 90
    if y > 0 and level[y-1][x] == "d":
        angle = 180
    if y < len(level)-1 and level[y+1][x] == "u":
        angle = 0
    return angle

def convet_turn(level, point, direction):
    d_angle = get_angle(level, point)

    dir_to_angle = {
        "r" : 0,
        "d" : 270,
        "l" : 180,
        "u" : 90,
    }

    angle_to_dir = dict(zip(dir_to_angle.values(), dir_to_angle.keys()))

    cur_angle = dir_to_angle[direction[0]]

    new_angle = cur_angle + d_angle

    return angle_to_dir[new_angle%360]



def get_next(level, point):
    x, y = point
    direction = level[y][x]


    if "t" in direction:
        direction = convet_turn(level, point, direction)

    if direction[0] == "u":
        if y > 0 :
            return (x, y-1)

    if direction[0] == "d":
        if y < len(level)-1:
            return (x, y+1)


    if direction[0] == "r":
        if x < len(level[0])-1:
            return (x+1, y)

    if direction[0] == "l":
        if x > 0:
            return (x-1, y)




def find_path(level, start):
    path = [start]

    while True:
        if path[-1] is None:
            return [((i[0]+0.5)*TILE_SIZE,(i[1]+0.5)*TILE_SIZE) for i in path[:-1]]
        path.append(get_next(level,path[-1]))



def make(level, path):
    # set up pygame
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    keys = tile_map.keys()
    for y, row in enumerate(level):
        for x, i in enumerate(row):
            if "t" in i:
                angle = get_angle(level, (x,y))

                img = pygame.image.load(tile_map[i])
                img = pygame.transform.rotate(img, angle)


            elif i in keys:
                img = pygame.image.load(tile_map[i])
            else:
                img = pygame.image.load(tile_map["b"])

            img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
            win.blit(img, (x*TILE_SIZE,y*TILE_SIZE))

    # pygame.draw.lines(win, YELLOW, False, path, 2)
    pygame.image.save(win, "./background.png")

    with open("path.json", "w") as file:
        json.dump(path, file)


if __name__ == '__main__':
    level = [
["b", "b", "b", "b", "b", "b", "b","b"], 
["b", "rt", "r", "rt", "b", "rt", "r","r"], 
["b", "u", "b", "d", "b", "u", "b","b"], 
["b", "u", "b", "d", "b", "u", "b","b"], 
["b", "u", "b", "lt", "r", "lt", "b","b"],
["b", "u", "b", "b", "b", "b", "b","b"],]
    
    path = find_path(level, (1,5))
    make(level, path)