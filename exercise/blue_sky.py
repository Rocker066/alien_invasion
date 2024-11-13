import sys
import pygame
from settings import Settings
from rocket import Rocket

class BlueSky:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,
             self.settings.screen_height)
        )

        self.rocket = Rocket(self)
        self.clock = pygame.time.Clock()


    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

        pygame.display.flip()



if __name__ == '__main__':
    bs = BlueSky()
    bs.run_game()