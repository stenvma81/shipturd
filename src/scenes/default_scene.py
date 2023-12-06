import pygame
import random
import sys
import utils.colors as colors
import settings
from game_objects.controllers.player_controller import PlayerController

def default_scene(screen):
    WIDTH, HEIGHT = settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT
    PLAYER_SIZE = 40
    ENEMY_SIZE = 40
    ENEMY_SPEED = 1
    FPS = settings.FPS

    WHITE = colors.WHITE
    RED = colors.RED

    player_x = WIDTH // 2 - PLAYER_SIZE // 2
    player_y = HEIGHT // 2 - PLAYER_SIZE // 2

    enemy_x = random.randint(0, WIDTH - ENEMY_SIZE)
    enemy_y = random.randint(0, HEIGHT - ENEMY_SIZE)

    game_over = False

    clock = pygame.time.Clock()

    player_controller = PlayerController(player_x, player_y)

    def player(x, y, screen):
        pygame.draw.rect(screen, WHITE, (x, y, PLAYER_SIZE, PLAYER_SIZE))

    def enemy(x, y, screen):
        pygame.draw.rect(screen, RED, (x, y, ENEMY_SIZE, ENEMY_SIZE))

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        
        player_controller.handle_input(keys)

        player_controller.apply_friction()

        player_controller.move_player()

        player_x, player_y = player_controller.get_position()

        player_x = max(0, min(WIDTH - PLAYER_SIZE, player_x))
        player_y = max(0, min(HEIGHT - PLAYER_SIZE, player_y))

        if enemy_x < player_x:
            enemy_x += ENEMY_SPEED
        elif enemy_x > player_x:
            enemy_x -= ENEMY_SPEED

        if enemy_y < player_y:
            enemy_y += ENEMY_SPEED
        elif enemy_y > player_y:
            enemy_y -= ENEMY_SPEED

        if player_x < enemy_x + ENEMY_SIZE and player_x + PLAYER_SIZE > enemy_x and player_y < enemy_y + ENEMY_SIZE and player_y + PLAYER_SIZE > enemy_y:
            game_over = True

        screen.fill((0, 0, 0))

        player(player_x, player_y, screen)
        enemy(enemy_x, enemy_y, screen)

        pygame.display.update()

        clock.tick(FPS)
