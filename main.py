# Importing the game library
import pygame

# Initializing the library
pygame.init()

# Adding a screen
screen = pygame.display.set_mode((600, 600))

# Adding a title for the game
pygame.display.set_caption("Sudoku", "Sudoku")

# Loading The icon and the background
icon = pygame.image.load("sudokuIcon.png")
backGround = pygame.image.load("sudokuGrid.jpg")
coordinates = [0, 0]

# Displaying the icon
pygame.display.set_icon(icon)

running = True

# Starting the game loop
while running:

    # Filling the BG with a color
    screen.fill((0, 0, 0))

    # Displaying the background
    screen.blit(backGround, coordinates)

    # We loop through the events
    for event in pygame.event.get():

        # Check if we pressed the quit button
        if event.type == pygame.QUIT:
            running = False

        # Check if we pressed the left mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.BUTTON_LEFT:
                print("left pressed")

    # Debugging
    screen.blit(pygame.font.Font.render(pygame.font.SysFont("arial", 32), "0", True, (0, 0, 0)), (300, 300))

    # Updating the game
    pygame.display.update()
