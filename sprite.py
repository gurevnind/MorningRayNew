import pygame
import time

WIDTH = 1550
HEIGHT = 820

player_img = pygame.image.load("img\\hero.png")

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.scale_f = 0.6
        self.i_x = 99 * self.scale_f
        self.i_y = 104 * self.scale_f
        self.image = player_img
        self.image = pygame.transform.scale(self.image, (self.i_x, self.i_y))
        self.rect = self.image.get_rect()
        self.rect.center = (60, HEIGHT-150)
        self.d_left = 0
        self.d_right = 0
        self.d_down = 0
        self.gravity = 0
        self.jump = 0
        self.is_moving = False
        self.speed = 7

    def stop_player(self, _key):
        if _key == pygame.K_a:
            self.d_left = 0

        if _key == pygame.K_d:
            self.d_right = 0

        # if _key == pygame.K_SPACE:
        #     self.jump = 0

    def move(self):
         self.rect.x += self.d_right + self.d_left
         self.rect.y += self.jump


         if self.d_right + self.d_left != 0 and self.jump == 0:
            self.is_moving = True
         else:
              self.is_moving = False





    def move_player(self, _key):

        if _key == pygame.K_a:
            self.d_left = -1 * self.speed

        if _key == pygame.K_d:
            self.d_right = 1 * self.speed

        if _key == pygame.K_SPACE:
            self.jump = -15
            self.is_moving = False




player = Hero()


