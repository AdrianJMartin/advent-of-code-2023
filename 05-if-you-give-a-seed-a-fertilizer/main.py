def lookup( mapping , input ) -> int :

	inter = input
	
	for lu in mapping:

		m_used =""

		for m in mapping[lu]:
			d,s,r = m
			u = s + r 
			if inter >= s and inter <= u:
				inter = d + ( inter -s )
				m_used = m
				break
	return inter


def lookup_p2( ranges ) -> [] :

	inter = ranges


	for lu in mapping:
		print(lu)
		result_ranges = []
		for rg in ranges:
			print(rg)
			rs,re = rg
			for m in mapping[lu]:
				d,s,r = m
				u = s + r 

				starts_in_range = rs >= s and rs <= u
				ends_in_range = re > s and re <= u

				if starts_in_range and ends_in_range:
					print( "in range")
					new_range = ( d + rs - s , d + re -s )
					print( new_range )
					result_ranges.append(new_range)
				
				if starts_in_range and ends_in_range == False:
					new_range = ( d + rs - s , s + r )
					result_ranges.append(new_range)
					ranges.append( (s+r+1 , re ))
					pass

				if ends_in_range and starts_in_range == False:
					ranges.append(( rs , d + re -s))
					result_ranges.append( (  rs , d + re - s))
					print()
					pass
		if len(result_ranges) == 0 :
			result_ranges.append(rg)
		print( result_ranges)

		ranges = result_ranges

	return ranges

	




seeds = []

mapping = {}



with open("data.txt") as f:

	seeds = f.readline().strip().split(" ")
	seeds.pop(0)
	
	seeds = map( int , seeds)
	seeds = list(seeds)
	
	current_map = None
	mapping_values = []

	for line in f:
		if line == "\n":
			if current_map != None:
				mapping[current_map]=mapping_values
				mapping_values=[]
			continue
		
		if "map" in line:
			current_map = line[:-6]
			continue

		m = line.strip().split()
		m = map(int,m)
		m = list(m)
		mapping_values.append(m)

locations = []

for s in seeds:
	loc = lookup( mapping , s)
	locations.append(loc)

#print( table )

l = min( locations)
print( f"Part 1: {l}")

import sys
print( sys.argv  )

start = int( sys.argv[1] )
end = start + int( sys.argv[2])

print( f"seeds {start} to {end}")

lowest_loc = sys.maxsize
for s in range( start,end ):
	if ( ( start - s ) % 100000  == 0 ):
		print( f"f{s} of {end} {s/end}")

	loc =  lookup( mapping , s )
	lowest_loc = min( lowest_loc , loc )


with open( f"outputs.txt" ,"t+a") as f:
	f.write( f"seeds { start} to { end} lowest { lowest_loc }\n" )




# import sys

# locations = []

# while len(seeds):

# 	s = seeds.pop(0)
# 	r = seeds.pop(0)

# 	print( f"range {s} to { s+r}, {r} seeds!")

# 	res = lookup_p2( [(s,s+r)] )
# 	pass


# 	# for t in range( s , s+r):
# 	# 	loc = lookup(mapping , t )
# 	# 	if loc < lowest_loc:
# 	# 		lowest_loc = loc
# 	# 		print( f"lowest loc changed to: {lowest_loc}" )

# print( f"part 2: { lowest_loc }")


