import os
import random

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'

def display_board(board):
    os.system('clear')

    print('')
    print('     |     |     ')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
    print('     |     |     ')
    print('-----+-----+-----')
    print('     |     |     ')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
    print('     |     |     ')
    print('-----+-----+-----')
    print('     |     |     ')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')
    print('     |     |     ')
    print('')

def initialise_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def prompt(message):
    print(f'==> {message}')

def empty_squares(board):
    return [key for key, value in board.items()
                     if value == INITIAL_MARKER]

def player_choose_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f'Choose a square ({', '.join(valid_choices)}):')
        square = input().strip()
        if square in valid_choices:
            break

        prompt('Sorry, that\'s not a valid choice')

    board[int(square)] = HUMAN_MARKER

def computer_choose_square(board):
    if len(empty_squares(board)) == 0:
        return
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return False

board = initialise_board()
display_board(board)

while True:
    player_choose_square(board)
    computer_choose_square(board)
    display_board(board)

    if someone_won(board) or board_full(board):
        break