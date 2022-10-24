import pygame
import make_layers
from conts import DAT_COLOUR

pygame.init()


def find_colour(image: pygame.Surface, colour: tuple[int]):
    # find coordinate of first pixel of colour

    for i in range(image.get_width()):
        for j in range(image.get_height()):
            c_rgba = tuple(image.get_at((i, j)))
            c_rgb = c_rgba[:3]
            if c_rgb == colour:
                return (i, j)
    return False


font = pygame.font.SysFont("ariali", 40)
font.set_italic(True)


def make(score):
    images, size = make_layers.make(
        "./assests/scoreboard/scoreboard.png", "./assests/scoreboard/scoreboard.json"
    )

    cords = find_colour(images["scoreboard (dat).aseprite"], DAT_COLOUR)
    surf = pygame.Surface(size, pygame.SRCALPHA)
    for name, image in images.items():
        if name == "scoreboard (dat).aseprite":
            image = pygame.Surface(size, pygame.SRCALPHA)
            text = font.render(f"SCORE {score}", False, (251, 241, 54))
            image.blit(text, cords)

        surf.blit(image, (0, 0))

    return surf


def get(score):
    return make(score)


if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode((800, 800))  # pygame.SRCALPHA)
    imgs, size = make_layers.make(
        "./assests/scoreboard/scoreboard.png", "./assests/scoreboard/scoreboard.json"
    )
    c = 0
    while True:
        c += 1
        surf = make(c)
        win.blit(surf, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
