with open("data.txt" ) as f:
	data = f.read()

data = """#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#."""

fields = [ f for f in data.split("\n\n")]

total = 0

for i, field in enumerate( fields ):

	if i % 2 != 0:
		#transpose every other field
		field = "\n".join( "".join(row) for row in zip(*field.splitlines()))

	score = 0

	print( field)

	values = []
	for r in field.split("\n"):
		values.append( int( "".join( [ { "#":"1" , ".":"0" }[b] for b in r ] ) , 2))
	
	# find two numbers the same next to each other
	for j,v in enumerate( values[:-1] ):
		if v == values[j+1]:
			if i % 2 != 1:
				print( f"rows above {j+2}")
				score = j+1
				break
			else:
				print( f"cols left {j+2}")
				score = 100 * j + 100
				break
	print(score)
	print()
	total += score
print( total )
print()






