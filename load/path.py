import json

def get_points():
    with open("./level/path.json") as file:
        points = json.load(file)
    return points["cords"]

def get_path():
    with open("./level/path.json") as file:
        points = json.load(file)
    return points["grid"]
