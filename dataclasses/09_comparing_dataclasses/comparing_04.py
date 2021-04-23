from dataclasses import dataclass, field
from typing import List
from random import sample


RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))

    def __str__(self):
        return f'{self.suit}{self.rank}'


"""
You can now easily create a sorted deck:
"""

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


deck = Deck(sorted(make_french_deck()))
print(deck)


"""
Or, if you don’t care about sorting, this is how you draw a random hand of 10 cards:
"""
li_playing_card: List[PlayingCard] = sample(population=make_french_deck(), k=2)
deck2 = Deck(li_playing_card)
print(deck2)
