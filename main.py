import pygame
from random import choice

PLAYER = 1  # by default player 1 aka the human goes first (for now it is just player 1 human v human)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

BOARD_ROWS = 3
BOARD_COLS = 3
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
LINE_WIDTH = 6
CELL_WIDTH = SCREEN_WIDTH // BOARD_COLS
CELL_HEIGHT = SCREEN_HEIGHT // BOARD_ROWS
X_CUSHION = 30  # the distance from the corners of a given cell that I want to start the X at
O_CUSHION = 25
COMPUTER_WIN = False
PLAYER_WIN = False

GAME_OVER_FLAG = False

GAME_BOARD = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cameron's Tic-Tac-Toe AI")
running = True


def draw_lines(color=WHITE):
    screen.fill(BLACK)
    # vertical lines
    pygame.draw.line(screen, color, (SCREEN_HEIGHT // BOARD_COLS, 0), (SCREEN_HEIGHT // BOARD_COLS, SCREEN_HEIGHT),
                     width=LINE_WIDTH)
    pygame.draw.line(screen, color, (SCREEN_HEIGHT // (BOARD_COLS / 2), 0),
                     (SCREEN_HEIGHT // (BOARD_COLS / 2), SCREEN_HEIGHT), width=LINE_WIDTH)

    # horizontal lines
    pygame.draw.line(screen, color, (0, SCREEN_WIDTH // BOARD_ROWS), (SCREEN_WIDTH, SCREEN_WIDTH // BOARD_ROWS),
                     width=LINE_WIDTH)
    pygame.draw.line(screen, color, (0, SCREEN_WIDTH // (BOARD_ROWS / 2)),
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
    pygame.draw.circle(screen, WHITE, (center_x, center_y), CELL_WIDTH // 2 - O_CUSHION, width=6)


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if GAME_BOARD[row][col] == 0:
                return False
    return True


def check_for_x_win():
    global PLAYER_WIN
    # row wins for x
    if GAME_BOARD[0][0] == 1 and GAME_BOARD[0][1] == 1 and GAME_BOARD[0][2] == 1:
        PLAYER_WIN = True
        game_over(1)
    if GAME_BOARD[1][0] == 1 and GAME_BOARD[1][1] == 1 and GAME_BOARD[1][2] == 1:
        PLAYER_WIN = True
        game_over(1)
    if GAME_BOARD[2][0] == 1 and GAME_BOARD[2][1] == 1 and GAME_BOARD[2][2] == 1:
        PLAYER_WIN = True
        game_over(1)
    # col wins for x
    if GAME_BOARD[0][0] == 1 and GAME_BOARD[1][0] == 1 and GAME_BOARD[2][0] == 1:
        PLAYER_WIN = True
        game_over(1)
    if GAME_BOARD[0][1] == 1 and GAME_BOARD[1][1] == 1 and GAME_BOARD[2][1] == 1:
        PLAYER_WIN = True
        game_over(1)
    if GAME_BOARD[0][2] == 1 and GAME_BOARD[1][2] == 1 and GAME_BOARD[2][2] == 1:
        PLAYER_WIN = True
        game_over(1)
    # diag wins for x
    if GAME_BOARD[0][0] == 1 and GAME_BOARD[1][1] == 1 and GAME_BOARD[2][2] == 1:
        PLAYER_WIN = True
        game_over(1)
    if GAME_BOARD[0][2] == 1 and GAME_BOARD[1][1] == 1 and GAME_BOARD[2][0] == 1:
        PLAYER_WIN = True
        game_over(1)


def check_for_o_win():
    global COMPUTER_WIN
    # row wins for o
    if GAME_BOARD[0][0] == 2 and GAME_BOARD[0][1] == 2 and GAME_BOARD[0][2] == 2:
        COMPUTER_WIN = True
        game_over(2)
    if GAME_BOARD[1][0] == 2 and GAME_BOARD[1][1] == 2 and GAME_BOARD[1][2] == 2:
        COMPUTER_WIN = True
        game_over(2)
    if GAME_BOARD[2][0] == 2 and GAME_BOARD[2][1] == 2 and GAME_BOARD[2][2] == 2:
        COMPUTER_WIN = True
        game_over(2)
    # col wins for o
    if GAME_BOARD[0][0] == 2 and GAME_BOARD[1][0] == 2 and GAME_BOARD[2][0] == 2:
        COMPUTER_WIN = True
        game_over(2)
    if GAME_BOARD[0][1] == 2 and GAME_BOARD[1][1] == 2 and GAME_BOARD[2][1] == 2:
        COMPUTER_WIN = True
        game_over(2)
    if GAME_BOARD[0][2] == 2 and GAME_BOARD[1][2] == 2 and GAME_BOARD[2][2] == 2:
        COMPUTER_WIN = True
        game_over(2)
    # diag wins for o
    if GAME_BOARD[0][0] == 2 and GAME_BOARD[1][1] == 2 and GAME_BOARD[2][2] == 2:
        COMPUTER_WIN = True
        game_over(2)
    if GAME_BOARD[0][2] == 2 and GAME_BOARD[1][1] == 2 and GAME_BOARD[2][0] == 2:
        COMPUTER_WIN = True
        game_over(2)


def game_over(player):
    global GAME_OVER_FLAG
    GAME_OVER_FLAG = True
    screen.fill(BLACK)
    # p1 win
    if player == 1:
        draw_lines(GREEN)
        pygame.display.set_caption("PLAYER WINS! (TO PLAY AGAIN PRESS \"r\")")
    # p2 win
    elif player == 2:
        draw_lines(RED)
        pygame.display.set_caption("CPU WINS! (TO PLAY AGAIN PRESS \"r\")")
    elif is_board_full():  # draw
        draw_lines(GRAY)
        pygame.display.set_caption("DRAW (TO PLAY AGAIN PRESS \"r\")")
    pygame.display.flip()


def reset_board():
    global GAME_BOARD
    global PLAYER
    pygame.display.set_caption("Cameron's Tic-Tac-Toe AI")
    GAME_BOARD = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
    PLAYER = 1
    screen.fill(BLACK)
    draw_lines()
    pygame.display.flip()


def score(board):
    # Check for wins
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            return 1 if board[row][0] == 2 else -1
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return 1 if board[0][col] == 2 else -1
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return 1 if board[0][0] == 2 else -1
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return 1 if board[0][2] == 2 else -1
    # Check for draw
    if is_board_full():
        return 0
    return None


def minimax(board, depth, is_maximizing):
    result = score(board)
    if result is not None:
        return result

    # cpu move -> maximize score
    if is_maximizing:
        best_score = -float('inf')
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 0:
                    board[row][col] = 2
                    score_ = minimax(board, depth + 1, False)
                    board[row][col] = 0
                    best_score = max(score_, best_score)
        return best_score
    # human move -> minimize score
    else:
        best_score = float('inf')
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 0:
                    board[row][col] = 1
                    score_ = minimax(board, depth + 1, True)
                    board[row][col] = 0
                    best_score = min(score_, best_score)
        return best_score


def best_move(board):
    best_score = -float('inf')
    move = None
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                board[row][col] = 2
                score_ = minimax(board, 0, False)
                board[row][col] = 0
                if score_ > best_score:
                    best_score = score_
                    move = (row, col)
    return move


def computer_move():
    if is_board_full():
        return  # Board is full, no move to make

    move = best_move(GAME_BOARD)
    if move is None:
        return  # No valid move found

    row, col = move
    GAME_BOARD[row][col] = 2
    draw_o(row, col)


# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_board()
                GAME_OVER_FLAG = False

        # only be able to place an x if the game is not over and the player is 1 (human)
        elif event.type == pygame.MOUSEBUTTONDOWN and not GAME_OVER_FLAG and PLAYER == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            cell_row = mouse_y // CELL_HEIGHT
            cell_col = mouse_x // CELL_WIDTH

            if GAME_BOARD[cell_row][cell_col] == 0:
                GAME_BOARD[cell_row][cell_col] = 1  # Player X move
                draw_x(cell_row, cell_col)
                check_for_x_win()
                PLAYER = 2  # switch to the computer

                if is_board_full() and not GAME_OVER_FLAG:
                    game_over(None)
                    pygame.display.set_caption("DRAW (TO PLAY AGAIN PRESS \"r\")")

    if PLAYER == 2 and not GAME_OVER_FLAG:
        computer_move()
        check_for_o_win()
        PLAYER = 1  # switch back to human

    # Fill the screen and draw the lines in each iteration
    if not GAME_OVER_FLAG:
        screen.fill(BLACK)
        draw_lines()

    # Draw the current board state
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if GAME_BOARD[row][col] == 1:
                draw_x(row, col)
            elif GAME_BOARD[row][col] == 2:
                draw_o(row, col)

    pygame.display.flip()

pygame.quit()
