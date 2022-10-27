import json
import pygame

pygame.init()


def get_points():
    with open("./level/path.json") as file:
        points = json.load(file)
    return points["cords"]


def get_path():
    with open("./level/path.json") as file:
        points = json.load(file)
    return points["grid"]


def get_zone():
    with open("./level/path.json") as file:

        points = json.load(file)
    zones = points["zone"]

    zone_rects = []
    for i in zones:
        zone_rects.append(pygame.Rect(i))

    return zone_rects
