import pygame


# initialize pygame
pygame.init()

# Create surface
WIDTH = 600
HEIGHT = 300
screen_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mouse Movement!')

# Load images
dragon_image = pygame.image.load('images/dragon_right.png')
dragon_image_rect = dragon_image.get_rect()
dragon_image_rect.topleft = (25, 25)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move based on mouse clicks (in this case left click) remove event.button for all buttons
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print(event)
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_image_rect.centerx = mouse_x
            dragon_image_rect.centery = mouse_y

        # Move based on mouse motion
        # if event.type == pygame.MOUSEMOTION:
        #     mouse_x = event.pos[0]
        #     mouse_y = event.pos[1]
        #     dragon_image_rect.centerx = mouse_x
        #     dragon_image_rect.centery = mouse_y

        # Drag the object when the left mouse button is clicked
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_image_rect.centerx = mouse_x
            dragon_image_rect.centery = mouse_y

    # Fill the screen
    screen_surface.fill((0, 0, 0))

    # Blit assets
    screen_surface.blit(dragon_image, dragon_image_rect)

    # Update the screen
    pygame.display.flip()

# End game
pygame.quit()