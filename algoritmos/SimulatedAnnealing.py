
import time
import random
import numpy as np

class SimulatedAnnealing(object):

    def __init__(self, game):
        self.game = game

    def result(self, limit, temperature, P, L, alpha):
        # Time
        start = time.time()

        # Iterations with limit
        for round in range(limit):
            nHits = 0
            for k in range(P):
                Si = self.pertuba()
                # Duvida: não pode repetir a escolha? Pode ser aleatório?
                # DUVIDA: transformar o simulated em hill Climbing


                delta = self.game.eval(Si) - self.game.eval(self.game.positions)
                if( (delta <= 0) or (np.exp(-delta / temperature) > random.random()) ):
                    self.game.positions = Si
                    nHits += 1
                if(nHits >= L):
                    break

            temperature = temperature * alpha
            if(nHits == 0):
                break

        # Time
        end = time.time()

        print("Total de excução: " + str(end - start))
        print("Total de execuções: " + str(round + 1))

        return self.game.positions

    def pertuba(self):
        neighbors = self.game.neighbors()
        k = random.randrange(0, len(neighbors))
        return neighbors[k]

    
    def result2(self, limit, temperature, P, L, alpha):
        # Time
        start = time.time()

        # Iterations with limit
        for round in range(limit):
            nHits = 0
            for k in range(P):
                Si = self.pertuba()
                # Duvida: não pode repetir a escolha? Pode ser aleatório?
                # DUVIDA: transformar o simulated em hill Climbing


                delta = self.game.eval(Si) - self.game.eval(self.game.positions)
                if( (delta <= 0) or (np.exp(-delta / temperature) > random.random()) ):
                    self.game.positions = Si
                    nHits += 1
                if(nHits >= L):
                    break

            temperature = temperature * alpha
            if(nHits == 0):
                break

        # Time
        end = time.time()

        print("Total de excução: " + str(end - start))
        print("Total de execuções: " + str(round + 1))

        return self.game.positions

    def pertuba(self):
        neighbors = self.game.neighbors()
        k = random.randrange(0, len(neighbors))
        return neighbors[k]








        '''
        print('\nProblema Inicial:')
        self.game.show(self.game.tabuleiro)

        totalColides = 0
        movements = 0

        inicio = time.time()

        # Execução do Método
        for k in range(int(limit)):
            print()

        fim = time.time()

        print('\nResultado:')
        self.game.mostrar(self.game.tabuleiro)
        print('Total de Colisões: ' + str(self.game.amountAtk(self.game.tabuleiro)))
        print('Total de Movimentos: ' + str(movements))
        print('Tempo Total: ' + str(round(fim - inicio, 4)) + ' milisegundos')

        print('\nQuadro de Movimentações')
        self.game.mostrar(self.game.neighbour())
        print()
        '''
