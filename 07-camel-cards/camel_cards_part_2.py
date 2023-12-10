
FIVE_OF_A_KIND  = 0x700000
FOUR_OF_A_KIND  = 0x600000
FULL_HOUSE      = 0x500000
THREE_OF_A_KIND = 0x400000
TWO_PAIR =        0x300000
ONE_PAIR =        0x200000
HIGH_CARD =       0x100000

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
	'A': 14, 'K' : 13 , 'Q':12 , 'J':0, 'T':10 ,
	'9': 9, '8' : 8 , '7':7 , '6':6 , '5':5,'4':4 ,
	'3': 3, '2':2
	}

class Hand  :
	cards : str
	bid : int
	type: int
	rank : int
	value : int
	rank: int
	was: int

	def classify(self):
		count_cards_by_type = {}

		for card in self.cards:
			if card in count_cards_by_type:
				count_cards_by_type[card]+=1
			else:
				count_cards_by_type[card] = 1


		counts = len( count_cards_by_type )
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
		
		self.was = self.type

		jokers = count_cards_by_type.get('J')
		if jokers:

#ONE_PAIR =        0x2
#HIGH_CARD =       0x1

			if self.type == FOUR_OF_A_KIND:
				if jokers == 4:
					self.type = FIVE_OF_A_KIND
				elif jokers == 1:
					self.type = FIVE_OF_A_KIND
				else:
					print("No!!!!")

			elif self.type == FULL_HOUSE:
				if jokers == 2:
					self.type = FIVE_OF_A_KIND
				elif jokers == 3:
					self.type = FIVE_OF_A_KIND
				else:
					print("No!!!!")

			elif self.type == THREE_OF_A_KIND:
				if jokers == 3:
					self.type = FOUR_OF_A_KIND
				elif jokers == 1:
					self.type = FOUR_OF_A_KIND
				else:
					print("No!!!!")
				
			elif self.type == TWO_PAIR:
				if jokers == 2:
					self.type = FOUR_OF_A_KIND
				elif jokers ==1:
					self.type = FULL_HOUSE
				else:
					print("No!!!!")

			elif self.type == ONE_PAIR:
				if jokers == 2:
					self.type = THREE_OF_A_KIND
				elif jokers == 1:
					self.type = THREE_OF_A_KIND
				else:
					print("No!!!!")

			elif self.type == HIGH_CARD:
				if jokers == 1:
					self.type = ONE_PAIR
				else:
					print("No!!!!")
			else:
				print( "stays the same")



		self.value = self.type
		self.value += card_values_look_up[self.cards[0]] * 0xF000
		self.value += card_values_look_up[self.cards[1]] * 0xF00
		self.value += card_values_look_up[self.cards[2]] * 0xF0
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
		return f"{self.rank:05}\t0x{self.value:08x}\t{types_to_str[self.type]}\t{types_to_str[self.was]}\t{self.cards}\t{self.bid}"


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
		check_sum += hand.rank * hand.bid

	print( f"part 2: {check_sum}")

	for hand in hands:
		print(hand)

	return check_sum

if __name__ == "__main__":
	r = camel_cards( "data.txt" )
	print( f"Part 2: {r}")

#249751625 wrong!
#250274742 wrong! too low
#250312564
#250289237
#251355437
#251330295
#252091155
#251544807
#250757288