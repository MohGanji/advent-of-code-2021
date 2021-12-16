from sys import stdin

ans = 0
for line in stdin:
	uniques, entry = line.strip('\n').split(" | ")
	for digit in entry.split(' '):
		# print(digit)
		if len(digit) in [2, 3, 4, 7]:
			ans += 1
	
print(ans)
