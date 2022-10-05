from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame  # import after disabling prompt
from conts import *
from enemy import Enemy
from turret import Turret





def main():
    baground = pygame.image.load("./background.png")
    # set up pygame
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # set up game eg payers

    # game loop
    enemys = [Enemy()]
    turrerts = [Turret((4.5*TILE_SIZE,3.5*TILE_SIZE))]
    bulets = []
    run = True

    while run:
        

        win.blit(baground, (0,0))

        dead = []
        for i in enemys:
            if not i.dead:
                # pygame.draw.rect(win, YELLOW, i.body)
                pygame.draw.circle(win,BLUE, i.move(), i.size/2)
            else:
                dead.append(i)

        for i in dead:
            enemys.remove(i)



        for i in turrerts:
            pygame.draw.circle(win,(BLACK), i.pos, 30)
            if (val := i.update(enemys)):
                bulets.append(val)

        dead = []
        for i in bulets:
            pygame.draw.circle(win,(RED), i.move(), 5)
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
        clock.tick(60)

    exit()


if __name__ == '__main__':
    main()
