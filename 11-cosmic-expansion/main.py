with open("data-test-1.txt") as f:
	input = f.read().splitlines()

print("finding blank lines")


blank_lines =[]


for y,line in enumerate( input ):
	x = line.find("#")
	if x > -1:
		pass
	else:
		blank_lines.append(y)

print( blank_lines)

blank_columns = []

for x, c in enumerate(input[0]):

	galaxy_found = False

	for y in range( len(input)):
		c = input[y][x]
		if c == '#':
			galaxy_found = True
			break

	if not galaxy_found:
		blank_columns.append(x)

	
print(blank_columns)
print("Before expansion")
print( "\n".join( input) )

bl =  "." * len( input[0])

blank_lines.reverse()

for b in blank_lines:
	input.insert(b,bl)

blank_columns.reverse()

for y,line in enumerate(input):
	for b in blank_columns:
		input[y] = input[y][:b] + "." + input[y][b:]

galaxies = []

for y,line in enumerate(input):
	for x, c in enumerate(line):
		if c == "#":
			galaxies.append((x,y))

print("After expansion")
print( "\n".join( input) )
print("")
print( galaxies )

sum_of_shortest = 0

print( "    1   2       3       4       5       6       7       8       9   ")

for y,g in enumerate( galaxies):
	p = ""
	for x,gg in enumerate( galaxies ):
		d = abs( gg[0] - g[0])
		d = 0
		d += abs( g[1] - gg[1])



		
		if x <= y :
			d = 0
		else:
			d = gg[0] - g[0] + gg[1] - g[1]
			d = abs(d)

		sum_of_shortest += d
		p += f"{d}\t"
	print(f"{y+1} | {p}")

print( sum_of_shortest)
"""
....#........ 9-4 + 1-0 = 6
.........#... 0-4 + 2-0 = 6
#............ 
.............
.............
........#.... 8-4+5-0 = 9 
.#........... 4-1 + 6-0 = 9
............#
.............
.............
.........#...
#....#.......
"""