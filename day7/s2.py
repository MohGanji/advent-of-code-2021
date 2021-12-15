nums = list(map(int, input().split(',')))

def get_diff(nums, r):
	return sum(list(
				map(
					lambda a: (abs(a-r) * (abs(a-r)+1)) // 2,
					nums
				)
			))

ans = float('inf')
for r in range(min(nums), max(nums)):
	diff = get_diff(nums, r)
	if diff < ans:
		ans = diff

print(ans)
