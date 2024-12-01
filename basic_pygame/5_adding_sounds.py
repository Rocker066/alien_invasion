import pygame


# Initialize pygame
pygame.init()

# Create screen surface
WIDTH = 600
HEIGHT = 300
screen_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Adding Sounds!')

# Load sound effects
sound_1 = pygame.mixer.Sound('images/sound_1.wav')
sound_2 = pygame.mixer.Sound('images/sound_2.wav')

# Play the sound effects
sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)

# Change the volume of a sound effect
sound_2.set_volume(.1)
sound_2.play()

# Load the background music
pygame.mixer.music.load('images/music.wav')

# play and stop the music
pygame.mixer.music.play(-1, 0.0)
pygame.time.delay(1000)
sound_2.play()
pygame.time.delay(5000)
pygame.mixer.music.stop()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

# End Game
pygame.quit()