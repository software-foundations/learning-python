class RegularCard:
	def __init__(self, rank: str, suit: str):
		self.rank = rank
		self.suit = suit

queen_of_hearts = RegularCard('Q', 'Hearts')
print(queen_of_hearts)
print(queen_of_hearts.rank)
print(queen_of_hearts == RegularCard('Q', 'Hearts'))
