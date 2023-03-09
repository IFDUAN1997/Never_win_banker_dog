import random

# Define the starting fund and bet amount
fund = 10000
bet = 100

# Define the cards and their values
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
values = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}

# Define the optimal strategy table
strategy_table_hit_soft17 = {
    (5, 2): "hit",
    (5, 3): "hit",
    (5, 4): "hit",
    (5, 5): "hit",
    (5, 6): "hit",
    (5, 7): "hit",
    (5, 8): "hit",
    (5, 9): "hit",
    (5, 10): "hit",
    (5, 11): "hit",
    (6, 2): "hit",
    (6, 3): "hit",
    (6, 4): "hit",
    (6, 5): "hit",
    (6, 6): "hit",
    (6, 7): "hit",
    (6, 8): "hit",
    (6, 9): "hit",
    (6, 10): "hit",
    (6, 11): "hit",
    (7, 2): "hit",
    (7, 3): "hit",
    (7, 4): "hit",
    (7, 5): "hit",
    (7, 6): "hit",
    (7, 7): "hit",
    (7, 8): "hit",
    (7, 9): "hit",
    (7, 10): "hit",
    (7, 11): "hit",
    (8, 2): "hit",
    (8, 3): "hit",
    (8, 4): "hit",
    (8, 5): "hit",
    (8, 6): "hit",
    (8, 7): "hit",
    (8, 8): "hit",
    (8, 9): "hit",
    (8, 10): "hit",
    (8, 11): "hit",
    (9, 2): "hit",
    (9, 3): "hit",
    (9, 4): "hit",
    (9, 5): "hit",
    (9, 6): "hit",
    (9, 7): "hit",
    (9, 8): "hit",
    (9, 9): "hit",
    (9, 10): "hit",
    (9, 11): "hit",
    (10, 2): "hit",
    (10, 3): "hit",
    (10, 4): "hit",
    (10, 5): "hit",
    (10, 6): "hit",
    (10, 7): "hit",
    (10, 8): "hit",
    (10, 9): "hit",
    (10, 10): "hit",
    (10, 11): "hit",
    (11, 2): "hit",
    (11, 3): "hit",
    (11, 4): "hit",
    (11, 5): "hit",
    (11, 6): "hit",
    (11, 7): "hit",
    (11, 8): "hit",
    (11, 9): "hit",
    (11, 10): "hit",
    (11, 11): "hit",
    (12, 2): "hit",
    (12, 3): "hit",
    (12, 4): "stand",
    (12, 5): "stand",
    (12, 6): "stand",
    (12, 7): "hit",
    (12, 8): "hit",
    (12, 9): "hit",
    (12, 10): "hit",
    (12, 11): "hit",
    (13, 2): "stand",
    (13, 3): "stand",
    (13, 4): "stand",
    (13, 5): "stand",
    (13, 6): "stand",
    (13, 7): "hit",
    (13, 8): "hit",
    (13, 9): "hit",
    (13, 10): "hit",
    (13, 11): "hit",
    (14, 2): "stand",
    (14, 3): "stand",
    (14, 4): "stand",
    (14, 5): "stand",
    (14, 6): "stand",
    (14, 7): "hit",
    (14, 8): "hit",
    (14, 9): "hit",
    (14, 10): "hit",
    (14, 11): "hit",
    (15, 2): "stand",
    (15, 3): "stand",
    (15, 4): "stand",
    (15, 5): "stand",
    (15, 6): "stand",
    (15, 7): "hit",
    (15, 8): "hit",
    (15, 9): "hit",
    (15, 10): "hit",
    (15, 11): "hit",
    (16, 2): "stand",
    (16, 3): "stand",
    (16, 4): "stand",
    (16, 5): "stand",
    (16, 6): "stand",
    (16, 7): "hit",
    (16, 8): "hit",
    (16, 9): "hit",
    (16, 10): "hit",
    (16, 11): "hit",
    (17, 2): "stand",
    (17, 3): "stand",
    (17, 4): "stand",
    (17, 5): "stand",
    (17, 6): "stand",
    (17, 7): "stand",
    (17, 8): "stand",
    (17, 9): "stand",
    (17, 10): "stand",
    (17, 11): "stand",
}

# Define the function to deal a card
def deal_card():
    card = random.choice(cards)
    value = values[card]
    return card, value

# Define the function to calculate the total value of a hand
def calculate_hand(hand):
    """Calculate the total value of a hand"""
    total_value = sum(hand)
    # If the hand contains an Ace and the total value is less than or equal to 11,
    # add 10 to the total value
    if 1 in hand and total_value <= 11:
        total_value += 10
    return total_value

# Define the function to play the player's turn
def play_player_turn(player_hand, dealer_card):
    """Play the player's turn"""
    while True:
        player_total = calculate_hand(player_hand)
    # If the player has a total of 21, stand
        if player_total == 21:
            return "stand"
        # If the player has a soft 20, stand
        if player_total == 20 and 1 in player_hand:
            return "stand"
        # If the player has a pair of Aces or 8s, split
        if len(player_hand) == 2 and player_hand[0] == player_hand[1]:
            if player_hand[0] == 1 or player_hand[0] == 8:
                return "split"
        # If the player has a hard total of 17 or higher, stand
        if player_total >= 17 and not 1 in player_hand:
            return "stand"
        # If the player has a hard total of 12 to 16 and the dealer's card is between 2 and 6, stand
        if player_total >= 12 and player_total <= 16 and dealer_card in range(2, 7):
            return "stand"
        # If none of the above conditions are met, use the basic strategy to decide whether to hit or stand
        if (player_total, dealer_card) in strategy_table_hit_soft17:
            return strategy_table_hit_soft17[(player_total, dealer_card)]
        else:
            return "hit"
        
# Define the function to play the dealer's turn
def play_dealer_turn(dealer_hand):
    """Play the dealer's turn"""
    while True:
        dealer_total = calculate_hand(dealer_hand)
        if dealer_total >= 17:
            return "stand"
        if dealer_total < 17:
            return "hit"

# Define the function to play a round of the game
def play_round(player_funds, bet_amount):
    """Play one round of the game"""
    # Deal cards
    deck = create_deck()
    player_hand, dealer_hand = deal_cards(deck)
    
    # Check for player blackjack
    player_total = calculate_hand(player_hand)
    if player_total == 21:
        player_funds += bet_amount * 2.5
        return player_funds, "Player"
    
    # Play player's hand
    while True:
        player_total = calculate_hand(player_hand)
        dealer_up_card = dealer_hand[0]
        if player_total >= 17:
            break
        elif player_total <= 8:
            player_hand.append(deck.pop())
        elif player_total >= 12 and dealer_up_card >= 7:
            player_hand.append(deck.pop())
        else:
            break
    
    # Play dealer's hand
    while True:
        dealer_total = calculate_hand(dealer_hand)
        if dealer_total >= 17:
            break
        elif dealer_total <= 16:
            dealer_hand.append(deck.pop())
    
    # Determine winner
    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)
    if player_total > 21:
        return player_funds, "Dealer"
    elif dealer_total > 21:
        player_funds += bet_amount * 2
        return player_funds, "Player"
    elif player_total == dealer_total:
        player_funds += bet_amount
        return player_funds, None
    elif player_total > dealer_total:
        player_funds += bet_amount * 2
        return player_funds, "Player"
    else:
        return player_funds, "Dealer"
# Define the function to run the game
def run_game(num_rounds, starting_funds, bet_amount):
    """Run the game"""
    player_funds = starting_funds
    for i in range(num_rounds):
        if player_funds < bet_amount:
            print("You don't have enough funds to place a bet. Game over!")
        break
    print(f"Round {i+1}:")
    print(f"Player funds: ${player_funds}")
    player_funds, winner = play_round(player_funds, bet_amount)
    if winner is None:
        print("Push")
    elif winner == "Player":
        print("Player wins")
    else:
        print("Dealer wins")
        print(f"Player funds: ${player_funds}")
        print("===============")
        print("Game over!")


        