import os
import random

INITIAL_MARKER = ' '
PLAYER_MARKER = 'X'
COMPUTER_MARKER = 'O'
WINING_SCORE = 3
DEFAULT_SQUARE = 5
WINNING_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],    # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],    # Columns
        [1, 5, 9], [3, 5, 7]                # Diagonals
    ]

def display_board(board):
    os.system('clear')

    prompt(f"You are {PLAYER_MARKER}. Computer is {COMPUTER_MARKER}.")
    prompt(f'First to win {WINING_SCORE} rounds will win the match!')
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

def find_at_risk_sq(line, board, marker):
    markers_in_line = [board[square] for square in line]

    if markers_in_line.count(marker) == 2:
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square
    return None

def player_choose_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f'Choose a square ({join_or(valid_choices)}):')
        square = input().strip()
        if square in valid_choices:
            break

        prompt('Sorry, that\'s not a valid choice')

    board[int(square)] = PLAYER_MARKER

def computer_choose_square(board):
    if len(empty_squares(board)) == 0:
        return

    square = None

    for line in WINNING_LINES: # offence
        square = find_at_risk_sq(line, board, COMPUTER_MARKER)
        if square:
            break

    if not square:
        for line in WINNING_LINES: # defence
            square = find_at_risk_sq(line, board, PLAYER_MARKER)
            if square:
                break

    if not square and DEFAULT_SQUARE in empty_squares(board):
        square = DEFAULT_SQUARE       

    if not square: # no defence or offence
        square = random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == PLAYER_MARKER
            and board[sq2] == PLAYER_MARKER
            and board[sq3] == PLAYER_MARKER):
            return 'Player'
        if (board[sq1] == COMPUTER_MARKER
            and board[sq2] == COMPUTER_MARKER
            and board[sq3] == COMPUTER_MARKER):
            return 'Computer'

    return None

def display_scores(player, computer):
    print(f'Scores: \nPlayer: {player} \nComputer: {computer}')

def display_winner(player, computer, board):
    if player > computer:
        prompt(f'{detect_winner(board)} won the match')
    else:
        prompt(f'{detect_winner(board)} won the match')

def play_tic_tac_toe():
    while True:
        player_score = 0
        computer_score = 0
        while WINING_SCORE not in (player_score, computer_score):
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
                prompt(f'{detect_winner(board)} won this round!')

                if detect_winner(board) == 'Player':
                    player_score += 1
                if detect_winner(board) == 'Computer':
                    computer_score += 1

            else:
                prompt('It\'s a tie!')

            display_scores(player_score, computer_score)

            if WINING_SCORE in (player_score, computer_score):
                display_winner(player_score, computer_score, board)
                break

            prompt('Do you want to play the next round? (y or n)')
            answer = input().lower()
            if answer != 'y':
                break

        prompt('Do you want to start a new match? (y or n)')
        answer = input().lower()
        if answer != 'y':
            break

    prompt('Thanks for playing Tic Tac Toe')

play_tic_tac_toe()
