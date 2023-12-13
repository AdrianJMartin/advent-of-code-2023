import time

xfield = """S-------7
|F-----7|
||.....||
||.....||
|L-7.F-J|
|..|.|..|
L--J.L--J"""
xdirection = "n"

xfield = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

xdirection = "w"

field = ""
with open("big-path.txt") as f:
	field = f.read()

t = str.maketrans( {
	"F" : "╔",
	"-": "═",
	"L": "╚",
	"|": "║",
	"J": "╝",
	"7": "╗"
})

field = field.translate( t  )

print(field)


s = field.index("S")
field = field.splitlines()

y = 0
x = 0

for y,l in enumerate(field):
	x = l.find("S")
	if x != -1:
		break

start = (x,y)


if field[y+1][x] in "╝╚║" and field[y][x+1] in "═╗╝":
	field[y] = field[y][:x] + "╔" + field[y][x+1:]
direction = "e"
# add fence

for y,l in enumerate(field):
	field[y] = f".{l}."

field = [ "." * len(field[0]) , *field, "." * len(field[0])]

start = ( start[0] + 1 , start[1] +1 )

squares = []
squares.append((0,0))

while len(squares):
	squares = set( squares)
	squares = list(squares)
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

	print( "\n".join(field[:100] ))
	print()
	time.sleep(0)


"""
╔ ═ ╗
║   ║
╚ ═ ╝
"""


print( "\n".join(field))

"""
Walk around the path, look to the right, if it's a .
then its inside.
"""
step = 0


x , y = start

def set_sq(x,y,c):
	field[y] = field[y][:x] + c + field[y][x+1:]

set_sq( x , y ,"╚" )
direction = "w"


print( "-" * 30 )
print( "-" * 30 )
print( "\n".join(field))

while True:

	t = field[y][x]
	set_sq( x , y , '*')

	if direction == 'w':
		if field[y+1][x] == '.':
			set_sq( x , y+1 , 'O') 
	elif direction == 'e':
		if field[y-1][x] == '.':
			set_sq( x , y-1 , 'O') 
	elif direction == 'n':
		if field[y][x-1] == '.':
			set_sq( x-1 , y , 'O') 
	elif direction == 's':
		if field[y][x+1] == '.':
			set_sq( x+1 , y , 'O') 

	if direction == 'w':
		direction = { '╔':'s' , '╚':'n', '═':'w' }.get(t)
	elif direction == 'e':
		direction = { '╝':'n' , '╗':'s', '═':'e' }.get(t)
	elif direction == 'n':
		direction = { '╔':'e' , '╗':'w', '║':'n' }.get(t)
	elif direction == 's':
		direction = { '╚':'e' , '╝':'w', '║':'s' }.get(t)

	if direction == 'n':
		y -= 1
	elif direction == 's':
		y += 1
	elif direction == 'e':
		x += 1
	elif direction == 'w':
		x -= 1
	
	print( "-" * 30 )
	if y < 40:
		print( "\n".join(field[:40]))
	else:
		print( "\n".join(field[40:]))

	time.sleep(0.01)
		

	if (x,y) == start:
		break


inside = 0
for y, l in enumerate(field):
	for x , c in enumerate(l):
		if c == ".":
			inside += 1

print(f"part 2: {inside}")



