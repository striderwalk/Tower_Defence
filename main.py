import itertools
from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame  # import after disabling prompt
from conts import WIDTH, HEIGHT, FPS, WHITE
import enemys
import towers
import shots
import health_bar
from turret_menu import Menu
from death_screen import death

############# TODO ###########
## add money / buying stuff ##
## placeing code            ##
## death screen             ##
## fix turret shooting      ##
## centrel mouse thing      ##
## fix mine animation       ##
##############################

f = pygame.font.init()
f = pygame.font.SysFont("ariali", 60)


def main():
    baground = pygame.image.load("./level/background.png")
    # set up pygame
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tower Defense")
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

        if not run:
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
