import minimax
import numpy as np

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-'*len(row)*3)

def get_best_move(board, depth=3):
    best_score = float('-inf')
    best_move = None
    for move in range(9):
        if board[move//3][move%3] == ' ':
            board[move//3][move%3] = 'X'
            score = minimax.minimax(board, depth, False)
            board[move//3][move%3] = ' '
            if score > best_score:
                best_score = score
                best_move = move
    return best_move

def play_game():
    board = np.zeros((3, 3), dtype=str)
    current_player = 'X'
    while True:
        print_board(board.tolist())
        if current_player == 'X':
            move = int(input("Player X, enter your move (0-8): "))
            board[move//3][move%3] = 'X'
        else:
            move = get_best_move(board.tolist())
            board[move//3][move%3] = 'O'
        if minimax.check_win(board.tolist()):
            print_board(board.tolist())
            print(f"Player {'X' if current_player == 'O' else 'O'} wins!")
            break
        if ' ' not in board.flatten():
            print_board(board.tolist())
            print("It's a draw!")

play_game()
