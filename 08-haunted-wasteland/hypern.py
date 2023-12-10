steps, _,*rest = open(0).read().splitlines()
print(steps)

mapping = {}

for line in rest:
	pos, tar = line.split( " = " )
	mapping[pos] = tar[1:-1].split(", ")

print( mapping )
	