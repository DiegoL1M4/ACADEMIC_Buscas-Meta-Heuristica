
import time

class SimulatedAnnealing(object):
    
    def __init__(self, game):
        self.game = game
    
    def result(self, limit):
        print('\nProblema Inicial:')
        self.game.mostrar(self.game.tabuleiro)

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