from sys import stdin

ans = 0
prev = float("inf")
for line in stdin:
	next = int(line)
	if next > prev:
		ans += 1
	prev = next

print(ans)
