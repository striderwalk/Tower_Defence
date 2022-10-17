import pygame
from player import Player
import enemys
import towers
import shots


class Game:
    def __init__(self):
        self.map = pygame.image.load("./level/background.png")
        self.turrets = []
        self.enemys = []
        self.bullets = []
        self.player = Player()

    def update(self, surf):
        surf.blit(self.map, (0, 0))

        # update game objects
        self.enemys = enemys.update(surf, self.enemys, self.player)
        self.turrets, new_bullets = towers.update(
            surf, self.turrets, self.enemys)
        self.bullets.extend(new_bullets)
        self.bullets = shots.update(surf, self.bullets, self.enemys)

        # update player
        self.player.update()
        self.player.draw(surf)

        if self.player.dead:
            return "dead"

        return surf

    def add_enemy(self):
        self.enemys.append(enemys.Enemy())
