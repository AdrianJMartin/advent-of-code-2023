good_report = """#.#.### 1,1,3
.#...#....###. 1,1,3
.#.###.#.###### 1,3,1,6
####.#...#... 4,1,1
#....######..#####. 1,6,5
.###.##....# 3,2,1""".split( "\n" )

bad_report = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

def parse_report( report):
	
	report = report.split( "\n" )

	for i, r in enumerate( report):
		map_cs = r.split(" ")
		map = map_cs[0]
		cs = map_cs[1]
		cs = cs.split(",")
		cs = [ int( c ) for c in cs ]
		report[i] = { "map":map, "positions":cs }

	return report	
	



def check_report( report ):
	parsed = parse_report( report )
	for r in parsed:
		damaged = r["map"].split(".")
		damaged = [ d for d in damaged if d != "" ]
		damaged = [ len(d) for d in damaged ]
		
		print( damaged == r["positions"])

def checksum_to_binary( checksum ):
	t   = ""
	binary = 0
	highest_bit = sum( checksum ) + len( checksum ) -1
	rt = 0

	for run in checksum:
		for i in range( run ):
			highest_bit -= 1
		highest_bit -= 1
		if highest_bit > 0:
			binary |= 1 << highest_bit

	print( binary )
	return binary

# should be 1010000
checksum_to_binary( [ 1 ,1,3 ])

def check_variations_with_checksum( map , cs ):
	
	c =str.count( map , "?" )
	max_variations = c ** 2

	for i in range( max_variations -1 ):
		v =  f"{i:0{c}b}"
		for a in cs:
			for b in a:

parsed = parse_report( bad_report )


for r in parsed:
	check_variations_with_checksum( r.get("map") , r.get("positions") )
	print( r["map"]) 
	print()




# 012345678901234567890123456789
# ???.### 1,1,3

# ??? 1000 
# 000 1000 3,3
# 001 1000 2,3
# 010 1000 1,1,3  <---
# 011 1000 1,3
# 100 1000 2,3
# 101 1000 1,3
# 110 1000 1,3
# 111 1000 3

# .??..??...?##. 1,1,3
# .??..??...?00
# 1??11??111?00

# 1001100111000 2,2,3
# 1001100111000 2,....
# 1001101111000 2
# 1001101111100
# 1001110111000
# 1001110111100
# 1001111111000
# 1001111111100
# 1011100111000 1,2
# 1011100111100
# 1011101111000 1,1,3
# 1011101111100 
# 1011110111000 1,1,3
# 1011110111100
# 1011111111000
# 1011111111100
# 1101100111000
# 1101100111100
# 1101101111000 1,1,3
# 1101101111100 
# 1101110111000 1,1,3
# 1101110111100 
# 1101111111000 
# 1101111111100
# 1111100111000
# 1111100111100
# 1111101111000
# 1111101111100
# 1111110111000
# 1111110111100
# 1111111111000
# 1111111111100



# 1??11??111?001

# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1
# ????.######..#####. 









