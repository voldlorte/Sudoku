# Importing the game library
import pygame

# Initializing the library
pygame.init()

# Adding a screen
screen = pygame.display.set_mode((900, 900))

running = True

# Starting the game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
