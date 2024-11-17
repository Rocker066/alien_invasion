import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the rocket"""

    def __init__(self, bs_game):
        super().__init__()
        self.screen = bs_game.screen
        self.settings = bs_game.settings
        self.color = self.settings.bullet_color

        # Creat a bullet rectangle
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)

        # Make the bullet emerge from the top of the ship
        self.rect.midtop = bs_game.rocket.rect.midtop

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)


    def update(self):
        """Move the bullet up the screen."""
        # Update the exact position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y


    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)