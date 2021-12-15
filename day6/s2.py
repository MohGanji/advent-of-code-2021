mem = {}

def headcount(rem_days, init_days):
	if rem_days <= init_days:
		return 1
	else:
		mem_key = "{}:{}".format(rem_days, init_days)
		if mem_key in mem:
			return mem[mem_key]
		ans = headcount(rem_days - init_days, 7) + headcount(rem_days - init_days, 9)
		mem[mem_key] = ans
		return ans

nums = list(map(int, input().split(',')))
DAYS = 256

ans = 0

for n in nums:
	ans += headcount(DAYS, n)

print(ans)
