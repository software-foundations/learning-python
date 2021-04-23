from dataclasses import dataclass
from typing import List


@dataclass
class PlayingCard:	
	rank: str
	suit: str

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()


def make_french_deck() -> List[PlayingCard]:
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


print(make_french_deck())