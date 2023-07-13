from typing import NamedTuple
import random


class Card(NamedTuple):
    rank: int
    suit: str


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self._cards.append(Card(rank, suit))

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()

for card in sorted(deck, key=lambda card: card.suit):
    print(card)
