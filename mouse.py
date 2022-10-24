import pygame
from conts import SIDEBAR_WIDTH, PLAYABLE_ZONES


def check_placement(win, pos):
    # pos = (pos[0] - SIDEBAR_WIDTH, pos[1])

    for zone in PLAYABLE_ZONES:
        if zone.collidepoint(pos):
            # vaild placement
            return True

    # invaild placement
    return False


def get_pos() -> dict:
    # check mouse pos
    pos = pygame.mouse.get_pos()

    if pos[0] < SIDEBAR_WIDTH:  # check if over sidebar
        return {"type": "pos", "zone": "SIDEBAR", "value": pos}

    pos = pos[0] - SIDEBAR_WIDTH, pos[1]
    return {"type": "pos", "zone": "MAIN", "value": pos}


def is_clicked(button) -> bool:
    return pygame.mouse.get_pressed()[button]
