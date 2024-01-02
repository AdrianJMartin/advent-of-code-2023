def count( pat , cs , left):
	# create a minimal match
	match = ""
	for n in cs:
		match += "#" * n + "."

	match = match[:-1]
	print(f"min match:{match}")

	len_diff = len(pat) - len(match)
	print(f"len_diff {len_diff}")

	match += "." * len_diff
	print(f"match:{match}")
	
	valid = True
	valid_count = 0
	
	for ci,c in enumerate(pat):
		if c == "?" and match[ci] in ".#":
			continue
		elif c == "#" and match[ci] == "#":
			continue
		elif c == "." and match[ci] == ".":
			continue
		else:
			valid = False 

	if valid:
		valid_count += 1

	return valid_count


bad_report = """???.### 1,1,3 1
.??..??...?##. 1,1,3 4
?#?#?#?#?#?#?#? 1,3,1,6 1
????.#...#... 4,1,1 1
????.######..#####. 1,6,5 4
?###???????? 3,2,1 10"""

rt = 0
for line in bad_report.split("\n"):
	p,cs,a = line.split(" ")
	cs = list( map( int , cs.split(",") ) )
	a = int(a)
	c = count( p , cs , "")
	rt + c
	print( f"{p} {cs} {a} {c} {c == a}" )

print("===============")
print(rt)
print("===============")