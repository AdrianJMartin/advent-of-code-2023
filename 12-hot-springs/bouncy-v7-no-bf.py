"""
so we need to use a solution that does not brute force

pat = "???.###"
cs = [1,1,3]

# a variation is a str which contains a series of . or #
# a run of # is a block of a certain size
# the pat is the pattern of the blocks
# each block must be separated by at least 1 . 
# if any character in pat is ? then it can be either . or #
# we only need the count of variations per input pat and cs
"""

"""
???.### cs= [1,1,3]

p[0] = ? , r = cs[0]
max_len = len(pat)
min_len_remaining = sum( cs[1:] ) + len(cs[1:]) - 1])
.
# start of run
p[1] = ?
..
## invalid as run is len 1
p[2] = ?
...
..#
p[3] = .
.
#
p[4] = #
variations = 2
.
#

p[1] = ?
p[2] = ?
p[3] = .
p[4] = #
p[5] = #
p[6] = #

"""


def count( pat , cs ):
	
	# at the begining we need to start with two
	# potential variations
	variations = []
	run_index = 0
	max_len = len(pat)
	
	for i,c in enumerate(pat):
		if i == max_len:
			break
		
		# create new variations
		
		if i == 0:
			variations.append( "." )
			variations.append( "#" )
		else:
			new_variations = []
			for vi,v in enumerate(variations):
				variations[vi] = v + "."
				new_variations.append( v + "#")
			variations = variations + new_variations

		# do all variations match the pat - so far?
		remove=[]
		if c != "?":
			for vi,v in enumerate(variations):
				if v[i] != c:
					remove.append(vi)
					continue
		variations = [ v for vi,v in enumerate( variations) if vi not in remove]

		remove =[]
		for vi,v in enumerate(variations):
			rl = [ len(x) for x in v.split(".") if x != ""]

			if len( rl) > len(cs):
				remove.append(vi)
				continue

			# check the run lengths)

			for j,r in enumerate(rl):

				if r > cs[j]:
					remove.append(vi)
					break

				if i == max_len-1 and cs != rl:
					remove.append(vi)
					break
				
				if v[-1] == ".":
					if r != cs[j]:
						remove.append(vi)
						break


				if r < cs[j]:
					break

				if r != cs[j]:
					remove.append(vi)
					break
		variations = [ v for vi,v in enumerate(variations) if vi not in remove ]

	print(variations)

	return len(variations)









input = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

with open("input.txt") as f:
 	input = f.read()


input = input.splitlines()
input = [ { "pat" : x.split()[0] , "cs" : list(map(int,x.split()[1].split(","))) } for x in input ]

total = 0

for x in input:
	print(f"{x['pat']} {x['cs']}")
	variations = count(x['pat'],x['cs'])
	print(f"variations: {variations}")
	print()

	total += variations

print(f"total: {total}")
