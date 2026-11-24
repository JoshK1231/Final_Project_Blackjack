#GLOBAL CONSTANTS
BLACKJACK = 21
DEALER_HIT = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
DEALER_STAND = 17,18,19,20
CARDS = ("2","3","4","5","6","7","8","9","10","Jack","Queen","King", "Ace")
SUIT = ("Clubs", "Spades", "Hearts", "Diamonds")

def make_deck():
    deck = []
    for suit in SUIT:
        for card in CARDS:
            deck.append((card,suit))
            random.shuffle(deck)
    return deck
def buy_in():
    while True:
        try:
            bet = float(input("Enter buy in of at least $5: $"))
            if bet >= 5:
                return bet
            else:
                print("Buy in must be at least $5")
        except ValueError:
            print("Please enter a valid amount")
def deal_deck(deck, hand):
    """should deal 2 cards to your hand"""
    for card in range(2):
        hand.append(deck.pop())
    return hand
def count_hand(hand, score=0):
    """Count up the value of the cards in players hand."""
    score = 0
    aces = 0
    for card in hand:
        rank = card[0]
        if rank in ("Jack", "Queen", "King"):
            score += 10
        elif rank == "Ace":
            score += 11
            aces += 1
        else:
            score += int(rank)
    while score > BLACKJACK and aces > 0:
        score -= 10
        aces -= 1
    return score

def players_turn(deck, players_hand):
    """Asks the player to either hit or stand"""
    while count_hand(players,hand) < BLACKJACK:
        print("Your hand:" players_hand)
        print("Your score:", count_hand(players_hand))
        choice = input ("Hit or Stand?").lower()
        if choice == "hit":
            break
        else:
            print("Invalid. Enter either hit or stand.")
    
    return players_hand
def dealers_turn(deck,dealers_hand):
        """Deals the dealer another card if they draw under 17. Turn will end once they reach 17 or more"""
        while count_hand(dealers_hand) < DEALER_STAND:
             dealers_hand.append(deck.pop())
        return dealers_hand
def calculate_score(players_hand, dealers_hand, score):
     """Adds up scores and displays who the winner is."""
    players_score = count_hand(players_hand)
    dealers_score = count_hand(dealers_hand)
    if players_score > BLACKJACK:
        score = "You busted. The dealer wins the round"
    elif dealers_score > BLACKJACK:
        score = "Dealer busted. You won the round!"
    elif players_score > dealers_score:
        score = "You got {players_score} dealer got {dealers_score}. You win!"
    elif players_score < dealers_score:
        score = "You got {players_score}, dealer got {dealers_score}. Dealer wins."
    else:
        score = "It's a tie!"

    print("Players score:" players_score)
    print("Dealers score:" dealers_score)
    print(score)
    return score