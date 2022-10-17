import pygame


def rot_center(surf, image, angle):
    # https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame#:~:text=at%2012%3A43-,rabbid76,-188k2525%20gold%20badges109109
    """rotate a Surface, maintaining position."""

    rotated_image = pygame.transform.rotozoom(image, angle, 1)
    new_rect = rotated_image.get_rect(center=image.get_rect().center)

    surf.blit(rotated_image, new_rect)
    return surf
