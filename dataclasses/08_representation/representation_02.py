from dataclasses import dataclass, field
from typing import List


@dataclass
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.suit}{self.rank}'


def make_french_deck() -> List[PlayingCard]:
    """Factory for cards field in Deck Dataclass"""
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = '♣ ♢ ♡ ♠'.split()
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    def __repr__(self):
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'

"""
To show that it is possible to add your own .__repr__() method as well, we will violate the principle that it should return code that can recreate an object. Practicality beats purity after all. The following code adds a more concise representation of the Deck:

Note the !s specifier in the {c!s} format string. It means that we explicitly want to use the str() representation of each PlayingCard. With the new .__repr__(), the representation of Deck is easier on the eyes:
"""

deck = Deck()

print(deck)