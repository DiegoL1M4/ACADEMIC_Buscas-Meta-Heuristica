
import random

class OitoRainhas(object):

	def __init__(self):
		# Board Creation
		self.tabuleiro = []
		for k in range(8):
			self.tabuleiro.append([0,0,0,0,0,0,0,0])

		# Queens Distribution
		self.rainhas = []
		for k in range(8):
			self.rainhas.append(random.randrange(0, 8))
		for k in range(8):
			self.tabuleiro[self.rainhas[k]][k] = 1

	def amountAtk(self):
		total = 0

		# Check all queens
		for queen in self.localQueens(self.tabuleiro):
			# Check in Line
			for line in self.tabuleiro[ queen[0] ]:
				if(line == 1):
					total += 1
			total -= 1

			# Check on main diagonal
			linhaAJD = queen[0];
			colunaAJD = queen[1];
			while (linhaAJD != 0 and colunaAJD != 0):
				linhaAJD -= 1
				colunaAJD -= 1

			for k in range(8):
				if((linhaAJD+k) == 8 or (colunaAJD+k) == 8):
					break;
				if(self.tabuleiro[linhaAJD+k][colunaAJD+k] == 1):
					total += 1
			total -= 1

			# Check on secondary diagonal
			linhaAJD = queen[0];
			colunaAJD = queen[1];
			while (linhaAJD != 0 and colunaAJD != 7):
				linhaAJD -= 1
				colunaAJD += 1

			for k in range(8):
				if((linhaAJD+k) == 8 or (colunaAJD-k) == -1):
					break;
				if(self.tabuleiro[linhaAJD+k][colunaAJD-k] == 1):
					total += 1
			total -= 1

		return total

	def localQueens(self, tabuleiro):
		list = []
		for i in range(8):
			for j in range(8):
				if(tabuleiro[i][j] == 1):
					list.append([i,j])
		return list

	# Show Board
	def mostrar(self):
		for i in self.tabuleiro:
			for j in i:
				print(" " + str(j), end="")
			print()

'''
e = OitoRainhas(5)
e.mostrar()
print(e.localQueens(e.tabuleiro))
print(e.amountAtk())
'''
