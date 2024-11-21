import pygame


# Initialize pygame
pygame.init()

# Create our display surface
WIDTH = 600
HEIGHT = 300
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Keyboard Movements!')

# Set the game values
VELOCITY = 10

# Load in images
dragon_image = pygame.image.load('images/dragon_right.png')
dragon_image_rect = dragon_image.get_rect()
dragon_image_rect.centerx = WIDTH // 2
dragon_image_rect.bottom = HEIGHT

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dragon_image_rect.y -= VELOCITY
            if event.key == pygame.K_DOWN:
                dragon_image_rect.y += VELOCITY
            if event.key == pygame.K_LEFT:
                dragon_image_rect.x -= VELOCITY
            if event.key == pygame.K_RIGHT:
                dragon_image_rect.x += VELOCITY

    # Fill the display surface to cover old images
    display_surface.fill((0, 0, 0))

    # Blit assets to the screen
    display_surface.blit(dragon_image, dragon_image_rect)

    # Update the display
    pygame.display.flip()

# End game
pygame.quit()