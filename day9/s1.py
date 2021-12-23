from sys import stdin

nums = []
for line in stdin:
	nums.append(list(map(int, list(line.strip()))))

ans = 0
for i in range(len(nums)):
	for j in range(len(nums[0])):
		left = j == 0 or nums[i][j] < nums[i][j-1]
		right = j == len(nums[0])-1 or nums[i][j] < nums[i][j+1]
		up = i == 0 or nums[i][j] < nums[i-1][j]
		down = i == len(nums)-1 or nums[i][j] < nums[i+1][j]

		low_point = up and left and right and down

		if low_point:
			ans += nums[i][j] + 1

print(ans)
