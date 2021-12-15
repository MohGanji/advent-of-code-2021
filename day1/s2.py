from sys import stdin

ans = 0
window = [float("inf"), float("inf"), float("inf"), float("inf")]

for line in stdin:
	next = int(line)
	window = window[1:] + [next]
	#print(window)
	if sum(window[:3]) < sum(window[1:]):
		ans += 1

print(ans)
