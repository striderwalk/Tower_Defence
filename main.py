import itertools
import sys
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame  # import after disabling prompt

import mouse
from turret_menu import Menu
from death_screen import death
from game import Game
from conts import WIDTH, HEIGHT, FPS, WHITE, SIDEBAR_WIDTH

############# TODO ###########
## add money / buying stuff ##
## placing code URGENT      ##
##    - location checker    ##
##      - general valid pos ##
##      - specific for type ##
## death screen -improve    ##
## fix mine animation       ##
## spell assests right      ##
## make turret rot smoother ##
##############################

f = pygame.font.init()
f = pygame.font.SysFont("ariali", 60)


def main():

    # set up pygame
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    surf = pygame.Surface((WIDTH - SIDEBAR_WIDTH, HEIGHT))
    pygame.display.set_caption("Tower Defence")
    clock = pygame.time.Clock()

    # set up game eg payers
    game = Game()
    side_bar = Menu()

    # game loop
    run = True

    counter = itertools.count()
    for frame in counter:
        if len(game.enemys) <= 10:
            if frame % 120 == 0:
                game.add_enemy()
        dat = game.update(surf.copy())
        draw_surf = dat["surf"]

        # draw screen
        win.blit(draw_surf, (SIDEBAR_WIDTH, 0))
        side_bar.update(win)

        # handle the losing event
        if dat["dead"] == True:
            death(win, clock)
            sys.exit()

        if not run:
            break

        # check for input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = mouse.get_pos()
                    if click["zone"] != "MAIN":
                        continue
                    pos = click["value"]
                    enemy_type = side_bar.turrets[side_bar.selection]
                    enemy = enemy_type(pos)
                    game.turrets.append(enemy)

        # update pygame
        clock.tick(FPS)
        pygame.display.flip()
        win.fill(WHITE)

    pygame.quit()
    exit()


if __name__ == "__main__":
    main()
