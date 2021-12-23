from sys import stdin

corr_mapping = {
	'{': '}',
	'(': ')',
	'<': '>',
	'[': ']'
}
closing = '})>]'
scores = {
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137
}


ans = 0
for line in stdin:
	ch_stack = []
	for ch in line:
		if ch in closing:
			top = ch_stack.pop()
			if corr_mapping[top] != ch:
				ans += scores[ch]
				break
		else:
			ch_stack.append(ch)

print(ans)
