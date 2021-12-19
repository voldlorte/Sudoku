# Importing the game library
import pygame
import random

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


def show_random(num_list):
    # font1 = pygame.font.Font.render(pygame.font.SysFont("arial", 26), str(random.randrange(10)), True, (0, 0, 0))
    f = 18
    for i in num_list:
        s = 28
        for j in i:
            print(f'{screen.blit(pygame.font.Font.render(pygame.font.SysFont("arial", 26), str(num_list[i][j]), True, (0, 0, 0)), (s, f))}')
            s += 66
        f += 66


# indexes of the random cells
def set_random_indexes(empty_cells):
    ran_list = []
    while True:
        ran_num = random.randrange(1, 10)
        ran_list.append(ran_num)
        if len(ran_list) == empty_cells:
            break

    for j in range(len(ran_list)):
        while ran_list.count(ran_list[j]) > 1:
            if ran_list.count(ran_list[j]) <= 1:
                continue
            else:
                ran_list[j] = random.randrange(1, 10)
    print("random indexes", ran_list)
    return ran_list


starting = True
while starting:

    # Filling the BG with a color
    screen.fill((0, 0, 0))

    # Displaying the background
    screen.blit(backGround, coordinates)

    my_list = []
    # adding random numbers to the whole matrix
    for row in range(9):
        n_list = []
        for column in range(9):
            n_list.append(random.randrange(1, 9))
        my_list.append(n_list)

    # extracting tables from the matrix
    for i in range(9):
        tables = [[], [], [], [], [], [], [], [], []]
        for row in range(9):
            for column in range(9):
                if row <= 2 and column <= 2:
                    tables[0].append(my_list[row][column])

                if row <= 2 and 3 <= column <= 5:
                    tables[1].append(my_list[row][column])

                if row <= 2 and 6 <= column <= 8:
                    tables[2].append(my_list[row][column])

                if 3 <= row <= 5 and column <= 2:
                    tables[3].append(my_list[row][column])

                if 3 <= row <= 5 and 3 <= column <= 5:
                    tables[4].append(my_list[row][column])

                if 3 <= row <= 5 and 6 <= column <= 8:
                    tables[5].append(my_list[row][column])

                if 6 <= row <= 8 and column <= 2:
                    tables[6].append(my_list[row][column])

                if 6 <= row <= 8 and 3 <= column <= 5:
                    tables[7].append(my_list[row][column])

                if 6 <= row <= 8 and 6 <= column <= 8:
                    tables[8].append(my_list[row][column])

    # indexes of the blank cells.
    for k in range(len(tables)):
        random_ind = set_random_indexes(5)
        for i in range(1, len(tables[k]) + 1):
            for j in range(len(random_ind)):
                if i == random_ind[j]:
                    # we leave this blank, the user should do an input.
                    tables[k][i - 1] = 11

    print(my_list)
    print(tables)

    pygame.display.update()
    starting = False


running = True


# Starting the game loop
while running:

    # We loop through the events
    for event in pygame.event.get():

        # Check if we pressed the quit button
        if event.type == pygame.QUIT:
            running = False

    # Updating the game
    pygame.display.update()
