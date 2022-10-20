import pygame
import make_layers


def make_bar(images, size, health_percent=1, /, layer_name="main_bar"):

    layer_name = f"healthbar ({layer_name}).aseprite"
    if 0 > health_percent or health_percent > 1:
        raise ValueError(
            f"health_percent must be between 0 and 1 {health_percent=}")
    swipe_x = health_percent * 222 + 13

    # setup
    base_surface = pygame.Surface(size, pygame.SRCALPHA)

    for name, img in images.items():
        if name == layer_name:
            img = img.subsurface((0, 0, swipe_x, size[1]))

        base_surface.blit(img, (0, 0))

    return base_surface


def get(health_percent):
    images, size = make_layers.make(
        "./assests/healthbar/healthbar.png",
        "./assests/healthbar/healthbar.json",
    )

    img = make_bar(images, size, health_percent)

    img.convert()
    img.set_alpha(255)
    img.set_colorkey((0, 0, 0, 255))
    return img


if __name__ == '__main__':

    pygame.init()
    pygame.display.set_mode((0, 0), pygame.HIDDEN)
    get(10)
