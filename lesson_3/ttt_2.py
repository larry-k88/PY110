import random 

def display_board(board):
    print(' _________________')
    print('|     |     |     |')
    print(f'|  {board[1]}  |  {board[2]}  |  {board[3]}  |')
    print('|_____|_____|_____|')   
    print('|     |     |     |')
    print(f'|  {board[4]}  |  {board[5]}  |  {board[6]}  |')
    print('|_____|_____|_____|')
    print('|     |     |     |')
    print(f'|  {board[7]}  |  {board[8]}  |  {board[9]}  |')
    print('|_____|_____|_____|')

def initialise_board():
    return {square: ' ' for square in range(1, 10)}

def player_choose_square(board):
    while True:
        valid_squares = [square for square in board if not square == ' ']
        print(f'Choose a square from: {valid_squares}')
        player_choice = input()
        if int(player_choice) in valid_squares:
            break

        print('That wasn\'t a valid choice, please try again')
    board[player_choice] = 'x'

def computer_choose_square(board):
    valid_squares = [square for square in board if not square == ' ']
    computer_choice = random.choice(valid_squares)
    print(computer_choice)
    board[computer_choice] = 'o'

board = initialise_board()
display_board(board)

player_choose_square(board)
computer_choose_square(board)
display_board(board)