import pygame
import random
import sys
import utils.colors as colors
import settings

def default_scene(screen):
    WIDTH, HEIGHT = settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT
    PLAYER_SIZE = 40
    ENEMY_SIZE = 40
    PLAYER_SPEED = 2
    ACCELERATION = 0.2
    ENEMY_SPEED = 1
    FPS = settings.FPS

    # Colors
    WHITE = colors.WHITE
    RED = colors.RED

    # Player attributes
    player_x = WIDTH // 2 - PLAYER_SIZE // 2
    player_y = HEIGHT // 2 - PLAYER_SIZE // 2
    player_speed_x = 0
    player_speed_y = 0

    # Enemy attributes
    enemy_x = random.randint(0, WIDTH - ENEMY_SIZE)
    enemy_y = random.randint(0, HEIGHT - ENEMY_SIZE)

    # Game over flag
    game_over = False

    # Clock for controlling FPS
    clock = pygame.time.Clock()

    # Functions
    def player(x, y, screen):
        pygame.draw.rect(screen, WHITE, (x, y, PLAYER_SIZE, PLAYER_SIZE))

    def enemy(x, y, screen):
        pygame.draw.rect(screen, RED, (x, y, ENEMY_SIZE, ENEMY_SIZE))

    # Game loop
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_speed_x = -PLAYER_SPEED
        elif keys[pygame.K_RIGHT]:
                player_speed_x = PLAYER_SPEED
        else:
            player_speed_x = 0

        if keys[pygame.K_UP]:
            player_speed_y = -PLAYER_SPEED
        elif keys[pygame.K_DOWN]:
            player_speed_y = PLAYER_SPEED
        else:
            player_speed_y = 0

        player_x += player_speed_x
        player_y += player_speed_y

        # Keep player within the screen boundaries
        player_x = max(0, min(WIDTH - PLAYER_SIZE, player_x))
        player_y = max(0, min(HEIGHT - PLAYER_SIZE, player_y))

        # Enemy follows the player
        if enemy_x < player_x:
            enemy_x += ENEMY_SPEED
        elif enemy_x > player_x:
            enemy_x -= ENEMY_SPEED

        if enemy_y < player_y:
            enemy_y += ENEMY_SPEED
        elif enemy_y > player_y:
            enemy_y -= ENEMY_SPEED

        # Check for collision
        if player_x < enemy_x + ENEMY_SIZE and player_x + PLAYER_SIZE > enemy_x and player_y < enemy_y + ENEMY_SIZE and player_y + PLAYER_SIZE > enemy_y:
            game_over = True

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw player and enemy
        player(player_x, player_y, screen)
        enemy(enemy_x, enemy_y, screen)

        # Update the display
        pygame.display.update()

        # Cap the frame rate
        clock.tick(FPS)
