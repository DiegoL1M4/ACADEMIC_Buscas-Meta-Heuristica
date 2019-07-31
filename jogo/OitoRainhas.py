
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

	def amountAtk(self,tabuleiro):
		total = 0

		# Check all queens
		for queen in self.localQueens(tabuleiro):
			# Check in Line
			for line in tabuleiro[ queen[0] ]:
				if(line == 1):
					total += 1
			total -= 1

			# Check on main diagonal
			linhaAJD = queen[0]
			colunaAJD = queen[1]
			while (linhaAJD != 0 and colunaAJD != 0):
				linhaAJD -= 1
				colunaAJD -= 1

			for k in range(8):
				if((linhaAJD+k) == 8 or (colunaAJD+k) == 8):
					break
				if(tabuleiro[linhaAJD+k][colunaAJD+k] == 1):
					total += 1
			total -= 1

			# Check on secondary diagonal
			linhaAJD = queen[0]
			colunaAJD = queen[1]
			while (linhaAJD != 0 and colunaAJD != 7):
				linhaAJD -= 1
				colunaAJD += 1

			for k in range(8):
				if((linhaAJD+k) == 8 or (colunaAJD-k) == -1):
					break
				if(tabuleiro[linhaAJD+k][colunaAJD-k] == 1):
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

	# Auxiliaries Methods
	def mostrar(self, tabuleiro):
		for i in tabuleiro:
			for j in i:
				print("  " + str(j), end="")
			print()

	def copy(self, tabuleiro):
		matrix = []
		for i in range(8):
			line = []
			for j in range(8):
				line.append(self.tabuleiro[i][j])
			matrix.append(line)
		return matrix

	# Neighbour
	def neighbour(self):
		matrix = []
		for i in range(8):
			line = []
			for j in range(8):
				newTab = self.copy(self.tabuleiro)

				# Erases the entire column of the jth
				for k in range(8):
					newTab[k][j] = 0
				# Places the queen
				newTab[i][j] = 1

				line.append( self.amountAtk(newTab) )
			matrix.append(line)
		return matrix

	def smallest(self,tabuleiro):
		menor = tabuleiro[0][0]
		pos = [0,0]
		for i in range(8):
			for j in range(8):
				if (tabuleiro[i][j] < menor):
					menor = tabuleiro[i][j]
					pos = [i,j]
		return pos

	def move(self):
		pos = self.smallest( self.neighbour() )
		
		# Erases the entire column of the jth
		for k in range(8):
			self.tabuleiro[ k ][ pos[1] ] = 0

		self.tabuleiro[ pos[0] ][ pos[1] ] = 1

'''
e = OitoRainhas()
e.mostrar(e.tabuleiro)
print()
e.mostrar(e.neighbour())
print()
e.move()
e.mostrar(e.tabuleiro)
print()
e.mostrar(e.neighbour())
'''