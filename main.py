import json
import itertools
from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame  # import after disabling prompt
from conts import *
import enemys
import towers
import shots
from load import path, image
import health_bar
from turret_menu import Menu

############# TODO ###########
## add money / buying stuff ##
## placeing code            ##
## death screen             ##
## fix turret shooting      ##
## centrel mouse thing      ##
##############################

f = pygame.font.init()
f = pygame.font.SysFont("ariali", 60)

def death(win, clock):
    dead_text = image.get_image("./assests/dead.png", (256 * 1.4, 96 * 1.4))
    x = WIDTH / 2 - dead_text.get_width() / 2
    max_y = HEIGHT / 2 - dead_text.get_height() / 2
    y = 0

    background = win.copy()
    background.set_alpha(150)

    while y <= max_y:
        y += 6
        win.blit(background, (0, 0))
        win.blit(dead_text, (x, y))


        # check for input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        pygame.display.update()
        win.fill((0, 0, 0))
        clock.tick(FPS)

    while True:
        # check for input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return


def main():
    baground = pygame.image.load("./level/background.png")
    # set up pygame
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # set up game eg payers

    # game loop
    active_enemys = [enemys.Enemy()]
    side_bar = Menu()

    turrets = [
        # towers.Turret((4.5 * TILE_SIZE, 5.5 * TILE_SIZE)),
        # towers.Mine_Shooter((2.5 * TILE_SIZE, 2.5 * TILE_SIZE)),
    ]

    bullets = []
    health = 100
    run = True
    pygame.mixer.music.set_volume(0)
    pygame.mixer.music.load("./assests/ExplosionSFX.wav")
    # pygame.mixer.music.play(-1)
    counter = itertools.count()
    for frame in counter:

        win.blit(baground, (0, 0))
        bar = health_bar.get(health / 100)
        win.blit(bar, (WIDTH - bar.get_width(), HEIGHT - bar.get_height()))
        side_bar.update(win)

        if run == False:
            break

        # print(active_enemys, health)
        if len(active_enemys) <= 10:
            if frame % 120 == 0:
                active_enemys.append(enemys.Enemy())

        active_enemys, health = enemys.update(active_enemys, health, win)

        turrets, new_bullets = towers.update(turrets, active_enemys, win)
        bullets.extend(new_bullets)

        shots.update(bullets, active_enemys, win)

        # update screen
        pygame.display.flip()
        if health <= 0:
            return death(win, clock)

        win.fill(WHITE)

        # check for input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                enemy = side_bar.turrets[side_bar.selection](pygame.mouse.get_pos())
                print(enemy)
                turrets.append(enemy)
        clock.tick(FPS)

    pygame.quit()
    exit()


if __name__ == "__main__":
    main()