import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions and settings
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# Colors (Default Theme)
BG_COLOR = (156, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Tic-Tac-Toe")
screen.fill(BG_COLOR)

# Board and game state
ROWS, COLS = 3, 3
board = [[0] * COLS for _ in range(ROWS)]
player = 1  # Player 1 starts
game_over = False

# Draw grid
def draw_grid():
    for row in range(1, ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, row * HEIGHT // ROWS), (WIDTH, row * HEIGHT // ROWS), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (row * WIDTH // COLS, 0), (row * WIDTH // COLS, HEIGHT), LINE_WIDTH)

# Draw shapes
def draw_shapes():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 1:
                pygame.draw.circle(
                    screen,
                    CIRCLE_COLOR,
                    (col * WIDTH // COLS + WIDTH // COLS // 2, row * HEIGHT // ROWS + HEIGHT // ROWS // 2),
                    CIRCLE_RADIUS,
                    CIRCLE_WIDTH,
                )
            elif board[row][col] == 2:
                pygame.draw.line(
                    screen,
                    CROSS_COLOR,
                    (col * WIDTH // COLS + SPACE, row * HEIGHT // ROWS + SPACE),
                    (col * WIDTH // COLS + WIDTH // COLS - SPACE, row * HEIGHT // ROWS + HEIGHT // ROWS - SPACE),
                    CROSS_WIDTH,
                )
                pygame.draw.line(
                    screen,
                    CROSS_COLOR,
                    (col * WIDTH // COLS + WIDTH // COLS - SPACE, row * HEIGHT // ROWS + SPACE),
                    (col * WIDTH // COLS + SPACE, row * HEIGHT // ROWS + HEIGHT // ROWS - SPACE),
                    CROSS_WIDTH,
                )

# Check for winner
def check_winner():
    # Check rows, columns, and diagonals
    for row in range(ROWS):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != 0:
            return board[row][0]
    for col in range(COLS):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]
    return 0

# Check if the board is full
def is_full():
    for row in board:
        if 0 in row:
            return False
    return True

# Computer move
def computer_move():
    empty_cells = [(row, col) for row in range(ROWS) for col in range(COLS) if board[row][col] == 0]
    if empty_cells:
        move = random.choice(empty_cells)
        board[move[0]][move[1]] = 2

# Restart the game
def restart_game():
    global board, player, game_over
    board = [[0] * COLS for _ in range(ROWS)]
    player = 1
    game_over = False
    screen.fill(BG_COLOR)
    draw_grid()

# Main game loop
def main():
    global player, game_over

    draw_grid()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                row, col = y // (HEIGHT // ROWS), x // (WIDTH // COLS)

                # Player move
                if board[row][col] == 0:
                    board[row][col] = player
                    if check_winner() == 1:
                        print("Player wins!")
                        game_over = True
                    elif is_full():
                        print("It's a tie!")
                        game_over = True
                    else:
                        # Computer's turn
                        computer_move()
                        if check_winner() == 2:
                            print("Computer wins!")
                            game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Press 'R' to restart
                    restart_game()

        # Draw board and update screen
        screen.fill(BG_COLOR)
        draw_grid()
        draw_shapes()
        pygame.display.update()

# Run the game
if __name__ == "__main__":
    main()