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
PLAYER_DISPLAY_NAME = 'Player'
COMPUTER_DISPLAY_NAME = 'Computer'
PLAYERS = {
    'Player': ['player', 'p', 'pl'],
    'Computer': ['computer', 'c', 'comp'],
    }
START_FIRST = 'Choose'

def display_board(board):
    os.system('clear')

    prompt(f'{PLAYER_DISPLAY_NAME} is {PLAYER_MARKER}. '
           f'{COMPUTER_DISPLAY_NAME} is {COMPUTER_MARKER}.')
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

    first_elements = ''.join([f'{element}{separator1}'
                             for element in lst[0:-1]])
    final_element = f'{separator2} {lst[-1]}'

    return first_elements + final_element

def initialise_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def prompt(message):
    print(f'==> {message}')

def who_starts(first_player):
    if first_player in PLAYERS:
        return first_player

    while True:
        prompt(f'Who goes first? Enter "{PLAYER_DISPLAY_NAME}" or '
               f'"{COMPUTER_DISPLAY_NAME}")')
        player_choice = input().lower()
        for player, variations in PLAYERS.items():
            if player_choice in variations:
                return player

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
            return PLAYER_DISPLAY_NAME
        if (board[sq1] == COMPUTER_MARKER
            and board[sq2] == COMPUTER_MARKER
            and board[sq3] == COMPUTER_MARKER):
            return COMPUTER_DISPLAY_NAME
    return None

def update_scores(board, scores):
    if detect_winner(board) == PLAYER_DISPLAY_NAME:
        scores['player'] += 1
    if detect_winner(board) == COMPUTER_DISPLAY_NAME:
        scores['computer'] += 1
    return scores

def display_scores(scores):
    print(f'Scores: \n'
          f'{PLAYER_DISPLAY_NAME}: {scores['player']}\n'
          f'{COMPUTER_DISPLAY_NAME}: {scores['computer']}')

def display_round_winner(board):
    if someone_won(board):
        prompt(f'{detect_winner(board)} won this round!')
    else:
        prompt('It\'s a tie!')

def display_match_winner(scores):
    if scores['player'] > scores['computer']:
        prompt(f'{PLAYER_DISPLAY_NAME} won the match')
    else:
        prompt(f'{COMPUTER_DISPLAY_NAME} won the match')

def play_another_round():
    prompt('Do you want to play the next round? (y or n)')
    while True:
        answer = input().lower()
        if answer == 'y':
            return True
        if answer == 'n':
            return False
        prompt('Do you want to play the next round? (y or n)')

def play_another_match():
    prompt('Do you want to start a new match? (y or n)')
    while True:
        answer = input().lower()
        if answer == 'y':
            return True
        if answer == 'n':
            return False
        prompt('Do you want to start a new match? (y or n)')

def choose_square(board, current_player):
    if current_player == PLAYER_DISPLAY_NAME:
        player_choose_square(board)
    if current_player == COMPUTER_DISPLAY_NAME:
        computer_choose_square(board)


def alternate_player(current_player):
    return (COMPUTER_DISPLAY_NAME if current_player == PLAYER_DISPLAY_NAME
            else PLAYER_DISPLAY_NAME)

def play_tic_tac_toe():
    while True:
        scores = {'player': 0, 'computer': 0}
        current_player = who_starts(START_FIRST)

        while WINING_SCORE not in (scores.values()):
            board = initialise_board()

            while True:
                display_board(board)
                choose_square(board, current_player)
                current_player = alternate_player(current_player)
                if someone_won(board) or board_full(board):
                    break

            display_board(board)
            display_round_winner(board)
            update_scores(board, scores)
            display_scores(scores)

            if WINING_SCORE in scores.values():
                display_match_winner(scores)
                break
            if not play_another_round():
                break

        if not play_another_match():
            break

    prompt('Thanks for playing Tic Tac Toe')

play_tic_tac_toe()
