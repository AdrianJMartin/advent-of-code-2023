field = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""

field = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""


field = field.splitlines()

for i,l in enumerate(field):
	field[i] = f".{l}."

field.insert(0 ,"." * len(field[0]))
field.append(field[0])
	

squares = []


squares.append((0,0))

while len(squares):
	for i in range( len(squares)):
		x , y = squares.pop(0)

		if field[y][x] == ".":
			field[y] = field[y][:x] + "X" + field[y][x+1:]


		if x+1 < len(field[0]) and field[y][x+1] == ".":
			squares.append( (x+1,y))
		
		if x-1 > 0 and field[y][x-1] == ".":
			squares.append( (x-1,y))
		
		if y+1 < len(field) and field[y+1][x] == ".":
			squares.append((x,y+1))

		if y-1 > 0 and field[y-1][x] == ".":
			squares.append((x,y-1))


inside = 0
for c in "".join(field):
	if c == ".":
		inside +=1


print( "\n".join(field))
print( f"inside {inside}")


ooiioiiiiiiiiiiiioooo
 .||.FJ||||||||L7....


L--J.L7...LJS7F-7L7.
L--JOL7IIILJS7F-7L7O



