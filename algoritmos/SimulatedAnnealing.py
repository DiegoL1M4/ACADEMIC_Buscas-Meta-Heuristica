
import time

class SimulatedAnnealing(object):

    def __init__(self, game):
        self.game = game

    def result(self, limit, temperature, nHits):
        # Time
        start = time.time()

        res = []

        # Iterations with limit
        for round in range(limit):
            print(self.game.neighbors())
            input()


        # Time
        end = time.time()

        print("Total de excução: " + str(end - start))
        print("Total de execuções: " + str(round + 1))

        return res








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
