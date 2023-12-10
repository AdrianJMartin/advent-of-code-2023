import os

print( os.getcwd() )

def parse( map_file):

	with open( map_file ) as f:
		input = f.read()

	input = input.split( "\n" )

	mapping = {}

	for i,line in enumerate( input ):

		if i == 0:
			route = line
			continue

		if line != "":
			mapping[line[0:3]] = { "L":line[7:10] , "R":line[12:15] }

	print( len( mapping ))
	return route , mapping



def walk( map_file , start = "AAA" , end= 'ZZZ' ):

	print( start)

	route,mapping = parse( map_file )
	steps = 0
	position = mapping.get( start )

	home = False

	while home != True:
		for s in route:
			
			# print(steps)
			# print(position)
			# print(s)
			# print()
			steps += 1

			if position.get(s) == 'ZZZ' :
				home = True
				break

			if end == 'Z' and position.get(s).endswith(end):
				home = True
				break

			position = mapping.get( position.get(s))


	return steps


def ghost_walk( map_file ):
	route,mapping = parse( map_file )
	steps = 0

	positions = [ k for k in mapping.keys() if k.endswith("A") ]

	home = False

	print("start")
	print( positions )

	loops = 0

	while home != True:
		loops += 1
		for s in route:
	#		print(positions)
			home = [ p.endswith("Z") for p in positions ] 
	#		print(home)


			# if any( home ):
			# 	print( loops )
			# 	print( steps )
			# 	print(home)
			# 	print("=" * 5)

				

			home = all( home )
			if  home:
				return steps

			steps += 1

			for i,k in enumerate(positions):
				positions[i] = mapping.get(k)[s]




# print( "example 1 should = ")
# assert( walk("data-test-1.txt") == 2)
# assert( walk("data-test-2.txt") == 6)
# print( "Part 1")
# print( walk( "data.txt" ))

print( "Part 2")

assert( ghost_walk("data-test-3.txt") == 6)

lcms = []

for sp in ['MXA', 'VQA', 'CBA', 'JBA', 'AAA', 'HSA']:
	s = walk( "data.txt" , sp , 'Z')
	lcms.append(s)
	print(lcms)


import itertools
from math import gcd

def lcm(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = result * num // gcd(result, num)
    return result


lcm = lcm(lcms)
print(lcm)

print( ghost_walk( "data.txt" ))



