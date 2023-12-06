import pygame
import game_objects.controllers.player_config as pc

class PlayerController:
    def __init__(self, initial_x, initial_y):
        self.player_x = initial_x
        self.player_y = initial_y
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration = 0.2
        self.friction = 0.1

    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.velocity_x -= self.acceleration
        if keys[pygame.K_RIGHT]:
            self.velocity_x += self.acceleration
        if keys[pygame.K_UP]:
            self.velocity_y -= self.acceleration
        if keys[pygame.K_DOWN]:
            self.velocity_y += self.acceleration

    def apply_friction(self):
        if self.velocity_x > 0:
            self.velocity_x -= self.friction
        elif self.velocity_x < 0:
            self.velocity_x += self.friction

        if self.velocity_y > 0:
            self.velocity_y -= self.friction
        elif self.velocity_y < 0:
            self.velocity_y += self.friction

    def move_player(self):
        self.player_x += self.velocity_x
        self.player_y += self.velocity_y

    def get_position(self):
        return self.player_x, self.player_y
