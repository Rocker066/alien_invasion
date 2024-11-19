import pygame


# Initialize pygame
pygame.init()

# Create a display surface
WIDTH = 600
HEIGHT = 300
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blitting Text!')

# Define colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
BLACK = (0, 0, 0)

# See all available system fonts
fonts = pygame.font.get_fonts()
for font in fonts:
    if font.startswith('b'):
        print(font)

# Define fonts
system_font = pygame.font.SysFont('calibri', 64)
custom_font = pygame.font.Font('images/AttackGraffiti.ttf', 32)

# Define text
system_text = system_font.render('Dragons Rule!', True, GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WIDTH // 2, HEIGHT // 2 - 50)

custom_text = custom_font.render('Move the dragon soon !', False, GREEN)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WIDTH // 2, HEIGHT // 2 + 50)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit the text surfaces to the display surface
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)

    # Update the display
    pygame.display.flip()


# End game
pygame.quit()