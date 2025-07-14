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

def display_cards(player, values):
    if player == dealer_cards:
        prompt(f'Dealer has: {join_and(list(player))}, for a total of '
               f'{total_hand(player, values)}')
    if player == player_cards:
        prompt(f'You have:   {join_and(list(player))}, for a total of '
               f'{total_hand(player, values)}')

def play_again():
    print("-------------")
    answer = input('Do you want to play again? (y or n) ')
    return answer == 'y'

def total_hand(cards, values):
    total = sum([values[card] for card in cards])

    aces = cards.count('Ace')
    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total

def busted(hand, values):
    return total_hand(hand, values) > 21

def who_won(player, dealer, values):
    player_total = total_hand(player, values)
    dealer_total = total_hand(dealer, values)

    if player_total > 21:
        return 'player_busted'
    if dealer_total > 21:
        return 'dealer_busted'
    if player_total > dealer_total:
        return 'player'
    if player_total < dealer_total:
        return 'dealer'
    return 'tie'

def display_winner(player, dealer, values):
    print('\nRESULTS')
    display_cards(dealer, values)
    display_cards(player_cards, values)
    match who_won(player, dealer, values):
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

### main code starts here
while True:
    os.system('clear')

    prompt('Welcome to Twenty One! ' \
    'Press any key to deal the cards, or type "exit" to quit\n')

    start_game = input()
    if start_game in ['Exit', 'exit']:
        break

    current_deck = initialise_deck(CARD_VALUES, STARTING_NUMBER)
    player_cards = deal(current_deck)
    dealer_cards = deal(current_deck)

    prompt(f'Dealer has: {dealer_cards[0]} and ?')
    display_cards(player_cards, CARD_VALUES)

    while True:
        player_choice = input('\nDo you want to (h)it or (s)tay?\n')
        if player_choice not in ['h', 's']:
            prompt('Please enter "h" or "s"')
            continue

        if player_choice == 'h':
            player_cards.append(current_deck.pop())
            display_cards(player_cards, CARD_VALUES)

        if player_choice == 's' or busted(player_cards, CARD_VALUES):
            break

    if busted(player_cards, CARD_VALUES):
        display_winner(player_cards, dealer_cards, CARD_VALUES)

        if play_again():
            continue
        else:
            break

    else:
        prompt(f'You chose to stay at {total_hand(player_cards, CARD_VALUES)}\n')

    # dealer's turn
    prompt('Dealer\'s turn:')

    while total_hand(dealer_cards, CARD_VALUES) < 17:
        prompt('Dealer hits!')
        dealer_cards.append(current_deck.pop())
        display_cards(dealer_cards, CARD_VALUES)

    if busted(dealer_cards, CARD_VALUES):
        display_winner(player_cards, dealer_cards, CARD_VALUES)

        if play_again():
            continue
        else:
            break

    else:
        prompt(f'Dealer stays at {total_hand(dealer_cards, CARD_VALUES)}')

    display_winner(player_cards, dealer_cards, CARD_VALUES)

    if not play_again():
        break