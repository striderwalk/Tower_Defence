import json
from os import environ
import itertools

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame  # import after disabling prompt
from conts import *
import enemys
import towers
import shots
from load import path, image
import health_bar


def main():
    baground = pygame.image.load("./level/background.png")
    # set up pygame
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # set up game eg payers

    # game loop
    active_enemys = [enemys.Enemy()]

    turrets = [
        #towers.Turret((4.5 * TILE_SIZE, 5.5 * TILE_SIZE)),
        towers.Mine_Shooter((2.5 * TILE_SIZE, 2.5 * TILE_SIZE), path.get_points()),
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
        health_bar.draw(win, health)
        if run == False:
            break
        # health -= 1
        print(health)
        # print(active_enemys, health)
        if len(active_enemys) <= 10:
            if frame % 120 == 0:
                active_enemys.append(enemys.Enemy())


        active_enemys, health = enemys.update(active_enemys,health, win)

        turrets, new_bullets = towers.update(turrets, active_enemys, win)
        bullets.extend(new_bullets)

        shots.update(bullets, active_enemys, win)

        # update screen
        pygame.display.flip()
        win.fill(WHITE)

        # check for input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        clock.tick(FPS)

    pygame.quit()
    exit()


if __name__ == "__main__":
    main()
