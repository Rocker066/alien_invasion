import pygame
from random import randint


class DragonCoin:
    """A class for the dragon and coin game"""

    def __init__(self):
        """Initialize game attributes"""
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

        # Load resources
        self._load_resources()

    def run_game(self):
        """Main game loop"""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Handle mouse movement and clicking
                if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
                    if event.buttons[0] == 1:  # Left mouse button pressed
                        self.dragon_image_rect.center = event.pos

            # Handle continuous movements
            keys = pygame.key.get_pressed()
            self._handle_movement(keys)

            # Check for collision with the coin
            if self.dragon_image_rect.colliderect(self.coin_image_rect):
                self._collect_coin()

            # Update the screen
            self._update_screen()

            # Tick the clock
            self.clock.tick(self.FPS)

    def _load_resources(self):
        """Load images, sounds, and fonts"""
        self.dragon_image = pygame.image.load('images/dragon_right.png')
        self.dragon_image_rect = self.dragon_image.get_rect(topleft=(25, 25))

        self.coin_image = pygame.image.load('images/coin.png')
        self.coin_image_rect = self.coin_image.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))

        self.coin_collect_sound = pygame.mixer.Sound('images/sound_1.wav')
        self.coin_collect_sound.set_volume(0.2)

        self.system_font = pygame.font.SysFont('calibri', size=30)
        self.system_text_rect = pygame.Rect(30, 10, 100, 30)  # Adjusted to fit text

    def _handle_movement(self, keys):
        """Handle dragon movement based on key presses"""
        if keys[pygame.K_LEFT] and self.dragon_image_rect.left > 0:
            self.dragon_image_rect.x -= self.VELOCITY
        if keys[pygame.K_RIGHT] and self.dragon_image_rect.right < self.WIDTH:
            self.dragon_image_rect.x += self.VELOCITY
        if keys[pygame.K_UP] and self.dragon_image_rect.top > 0:
            self.dragon_image_rect.y -= self.VELOCITY
        if keys[pygame.K_DOWN] and self.dragon_image_rect.bottom < self.HEIGHT:
            self.dragon_image_rect.y += self.VELOCITY

    def _collect_coin(self):
        """Handle coin collection"""
        pygame.mixer.Sound.play(self.coin_collect_sound)
        self.coin_image_rect.topleft = (randint(0, self.WIDTH - 32), randint(0, self.HEIGHT - 32))

        # Update score and text only if score changes
        previous_score = self.SCORE
        self.SCORE += 1

        if previous_score != self.SCORE:
            system_text_surface = self.system_font.render(str(self.SCORE), True, self.GREEN, self.DARKGREEN)
            # Update text position based on the new score surface size
            system_text_surface_rect = system_text_surface.get_rect(topleft=self.system_text_rect.topleft)

    def _update_screen(self):
        """Update the game screen"""
        # Fill the screen with black color
        self.screen_surface.fill(self.BLACK)

        # Draw rectangles to represent the rects of each object (for debugging)
        pygame.draw.rect(self.screen_surface, (0, 255, 0), self.dragon_image_rect, 1)
        pygame.draw.rect(self.screen_surface, (255, 255, 0), self.coin_image_rect, 1)

        # Blit assets onto the screen
        self.screen_surface.blit(self.dragon_image, self.dragon_image_rect)
        self.screen_surface.blit(self.coin_image, self.coin_image_rect)

        # Blit coin image onto the screen
        # Blit score text onto the screen only when it changes to avoid unnecessary rendering.
        system_text_surface = self.system_font.render(str(self.SCORE), True,
                                                      (255, 255, 255),
                                                      (0, 0, 0))
        system_text_surface_rect = system_text_surface.get_rect(topleft=self.system_text_rect.topleft)
        # Draw score on screen.
        pygame.draw.rect(self.screen_surface, (0, 0, 0), system_text_surface_rect)
        # Draw updated score on screen.
        # pygame.blit(system_text_surface, (system_text_surface.x, system_text_surface.y))
        self.screen_surface.blit(system_text_surface, system_text_surface_rect)

        # Flip the display to show new frame
        pygame.display.flip()


if __name__ == '__main__':
    dc = DragonCoin()
    dc.run_game()