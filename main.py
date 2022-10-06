import json
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame  # import after disabling prompt
from conts import *
from enemys import Enemy
from towers import Turret, Mine_Shooter



def get_points():
    with open("./path.json") as file:
        points = json.load(file)
    return points


def main():
    baground = pygame.image.load("./background.png")
    # set up pygame
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # set up game eg payers

    # game loop
    enemys = [Enemy()]
 
    turrerts = [Turret((4.5*TILE_SIZE,5.5*TILE_SIZE)),Mine_Shooter((4.5*TILE_SIZE,3.5*TILE_SIZE), get_points())]

    bulets = []
    run = True
    pygame.mixer.music.load("./ExplosionSFX.wav")
    # pygame.mixer.music.play(-1)
    while run:
        if all([i.dead for i in enemys]):
            enemys = [Enemy()]


        win.blit(baground, (0,0))

        dead = []
        for i in enemys:
            if not i.dead:
                i.draw(win)
            else:
                dead.append(i)

        for i in dead:
            enemys.remove(i)



        for i in turrerts:
            i.draw(win)
            if (val := i.update(enemys)):
                bulets.append(val)

        dead = []
        for i in bulets:
            if i.dead:
                dead.append(i)
                continue
            i.draw(win)
            if i.update(enemys) == "die":
                dead.append(i)

        for i in dead:
            dead.remove(i)  


        # update screen
        pygame.display.flip()
        win.fill(WHITE)

        # check for input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        clock.tick(FPS)

    exit()


if __name__ == '__main__':
    main()
