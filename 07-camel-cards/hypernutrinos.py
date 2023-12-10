def replacements( hand ):
	if hand == "":
		return [""]
	
	return [
		x + y 
		for x in ( "23456789TQKA" if hand[0] == "J" else hand[0] )
		for y in replacements(hand[1:0])
	]

print( replacements( "4446J") )
