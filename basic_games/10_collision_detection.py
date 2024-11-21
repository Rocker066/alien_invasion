import pygame
from random import random, randint



# Initialize pygame
pygame.init()

# Create a screen surface
WIDTH = 600
HEIGHT = 300
screen_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Collision Detection')

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Define colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
BLACK = (0, 0, 0)

# Set game values
VELOCITY = 5

# Coin collection score
SCORE = 0

# Load in images
dragon_image = pygame.image.load('images/dragon_right.png')
dragon_image_rect = dragon_image.get_rect()
dragon_image_rect.topleft = (25, 25)

coin_image = pygame.image.load('images/coin.png')
coin_image_rect = coin_image.get_rect()
coin_image_rect.center = (WIDTH // 2, HEIGHT // 2)

# Load sound effect
coin_collect = pygame.mixer.Sound('images/sound_1.wav')
coin_collect.set_volume(.2)

# Load fonts and text
system_font = pygame.font.SysFont('calibri',size=30)
system_text = system_font.render(str(SCORE), True, GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.topright = (30, 10)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Define Mouse movement (click and drag)
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_image_rect.centerx = mouse_x
            dragon_image_rect.centery = mouse_y

        # Define Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_image_rect.centerx = mouse_x
            dragon_image_rect.centery = mouse_y

    # Get a list of keys currently being pressed down
    keys = pygame.key.get_pressed()

    # Define continuous movements
    if keys[pygame.K_LEFT] and dragon_image_rect.left > 0:
        dragon_image_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT] and dragon_image_rect.right < WIDTH:
        dragon_image_rect.x += VELOCITY
    if keys[pygame.K_UP] and dragon_image_rect.top > 0:
        dragon_image_rect.y -= VELOCITY
    if keys[pygame.K_DOWN] and dragon_image_rect.bottom < HEIGHT:
        dragon_image_rect.y += VELOCITY


    # Check for collision between two rects
    if dragon_image_rect.colliderect(coin_image_rect):
        pygame.mixer.Sound.play(coin_collect)
        coin_image_rect.x = randint(0, WIDTH - 32)
        coin_image_rect.y = randint(0, HEIGHT - 32)
        SCORE += 1
        system_text = system_font.render(str(SCORE), True, GREEN, DARKGREEN)
        print('HIT!')

    # Fill the screen
    screen_surface.fill((0, 0, 0))

    # Draw rectangles to represent the rects of each object
    pygame.draw.rect(screen_surface, (0, 255, 0), dragon_image_rect, 1)
    pygame.draw.rect(screen_surface, (255, 255, 0), coin_image_rect, 1)

    # Blit assets
    screen_surface.blit(dragon_image, dragon_image_rect)
    screen_surface.blit(coin_image, coin_image_rect)
    screen_surface.blit(system_text, system_text_rect)

    # Update the screen
    pygame.display.flip()

    # Tick the clock
    clock.tick(FPS)

# End game
pygame.quit()