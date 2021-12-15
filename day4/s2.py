from sys import stdin

class Board:
	
	def __init__(self, rows):
		self.rows = rows
		self.seen_rows = [[] for i in range(5)]
		self.winning_row = None
		self.seen_cols = [[] for i in range(5)]
	
	def see(self, num):
		for i in range(len(self.rows)):
			for j in range(len(self.rows[i])):
				if self.rows[i][j] == num:
					self.rows[i][j] = None
					self.seen_rows[i].append(num)
					# print('row{}: {}'.format(i+1, self.seen_rows[i]))
					if len(self.seen_rows[i]) == 5:
						self.winning_row = self.seen_rows[i]
						return True
					self.seen_cols[j].append(num)
					# print('col{}: {}'.format(j+1, self.seen_cols[j]))
					# print()
					if len(self.seen_cols[j]) == 5:
						self.winning_row = self.seen_cols[j]
						return True
	
	def winner(self):
		return self.winning_row is not None

	def get_winning_score(self):
		if not self.winning_row:
			return 0
		return sum([sum(list(map(lambda x: x if x else 0, row))) for row in self.rows]) * self.winning_row[-1]
				

nums = list(map(int, input().split(',')))
boards = []
current_board = []

for line in stdin:	
	if len(line) < 2: # new line
		if len(current_board):
			boards.append(Board(current_board))
		current_board = []
	
	else: # a line of numbers
		row = list(
					map(
						int, 
						filter(
							lambda x: x != '', 
							line.split(' ')
						)
					)
				)
		current_board.append(row)
	
if len(current_board) == 5:
	boards.append(Board(current_board))

boards_to_remove = []
for num in nums:
	print('------')
	print('num: {}'.format(num))
	for board in boards:
		win = board.see(num)
		if win:
			print(board.get_winning_score())
			boards_to_remove.append(board)
	if len(boards_to_remove):
		for b in boards_to_remove:
			boards.remove(b)
		boards_to_remove = []

