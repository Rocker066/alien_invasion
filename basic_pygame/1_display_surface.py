import pygame
import sys

# initialize pygame
pygame.init()

# creat a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Hello World!')

# The main game loop
running = True
while running:
    # Loop through a list of events that have occurred
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

# End the game
pygame.quit()