from sys import stdin

diffs = []

for line in stdin:
	if not len(diffs):
		diffs = [0]*(len(line)-1)
	for i in range(len(line)):
		if line[i] == '1':
			diffs[i] += 1
		elif line[i] == '0':
			diffs[i] -= 1
	
most_common = ""
least_common = ""
for i in diffs:
	if i >= 0:
		most_common += "1"
		least_common += "0"
	else:
		most_common += "0"
		least_common += "1"
	


print(int(most_common, 2) * int(least_common, 2))
