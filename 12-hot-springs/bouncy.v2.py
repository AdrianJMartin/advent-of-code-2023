def count( pat , cs , left ):

	print( f"{left}")

	if len(cs) == 0:
		return 0
	
	if len(pat) == 0:
		return 0


	l = len(pat)

	test_pat = "#" * cs[0]

	if len(test_pat) > l:
		test_pat += "."
	test_pat_len = len(test_pat)

	min_right_len = sum( cs[1:] ) + len( cs[1:]) -1

	valid_count = 0

	max = l - min_right_len 

	for i in range( 0 , max ):
		p = "." * i + test_pat

		valid = True

		for ci,c in enumerate(p):
			if	pat[ci] == "?":
				continue
			elif pat[ci] == c:
				continue
			else:
				valid = False
				break
		
		if valid:
			valid_count += count( pat[len(p):], cs[1:] , left + p )

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

	assert c == a

print("===============")
print(rt)
print("===============")