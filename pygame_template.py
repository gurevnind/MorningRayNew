import pygame
from block import *
from sprite import *
from maps import *
WIDTH = 1600
HEIGHT = 832
FPS = 60
bg = pygame.image.load("img\\bg.jpg")
klick = 0
hp = 5
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('MorningRay')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
test_group = pygame.sprite.Group()
player = Hero()
all_sprites.add(player)
map = maps[0]
gravity_v = 2

for y1 in range(13):
    for x1 in range(25):
        if map[y1][x1] == 2:
            brick = pygame.sprite.Sprite()
            brick.image = pygame.Surface((64, 64), pygame.SRCALPHA)  #
            brick.image = pygame.image.load("img\\object.JPG")
            brick.rect = brick.image.get_rect()
            brick.rect.topleft = (x1 * 64, y1 * 64)
            test_group.add(brick)
        elif map[y1][x1] == 1:
            floor = pygame.sprite.Sprite()
            floor.image = pygame.Surface((64, 64), pygame.SRCALPHA)  #
            floor.image = pygame.image.load("img\\floor.JPG")
            floor.rect = floor.image.get_rect()
            floor.rect.topleft = (x1 * 64, y1 * 64)
            test_group.add(floor)

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
            player.jump = -17
            player.is_moving = False
            klick += 1

        if event.type == pygame.KEYUP and  event.key != pygame.K_SPACE:
            player.stop_player(event.key)

    for brick in test_group:
        screen.blit(brick.image, brick.rect)

    old_player = player.rect.copy()
    gravity_v = 2
    player.move()
    if not isJump:
        if player.is_moving and player.rect.colliderect(brick) == False:
            player.move()
        elif player.is_moving and player.rect.colliderect(brick):
            player.stop_player()
    else:
        # print(player.rect.y)
        # min_y = [player.rect.y - brick.rect.y for brick in test_group]
        # min_y = [x for x in min_y if x < 0]
        # min_y = max(min_y)
                if player.rect.colliderect(brick) == False:
                    player.rect.y = player.rect.y + player.jump
                    player.jump = player.jump + 1.5
                    if player.jump == 0:
                        player.jump += 1
                    print(player.jump, player.rect.y )
                else:
                    isJump = False
                    player.jump = 0
                    klick = 0
                    player.stop_player()




    for brick in test_group:
        if player.rect.colliderect(brick):
            print("COLLISION")
            player.rect = old_player
            gravity_v = 0

    player.rect.y += gravity_v
    all_sprites.update()
    test_group.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.display.update()









