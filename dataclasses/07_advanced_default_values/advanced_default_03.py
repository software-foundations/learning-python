from dataclasses import dataclass, field
from typing import List


@dataclass
class PlayingCard:  
    rank: str
    suit: str

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()


def make_french_deck() -> List[PlayingCard]:
    """Factory for cards field in Deck Dataclass"""
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


@dataclass
class Deck:  # Works
    # ValueError: mutable default <class 'list'> for field cards is not allowed: use default_factory
    # cards: List[PlayingCard] = make_french_deck()
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

deck = Deck()
print(deck)

"""
The field() specifier is used to customize each field of a data class individually. You will see some other examples later. For reference, these are the parameters field() supports:

default: Default value of the field
default_factory: Function that returns the initial value of the field
init: Use field in .__init__() method? (Default is True.)
repr: Use field in repr of the object? (Default is True.)
compare: Include the field in comparisons? (Default is True.)
hash: Include the field when calculating hash()? (Default is to use the same as for compare.)
metadata: A mapping with information about the field
In the Position example, you saw how to add simple default values by writing lat: float = 0.0. However, if you also want to customize the field, for instance to hide it in the repr, you need to use the default parameter: lat: float = field(default=0.0, repr=False). You may not specify both default and default_factory.
"""