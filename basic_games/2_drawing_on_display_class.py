from platform import system

import pygame
import pygame.draw
import sys


class Draw:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Create a display surface and set its caption
        self.WINDOW_WIDTH = 600
        self.WINDOW_HEIGHT = 600
        self.display_surface = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption('Drawing Objects')

        # Define colors as RGB tuples
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (255, 255, 0)
        self.CYAN = (0, 255, 255)
        self.MAGENTA = (255, 0, 255)

        # Set framerate
        self.clock = pygame.time.Clock()


    def run_game(self):
        # The main game loop
        while True:
            self._check_events()

            self._update_screen()

            self.clock.tick(60)


    def _check_events(self):
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                sys.exit()


    def draw_line(self):
        # Line(surface, color, starting point, ending point, thickness)
        pygame.draw.line(self.display_surface, self.RED, (0, 0), (100, 100), 5)
        pygame.draw.line(self.display_surface, self.GREEN, (100, 100), (200, 300), 5)


    def draw_circle(self):
        # Circle(surface, color, center, radius, thickness...0 for fill)
        pygame.draw.circle(self.display_surface, self.WHITE,
                           (self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2),
                           300,
                           6)
        pygame.draw.circle(self.display_surface, self.MAGENTA,
                           (self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2),
                           200,
                           6)


    def draw_rectangle(self):
        # Rectangle(surface, color, (top-left x, top-left y, width, height))
        pygame.draw.rect(self.display_surface, self.CYAN, (500, 50, 50, 100))
        pygame.draw.rect(self.display_surface, self.RED, (500, 100, 50, 100))


    def _update_screen(self):
        # Give a background color to the display
        self.display_surface.fill(self.BLUE)

        self.draw_line()
        self.draw_circle()
        self.draw_rectangle()

        # Update the display
        pygame.display.flip()



if __name__ == '__main__':
    draw = Draw()
    draw.run_game()

