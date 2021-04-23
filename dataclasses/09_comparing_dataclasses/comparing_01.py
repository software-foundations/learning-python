from dataclasses import dataclass


@dataclass
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.suit}{self.rank}'


queen_of_hearts = PlayingCard('Q', '♡')
ace_of_spades = PlayingCard('A', '♠')
ace_of_spades > queen_of_hearts

# TypeError: '>' not supported between instances of 'PlayingCard' and 'PlayingCard'