import unittest

from camel_cards_part_1 import camel_cards as part1
from camel_cards_part_2 import camel_cards as part2
from camel_cards_part_2 import Hand,FOUR_OF_A_KIND,THREE_OF_A_KIND


class Test_camel_cards( unittest.TestCase ):

	def test_example_data(self):
		df = "./07-camel-cards/data-example.txt"
		r = 6440
		self.assertEqual( part1( df ) , r )

	def test_joker_example( self ):
		df = "./07-camel-cards/data-2-example.txt"
		r = 5905
		self.assertEqual( part2( df ) , r )

	def test_QJJQ2_is_FOUR_OF_A_KIND(self):
		t = Hand.fromStr( "QJJQ2 9999")
		self.assertEqual( t.type , FOUR_OF_A_KIND )

	def test_K999J_is_FOUR_OF_A_KIND(self):
		t = Hand.fromStr( "K999J 9999")
		self.assertEqual( t.type , FOUR_OF_A_KIND )


	def test_J3J29_is_THREE_OF_A_KIND(self):
		t = Hand.fromStr( "J3J29 9999")
		self.assertEqual( t.type , THREE_OF_A_KIND )