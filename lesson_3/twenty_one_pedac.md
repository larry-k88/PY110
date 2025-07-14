Problem:

  - Code the game twenty-one 
     
  - Explicit requirements:
      - Standard 52 card deck
      - 2 players, 2 cards each (player sees both theirs but only 1 of dealer's)
      - Over 21 is bust and a loss
      - Aces are either 1 or 11, depending on the hand
      - 10, J, Q, K are all worth 10
  - Implicit requirements:
      - 2 or more aces in the hand can be worth different amounts
      - Dealer must hit until total is >= 17, then stay
      - Suit is irrelevant
  - Questions
      - 

Examples/Test Cases:
  - to follow

Data Structure:
  - Input: String command, either hit or stay
  - Output: String saying if player won or lost
    
  - Intermediate: Deck - nested list or dict

High-level strategies:
1. Initialize deck
2. Deal cards to player and dealer
3. Player turn: hit or stay
    a. Ask player to hit or stay.
    b. If stay, stop asking.
    c. Otherwise, go to a.
   - repeat until bust, or stay
4. If player bust, dealer wins.
5. Dealer turn: hit or stay
   - repeat until total >= 17
6. If dealer busts, player wins.
7. Compare cards and declare winner.

Algorithm:  

  # Language agnostic for a non-programmer
  # Helper functions
  # Descriptive variable names
  # Run test cases through algo
  - 


