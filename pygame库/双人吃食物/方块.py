import pygame
from 设置 import Settings


class Block:
    def __init__(self):
        self.settings = Settings()

        self.size = 25
        self.grow_speed = 5
        self.pos = [600, 400]
        self.colour = (255, 0, 0)
        self.speed = 0.5
        self.rect = pygame.Rect((self.pos[0], self.pos[1]), (self.size, self.size))

    def update_pos(self):
        self.rect = pygame.Rect((self.pos[0], self.pos[1]), (self.size, self.size))

    def move_up(self):
        if self.move_up and self.pos[1] > 0:
            self.pos[1] -= self.speed

    def move_down(self):
        if self.move_down and self.pos[1] < self.settings.screen_height - self.size:
            self.pos[1] += self.speed

    def move_left(self):
        if self.move_left and self.pos[0] > 0:
            self.pos[0] -= self.speed

    def move_right(self):
        if self.move_right and self.pos[0] < self.settings.screen_width - self.size:
            self.pos[0] += self.speed

    def update_size(self):
        self.size += self.grow_speed
        self.rect = pygame.Rect((self.pos[0], self.pos[1]), (self.size, self.size))
        if self.speed > 0.3:
            self.speed = self.speed * 0.95