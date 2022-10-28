import pygame
from conts import WIDTH, HEIGHT, FPS
from load import image


def death(win, clock):
    dead_text = image.get_image("./assets/dead.png", (256 * 1.4, 96 * 1.4))
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
