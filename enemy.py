import pygame
import random
from pygame.math import Vector2


class Enemy(object):
    def __init__(self, game):
        self.game = game
        self.gravity = 0.1
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

        self.enemies = []
        self.enemies_per_lvl = 5
        self.enemy_position = Vector2(random.randint(
            0, 1180), random.randint(50, 150))
        for i in range(self.enemies_per_lvl):
            self.enemies.append(self.enemy_position)

    def generate_enemy(self):

        self.game.screen.blit(self.game.enemy_surface,
                              (self.enemy_position.x, self.enemy_position.y))
        self.crash_course()

    def crash_course(self):
        # physics
        self.vel *= 0.1
        self.vel -= Vector2(0, -self.gravity)
        self.vel += self.acc
        self.enemy_position += self.vel
        self.acc *= 0
