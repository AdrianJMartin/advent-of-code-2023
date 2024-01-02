check_sum = [3,2,1]
pattern = "?###????????"
pat_len = len(pattern)
# 012345678901
# ###.....##.#
# ------

for ri,run in enumerate(check_sum):
	left = sum( check_sum[:ri] ) + ri
	mid = "#" * run
	right = sum( check_sum[ri+1:] ) + len(check_sum[ri+1:]) - 1
	max = pat_len - len(mid) - right - left -1
	for i in range(max):
		t = "." * i
		t += mid
		t += "." * ( right - i )
		print(t)

# ###.....##.# 