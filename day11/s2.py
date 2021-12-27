from sys import stdin

nums = []
for line in stdin:	
	nums.append(list(map(int, list(line.strip()))))

w = len(nums)
h = len(nums[0])

def increase(x, y):
	if nums[x][y] == -1:
		return
	if nums[x][y] != 9:
		nums[x][y] += 1
		return

	# nums[x][y] == 9:
	nums[x][y] = -1
	RADIUS = 1
	for i in range(x-RADIUS, x+RADIUS+1):
		if i not in list(range(w)):
			continue
		for j in range(y-RADIUS, y+RADIUS+1):
			if j not in list(range(h)):
				continue
			increase(i, j)

def set_zero(x, y):
	if nums[x][y] == -1:
		nums[x][y] = 0
		return 1
	return 0

for r in range(10000):
	for i in range(w):
		for j in range(h):
			increase(i, j)
	flashes = 0
	for i in range(w):
		for j in range(h):
			flashes += set_zero(i, j)
	if flashes == w*h:
		print(r+1)
		break

