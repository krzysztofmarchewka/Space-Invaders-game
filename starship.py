import pygame
import math
import random
from pygame.math import Vector2


class StarShip(object):
    def __init__(self, game):
        self.game = game
        self.speed = 1.3
        self.gravity = 0.5

        size = self.game.screen.get_size()

        self.position = Vector2(size[0]/2, 800)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

        # Bullet
        self.bullet_state = 'ready'
        self.bullet_speed = 2.0
        self.bullet_position = Vector2(self.position.x, self.position.y)

    def add_force(self, force):
        self.acc += force

    def shoot(self, x, y):
        self.bullet_state = "fire"
        self.game.screen.blit(
            self.game.laser_surface, (x + 32, y-20))
        if self.bullet_position.y <= 0:
            self.bullet_position.y = self.position.y
            self.bullet_state = "ready"

    def is_collision(self, enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt(math.pow((enemyX - bulletX), 2) +
                             math.pow((enemyY - bulletY), 2))
        if distance < 40:
            return True
        else:
            return False

    def tick(self):
        # input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.add_force(Vector2(0, -self.speed))
        if self.position.y <= 0:
            self.position.y = 0
        if pressed[pygame.K_DOWN]:
            self.add_force(Vector2(0, self.speed))
        if self.position.y >= 750:
            self.position.y = 750
        if pressed[pygame.K_LEFT]:
            self.add_force(Vector2(-self.speed, 0))
        if self.position.x <= 0:
            self.position.x = 0
        if pressed[pygame.K_RIGHT]:
            self.add_force(Vector2(self.speed, 0))
        if self.position.x >= 1180:
            self.position.x = 1180
        if pressed[pygame.K_SPACE]:
            if self.bullet_state is "ready":
                self.bullet_position.x = self.position.x
                self.shoot(self.bullet_position.x, self.bullet_position.y)
        # physics
        self.vel *= 0.8
        self.vel -= Vector2(0, -self.gravity)

        self.vel += self.acc
        self.position += self.vel
        self.acc *= 0

    def draw(self):
        if self.bullet_state is "fire":
            self.shoot(self.bullet_position.x, self.bullet_position.y)
            self.bullet_position.y -= self.bullet_speed

        collision = self.is_collision(self.game.enemy.enemy_position.x,
                                      self.game.enemy.enemy_position.y, self.bullet_position.x, self.bullet_position.y)
        if collision:
            self.bullet_position.y = self.position.y
            self.bullet_state = "ready"
            self.game.score += 1
            # self.game.screen.blit(self.game.explosion_surface, (
            #     self.game.enemy.enemy_position.x, self.game.enemy.enemy_position.y))
            self.game.enemy.enemy_position.x = random.randint(
                0, 1180)
            self.game.enemy.enemy_position.y = random.randint(50, 150)
        self.game.screen.blit(self.game.ship_surface,
                              (self.position.x, self.position.y))
