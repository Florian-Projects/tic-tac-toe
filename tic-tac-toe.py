#TODO create function to create different sizes of playing fields
#TODO add checks for valid player symbols (2 players cannot use the same symbol, symbol needs to be a visible character and can't be a number)
#TODO refactor comments
#TODO change self parameters such that only the necessary information is given to the function instead of all
#TODO improve Board.check_column() by using transposition check: https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions for more information
import numpy as np

class Board:
	board = []
	
	def __init__(self, *args):
		if args:
			print(type(args[0]))
			if self.is_square(args[0]):
				self.create_board(args[0])
				print(self.board)
			else:
				board = [[1,2,3],
					 	[4,5,6],
						[7,8,9]]
					 			
	def is_square(self, x):
		print(x)
		y = np.sqrt(x)
		y = int(y)
		if y*y == x:
			return True
		else:
			return False
	

	def create_board(self, size):
		width, height = np.sqrt(size) #technically 1 variable would be enough to conserve memory space however this makes the code easier to read
		for i in range(size, height):
			self.board.append([])
			for j in range(height,width*i, 1):
				self.board[i].append(j)
			
	def check_win_condition(self):
		if self.check_rows() or self.check_columns() or self.check_diagonals(): #Why do I have to add selfe as a parameter?
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
		for i in range(len(self.board)-1,-1,-1):
			diagonal.append(self.board[i][i-len(self.board)])	
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
	
	board = 0
	
	def __init__(self, board, player1, player2):
		self.board = board
		self.player1 = player1
		self.player2 = player2
		
	#We could make the game logic by using a while loop an the Board.check_win_condition() method. However we want to try to use recursion for this. As far as we can tell there is no logical reason to use recursion here. This is purely for fun
	
	def start_game(self): 
		return self.turn_player1()
	
	def turn_player1(self):
		self.player1.make_move(self.board)
		if self.board.check_win_condition(self.board):
			return "{} Wins".format(self.player1.name)
		
		else:
			return self.turn_player2()
		
	def turn_player2(self):
		self.player2.make_move(self.board)
		if self.board.check_win_condition(self.board):
			return "{} Wins".format(self.player2.name)
		else:
			return self.turn_player1()
		
	
class Player:
	def __init__(self, name, symbol):
		self.name = name
		self.symbol = self.name
	
	def make_move(self, board):
		position = input("{} choose a Position.".format(self.name))
		index = board.board.index(position)
		board.board[index[0]][index[1]] = self.symbol

						
		
board = Board(25)
#player1 = Player("Florian", "X")
#player2 = Player("Kilian", "O")

#game = Game(board, player1, player2)

#game.start_game()

