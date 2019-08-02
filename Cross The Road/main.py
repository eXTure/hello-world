#Basic cross the road game using pygame

import sys
import pygame

#print(dir(pygame))
pygame.init()

SCREEN_WIDHT = 800
SCREEN_HEIGHT = 800
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()
TICK_RATE = 60 #Frame rate for the game
is_game_over = False

game_screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
game_screen.fill(WHITE_COLOR)

while not is_game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True

    pygame.display.update()
    clock.tick(TICK_RATE)

pygame.quit()
quit()