

races = [ (71530,940200)]

races = [ (7,9),(15,40),(30,200) ]
races = [ (46689866,358105418071080)]
races = [ (46,358),(68,1054),(98,1807),(66,1080) ]

ways_to_win = []


ways_to_win_product = 1

for race_number, race in  enumerate( races ):

	print( f"race {race_number}")
	time,dist = race
	print( f"distance: {dist} over {time}" )

	#low to high
	for t in range( 1 , time ):
		if ( time - t ) * t > dist:
			low = t
			break

	high = time - low

	# # high to low
	# for t in range( time -1 , 0 , -1 ):
	# 	if ( time - t ) * t > dist:
	# 		high = t
	# 		break


	print(f"low : {low}")
	print(f"high: {high}")
	ways_to_win = high - low +1
	ways_to_win_product *= ways_to_win
	print( f"ways to win: {ways_to_win}")

	print( "*" * 100)


print( "*" * 100)
print( f"{ways_to_win_product}")		
	
