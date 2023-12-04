import regex
rx = r"(\d|one|two|three|four|five|six|seven|eight|nine)"
num_list = rx[1:-1].split("|")

def part_1( line : str ):
	f = None
	l = None

	for c in line:
		if c.isdigit() :
			l = c
		
			if f == None:
				f = c

	if f and l:
		return int( f + l )
	else:
		return 0

def part_2( line : str ):
	m = regex.findall( rx , line , overlapped=True )

	f = m[0]
	if f in num_list:
		f = str( num_list.index(f) )

	l = m[-1:][0]
	if l in num_list:
		l = str( num_list.index(l))

	print(f"{line.rstrip()} {f}{l}")

	return int( f + l )

def no_rx( line:str):
	digits = []
	for i in range(len(line)):
		if line[i:i+3] == 'one':
			digits.append(1)
		
		if line[i:i+3] == 'two':
			digits.append(2)
		
		if line[i:i+5] == 'three':
			digits.append(3)
		
		if line[i:i+4] == 'four':
			digits.append(4)
		
		if line[i:i+4] == 'five':
			digits.append(5)
		
		if line[i:i+3] == 'six':
			digits.append(6)
		
		if line[i:i+5] == 'seven':
			digits.append(7)
		
		if line[i:i+5] == 'eight':
			digits.append(8)
		
		if line[i:i+4] == 'nine':
			digits.append(9)
		
		if line[i].isdigit() :
			digits.append(int(line[i]))
	
	print( digits)

	return int( f"{digits[0]}{digits[-1]}" )

with open("input-data-p2-test.txt","r") as f:

	sum1 = 0
	sum2 = 0
	sum3 = 0

	for line in f:

		sum1 += part_1(line)
		sum2 += part_2(line)
		sum3 += no_rx(line)
	
	print( f"part 1: {sum1}" )
	print( f"part 2: {sum2}" )
	print( f"part 2 no rx: {sum3}" )
