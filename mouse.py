import pygame
from load import path, image
from conts import WIDTH, HEIGHT, SIDEBAR_WIDTH



def get_pos() -> dict:
    ## check pos of click ##
    pos = pygame.mouse.get_pos()

    if pos[0] < SIDEBAR_WIDTH: ## check if over sidebar
        return {"type" : "pos", "zone" : "SIDEBAR", "value" : pos}

    return {"type" : "pos", "zone" : "MAIN", "value" : pos}

def is_clicked(button) -> bool:
    return pygame.mouse.get_pressed()[button]







