import pygame
from block import *
from sprite import *
WIDTH = 1550
HEIGHT = 820
FPS = 60
bg = pygame.image.load("img\\bg.jpg")
klick = 0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('MorningRay')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Hero()
floor = Floor()
all_sprites.add(player)
all_sprites.add(floor)







isJump = False
run = True
while run:

    clock.tick(FPS)
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Проверяем нажатые кнопки
        if event.type == pygame.KEYDOWN and event.key != pygame.K_SPACE:
            player.move_player(event.key)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and klick < 2:
            isJump = True
            player.jump = -15
            player.is_moving = False
            klick += 1




        if event.type == pygame.KEYUP and  event.key != pygame.K_SPACE:
            player.stop_player(event.key)

    player.move()

    if player.is_moving:
        player.move()

    elif isJump:
        print(player.rect.y)
        if player.rect.y <= 650:
            player.rect.y = player.rect.y + player.jump
            player.jump = player.jump + 1
            if player.jump == 0:
                player.jump += 1
            print(player.jump, player.rect.y )
        else:
            isJump = False
            player.jump = 0
            player.rect.y = 650
            klick = 0


    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

    pygame.display.update()









