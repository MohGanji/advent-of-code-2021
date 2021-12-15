nums = list(map(int, input().split(',')))
DAYS = 80
for _ in range(DAYS):
	nums_copy = nums[:]
	for i in range(len(nums_copy)):
		if nums_copy[i] == 0:
			nums[i] = 6
			nums.append(8)
		else:
			nums[i] -= 1

print(len(nums))
