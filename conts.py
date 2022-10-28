from load import path
import pygame

"""
 zones
 MAIN: (SIDEBAR_WIDTH,0) -- (WIDTH, HEIGHT)

 SIDEBAR: (0,0) -- (SIDEBAR_WIDTH, HEIGHT)

"""
PLAYABLE_ZONES = path.get_zone()

# fonts
pygame.font.init()
MENU_FONT = pygame.font.SysFont("ariali", 40)
MENU_FONT.set_italic(True)

# constants
WIDTH, HEIGHT = 832, 624
TILE_SIZE = 104
SIDEBAR_WIDTH = 104
FPS = 60


# colours
DAT_COLOUR = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
MAGENTA = (255, 0, 255)
LIME = (0, 255, 0)
CYAN = (0, 255, 255)
SILVER = (192, 192, 192)
GRAY = (128, 128, 128)
MAROON = (128, 0, 0)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
TEAL = (0, 128, 128)
NAVY = (0, 0, 128)
