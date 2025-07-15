import os
import random

STARTING_NUMBER = 4

CARD_VALUES = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11,
}

def prompt(message):
    print(f'==> {message}')

def join_and(lst, separator1=', ', separator2='and'):
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

def initialise_deck(cards, starting_number):
    starting_deck = list(cards) * starting_number
    random.shuffle(starting_deck)
    return starting_deck

def deal(deck):
    return [deck.pop(), deck.pop()]

def display_cards(player, player_type, total):
    cards_str = join_and(list(player))

    if player_type == 'dealer': # issues - LSBot
        prompt(f'Dealer has: {cards_str}, for a total of '
               f'{total}')
    if player_type == 'player':
        prompt(f'You have:   {cards_str}, for a total of '
               f'{total}')

def play_again():
    while True:
        print("-------------")
        answer = input('Do you want to play again? '
                       '(y or n)\n').casefold().strip()
        if answer in ['y', 'yes', 'n', 'no']:
            return answer[0] == 'y'
        prompt('Please enter "y" or "n"')

def get_player_choice():
    while True:
        answer = input('Do you want to (h)it or (s)tay? ').casefold().strip()
        if answer in ['h', 'hit', 's', 'stay']:
            return answer[0]
        prompt('Please enter "h" or "s"')

def total_hand(cards, values):
    total = sum([values[card] for card in cards])

    aces = cards.count('Ace')
    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total

def player_turn(player, deck, values):
    while True:
        choice = get_player_choice()
        if choice == 'h':
            player.append(deck.pop())
            total = total_hand(player, values)
            display_cards(player, 'player', total)

        if choice == 's' or total > 21:
            break
    return total_hand(player, values)

def dealer_turn(dealer, deck, values):
    prompt('Dealer\'s turn:')

    while total_hand(dealer, values) < 17:
        prompt('Dealer hits!')
        dealer.append(deck.pop())
        total = total_hand(dealer, values)
        display_cards(dealer, 'dealer', total)

    return total_hand(dealer, values)

def who_won(player_total, dealer_total):
    if player_total > 21:
        return 'player_busted'
    if dealer_total > 21:
        return 'dealer_busted'
    if player_total > dealer_total:
        return 'player'
    if player_total < dealer_total:
        return 'dealer'
    return 'tie'

def display_winner(player, dealer, player_total, dealer_total):
    print('\nRESULTS')
    display_cards(dealer, 'dealer', dealer_total)
    display_cards(player, 'player', player_total)
    match who_won(player_total, dealer_total):
        case 'player_busted':
            prompt('You went bust - Dealer wins!')
        case 'dealer_busted':
            prompt('Dealer went bust - you win!')
        case 'player':
            prompt('You win!')
        case 'dealer':
            prompt('Dealer wins!')
        case 'tie':
            prompt('It\'s a tie!')

def play_single_game():

    current_deck = initialise_deck(CARD_VALUES, STARTING_NUMBER)
    player_cards = deal(current_deck)
    dealer_cards = deal(current_deck)

    player_total = total_hand(player_cards, CARD_VALUES)
    dealer_total = total_hand(dealer_cards, CARD_VALUES)

    prompt(f'Dealer has: {dealer_cards[0]} and ?')
    display_cards(player_cards, 'player', player_total)

    player_total = player_turn(player_cards, current_deck, CARD_VALUES)

    if player_total > 21:
        display_winner(player_cards, dealer_cards, player_total, dealer_total)
        return

    prompt(f'You chose to stay at {player_total}\n')

    dealer_total = dealer_turn(dealer_cards, current_deck, CARD_VALUES)

    if dealer_total > 21:
        display_winner(player_cards, dealer_cards, player_total, dealer_total)
        return

    prompt(f'Dealer stays at {dealer_total}')

    display_winner(player_cards, dealer_cards, player_total, dealer_total)

### main code starts here
while True:
    os.system('clear')

    prompt('Welcome to Twenty One! ' \
    'Press any key to deal the cards, or type "exit" to quit')

    start_game = input()
    if start_game.casefold() == 'exit':
        break

    play_single_game()

    if not play_again():
        break