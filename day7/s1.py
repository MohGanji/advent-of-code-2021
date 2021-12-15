nums = list(map(int, input().split(',')))

nums.sort()

median = nums[len(nums)//2]

diff = 0
for i in nums:
	diff += abs(i - median)

print(diff)
