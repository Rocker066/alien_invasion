import random

import pygame
from pygame.sprite import Sprite


class Monster(Sprite):
    """A simple class to create a monster"""

    def __init__(self, x, y):
        """Initiate the attributes"""
        super().__init__()
        self.image = pygame.image.load('knight.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 10)

    def update(self):
        self.rect.y += self.velocity


# Initialize pygame
pygame.init()

# Set display surface
WIDTH = 800
HEIGHT = 600
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sprite Groups!')

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Create a monster group and add 10 monsters
monster_group = pygame.sprite.Group()
for i in range(10):
    monster = Monster(i * 64, 10)
    monster_group.add(monster)

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the display
    display_surface.fill((0, 0, 0))

    # Update and draw assets
    monster_group.draw(display_surface)
    monster_group.update()

    # Update the display and tick the clock
    pygame.display.flip()
    clock.tick(FPS)

# End the game
pygame.quit()