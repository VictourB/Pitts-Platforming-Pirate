import pygame, sys
from settings import *
from tiles import Tile
from level import Level

#General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up main window
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(game_title)
pygame.display.set_icon(pygame.image.load(game_icon))

# instatiate objects
level = Level(level_map,screen)

while True:
    # Input Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Updating the Window
    screen.fill((55,50,60))
    level.run()
    pygame.display.update()
    clock.tick(60)