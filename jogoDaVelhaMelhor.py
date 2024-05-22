import pygame
import sys

# Configurações iniciais
WIDTH = 400
HEIGHT = 400
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = int(SQUARE_SIZE * 0.3)
CIRCLE_WIDTH = int(SQUARE_SIZE * 0.1)
CROSS_WIDTH = int(SQUARE_SIZE * 0.2)
SPACE = int(SQUARE_SIZE * 0.2)

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Tabuleiro do jogo
board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]

# Funções auxiliares
def draw_lines():
    # Desenha as linhas do tabuleiro
    pygame.draw.line(screen, WHITE, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (0, 2*SQUARE_SIZE), (WIDTH, 2*SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (2*SQUARE_SIZE, 0), (2*SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_board():
    screen.fill(BLACK)
    draw_lines()

def draw_circle(row, col):
    pygame.draw.circle(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)

def draw_x(row, col):
    start_desc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
    end_desc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
    start_asc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
    end_asc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
    pygame.draw.line(screen, WHITE, start_desc, end_desc, CROSS_WIDTH)
    pygame.draw.line(screen, WHITE, start_asc, end_asc, CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] is None

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True

def check_win(player):
    # Verifica linhas
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    # Verifica colunas
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    # Verifica diagonais
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def main():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Jogo da Velha')
    screen.fill(BLACK)
    draw_board()

    game_over = False
    player_one_turn = True

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // SQUARE_SIZE
                row = y // SQUARE_SIZE

                if available_square(row, col):
                    if player_one_turn:
                        mark_square(row, col, 'O')
                        draw_circle(row, col)
                        if check_win('O'):
                            game_over = True
                    else:
                        mark_square(row, col, 'X')
                        draw_x(row, col)
                        if check_win('X'):
                            game_over = True

                    player_one_turn = not player_one_turn

        pygame.display.update()

if __name__ == "__main__":
    main()
