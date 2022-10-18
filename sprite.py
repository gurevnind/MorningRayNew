import pygame
from block import *

WIDTH = 1550
HEIGHT = 820
vec = pygame.math.Vector2


class Hero(pygame.sprite.Sprite):
    def __init__(self, _game):
        pygame.sprite.Sprite.__init__(self)
        self.scale_f = 3
        self.i_x = 180 * self.scale_f
        self.i_y = 104 * self.scale_f

        self.game = _game

        self.image = pygame.image.load("img\\hero.png")
        self.image = pygame.transform.scale(self.image, (64, 64))

        self.rect = pygame.Rect(0, 0, 64, 64)
        self.rect.bottomleft = (20, 832 - 64)

        self.image.fill(pygame.Color(255, 255, 255))

        self.pos = vec(20, 832 - 64)
        self.acc = vec(0, 0)
        self.vel = vec(0, 0)

        self.speed = 0.5
        self.g_v = -0.12

        self.jumps = 0

        self.is_moving = False

    def check_collision(self):
        self.rect.move_ip(self.vel)

        hits = pygame.sprite.spritecollideany(self, self.game.test_group)

        if hits:
            self.rect.move_ip(-self.vel)

        return hits

    def update(self):
        ground = self.check_collision()

        if ground:
            self.rect.move(-self.vel)
            self.pos = self.rect.midbottom
            self.vel.y = 0
            self.jumps = 0

    def jump(self):
        print(self.jumps)
        if self.jumps < 2:
            self.vel.y = -12
            self.jumps += 1

    def move(self):
        self.acc = vec(0, 0.5)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            self.acc.x = -self.speed

        elif pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            self.acc.x = self.speed

        self.acc.x += self.vel.x * self.g_v
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos
