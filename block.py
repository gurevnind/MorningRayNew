import pygame


WIDTH = 1550
HEIGHT = 820

wd = 1550
hg = 50


class Floor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((wd, hg))
        self.image = pygame.image.load("img\\floor.PNG")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 40)
