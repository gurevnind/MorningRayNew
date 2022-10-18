import pygame
import numpy as np

WIDTH = 1600
HEIGHT = 832

wd = 64
hg = 64


class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x, self.y = x, y
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((wd, hg))
        self.image = pygame.image.load("img\\floor.JPG")

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

        self.rect.topleft = (self.x, self.y)


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x, self.y = x, y
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((64, 64))
        self.image = pygame.image.load("img\\object.JPG")

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
