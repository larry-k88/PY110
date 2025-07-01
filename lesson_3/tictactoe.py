import os
import random

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
WINING_SCORE = 5

def display_board(board):
    os.system('clear')

    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
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

def join_or(lst, separator1=', ', separator2='or'):
    match len(lst):
        case 0:
            return ''
        case 1:
            return str(lst[0])
        case 2:
            return f"{lst[0]} {separator2} {lst[1]}"

    first_elements = ''.join([f'{element}{separator1}' for element in lst[0:-1]])
    final_element = f'{separator2} {lst[-1]}'

    return first_elements + final_element

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
        prompt(f'Choose a square ({join_or(valid_choices)}):')
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
    return bool(detect_winner(board))

def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
            and board[sq2] == HUMAN_MARKER
            and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
            and board[sq2] == COMPUTER_MARKER
            and board[sq3] == COMPUTER_MARKER):
            return 'Computer'

    return None

def play_tic_tac_toe():
    while True:
        board = initialise_board()

        while True:
            display_board(board)

            player_choose_square(board)
            if someone_won(board) or board_full(board):
                break
            
            computer_choose_square(board)
            if someone_won(board) or board_full(board):
                break

        display_board(board)

        if someone_won(board):
            prompt(f'{detect_winner(board)} won!')
        else:
            prompt('It\'s a tie!')
        
        prompt('Do you want to play again? (y or n)')
        answer = input().lower()
        if answer != 'y':
            break

    prompt('Thanks for playing Tic Tac Toe')

play_tic_tac_toe()
