from sys import stdin

ROUNDS = 100
flashes = 0
nums = []
for line in stdin:	
	nums.append(list(map(int, list(line.strip()))))

w = len(nums)
h = len(nums[0])

def increase(x, y):
	global flashes
	if nums[x][y] == -1:
		return
	if nums[x][y] != 9:
		nums[x][y] += 1
		return

	# nums[x][y] == 9:
	nums[x][y] = -1
	flashes += 1
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

for r in range(ROUNDS):
	for i in range(w):
		for j in range(h):
			increase(i, j)
	for i in range(w):
		for j in range(h):
			set_zero(i, j)

print(flashes)
