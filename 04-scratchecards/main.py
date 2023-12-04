data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

with open( "data.txt") as f:
	data = f.read()

part_1_score = 0 

# for row in data.split("\n"):
# 	colon_pos = row.index( ":") 
# 	bar_pos = row.index("|") 

# 	winners =  set( row[colon_pos+1 :bar_pos -1 ].replace("  " , " ").strip().split(" ") )
# 	my_numbers = set(  row[ bar_pos + 1:].strip().replace("  "," ").split(" ") )

# 	print( winners)
# 	print( my_numbers)
# 	print( len( my_numbers & winners ))
# 	card_score = int(  2 ** (len( my_numbers & winners ) -1 ) )
	 
# 	print( card_score)
# 	score += card_score

# 	print( score)
# 	print( "=" * 100 )

next_rows = []

for i in range (200):
	next_rows.append(0)

row_counter = 0


for row in data.split("\n"):

	next_rows[row_counter]+=1


	colon_pos = row.index( ":") 
	bar_pos = row.index("|") 

	winners =  set( row[colon_pos+1 :bar_pos -1 ].replace("  " , " ").strip().split(" ") )
	my_numbers = set(  row[ bar_pos + 1:].strip().replace("  "," ").split(" ") )


	print( winners)
	print( my_numbers)
	wins = len( my_numbers & winners)

	print( wins )
	card_score = int( 2 ** ( wins -1 ))
	part_1_score += card_score

	m = next_rows[row_counter]

	for i in range(wins):
		next_rows[i+row_counter+1] += 1 * m

	row_counter += 1	
	print( "=" * 100 )


print("part 1 ")
print(part_1_score)

print( "part 2 ")
print( sum( next_rows ))


print()
exit

"""
1 wins 4 = 2 3 4 5
2 wins 2 = 3 4
2 wins 2 = 3 4
3 wins 2 = 4 5
3 wins 2 = 4 5
3 wins 2 = 4 5
3 wins 2 = 4 5
4 wins 1 = 5
4 wins 1 = 5
4 wins 1 = 5
4 wins 1 = 5
4 wins 1 = 5
4 wins 1 = 5
4 wins 1 = 5
4 wins 1 = 5
4 wins 1 = 5
5 wins 0
5 wins 0
5 wins 0
5 wins 0
5 wins 0
5 wins 0
5 wins 0
5 wins 0
5 wins 0
5 wins 0
5 wins 0
5 wins 0
5 wins 0
6 wins 0

"""