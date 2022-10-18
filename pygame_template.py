import pygame
from block import *
from sprite import *
from maps import *

WIDTH = 1600
HEIGHT = 832
FPS = 60


class MorningRay:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('MorningRay')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.test_group = pygame.sprite.Group()

        self.player = Hero(self)
        self.all_sprites.add(self.player)

        self.map_ = maps[0]

        self.gravity_v = 2

        self.bg = pygame.image.load("img\\bg.jpg")

        self.click = 0
        self.hp = 5

        self.isJump = False
        self.run = True

        # Generating the map
        for y1 in range(13):
            for x1 in range(25):
                if self.map_[y1][x1] == 2:
                    brick = Wall(x1 * 64, y1 * 64)
                    self.test_group.add(brick)

                elif self.map_[y1][x1] == 1:
                    floor = Floor(x1 * 64, y1 * 64)
                    self.test_group.add(floor)

    def main_loop(self):
        while self.run:
            self.clock.tick(FPS)
            self.screen.blit(self.bg, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                # Проверяем нажатые кнопки
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.run = False

            self.player.move()

            self.all_sprites.update()
            self.test_group.update()

            self.all_sprites.draw(self.screen)
            self.test_group.draw(self.screen)

            pygame.display.flip()
            pygame.display.update()

    @staticmethod
    def clean_up():
        pygame.quit()


if __name__ == '__main__':
    game = MorningRay()
    game.main_loop()
    game.clean_up()
