import pygame
from 设置 import Settings


class Block:
    def __init__(self):
        self.settings = Settings()

        self.size = 25
        self.grow_speed = 5
        self.pos = [600, 400]
        self.colour = (255, 0, 0)
        self.speed = 0.4
        self.surface = pygame.Rect((self.pos[0], self.pos[1]), (self.size, self.size))

        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        self.speed_up = False

    def update_pos(self):
        if self.speed_up:
            self.speed = 1
        else:
            self.speed = 0.4

        if self.move_up and self.pos[1] > 0:
            self.pos[1] -= self.speed
        if self.move_down and self.pos[1] < self.settings.screen_height - self.size:
            self.pos[1] += self.speed
        if self.move_left and self.pos[0] > 0:
            self.pos[0] -= self.speed
        if self.move_right and self.pos[0] < self.settings.screen_width - self.size:
            self.pos[0] += self.speed

        self.surface = pygame.Rect((self.pos[0], self.pos[1]), (self.size, self.size))

    def update_size(self):
        self.surface = pygame.Rect((self.pos[0], self.pos[1]), (self.size, self.size))