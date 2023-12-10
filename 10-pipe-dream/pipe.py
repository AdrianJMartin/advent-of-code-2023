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

while field[y][x] != "S" or steps == 0:
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


