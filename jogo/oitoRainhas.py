
import random
import numpy as np

class OitoRainhas(object):

	"""docstring for oitoRainhas"""
	def __init__(self, d):
		self.tabuleiro = []

		print(np.random.uniform(1, 8))


		for x in range(8):
			self.tabuleiro.append([0,0,0,0,0,0,0,0])

	def mostrar(self):
		print(self.tabuleiro)


e = OitoRainhas(5)
e.mostrar()
		