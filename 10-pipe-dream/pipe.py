field = open(0).read().splitlines()

# add a fence arround the field
for i,l in enumerate(field):
	field[i] = "." + l + "."

field = [ "." * len( field[1] ) , *field ]
field = [ *field , field[0]]

x = 0
y = 0
# find start
for i,l in enumerate(field):
	x = l.find("S")
	if x != -1:
		y = i
		break

last_direction = None
steps = 0
path = []

while field[y][x] != "S" or steps == 0:
	
	path.append((x,y))

	# can we move north
	if last_direction != "s" and field[y-1][x] in "|7FS" and field[y][x] in "S|LJ":
		y -= 1
		last_direction = "n"
	elif last_direction != "w" and field[y][x+1] in "-7JS" and field[y][x] in "S-LF": # east
		x += 1
		last_direction = "e"
	elif last_direction != "n" and field[y+1][x] in "|JLS" and field[y][x] in "S7|F": # south
		y += 1
		last_direction = "s"
	elif last_direction != "e" and field[y][x-1] in "-LFS" and field[y][x] in "S7-J": # west steps +=1
		x -= 1
		last_direction = "w"
	
	steps += 1

	print(f"{steps} {last_direction}")

print(f"furthest step: {steps//2}")
print()
for l in field:
	print(l)
print()
print("-----------------------------------")
for y,l in enumerate(field):
	nl = ""
	for x,c in enumerate(l):
		if (x,y) in path:
			nl += "*"
		else:
			nl += "."
	field[y] = nl
print("-----------------------------------")
print( "\n".join( field)) 
print("-----------------------------------")

c_inside = 0
for y,l in field:
	expected = "."
	changes = 0 
	for x,c in l:
		if c != expected:
			changes += 1
			expected = "*"

print("-----------------------------------")
print("-----------------------------------")

"""
The pipes are arranged in a two-dimensional grid of tiles:

| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, 
but your sketch doesn't show what shape the pipe has.
"""


