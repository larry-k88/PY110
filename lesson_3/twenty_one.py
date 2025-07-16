import os
import random
import json
import inflect

with open('twenty_one.json', 'r') as file:
    MESSAGES = json.load(file)

STARTING_NUMBER = 4
MAX_SCORE = 3
WINNING_TOTAL = 21
DEALER_LIMIT = 17

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
    prefix = 'Dealer has: ' if player_type == 'dealer' else 'You have:   '

    prompt(f'{prefix}{cards_str}, for a total of {total}')

def play_again():
    while True:
        print("-------------")
        answer = (input(MESSAGES["play_next_round"]).casefold().strip())
        if answer in ['y', 'yes', 'n', 'no']:
            return answer[0] == 'y'
        prompt(MESSAGES['play_next_round_error'])

def get_player_choice():
    while True:
        answer = input(MESSAGES['hit_or_stay']).casefold().strip()
        if answer in ['h', 'hit', 's', 'stay']:
            return answer[0]
        prompt(MESSAGES['hit_or_stay_error'])

def total_hand(cards, values):
    total = sum([values[card] for card in cards])

    aces = cards.count('Ace')
    while total > WINNING_TOTAL and aces:
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

        if choice == 's' or total > WINNING_TOTAL:
            break
    return total_hand(player, values)

def dealer_turn(dealer, deck, values):
    prompt(MESSAGES['dealer_turn'])

    while total_hand(dealer, values) < DEALER_LIMIT:
        prompt(MESSAGES['dealer_hit'])
        dealer.append(deck.pop())
        total = total_hand(dealer, values)
        display_cards(dealer, 'dealer', total)

    return total_hand(dealer, values)

def who_won(player_total, dealer_total):
    if player_total > WINNING_TOTAL:
        return 'player_busted'
    if dealer_total > WINNING_TOTAL:
        return 'dealer_busted'
    if player_total > dealer_total:
        return 'player'
    if player_total < dealer_total:
        return 'dealer'
    return 'tie'

def display_winner(player, dealer, player_total, dealer_total):
    print(MESSAGES['results'])
    display_cards(dealer, 'dealer', dealer_total)
    display_cards(player, 'player', player_total)
    match who_won(player_total, dealer_total):
        case 'player_busted':
            prompt(MESSAGES['player_busted'])
        case 'dealer_busted':
            prompt(MESSAGES['dealer_busted'])
        case 'player':
            prompt(MESSAGES['player_win_round'])
        case 'dealer':
            prompt(MESSAGES['dealer_win_round'])
        case 'tie':
            prompt(MESSAGES['tie'])

def update_scores(winner, scores):
    if winner in ('player', 'dealer_busted'):
        scores['player'] += 1
    elif winner in ('dealer', 'player_busted'):
        scores['dealer'] += 1
    return scores

def display_scores(scores):
    print(f'SCORES:'
          f'\nPlayer: {scores['player']}\nDealer: {scores['dealer']}\n')

def play_single_game():

    current_deck = initialise_deck(CARD_VALUES, STARTING_NUMBER)
    player_cards = deal(current_deck)
    dealer_cards = deal(current_deck)

    player_total = total_hand(player_cards, CARD_VALUES)
    dealer_total = total_hand(dealer_cards, CARD_VALUES)

    prompt(f'Dealer has: {dealer_cards[0]} and ??')
    display_cards(player_cards, 'player', player_total)

    player_total = player_turn(player_cards, current_deck, CARD_VALUES)

    if player_total > WINNING_TOTAL:
        display_winner(player_cards, dealer_cards, player_total, dealer_total)
        return who_won(player_total, dealer_total)

    prompt(f'You chose to stay at {player_total}\n')

    dealer_total = dealer_turn(dealer_cards, current_deck, CARD_VALUES)

    if dealer_total > WINNING_TOTAL:
        display_winner(player_cards, dealer_cards, player_total, dealer_total)
        return who_won(player_total, dealer_total)

    prompt(f'Dealer stays at {dealer_total}')

    display_winner(player_cards, dealer_cards, player_total, dealer_total)

    return who_won(player_total, dealer_total)

### main code starts here
current_scores = {'player': 0, 'dealer': 0}
current_round = 1
p = inflect.engine()

prompt(f'Welcome to {p.number_to_words(WINNING_TOTAL).title()}'
       f' - first to {MAX_SCORE} rounds is the winner! \n')

while True:

    prompt(MESSAGES['deal_rules_exit'])
    start_game = input()
    if start_game.casefold().strip() == 'exit':
        break
    if start_game.casefold().strip() == 'rules':
        prompt(MESSAGES['rules'])
        prompt(MESSAGES['continue'])
        input()

    os.system('clear')
    prompt(f'Round {current_round}\n')
    current_round += 1

    display_scores(current_scores)
    round_winner = play_single_game()
    current_scores = update_scores(round_winner, current_scores)
    print()
    display_scores(current_scores)

    if current_scores['player'] == MAX_SCORE:
        prompt(MESSAGES['play_win_game'])
        break
    if current_scores['dealer'] == MAX_SCORE:
        prompt(MESSAGES['dealer_win_game'])
        break

    if not play_again():
        break