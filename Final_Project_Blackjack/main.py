"""Blackjack games main program"""
import blackjack
import data_store
#TODO figure out how I want to store player info
"""I am trying to think of a way to store these scores without entering your name, as blackjack does not ask for player names"""
def main():
    balance = blackjack.buy_in()

    while balance > 5:
        deal = blackjack.make_deck()
        players_hand = []
        dealers_hand = []
        player_hand = blackjack.deal_cards(deck, players_hand)
        dealers_hand = blackjack.deal_cards(deck, dealers hand)
        player_hand =blackjack.players_turn(deck, players_hand)
        dealer_hand = blackjack.dealers_turn(deck,dealers_hand)
        if blackjack.count_hand(players_hand, 0) <= blackjack.BLACKJACK:
            dealers_hand = blackjack.dealers_turn(deck, dealers_hand)
        score = blackjack.calculate_score(players_hand, dealers_hand, 0)
        print("Results:", results)
        print(f"Balance: ${balance:.2f}")

    if balance >= 10:
        choice = input(int("Place a bet of at least $10 to keep playing yes?no: ").lower()
        if choice != "yes":
        break
    else:
        print("You must have a balance of at least $10 to play.")
    
    #TODO allow the player to deposit money to add to the balance

     print("Balance: ${balance:.2f}")
           
main()
    