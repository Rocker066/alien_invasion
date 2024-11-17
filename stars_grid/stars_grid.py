import pygame
import sys
from settings import Settings
from star import Star


class StarsGrid:
    """A class to show stars grid"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption('Stars Grid')
        self.clock = pygame.time.Clock()

        self.stars = pygame.sprite.Group()
        self._create_bunch()


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()

            self._update_screen()
            self.clock.tick(60)


    def _create_bunch(self):
        """Create a bunch of stars."""
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < (self.settings.screen_height - 2 * star_height):
            while current_x < (self.settings.screen_width - 2 * star_width):
                self._create_star(current_x, current_y)
                current_x += 2 * star_width

            # Finished a row; reset x value, and increment y value.
            current_x = star_width
            current_y += 2 * star_height


    def _create_star(self, x_position, y_position):
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()



if __name__ == '__main__':
    sg = StarsGrid()
    sg.run_game()