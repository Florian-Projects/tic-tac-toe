# TODO add checks for valid player symbols (2 players cannot use the same symbol,
#  symbol needs to be a visible character and can't be a number)
# TODO refactor comments
# TODO change self parameters such that only the necessary information is given to the function instead of all
# TODO improve Board.check_column() by using transposition check:
#  https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions for more information

import numpy as np


class Board:

	def __init__(self, size=9):
		self.board = [[1, 2, 3],
					  [4, 5, 6],
					  [7, 8, 9]]
		if self.is_square(size):
			self.board = self.create_board(size)
		else:
			self.board = [[1, 2, 3],
						[4, 5, 6],
						[7, 8, 9]]

	@staticmethod
	def is_square(x):
		y = np.sqrt(x)
		y = int(y)
		if y * y == x:
			return True
		else:
			return False

	def print_board(self):
		for i in self.board:
			print(str(i).replace(","," "))

	def create_board(self, size):
		board = []
		width, height = int(np.sqrt(size)), int(np.sqrt(size))
		index = 1
		for y in range(height):
			board.append([])
			for x in range(width):
				board[y].append(index)

		return board


	def check_win_condition(self):
		if self.check_rows() or self.check_columns() or self.check_diagonals():
			return True
		else:
			return False

	def check_rows(self):
		for i in range(len(self.board)):
			if self.is_list_equal(self.board[i]):
				return True
		return False

	def check_columns(self):
		column = []
		for i in range(len(self.board)):
			for j in range(len(self.board)):
				column.append(self.board[j][i])
			if self.is_list_equal(column):
				return True
			column = []
		return False

	def check_diagonals(self):
		diagonal = []
		for i in range(len(self.board)):
			diagonal.append(self.board[i][i])
		if self.is_list_equal(diagonal):
			return True

		diagonal = []
		for i in range(len(self.board) - 1, -1, -1):
			diagonal.append(self.board[i][i - len(self.board)])
		if self.is_list_equal(diagonal):
			return True

		return False

	@staticmethod
	def is_list_equal(x):
		"""checks if all elemnts of a 1d Array are the same and returns a boolean"""

		for i in range(len(x) - 1):
			if x[i] == x[i + 1]:
				continue
			else:
				return False

		return True


class Game:

	def __init__(self, board, player1, player2):
		self.board = board
		self.player1 = player1
		self.player2 = player2

	# We could make the game logic by using a while loop an the Board.check_win_condition() method.
	# However we want to try to use recursion for this.
	# As far as we can tell there is no logical reason to use recursion here.
	# This is purely for fun

	def start_game(self):
		return self.turn_player1()

	def turn_player1(self):
		self.player1.make_move(self.board)
		if self.board.check_win_condition():
			return "{} Wins".format(self.player1.name)

		else:
			return self.turn_player2()

	def turn_player2(self):
		self.player2.make_move(self.board)
		if self.board.check_win_condition():
			return "{} Wins".format(self.player2.name)
		else:
			return self.turn_player1()


class Player:
	def __init__(self, name, symbol):
		self.name = name
		self.symbol = symbol

	def make_move(self, board):
		board.print_board()
		position = int(input("{} choose a Position.\n".format(self.name)))
		for i, sublist in enumerate(board.board):
			if position in sublist:
				board.board[i][board.board[i].index(position)] = self.symbol

playingfield = Board(25)
player1 = Player("Florian", "X")
player2 = Player("Kilian", "O")
game = Game(playingfield, player1, player2)
game.start_game()
