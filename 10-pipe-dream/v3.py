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


fields = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""


state = "O"

def flip_state():
	global state
	if state == "o":
		state ="i"
	else:
		state = "o"

field_out = ""

field = field.splitlines()

inside = 0
in_pipe = False

for line in field:
	state = "o"
	for s in line:

		if s == "S":
			in_pipe == True
		elif s in "7J":
			in_pipe = False
		elif in_pipe and s == "|":
			in_pipe = False
		elif not in_pipe and s == "|":
			in_pipe = True

		if in_pipe and s == ".":
			field_out += "."
		elif not in_pipe and s == ".":
			field_out += "O"


	field_out += "\n"


print("\n".join( field ) )
print( field_out )
print( inside )
		

			
