from sys import stdin

corr_mapping = {
	'{': '}',
	'(': ')',
	'<': '>',
	'[': ']'
}
closing = '})>]'
scores = {
	')': 1,
	']': 2,
	'}': 3,
	'>': 4
}


answers = []
for line in stdin:
	ch_stack = []
	corrupted = False
	ans = 0
	for ch in line.strip():
		if ch in closing:
			top = ch_stack.pop()
			if corr_mapping[top] != ch:
				corrupted = True
				break
		else:
			ch_stack.append(ch)
	if corrupted:
		continue
	for c in reversed(ch_stack):
		ans = (ans * 5) + scores[corr_mapping[c]]
	answers.append(ans)

answers.sort()
print(answers[len(answers)//2])
