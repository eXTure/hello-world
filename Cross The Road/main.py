#Basic cross the road game using pygame

import sys
import pygame

SCREEN_WIDHT = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Cross The Road RPG"
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()
bg = pygame.image.load("background.png") ###############
bg = pygame.transform.scale(bg, (800, 800)) ########################

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
        direction = 0
        player_character = PlayerCharacter("player.png", 375, 700, 50, 50)
        enemy_0 = NonPlayerCharacter("enemy.png", 20, 400, 50, 50)

        while not is_game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN: #Event, when key is pressed
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                elif event.type == pygame.KEYUP: #Event, when key is released
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0

            print(event)

            self.game_screen.fill(WHITE_COLOR) #Redraw the background image
            self.game_screen.blit(bg, (0, 0)) ####################
            player_character.move(direction, self.height)
            player_character.draw(self.game_screen)
            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)
            pygame.display.update() #updates all game graphics
            clock.tick(self.TICK_RATE)

class GameObject:

    def __init__(self, image_path, x, y, width, height):

        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

class PlayerCharacter(GameObject):
    """Character controled by a human player."""

    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, direction, max_height):
        #self.y_pos += direction * SPEED  <<<<Unreliable way of doing the same
        if direction > 0: #Positive direction moves character downwards
            self.y_pos -= self.SPEED
        elif direction < 0: #Negative values moves character upwards
            self.y_pos += self.SPEED

        if self.y_pos >= max_height - 50:
            self.y_pos = max_height - 50
        elif self.y_pos <= 0:
            self.y_pos = 0


class NonPlayerCharacter(GameObject):

    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 20:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED


pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDHT, SCREEN_HEIGHT)
new_game.run_game_loop()

pygame.quit()
quit()

#self.game_screen.blit(player_image, (375, 375))
#pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
#pygame.draw.circle(game_screen, BLACK_COLOR, [400, 300], 50)
#Position on the screen and width, height of the rectangle [x, y, width, height]
