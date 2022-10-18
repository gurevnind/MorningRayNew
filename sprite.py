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

        # self.image.fill(pygame.Color(255, 255, 255))

        self.speed = 5
        self.g_v = 0.12

        self.pos = vec(20, 832 - 64)
        self.acc = vec(0, 0)
        self.vel = vec(0, 0)

        self.jumps = 0

        self.is_moving = False

    def check_collision(self):
        self.rect.move_ip(self.vel)

        hits = pygame.sprite.spritecollide(self, self.game.test_group, False)

        if hits:
            self.rect.move_ip(-self.vel)

        return hits

    def update(self):
        collision_type = {
            'top': False, 'bottom': False, 'right': False, 'left': False
        }

        self.vel = vec(0, self.vel.y)

        pressed_keys = pygame.key.get_pressed()

        # LEFT RIGHT MOVE
        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            self.vel.x = -self.speed

        if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            self.vel.x = self.speed

        self.rect.move(self.vel.x, 0)

        collisions = self.check_collision()

        # LEFT RIGHT COLLISION
        for block in collisions:
            if self.vel.x > 0:
                self.rect.right = block.rect.left
                collision_type['right'] = True

            elif self.vel.x < 0:
                self.rect.left = block.rect.right
                collision_type['left'] = True

        if collision_type['right'] or collision_type['left']:
            self.vel.x = 0

        # JUMP MOVE
        if pressed_keys[pygame.K_SPACE]:
            self.jump()

        self.rect.move(0, self.vel.y)

        collisions = self.check_collision()

        # JUMP COLLISION
        for block in collisions:
            if self.vel.y > 0:
                self.rect.bottom = block.rect.top
                collision_type['bottom'] = True

                self.jumps = 0

            elif self.vel.y < 0:
                self.rect.top = block.rect.bottom
                collision_type['top'] = True

                self.jumps = 0

        if collision_type['top'] or collision_type['bottom']:
            self.vel.y = 0

        self.vel.y += self.g_v
        self.rect.move(0, self.vel.y)

    def jump(self):
        if self.jumps < 2:
            self.vel.y = -6
            self.jumps += 1

    def move(self):
        pass
