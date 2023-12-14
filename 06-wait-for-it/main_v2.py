


races = [ (71530,940200)]
races = [ (7,9),(15,40),(30,200) ]

races = [ (46689866,358105418071080)]
races = [ (46,358),(68,1054),(98,1807),(66,1080) ]

ways_to_win = []

ways_to_win_product = 1

for race_number, race in  enumerate( races ):
	print( f"race {race_number}")
	time,dist = race
	print( f"distance: {dist}" )

	#low to high
	for t in range( 1 , time ):
		if ( time - t ) * t > dist:
			low = t
			break



	print(f"low : {low}")
	if low % 2 == 0:
		ways_to_win = low * 2
	else:
		ways_to_win = low - 2
		
	

	ways_to_win_product *= ways_to_win
	print( f"ways to win: {ways_to_win}")

	print( "*" * 100)


print( "*" * 100)
print( f"{ways_to_win_product}")		
	
