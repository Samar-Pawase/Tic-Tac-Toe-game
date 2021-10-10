
# To install the below modules:
# Open your terminal and type - 
# pip install pygame
# pip install sys
# pip install numpy as np
# Once done run the the code 

# Importing Modules
import pygame
import sys
import numpy as np
pygame.init()

# Declaring the necessary dimensions
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COL = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
SPACE = 50

# Creating the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC-TAC-TOE')

# Filling the rows and columns with 0
board = np.zeros((BOARD_ROWS, BOARD_COL))

# Declaring the colours (Don't hesitate to change colours, you can change the R,G,B values from the tuple. Here I have tried to mimic the google tic-tac-toe colours)
BG_CLR = (21, 189, 172)
LINE_CLR = (13, 161, 145)
CIRCLE_CLR = (239, 236, 212)
CROSS_CLR = (84, 84, 84)

# Filling the screen with background colour
screen.fill(BG_CLR)
player = 1
gameover = False

# This function draws lines for rows and columns
def drawline():
    pygame.draw.line(screen, LINE_CLR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_CLR, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_CLR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_CLR, (400, 0), (400, 600), LINE_WIDTH)

# This function draws Xs and Os on the board
def draw_fig():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COL):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_CLR, (int(
                    col*200 + 200/2), int(row*200 + 200/2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_CLR, (col*200+SPACE, row *
                                 200+200-SPACE), (col*200+200-SPACE, row*200+SPACE), 25)
                pygame.draw.line(screen, CROSS_CLR, (col*200+SPACE, row *
                                 200+SPACE), (col*200+200-SPACE, row*200+200-SPACE), 25)

# This function marks the squares with player's fig (X or O)
def mark_square(row, col, player):
    board[row][col] = player

# This function will check if or not the squares are available
def available_square(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False

# This function will return true if the board is full
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COL):
            if board[row][col] == 0:
                return False
    return True

# This function returns true if a player wins
def check_win(player):

    for col in range(BOARD_COL):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_dsc_diagonal(player)
        return True

    return False

# This function will reset the board and restart the game when the key 'r' is pressed
def restart():
    screen.fill(BG_CLR)
    drawline()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COL):
            board[row][col] = 0
    draw_fig()

# This function draws a winning vertical line
def draw_vertical_winning_line(col, player):
    posX = col*200+100

    if player == 1:
        colour = CIRCLE_CLR
    if player == 2:
        colour = CROSS_CLR

    pygame.draw.line(screen, colour, (posX, 15), (posX, HEIGHT-15), 15)

# This function draws a winning horizontal line
def draw_horizontal_winning_line(row, player):
    posY = row*200+100

    if player == 1:
        colour = CIRCLE_CLR
    if player == 2:
        colour = CROSS_CLR

    pygame.draw.line(screen, colour, (15, posY), (WIDTH-15, posY), 15)

# This function draws winning ascending diagonal
def draw_asc_diagonal(player):
    if player == 1:
        colour = CIRCLE_CLR

    if player == 2:
        colour = CROSS_CLR

    pygame.draw.line(screen, colour, (15, HEIGHT-15), (WIDTH-15, 15), 15)

# This function draws winning decending diagonal
def draw_dsc_diagonal(player):
    if player == 1:
        colour = CIRCLE_CLR

    if player == 2:
        colour = CROSS_CLR

    pygame.draw.line(screen, colour, (15, 15), (WIDTH-15, HEIGHT-15), 15)

# Calling the function to draw rows and column lines
drawline()

# Initializing the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not gameover:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY//200)
            clicked_col = int(mouseX//200)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        gameover = True
                    player = 2

                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        gameover = True
                    player = 1
                draw_fig()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1  
                gameover = False
                draw_fig()
    pygame.display.update()

# Have fun!
