import json
from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame  # import after disabling prompt
from conts import WIDTH, HEIGHT, TILE_SIZE


tile_map = {
    "b": "./assets/base_tile.png",
    "r": "./assets/right_arrow.png",
    "l": "./assets/left_arrow.png",
    "u": "./assets/up_arrow.png",
    "d": "./assets/down_arrow.png",
    "lt": "./assets/left_turn.png",
    "rt": "./assets/right_turn.png",
}

""" u
  l # r
    d
"""


def get_angle(level, point):
    x, y = point
    angle = 0
    if x > 0 and level[y][x - 1] == "r":
        angle = 270
    if x < len(level[0]) - 1 and level[y][x + 1] == "l":
        angle = 90
    if y > 0 and level[y - 1][x] == "d":
        angle = 180
    if y < len(level) - 1 and level[y + 1][x] == "u":
        angle = 0
    return angle


def convet_turn(level, point, direction):
    d_angle = get_angle(level, point)

    dir_to_angle = {
        "r": 0,
        "d": 270,
        "l": 180,
        "u": 90,
    }

    angle_to_dir = dict(zip(dir_to_angle.values(), dir_to_angle.keys()))

    cur_angle = dir_to_angle[direction[0]]

    new_angle = cur_angle + d_angle

    return angle_to_dir[new_angle % 360]


def get_next(level, point):
    x, y = point
    direction = level[y][x]

    if "t" in direction:
        direction = convet_turn(level, point, direction)

    if direction[0] == "u":
        if y > 0:
            return (x, y - 1)

    if direction[0] == "d":
        if y < len(level) - 1:
            return (x, y + 1)

    if direction[0] == "r":
        if x < len(level[0]) - 1:
            return (x + 1, y)

    if direction[0] == "l":
        if x > 0:
            return (x - 1, y)


def find_path(level, start):
    path = [start]

    while True:
        if path[-1] is None:
            return [
                ((i[0] + 0.5) * TILE_SIZE, (i[1] + 0.5) * TILE_SIZE) for i in path[:-1]
            ]
        path.append(get_next(level, path[-1]))


def make(level, path, playable_zone):
    # set up pygame
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))

    keys = tile_map.keys()
    for y, row in enumerate(level):
        for x, i in enumerate(row):
            if "t" in i:
                angle = get_angle(level, (x, y))

                img = pygame.image.load(tile_map[i])
                img = pygame.transform.rotate(img, angle)

            elif i in keys:
                img = pygame.image.load(tile_map[i])
            else:
                img = pygame.image.load(tile_map["b"])

            img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
            win.blit(img, (x * TILE_SIZE, y * TILE_SIZE))

    # pygame.draw.lines(win, YELLOW, False, path, 2)
    pygame.image.save(win, "./level/background.png")

    with open("./level/path.json", "w") as file:
        grid = [
            (int((i[0] / TILE_SIZE) - 0.5) - 1, int((i[1] / TILE_SIZE) - 0.5) - 1)
            for i in path[:-1]
        ]
        data = {"cords": path, "grid": grid, "zone": playable_zone}
        json.dump(data, file, indent=4)


def get_playable_zone(level):
    zone = []
    for i, row in enumerate(level):
        for j, value in enumerate(row):
            if value == "b":
                zone.append((i, j))

    boxes = []
    for y, x in zone:
        top_left = (x * TILE_SIZE, y * TILE_SIZE)
        bottem_right = (TILE_SIZE, TILE_SIZE)
        boxes.append((top_left, bottem_right))

    return boxes


if __name__ == "__main__":
    level = [
        ["b", "b", "b", "b", "b", "b", "b"],
        ["rt", "r", "rt", "b", "rt", "r", "r"],
        ["u", "b", "d", "b", "u", "b", "b"],
        ["u", "b", "d", "b", "u", "b", "b"],
        ["u", "b", "lt", "r", "lt", "b", "b"],
        ["u", "b", "b", "b", "b", "b", "b"],
    ]

    playable_zone = get_playable_zone(level)
    start_pos = (0, 5)
    path = find_path(level, start_pos)
    make(level, path, playable_zone)
