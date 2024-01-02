import math

races = [ (71530,940200)]
races = [ (7,9),(15,40),(30,200) ]
races = [ (46,358),(68,1054),(98,1807),(66,1080) ]
races = [ (46689866,358105418071080)]

ways_to_win = []
ways_to_win_product = 1

for race_number, race in  enumerate( races ):
	print( f"race {race_number}")
	time,dist = race
	print( f"distance: {dist} over {time}" )

	a = math.sqrt( ( (time*time) - dist * 4 ) / 4 )
	low = a - time / 2 
	high = a + time /2
	ways_to_win = high - abs( low ) 
	print( f"ways to win: {ways_to_win}")
	ways_to_win_product *= int( ways_to_win )
	print( "*" * 100)
print( "*" * 100)
print( f"{ways_to_win_product}")
print( 27340847 == ways_to_win_product )
