import pygame
from pygame.examples.grid import WINDOW_WIDTH

# Initialize pygame
pygame.init()

# Create a display surface
WIDTH = 600
HEIGHT = 300
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blitting Images!')

# Create images...returns a surface object with the image drawn on it.
# We can then get the rect of the surface and use the rect to position the image.
dragon_left_image = pygame.image.load('images/dragon_left.png')
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0, 0)

dragon_right_image = pygame.image.load('images/dragon_right.png')
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.bottomright = (WIDTH, HEIGHT)



# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit (copy) a surface object at the given coordinates to our display
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)

    # Draw a line
    pygame.draw.line(display_surface, 
                     (255, 255, 255),
                     (70, 0),
                     (530, HEIGHT),
                     4)

    # Update the display
    pygame.display.update()

# End game
pygame.quit()