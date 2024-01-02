# find number of strings that match this pattern
# . good spring
# # broken spring
# ? good or broken spring
# given checksum [3,2,1]
# where each value is a run of broken springs, separated 
# by at least 1 good spring
# e.g.
# pattern ?###????????
# check_sum [3,2,1]
# 10 variations:
# .###.##.#...
# .###.##..#..
# .###.##...#.
# .###.##....#
# .###..##.#..
# .###..##..#.
# .###..##...#
# .###...##.#.
# .###...##..#
# .###....##.#

count_variations = 0

def count(pat, cs , mn ):

	global count_variations


	if len(cs) == 0:
		count_variations += 1
		return


	ln = cs[0] + 1 #e.g. ###.
	mx = len(pat) - cs[0] - sum(cs[1:]) - len( cs[1:]) +2

	if len(cs) == 1:
		mx -=1

	print( f"{pat} {cs} {mn} {mx}")

	for i in range(0, mx):
		t =  f"{'.' * i}{'#'* cs[0]}"
		if len(cs) > 1:
			t += "."
		# does this t match the pattern so far?
		match = True
		for j in range(0,len(t)):
			if pat[j] == '?':
				continue
			if pat[j] != t[j]:
				match = False
				break

		if match:
			print(f"{' ' * mn }{t}")
			count( pat[len(t):] , cs[1:] , mn = mn + len(t))
	return


count_variations = 0
count("#?#???????#?.?" , [3,1,2,2] , 0 )
print( count_variations)

exit()


data = """
???.### 1,1,3 1
.??..??...?##. 1,1,3 4
?#?#?#?#?#?#?#? 1,3,1,6 1
????.#...#... 4,1,1 1
????.######..#####. 1,6,5 4
?###???????? 3,2,1 10
#?#???????#?.? 3,1,2,2 0
.??.##.?#????.??#? 2,2,1,2,4 0
.?.??#?##??#????.. 8,1 0
""".splitlines()

data.remove("")

running_total = 0

print("test data")

for t in data:
	pat,cs,exp = t.split(" ")
	cs = list( map(int,cs.split(",")))

	print(pat)
	print(cs)
	print(exp)
	count_variations = 0
	count( pat , cs , 0 )
	print(count_variations)
	print( count_variations == exp )
	running_total += count_variations
	print( )

print( running_total )

print("* % " * 50)

exit()

print("Stupid elfs data")


with open("input.txt") as f:
	data = f.readlines()

running_total = 0

for t in data:
	pat,cs = t.split(" ")
	cs = list( map(int,cs.split(",")))

	print(pat)
	print(cs)
	count_variations = 0
	count( pat , cs , 0 )
	print(count_variations)
	running_total += count_variations
	print( )

print( running_total )

print("* % " * 50)


