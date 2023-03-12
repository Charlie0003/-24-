import pygame
from random import randint
from 设置 import Settings
from 方块 import Block


class Food:
    def __init__(self):
        self.settings = Settings()
        self.block = Block()

        self.size = 20
        self.pos = [randint(0, self.settings.screen_width - self.block.size),
                    randint(0, self.settings.screen_height - self.block.size)]
        self.colour = (0, 0, 255)
        self.rect = pygame.Rect((self.pos[0], self.pos[1]), (self.size, self.size))

    def update_pos(self):
        self.pos = [randint(0, self.settings.screen_width - self.block.size),
                    randint(0, self.settings.screen_height - self.block.size)]
        self.rect = pygame.Rect((self.pos[0], self.pos[1]), (self.size, self.size))