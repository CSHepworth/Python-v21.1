from turtle import title
from unittest import suite
import random


class Deck:

    def __init__(self):
        self.cards = []

    def generate_cards(self):
        titles = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
        for suit in suits:
            for index, title in enumerate(titles):
                card = Card(values[index], suit, title)
                self.cards.append(card)

    def show_cards(self):
        for card in self.cards:
            card.info()
        return self

    def shuffle(self):
        random.shuffle(self.cards)
        self.cards
        return self
       
    

class Card:

    def __init__(self, value, suit, title):
        self.value = value
        self.suit = suit
        self.title = title

    def info(self):
        print(f"{self.title} of {self.suit}: {self.value}")

newdeck = Deck()
newdeck.generate_cards()
newdeck.shuffle()
print(newdeck.show_cards())

class Split:

    def __init__(self, player1, player2):
        pass