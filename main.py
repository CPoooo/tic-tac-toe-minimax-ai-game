import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

BOARD_ROWS = 3
BOARD_COLS = 3
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
LINE_WIDTH = 6
CELL_WIDTH = SCREEN_WIDTH // BOARD_COLS
CELL_HEIGHT = SCREEN_HEIGHT // BOARD_ROWS
X_CUSHION = 30 # the distance from the corners of a given cell that i want to start the x at

GAME_BOARD = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True


def draw_lines():
    # vertical lines
    pygame.draw.line(screen, WHITE, (SCREEN_HEIGHT // BOARD_COLS, 0), (SCREEN_HEIGHT // BOARD_COLS, SCREEN_HEIGHT),
                     width=LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (SCREEN_HEIGHT // (BOARD_COLS / 2), 0),
                     (SCREEN_HEIGHT // (BOARD_COLS / 2), SCREEN_HEIGHT), width=LINE_WIDTH)

    # horizontal lines
    pygame.draw.line(screen, WHITE, (0, SCREEN_WIDTH // BOARD_ROWS), (SCREEN_WIDTH, SCREEN_WIDTH // BOARD_ROWS),
                     width=LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (0, SCREEN_WIDTH // (BOARD_ROWS / 2)),
                     (SCREEN_WIDTH, SCREEN_WIDTH // (BOARD_ROWS / 2)), width=LINE_WIDTH)


def draw_x(row, col):

    # Calculate the top-left corner of the cell with cushion
    top_left_x = col * CELL_WIDTH + X_CUSHION
    top_left_y = row * CELL_HEIGHT + X_CUSHION

    # Calculate the bottom-right corner of the cell with cushion
    bottom_right_x = (col + 1) * CELL_WIDTH - X_CUSHION
    bottom_right_y = (row + 1) * CELL_HEIGHT - X_CUSHION

    # Draw two intersecting lines to form X
    pygame.draw.line(screen, WHITE, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), width=6)
    pygame.draw.line(screen, WHITE, (top_left_x, bottom_right_y), (bottom_right_x, top_left_y), width=6)



def draw_o(row, col):
    # Calculate the center of the cell
    center_x = col * CELL_WIDTH + CELL_WIDTH // 2
    center_y = row * CELL_HEIGHT + CELL_HEIGHT // 2
    # Draw a circle to form O
    pygame.draw.circle(screen, WHITE, (center_x, center_y), CELL_WIDTH // 2, width=6)


def process_click(x, y):
    cell_row = y // (SCREEN_HEIGHT // BOARD_ROWS)
    cell_col = x // (SCREEN_WIDTH // BOARD_COLS)
    if GAME_BOARD[cell_row][cell_col] == 0:
        print("cell available")

    return [cell_row, cell_col]


# game loop
while running:

    # checks if user clicks x to exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check where player clicked and draw x
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # get coords of mouse click
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Determine which cell was clicked
            cell_row = mouse_y // CELL_HEIGHT
            cell_col = mouse_x // CELL_WIDTH
            # Check if the cell is empty
            if GAME_BOARD[cell_row][cell_col] == 0:
                # Update the board state
                GAME_BOARD[cell_row][cell_col] = 1  # Player X move

    # initial screen
    screen.fill(BLACK)
    draw_lines()

    # Redraw X's and O's
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if GAME_BOARD[row][col] == 1:
                draw_x(row, col)
            elif GAME_BOARD[row][col] == 2:
                draw_o(row, col)

    # updates the screen
    pygame.display.flip()

pygame.quit()
