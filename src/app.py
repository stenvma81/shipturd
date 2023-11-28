import pygame
import sys
from scenes.default_scene import default_scene
import settings
import utils.colors as colors

pygame.init()

WIDTH, HEIGHT = settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def game_start():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    default_scene(screen)

game_start()

font = pygame.font.Font(None, 36)
text = font.render("Game Over", True, colors.WHITE)
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(text, text_rect)
pygame.display.update()

pygame.time.wait(2000)

# Quit Pygame
pygame.quit()
sys.exit()
