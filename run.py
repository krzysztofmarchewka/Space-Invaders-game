import pygame
import sys
from starship import StarShip
from enemy import Enemy


class Game(object):
    def __init__(self):
        self.fps_max = 100.0

        pygame.init()
        pygame.font.init()
        pygame.display.set_caption('Space invaders')
        self.screen = pygame.display.set_mode((1280, 900))
        self.fps_clock = pygame.time.Clock()
        self.fps_delta = 0.0

        bg_surface = pygame.image.load('assets/space_bg.jpg')
        self.ship_surface = pygame.image.load('assets/starship2.png')
        self.lives_left = pygame.image.load('assets/lives.png')

        self.enemy_surface = pygame.image.load('assets/enemy.png')
        self.explosion_surface = pygame.image.load('assets/explosion.png')
        self.laser_surface = pygame.image.load('assets/laser.png')
        self.bullet_surface = pygame.image.load('assets/bullet.png')

        self.player = StarShip(self)
        self.enemy = Enemy(self)
        self.level = 1
        self.lives = 5

        self.score = 0
        myfont = pygame.font.SysFont('Comic Sans MS', 26)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            self.fps_delta += self.fps_clock.tick()/1000.0
            while self.fps_delta > 1/self.fps_max:
                self.tick()
                self.fps_delta -= 1/self.fps_max

            if self.enemy.enemy_position.y == 900:
                self.lives -= 1

            self.score_surface = myfont.render(
                f'Your score: {self.score}', False, (255, 255, 255))
            self.lives_number = myfont.render(
                f'Lives left: {self.lives}', False, (255, 255, 255))

            self.screen.blit(bg_surface, (0, 0))
            self.screen.blit(self.score_surface, (1050, 850))
            self.screen.blit(self.lives_number, (50, 850))
            self.draw()
            pygame.display.update()

    def tick(self):
        self.player.tick()

    def draw(self):
        self.player.draw()
        self.enemy.generate_enemy()


if __name__ == "__main__":
    Game()
