from sys import stdin

depth = 0
x = 0

for line in stdin:
	cmd, amount = line.split(' ')
	amount = int(amount)
	if cmd == 'up':
		depth -= amount
	elif cmd == 'down':
		depth += amount
	elif cmd == 'forward':
		x += amount


print(x * depth)
