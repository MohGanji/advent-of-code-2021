from sys import stdin

depth = 0
x = 0
aim = 0

for line in stdin:
	cmd, amount = line.split(' ')
	amount = int(amount)
	if cmd == 'up':
		aim -= amount
	elif cmd == 'down':
		aim += amount
	elif cmd == 'forward':
		x += amount
		depth += aim * amount


print(x * depth)
