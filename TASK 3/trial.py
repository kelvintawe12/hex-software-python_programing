import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 3, 3
LINE_WIDTH = 15
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (84, 84, 84)
BUTTON_COLOR = (0, 0, 0)
BUTTON_TEXT_COLOR = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# Board
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# Load music and sound effects
try:
    pygame.mixer.music.load("TASK 3/Show Me More.mp3")  # Local file for background music
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  # Loop the music
except pygame.error as e:
    print(f"Error loading music: {e}")

try:
    move_sound = pygame.mixer.Sound("TASK 3/Show Me More.mp3")
except pygame.error as e:
    print(f"Error loading sound: {e}")
    move_sound = None

# Draw lines
def draw_lines():
    for row in range(1, ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, row * HEIGHT // ROWS), (WIDTH, row * HEIGHT // ROWS), LINE_WIDTH)
    for col in range(1, COLS):
        pygame.draw.line(screen, LINE_COLOR, (col * WIDTH // COLS, 0), (col * WIDTH // COLS, HEIGHT), LINE_WIDTH)

draw_lines()

# Draw figures
def draw_figures():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * WIDTH // COLS + WIDTH // COLS // 2, row * HEIGHT // ROWS + HEIGHT // ROWS // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * WIDTH // COLS + SPACE, row * HEIGHT // ROWS + HEIGHT // ROWS - SPACE), (col * WIDTH // COLS + WIDTH // COLS - SPACE, row * HEIGHT // ROWS + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * WIDTH // COLS + SPACE, row * HEIGHT // ROWS + SPACE), (col * WIDTH // COLS + WIDTH // COLS - SPACE, row * HEIGHT // ROWS + HEIGHT // ROWS - SPACE), CROSS_WIDTH)

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

# Draw buttons
def draw_button(text, x, y, width, height, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, (170, 170, 170), (x, y, width, height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, (x, y, width, height))

    font = pygame.font.Font(None, 36)
    text_surf = font.render(text, True, BUTTON_TEXT_COLOR)
    text_rect = text_surf.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surf, text_rect)

# Restart game
def restart_game():
    global board, player, game_over
    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    player = 1
    game_over = False
    screen.fill(BG_COLOR)
    draw_lines()
    draw_buttons()

# Pause game
paused = False
def pause_game():
    global paused
    paused = True

# Resume game
def resume_game():
    global paused
    paused = False

# Draw buttons
def draw_buttons():
    draw_button("Restart", 50, 550, 100, 40, restart_game)
    draw_button("Pause", 250, 550, 100, 40, pause_game)
    draw_button("Resume", 450, 550, 100, 40, resume_game)

# Display winner popup
def display_winner(winner):
    font = pygame.font.Font(None, 74)
    text = font.render(f"Player {winner} wins!", True, (255, 255, 255))
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, rect)
    pygame.display.update()
    pygame.time.wait(2000)
    restart_game()

# Welcome dashboard
def welcome_dashboard():
    screen.fill(BG_COLOR)
    font = pygame.font.Font(None, 74)
    text = font.render("Welcome to Tic Tac Toe!", True, (255, 255, 255))
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(text, rect)
    draw_buttons()
    pygame.display.update()
    pygame.time.wait(2000)
    screen.fill(BG_COLOR)
    draw_lines()
    draw_buttons()

# Main loop
player = 1
game_over = False
welcome_dashboard()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and not paused:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = mouseY // (HEIGHT // ROWS)
            clicked_col = mouseX // (WIDTH // COLS)

            if board[clicked_row][clicked_col] == 0:
                board[clicked_row][clicked_col] = player
                if move_sound:
                    move_sound.play()
                player = 3 - player
                draw_figures()
                winner = check_winner()
                if winner != 0:
                    game_over = True
                    display_winner(winner)

    if paused:
        font = pygame.font.Font(None, 74)
        text = font.render("Paused", True, (255, 255, 255))
        rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, rect)
        pygame.display.update()

    pygame.display.update()