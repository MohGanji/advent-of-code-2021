from sys import stdin

diffs = []
items = []

for line in stdin:
	items.append(line.strip('\n'))

diffs = [0]*len(line)
oxygen_rating_items = items[:]
# print(oxygen_rating_items)
for i in range(len(items[0])): # at most iterate until all bits are seen
	for line in oxygen_rating_items:
		if line[i] == '1':
			diffs[i] += 1
		elif line[i] == '0':
			diffs[i] -= 1
	
	filter_bit = "1" if diffs[i] >= 0 else "0"
	oxygen_rating_items = list(filter(lambda item: item[i] == filter_bit, oxygen_rating_items))
	# print(filter_bit, oxygen_rating_items)
	if len(oxygen_rating_items) == 1:
		break
	
co2_rating_items = items[:]
# print(co2_rating_items)
for i in range(len(items[0])): # at most iterate until all bits are seen
	for line in co2_rating_items:
		if line[i] == '1':
			diffs[i] += 1
		elif line[i] == '0':
			diffs[i] -= 1
	
	filter_bit = "0" if diffs[i] >= 0 else "1"
	co2_rating_items = list(filter(lambda item: item[i] == filter_bit, co2_rating_items))
	# print(filter_bit, co2_rating_items)
	if len(co2_rating_items) == 1:
		break
	

print(int(oxygen_rating_items[0], 2) * int(co2_rating_items[0], 2))
