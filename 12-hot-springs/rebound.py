report = """???.### 1,1,3 1
.??..??...?##. 1,1,3 4
?#?#?#?#?#?#?#? 1,3,1,6 1
????.#...#... 4,1,1 1
????.######..#####. 1,6,5 4
?###???????? 3,2,1 10"""

records = []

def parse( report : str ):
	for l in report.splitlines():
		s = l.split(" ")
		rec = { "con":s[0], "groups": tuple( map( int , s[1].split(",")))}
		if len(s) == 3:
			rec["assert"] = int( s[2]) 
		records.append(rec)
		
var_count = 0

def count( r ):

	variation = r["con"]
	print(variation)
	groups = r['groups']
	con_len = len(variation)
	group_len = groups[0]

	for i in range(con_len):
		c = variation[i]

		if c == "?" and variation[i + group_len] in "?.":
			sub_variation = variation[i+group_len+1:]
			print(f"{sub_variation} {len(groups)}")
	
	return 0
		

parse(report)

total = 0
for r in records[0:2]:
	c = count(r)
	if r['assert']:
		print( f"{c} == {r['assert']}: { c == r['assert']}")
	total += c
	print( f"Count {c}" )

print(total)