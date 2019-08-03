#Basic cross the road game using pygame

import sys
import pygame

SCREEN_WIDHT = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Cross The Road RPG"
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()

class Game:

    TICK_RATE = 60 #Frame rate for the game

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False

        while not is_game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
            print(event)

            #self.game_screen.blit(player_image, (375, 375))

            #pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
            #pygame.draw.circle(game_screen, BLACK_COLOR, [400, 300], 50)
            #Position on the screen and width, height of the rectangle [x, y, width, height]

            pygame.display.update() #updates all game graphics
            clock.tick(self.TICK_RATE)


pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDHT, SCREEN_HEIGHT)
new_game.run_game_loop()

#player_image = pygame.image.load("player.png")
#player_image = pygame.transform.scale(player_image, (50, 50))

pygame.quit()
quit()
