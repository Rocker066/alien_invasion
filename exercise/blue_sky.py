import sys
import pygame
from settings import Settings
from rocket import Rocket


class BlueSky:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # self.screen = pygame.display.set_mode(
        #     (self.settings.screen_width,
        #      self.settings.screen_height)
        # )

        self.rocket = Rocket(self)
        self.clock = pygame.time.Clock()


    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            self.clock.tick(120)


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True

        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = True

        if event.key == pygame.K_UP:
            self.rocket.moving_up = True

        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = True

        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False

        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = False

        if event.key == pygame.K_UP:
            self.rocket.moving_up = False

        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = False


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

        pygame.display.flip()



if __name__ == '__main__':
    bs = BlueSky()
    bs.run_game()