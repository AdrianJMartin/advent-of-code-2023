input_data : bytearray
width : int
height : int

NEW_LINE = ord(("\n"))
GALAXY = ord("#")
EXPANSION = ord("E")

d = "data-test-1.txt"
d = "data.txt"

with open( d , "br") as f:

	input_data = bytearray( f.read() )
	width = input_data.index( NEW_LINE )
	height = input_data.count( NEW_LINE) + 1
	while input_data.find( NEW_LINE ) != -1:
		input_data.remove( NEW_LINE)

def dump():
	for i in range(height):
		for j in range(width):
			print( chr(input_data[i*width+j]), end="")
		print()


blank_lines = []
blank_columns  = []

def detect_expansion():

	for y in range( height):
		line =input_data[y*width:y*width+width]
		if line.find(GALAXY) == -1:
			blank_lines.append(y)

	for x in range(width):
		found = False
		for y in range(height):
			if input_data[y*width+x] == GALAXY:
				found = True
				break
		if not found:
			blank_columns.append(x)

def expand():

	for y in blank_lines:
		for x in range(width):
			input_data[y*width+x] =  EXPANSION

	for y in range(height):
		for x in blank_columns:
			for y in range(height):
				input_data[y*width+x] =  EXPANSION

galaxies = []

def detext_galaxies():
	for y in range(height):
		for x in range(width):
			if input_data[y*width+x] == GALAXY:
				galaxies.append( (x,y) )



dump()
detect_expansion( )
expand()
detext_galaxies()

print()
dump()

print( blank_lines)
print( blank_columns)
print( width)
print( height)
print( galaxies)

from itertools import combinations, permutations


#from a list of x,y tuples produce a list of unique combinations of them
galaxy_to_galaxy_combinations = list(combinations([*range(len(galaxies))],2))
print(galaxy_to_galaxy_combinations)

sum = 0


for c in galaxy_to_galaxy_combinations:
	print( f"{c[0]+1} to {c[1]+1}" )

	accross_start = min(galaxies[c[0]][0],galaxies[c[1]][0])
	accross_end = max(galaxies[c[0]][0],galaxies[c[1]][0])

	space_walk =  input_data[accross_start:accross_end]
	space_walk.append(ord(" "))
	down_start = min(galaxies[c[0]][1],galaxies[c[1]][1])
	down_end = max(galaxies[c[0]][1],galaxies[c[1]][1])
	for y in range(down_start,down_end+1):
		space_walk.append( input_data[y*width+accross_end])
	print(space_walk)

	steps = 0
	for s in space_walk[:-1]:
		if s == ord("#"):
			steps += 1
		elif s == ord("."):
			steps += 1
		elif s == ord("E"):
			steps += 1000000
	print(steps)

	sum += steps

	print()
	
print(sum)	


#   0   1   2
# 0 x   1,0 2,0
# 1 x   x   2,1

# part 1 9947476 ! correct!

# part 2