from random import shuffle
from time import sleep

class Card:

    def __init__(self, suit, char):
        self.suit = suit
        self.char = char

    def __repr__(self):
        return f"{self.char}{self.suit}"


class Deck:
    """Pack of 52 standard Cards."""

    def __init__(self):

        chars = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        suits = ["♥", "♣", "♠", "♦"]
        self.cards = [Card(suit, char)
                      for suit in suits
                        for char in chars]

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop()
        else:
            print("Oops! We ran out of cards.")    


class Hand:

    def __init__(self):
        self.cards = []

    def __repr__(self):
        return f"{self.cards}"

    def hit(self, deck):
        self.cards.append(deck.deal())

    def get_play_value(self):
        
        play_value = 0
        aces = 0

        for card in self.cards:
            if str(card.char).isnumeric():
                play_value += card.char
            elif card.char == "A":
                play_value += 11
                aces += 1
            else:
                play_value += 10

        while aces and play_value > 21:
            play_value -= 10
            aces -= 1

        return play_value

    def get_hit_value(self):

        hit_value = 0

        for card in self.cards:
            if str(card.char).isnumeric():
                hit_value += card.char
            elif card.char == "A":
                hit_value += 1
            else:
                hit_value += 10

        return hit_value


class Game:

    def __init__(self):
        deck = Deck()
        shuffle(deck.cards)

        player_hand = Hand()
        dealer_hand = Hand()
        stop = False

        player_hand.hit(deck)
        player_hand.hit(deck)

        print("\n\nWelcome to the blackjack table. Let's play!")
        sleep(1)
        print(f"\n\nYou start. Your hand: {player_hand}")

        while stop == False:
            if player_hand.get_play_value() == 21:
                stop = True
                print("You reached 21!")
            
            elif player_hand.get_play_value() > 21:
                stop = True
                print("Oops – you bust!")
            
            else:
                player_input = input("Would you like to hit? (y/n):")

                if player_input == "y":
                    player_hand.hit(deck)
                    print(f"\nYou hit. Your hand: {player_hand}")
                    
                else:
                    stop = True
                    print("\nYou stay.")

        dealer_hand.hit(deck)
        dealer_hand.hit(deck)
        sleep(2)

        print(f"\n\nDealer's turn. Dealer's hand: {dealer_hand}")
        while dealer_hand.get_hit_value() < 17:
            dealer_hand.hit(deck)
            sleep(2)
            print(f"\nDealer hits. Dealer's hand: {dealer_hand}")

        sleep(2)
        if dealer_hand.get_play_value() > 21:
            print("Oops - dealer busts!")
        elif dealer_hand.get_play_value() == 21:
            print("Dealer reached 21!")
        else:
            print("\nDealer stays.")

        player_score = player_hand.get_play_value()
        dealer_score = dealer_hand.get_play_value()

        sleep(2)
        print("\n\nFINAL SCORES")
        print(f"You: {player_score}")
        print(f"Dealer: {dealer_score}\n")

        if (player_score > dealer_score and player_score <= 21) \
            or (player_score <= 21 and dealer_score >= 21):
            print("You win!")
        elif (dealer_score > player_score and dealer_score <= 21) \
            or (dealer_score <= 21 and player_score >= 21):
            print("Dealer wins!")
        else:
            print("Tie game!")

        sleep(2)
        play_again = input("\nPlay again? (y/n):")

        if play_again.lower() == "y":
            Game()
        else:
            print("\nThanks for playing!")


if __name__ == "__main__":
    game = Game()
