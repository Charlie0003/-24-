import pygame
from pygame.locals import *
import sys

from 设置 import Settings
from 方块 import Block
from 方块2 import Block2
from 食物 import Food
pygame.init()
font = pygame.font.Font(None, 20)


class Game:
    def __init__(self):
        self.settings = Settings()
        self.block = Block()
        self.block2 = Block2()
        self.food = Food()

        self.bg_colour = self.settings.bg_colour
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        self.bg = pygame.Surface(self.settings.screen_size)

        start_font = pygame.font.SysFont("arial", 50)
        self.start_text = start_font.render("Play", True, (0, 0, 0))

        self.flag = 1
        self.start_game = False

    def main(self):
        while True:
            self.get_events()
            self.update()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                self.check_mouse_events(mouse_presses)
            if event.type == KEYDOWN:
                self.change_mouse(event)

        pressed_keys = pygame.key.get_pressed()
        self.check_events_pressed(pressed_keys)

    def check_events_pressed(self, pressed_key):
        # 方块1移动
        if pressed_key[K_LEFT]:
            self.block.move_left()
        if pressed_key[K_RIGHT]:
            self.block.move_right()
        if pressed_key[K_UP]:
            self.block.move_up()
        if pressed_key[K_DOWN]:
            self.block.move_down()
        # 方块2移动
        if pressed_key[K_a]:
            self.block2.move_left()
        if pressed_key[K_d]:
            self.block2.move_right()
        if pressed_key[K_w]:
            self.block2.move_up()
        if pressed_key[K_s]:
            self.block2.move_down()
        # 游戏开始
        if pressed_key[K_p]:
            self.start_game = True
        # 退出游戏
        if pressed_key[K_ESCAPE]:
            pygame.quit()
            sys.exit()

    def check_mouse_events(self, mouse_presses):
        # 点击Play开始游戏
        if mouse_presses[0]:
            self.food.update_pos()
            self.mouse_pos = list(pygame.mouse.get_pos())
            if 551 < self.mouse_pos[0] < 658 and 405 > self.mouse_pos[1] > 360 \
                    and not self.start_game:
                self.start_game = True
        # 中间的鼠标消失
        if mouse_presses[1]:
            if self.flag == 1:
                pygame.mouse.set_visible(False)
                self.flag = 0
            elif self.flag == 0:
                pygame.mouse.set_visible(True)
                self.flag = 1

    def change_mouse(self, event):
        # 改变形态
        if event.key == pygame.K_1:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if event.key == pygame.K_2:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    def update(self):
        # 绘制屏幕
        self.screen.blit(self.bg, (0, 0))
        self.screen.fill(self.bg_colour)
        if self.start_game:
            # 绘制食物
            pygame.draw.rect(self.screen, self.food.colour, self.food.rect)
            # 更新两个方块
            self.block.update_pos()
            pygame.draw.rect(self.screen, self.block.colour, self.block.rect)
            self.block2.update_pos()
            pygame.draw.rect(self.screen, self.block2.colour, self.block2.rect)
            # 如果方块与食物碰撞，变大
            if self.block.rect.colliderect(self.food.rect):
                self.food.update_pos()
                self.block.update_size()
            if self.block2.rect.colliderect(self.food.rect):
                self.food.update_pos()
                self.block2.update_size()
        else:
            # 把Play建在中心
            self.screen.blit(self.start_text, (550, 350))
        # 将标题写入大小
        pygame.display.set_caption(f'red:{self.block.size} black:{self.block2.size}')
        # 屏幕更新
        pygame.display.update()


if __name__ == '__main__':
    ga = Game()
    ga.main()