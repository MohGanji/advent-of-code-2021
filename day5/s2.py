from sys import stdin
from collections import defaultdict

cov = defaultdict(int)

for line in stdin:	
	p1, p2 = line.split("->")
	p1 = list(map(int, p1.split(",")))
	p2 = list(map(int, p2.split(",")))
	if p1[0] == p2[0]:
		for i in range(min(p1[1], p2[1]), max(p1[1], p2[1])+1):
			s = "{},{}".format(p1[0], i)
			cov[s] += 1
	elif p1[1] == p2[1]:
		for i in range(min(p1[0], p2[0]), max(p1[0], p2[0])+1):
			s = "{},{}".format(i, p1[1])
			cov[s] += 1
	else:
		slope = (p2[1]-p1[1])//(p2[0]-p1[0])
		x_dir = 1 if p2[0] - p1[0] > 0 else -1
		y_diff = 0
		for i in range(p1[0], p2[0] + (1 * x_dir), 1*x_dir):
			s = "{},{}".format(i, p1[1] + (x_dir * slope * y_diff))
			cov[s] += 1
			y_diff += 1

cnt = 0
for val in cov.values():
	if val > 1:
		cnt += 1

print(cnt)
		
