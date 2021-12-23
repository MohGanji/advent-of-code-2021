from sys import stdin

nums = []
for line in stdin:
	nums.append(list(map(int, list(line.strip()))))

height = len(nums)
width = len(nums[0])

low_points = []
for i in range(height):
	for j in range(width):
		left = j == 0 or nums[i][j] < nums[i][j-1]
		right = j == width-1 or nums[i][j] < nums[i][j+1]
		up = i == 0 or nums[i][j] < nums[i-1][j]
		down = i == height-1 or nums[i][j] < nums[i+1][j]

		low_point = up and left and right and down

		if low_point:
			low_points.append((i, j))


marked = [[False for j in range(width)] for i in range(height)]
def rec_find_basin(point):
	x = point[0]
	y = point[1]
	if x >= height or y < 0 or y >= width or x < 0:
		return 0
	if nums[x][y] == 9:
		return 0
	if marked[x][y]:
		return 0
	marked[x][y] = True
	left = rec_find_basin((x, y-1))
	right = rec_find_basin((x, y+1))
	up = rec_find_basin((x-1, y))
	down = rec_find_basin((x+1, y))

	return 1 + right + left + up + down

basins = []
for p in low_points:
	basin_size = rec_find_basin(p)
	basins.append(basin_size)

basins.sort(reverse=True)
print(basins[0] * basins[1] * basins[2])

