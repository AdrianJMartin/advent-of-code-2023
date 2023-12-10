seeds: 79 14 55 13

ranges = [
	(79,14),
	(55,13)
]



map:
50 98 2
52 50 48

for each range:
	for each map:
		for each mapping:

r 79,14
	if 79 => 98 and 79+14 <= 98+2: no
	if 79 => 50 and 79+14 <= 50+48:

yes:
		79 -> 79 - 98 - 50 = 31
		14 -> 14

r55,13
if 55 => 98 and 55+13 <= 98+2: no
if 55 => 50 and 55+13 <= 50+48:
	yes:
		55 -> 55 + 52 - 50 = 57 
		13 -> 13

31,14
7,13

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

31,14

if 31 => 15 and 31+14 <= 15+37:
	yes
	31,14 -> 31 + 15 - 0 = 46,14

if 31 => 52 and 31+14 <= 52+2:
	no:

if 31 => 0 and 31+14 <= 0 + 15:
	no

