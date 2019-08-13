
import random
import math

class OitoRainhas(object):

	def __init__(self):
		# Board Creation
		self.positions = self.create()

	# Generate one position on board
	def getValue(self):
		return random.randrange(1, 9)

	# Create the positions of the board
	def create(self):
		list = []
		for k in range(8):
			list.append( self.getValue() )
		return list

	# Mathematics
	def combinacao(self, n, p):
		return ( math.factorial(n) / (math.factorial(p) * math.factorial(n - p)) )

	# Evaluation the queens atacks
	def eval(self,positions):
		total = 0
		
		board = []
		for k in range(8):
			board.append([0,0,0,0,0,0,0,0])
		for k in range(8):
			board[positions[k] - 1][k] = 1

		# All lines
		for line in board:
			cont = 0
			for column in range(8):
				if(line[column] == 1):
					cont += 1
			if(cont > 1):
				total += self.combinacao(cont, 2)

		# All main diagonal
		for k in range(0,7):
			cont = 0
			i = k
			j = 0
			while (i <= 7):
				if(board[i][j] == 1):
					cont += 1
				i += 1
				j += 1
			if(cont > 1):
				total += self.combinacao(cont, 2)
		for k in range(1,7):
			cont = 0
			i = 0
			j = k
			while (j <= 7):
				if(board[i][j] == 1):
					cont += 1
				i += 1
				j += 1
			if(cont > 1):
				total += self.combinacao(cont, 2)

		# All second diagonal
		for k in range(1,8):
			cont = 0
			i = k
			j = 0
			while (i >= 0):
				if(board[i][j] == 1):
					cont += 1
				i -= 1
				j += 1
			if(cont > 1):
				total += self.combinacao(cont, 2)
		for k in range(1,7):
			cont = 0
			i = 7
			j = k
			while (j <= 7):
				if(board[i][j] == 1):
					cont += 1
				i -= 1
				j += 1
			if(cont > 1):
				total += self.combinacao(cont, 2)

		return total

	# Find the neighbors
	def neighbors(self):
		list = []
		for column in range(8):
			for k in range(1,9):
				if( k != self.positions[column] ):
					copy = self.positions[:]
					copy[column] = k
					list.append( copy )
		return list

	# Auxiliaries Methods
	def show(self, tabuleiro):
		for i in range(8):
		    for j in range(8):
		        if(tabuleiro[j] == i+1):
		            print(" 1", end="")
		        else:
		            print(" 0", end="")
			print()
