import pygame
from player import Player
import enemys
import towers
import shots
import menu


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
        self.enemys, dead_count = enemys.update(surf, self.enemys, self.player)
        self.turrets, new_bullets = towers.update(surf, self.turrets, self.enemys)
        self.bullets.extend(new_bullets)
        self.bullets = shots.update(surf, self.bullets, self.enemys)

        # update player
        self.player.update(dead_count)
        menu.draw(surf, self.player)

        if self.player.dead:
            return {"surf": surf, "dead": True}

        return {"surf": surf, "dead": False}

    def add_enemy(self):
        self.enemys.append(enemys.Enemy())
