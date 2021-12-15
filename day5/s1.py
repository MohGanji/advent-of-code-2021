from sys import stdin
from collections import defaultdict

cov = defaultdict(int)

for line in stdin:	
	p1, p2 = line.split("->")
	p1 = list(map(int, p1.split(",")))
	p2 = list(map(int, p2.split(",")))
	
	if p1[0] == p2[0]:
		for i in range(min(p1[1], p2[1]), max(p1[1], p2[1])+1):
			cov["{},{}".format(p1[0], i)] += 1
	elif p1[1] == p2[1]:
		for i in range(min(p1[0], p2[0]), max(p1[0], p2[0])+1):
			cov["{},{}".format(i, p1[1])] += 1
	
cnt = 0
for val in cov.values():
	if val > 1:
		cnt += 1

print(cnt)
		

		
