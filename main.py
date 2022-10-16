import itertools
from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame  # import after disabling prompt
from conts import WIDTH, HEIGHT, FPS, WHITE, SIDEBAR_WIDTH


from turret_menu import Menu
from death_screen import death
import mouse
from game import Game

############# TODO ###########
## add money / buying stuff ##
## placeing code            ##
##    - location checker    ##
## death screen             ##
## fix mine animation       ##
##############################

f = pygame.font.init()
f = pygame.font.SysFont("ariali", 60)


def main():

    # set up pygame
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    surf = pygame.Surface((WIDTH-SIDEBAR_WIDTH, HEIGHT))
    pygame.display.set_caption("Tower Defense")
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
        draw_surf = game.update(surf.copy())
        win.blit(draw_surf, (SIDEBAR_WIDTH, 0))

        side_bar.update(win)

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

        ## update pygame ##
        clock.tick(FPS)
        pygame.display.flip()
        win.fill(WHITE)

    pygame.quit()
    exit()


if __name__ == "__main__":
    main()
