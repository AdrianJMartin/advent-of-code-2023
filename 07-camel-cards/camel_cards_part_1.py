
FIVE_OF_A_KIND  = 0x7
FOUR_OF_A_KIND  = 0x6
FULL_HOUSE      = 0x5
THREE_OF_A_KIND = 0x4
TWO_PAIR =        0x3
ONE_PAIR =        0x2
HIGH_CARD =       0x1

THREE_OF_A_KIND_OR_TWO_PAIR = 11
FULL_HOUSE_OR_FOUR_OF_A_KIND = 10

types_look_up = { 1 : FIVE_OF_A_KIND  , 2:FULL_HOUSE_OR_FOUR_OF_A_KIND , 3:THREE_OF_A_KIND_OR_TWO_PAIR , 4:ONE_PAIR , 5:HIGH_CARD }
types_to_str = {
	FIVE_OF_A_KIND:"Five of a kind",
	FOUR_OF_A_KIND:"Four of a kind",
	FULL_HOUSE:"Full house",
	THREE_OF_A_KIND:"Three of a kind",
	TWO_PAIR: "Two pair" ,
	ONE_PAIR:"One pair" ,
	HIGH_CARD:"High Card" }

card_values_look_up = {
	'A': 12, 'K' : 11 , 'Q':10 , 'J':9 , 'T':8 ,
	'9': 7, '8' : 6 , '7':5 , '6':4 , '5':3,'4':2 ,
	'3': 1, '2':0
	}

class Hand  :
	cards : str
	bid : int
	type: int
	rank : int
	value : int
	rank: int

	def classify(self):
		count_cards_by_type = {}

		for card in self.cards:
			if card in count_cards_by_type:
				count_cards_by_type[card]+=1
			else:
				count_cards_by_type[card] = 1


		counts = len( count_cards_by_type )
		print( f"{self.cards}: {counts}")
		self.type = types_look_up[counts]

		if self.type == FULL_HOUSE_OR_FOUR_OF_A_KIND:
			if max( count_cards_by_type.values() ) == 4:
				self.type = FOUR_OF_A_KIND
			else:
				self.type = FULL_HOUSE

		if self.type == THREE_OF_A_KIND_OR_TWO_PAIR:
			if max( count_cards_by_type.values() ) == 3:
				self.type = THREE_OF_A_KIND
			else:
				self.type = TWO_PAIR

		self.value = self.type * 10000000
		self.value += card_values_look_up[self.cards[0]] * 0xFFFF
		self.value += card_values_look_up[self.cards[1]] * 0xFFF
		self.value += card_values_look_up[self.cards[2]] * 0xFF
		self.value += card_values_look_up[self.cards[3]] * 0xF
		self.value += card_values_look_up[self.cards[4]]

	def fromStr( s):
		h = Hand()
		tmp = s.split(" ")
		h.cards = tmp[0]
		h.bid = int( tmp[1])
		h.classify()
		return h
	
	def __str__(self) -> str:
		return f"{self.rank}\t0x{self.value:08x}\t{types_to_str[self.type]}\t{self.cards}\t{self.bid}"


def camel_cards( data_file ):

	with open( data_file ) as f:
		data = f.read()

	hands = []

	for line in data.split("\n"):
		hands.append( Hand.fromStr(line) )
	
	hands.sort( key=lambda x:x.value , reverse=True)

	check_sum = 0
	number_of_hands = len( hands )

	for i,hand in enumerate(hands):
		hand.rank = ( number_of_hands -i )
	
	for hand in hands:
		print(hand)
		check_sum += hand.rank * hand.bid

	return check_sum


if __name__ == "__main__":
	r = camel_cards( "data.txt" )
	print( f"Part 1: {r}")



