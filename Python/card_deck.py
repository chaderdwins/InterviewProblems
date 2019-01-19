# Introduction
#
# Your goal in this exercise is to implement two classes, Card  and Deck .
#
# Specifications
#
# Card
#
# Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
# Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
# Card 's __repr__  method should return the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)
# Deck
#
# Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
# Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
# Deck 's __repr__  method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
# Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
# Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should return a ValueError  with the message "Only full decks can be shuffled".  shuffle should return the shuffled deck.
# Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck and return that single card.
# Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck and return that list of cards.
from random import shuffle as s
class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return self.value + " of " + self.suit

class Deck:
    def __init__(self):
        values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        self.cards = []
        for suit in suits:
            for value in values:
                # print(Card(suit, value))
                self.cards.append(Card(suit, value))
        # print(self.cards)

    def __repr__(self):
        x = str(Deck.count(self))
        return "Deck of " + x + " cards"

    def count(self):
        """returns count of how many cards remain in the deck"""
        return len(self.cards)

    def _deal(self, number, deal=None):
        if Deck.count(self) == 0:
            raise ValueError("All cards have been dealt")
        if number > Deck.count(self):
            number = Deck.count(self)
        if deal == 'y':
            return self.cards.pop()
        array = []
        l = 0
        while l < number:
            array.append(self.cards.pop())
            l += 1
        return array

    def shuffle(self):
        if Deck.count(self) == 52:
            s(self.cards)
        else:
            raise ValueError("Only full decks can be shuffled")
        return self.cards

    def deal_card(self):
        new_card = Deck._deal(self, 1, deal='y')
        return new_card

    def deal_hand(self, number):
        v = Deck._deal(self, number)
        return v




#debug
card1 = Card("Diamonds","A")
# print(card1)
d = Deck()
d.shuffle()
# print(d.deal_hand(1))
print(d.deal_card())
# print(d)
