import pygame


# Initialize pygame
pygame.init()

# Create surface
WIDTH = 600
HEIGHT = 300
screen_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Restrict Movement')

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Set game values
VELOCITY = 5

# Load images
dragon_image = pygame.image.load('images/dragon_right.png')
dragon_image_rect = dragon_image.get_rect()
dragon_image_rect.center = (WIDTH // 2, HEIGHT // 2)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    # Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()

    # Move the dragon continuously
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_image_rect.x > 0:
        dragon_image_rect.x -= VELOCITY
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_image_rect.right < WIDTH:
        dragon_image_rect.x += VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_image_rect.y > 0:
        dragon_image_rect.y -= VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_image_rect.bottom < HEIGHT:
        dragon_image_rect.y += VELOCITY

    # Fill the screen
    screen_surface.fill((0, 0, 0))

    # Blit the assets
    screen_surface.blit(dragon_image, dragon_image_rect)

    # Update the screen
    pygame.display.flip()

    # Tick the clock
    clock.tick(FPS)

# End game
pygame.quit()