import pygame
from pygame.locals import *
import sys

from 设置 import Settings
from 方块 import Block
from 食物 import Food
pygame.init()


class Game:
    def __init__(self):
        self.settings = Settings()
        self.block = Block()
        self.food = Food()

        self.bg_colour = self.settings.bg_colour
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        self.bg = pygame.Surface(self.settings.screen_size)

    def main(self):
        while True:
            self.get_events()
            self.update()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                self.check_events_keydown(event)
            elif event.type == KEYUP:
                self.check_events_keyup(event)

    def check_events_keydown(self, event):
        if event.key == K_SPACE:
            if self.block.speed_up:
                self.block.speed_up = False
            else:
                self.block.speed_up = True
        if event.key == K_LEFT:
            self.block.move_left = True
        if event.key == K_RIGHT:
            self.block.move_right = True
        if event.key == K_UP:
            self.block.move_up = True
        if event.key == K_DOWN:
            self.block.move_down = True
        if event.key == K_q:
            pygame.quit()
            sys.exit()

    def check_events_keyup(self, event):
        if event.key == K_LEFT:
            self.block.move_left = False
        if event.key == K_RIGHT:
            self.block.move_right = False
        if event.key == K_UP:
            self.block.move_up = False
        if event.key == K_DOWN:
            self.block.move_down = False

    def update(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.fill(self.bg_colour)
        pygame.draw.rect(self.screen, self.food.colour, self.food.surface)
        self.block.update_pos()
        pygame.draw.rect(self.screen, self.block.colour, self.block.surface)
        if self.block.surface.colliderect(self.food.surface):
            self.food.update_pos()
            self.block.size += self.block.grow_speed
            self.block.update_size()
        pygame.display.set_caption(str(self.block.size))
        pygame.display.update()


if __name__ == '__main__':
    ga = Game()
    ga.main()