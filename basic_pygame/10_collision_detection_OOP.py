import pygame
from random import random, randint


class DragonCoin:
    """A class for the dragon and coin game"""

    def __init__(self):
        """attributes for game"""
        # Initialize pygame
        pygame.init()

        # Create a screen surface
        self.WIDTH = 600
        self.HEIGHT = 300
        self.screen_surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Collision Detection')

        # Set FPS and clock
        self.FPS = 60
        self.clock = pygame.time.Clock()

        # Define colors
        self.GREEN = (0, 255, 0)
        self.DARKGREEN = (10, 50, 10)
        self.BLACK = (0, 0, 0)

        # Set game values
        self.VELOCITY = 5
        self.SCORE = 0

        # Load in images
        self._load_image()

        # Load sound effects
        self._load_sound_effect()

        # Load fonts and text
        self._load_font_text()


    def run_game(self):
        """Main game loop"""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Define Mouse movement (click and drag)
                if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
                    mouse_x = event.pos[0]
                    mouse_y = event.pos[1]
                    self.dragon_image_rect.centerx = mouse_x
                    self.dragon_image_rect.centery = mouse_y

                # Define Mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x = event.pos[0]
                    mouse_y = event.pos[1]
                    self.dragon_image_rect.centerx = mouse_x
                    self.dragon_image_rect.centery = mouse_y

            # Get a list of keys currently being pressed down
            keys = pygame.key.get_pressed()

            # Define continuous movements
            if keys[pygame.K_LEFT] and self.dragon_image_rect.left > 0:
                self.dragon_image_rect.x -= self.VELOCITY
            if keys[pygame.K_RIGHT] and self.dragon_image_rect.right < self.WIDTH:
                self.dragon_image_rect.x += self.VELOCITY
            if keys[pygame.K_UP] and self.dragon_image_rect.top > 0:
                self.dragon_image_rect.y -= self.VELOCITY
            if keys[pygame.K_DOWN] and self.dragon_image_rect.bottom < self.HEIGHT:
                self.dragon_image_rect.y += self.VELOCITY

            # Check for collision between two rects
            if self.dragon_image_rect.colliderect(self.coin_image_rect):
                pygame.mixer.Sound.play(self.coin_collect)
                self.coin_image_rect.x = randint(0, self.WIDTH - 32)
                self.coin_image_rect.y = randint(0, self.HEIGHT - 32)
                self.SCORE += 1
                self.system_text = self.system_font.render(str(self.SCORE), True, self.GREEN, self.DARKGREEN)
                print('HIT!')

            # Update the screen
            self._update_screen()

            # Tick the clock
            self.clock.tick(self.FPS)


    def _load_image(self):
        self.dragon_image = pygame.image.load('images/dragon_right.png')
        self.dragon_image_rect = self.dragon_image.get_rect()
        self.dragon_image_rect.topleft = (25, 25)

        self.coin_image = pygame.image.load('images/coin.png')
        self.coin_image_rect = self.coin_image.get_rect()
        self.coin_image_rect.center = (self.WIDTH // 2, self.HEIGHT // 2)


    def _load_sound_effect(self):
        self.coin_collect = pygame.mixer.Sound('images/sound_1.wav')
        self.coin_collect.set_volume(.2)


    def _load_font_text(self):
        self.system_font = pygame.font.SysFont('calibri', size=30)
        self.system_text = self.system_font.render(str(self.SCORE), True, self.GREEN, self.DARKGREEN)
        self.system_text_rect = self.system_text.get_rect()
        self.system_text_rect.topright = (30, 10)


    def _update_screen(self):
        # Fill the screen
        self.screen_surface.fill((0, 0, 0))

        # Draw rectangles to represent the rects of each object
        pygame.draw.rect(self.screen_surface, (0, 255, 0), self.dragon_image_rect, 1)
        pygame.draw.rect(self.screen_surface, (255, 255, 0), self.coin_image_rect, 1)

        # Blit assets
        self.screen_surface.blit(self.dragon_image, self.dragon_image_rect)
        self.screen_surface.blit(self.coin_image, self.coin_image_rect)
        self.screen_surface.blit(self.system_text, self.system_text_rect)

        pygame.display.flip()



if __name__ == '__main__':
    dc = DragonCoin()
    dc.run_game()
