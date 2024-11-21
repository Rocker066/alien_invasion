import pygame


# Initialize pygame
pygame.init()

# Create a screen surface
WIDTH = 600
HEIGHT = 300
screen_surface = pygame.display.set_mode((WIDTH, HEIGHT))

# Give a background color to the display
screen_surface.fill((0, 0, 0))

# Show image
image1 = pygame.image.load('images/dragon_left.png')
image1_rect = image1.get_rect()
image1_rect.topleft = (0, 0)

image2 = pygame.image.load('images/dragon_right.png')
image2_rect = image2.get_rect()
image2_rect.topright = (WIDTH, 0)

# Draw a line
# (surface, color, starting point, ending point, thickness)
pygame.draw.line(screen_surface, (255, 255, 0),
                 (0, 74), (WIDTH, 74), 5)

# Draw text on screen
# Define fonts
system_font = pygame.font.SysFont('calibri', 60)
custom_font = pygame.font.Font('images/AttackGraffiti.ttf', 60)

# Define text
system_text = system_font.render('Dragon Rules!',
                                 True, (0, 255, 0), (10, 50, 10))
system_text_rect = system_text.get_rect()
system_text_rect.midtop = (WIDTH // 2, 5)

custom_text = custom_font.render('COMING SOON...', True, (0, 255, 0))
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WIDTH // 2, HEIGHT // 2 + 20)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit the images
    screen_surface.blit(image1, image1_rect)
    screen_surface.blit(image2, image2_rect)

    # Blit the text
    screen_surface.blit(system_text, system_text_rect)
    screen_surface.blit(custom_text, custom_text_rect)

    # Update the screen
    pygame.display.flip()

# End game
pygame.quit()


