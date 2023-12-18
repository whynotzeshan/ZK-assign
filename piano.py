import pygame
from pygame import mixer

# Initialize Pygame and mixer
pygame.init()
mixer.init()

# Set up screen dimensions
screen_width = 800
screen_height = 300

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Virtual Piano")

# Load piano sounds
mixer.music.load("E:\Music\\AFSANAY_-_Young_Stunners__Talhah_Yunus__Talha_Anjum__Prod._By_Jokhay_(Official_Music_Video)(128k).mp3")

# Define piano key dimensions
key_width = screen_width // 14
key_height = screen_height

# Define key colors
key_colors = [white, black] * 7

# Define key positions
key_positions = [(i * key_width, 0) for i in range(14)]

# Define key sounds
key_sounds = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C2", "C2#"]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # Play C
                mixer.music.load(f"E:\Music\\AFSANAY_-_Young_Stunners__Talhah_Yunus__Talha_Anjum__Prod._By_Jokhay_(Official_Music_Video)(128k).mp3{key_sounds[0]}")
                mixer.music.play()
            elif event.key == pygame.K_s:  # Play C#
                mixer.music.load(f"E:\Music\\AFSANAY_-_Young_Stunners__Talhah_Yunus__Talha_Anjum__Prod._By_Jokhay_(Official_Music_Video)(128k).mp3{key_sounds[1]}")
                mixer.music.play()
            # Add similar conditions for other keys

    # Draw piano keys
    for i in range(14):
        pygame.draw.rect(screen, key_colors[i % 2], (key_positions[i], (key_width, key_height)))

    pygame.display.flip()

# Quit Pygame

pygame.quit()