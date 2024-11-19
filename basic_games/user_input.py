import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hello User!")

# Set up fonts
font = pygame.font.Font(None, 36)
input_box = pygame.Rect(100, 100, 200, 50)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    # Display greeting when Enter is pressed
                    greeting_text = f"Hello, {text}!"
                    text = ''  # Clear input after greeting
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # Fill the background
    screen.fill((255, 255, 255))

    # Render the current text.
    txt_surface = font.render(text, True, color)
    width_input_box = max(200, txt_surface.get_width() + 10)
    input_box.w = width_input_box

    # Blit the input box and text
    pygame.draw.rect(screen, color, input_box, 2)
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

    # Display greeting if applicable
    if 'greeting_text' in locals():
        greeting_surface = font.render(greeting_text, True, (0, 0, 0))
        screen.blit(greeting_surface, (100, 200))

    # Update the display
    pygame.display.flip()