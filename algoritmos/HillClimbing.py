
import time

class HillClimbing(object):

    def __init__(self, game):
        self.game = game

    def result(self, limit):
        # Time
        start = time.time()

        res = []

        # Iterations with limit
        for round in range(limit):
            neighbors = self.game.neighbors()
            
            # Evaluation
            evaluations = []
            for one in neighbors:
                evaluations.append( self.game.eval( one ) )

            res = population[ evaluations.index( min(evaluations) ) ]

            if(newTotalColides == totalColides):
                break
            else:
                totalColides = newTotalColides







        print('\nProblema Inicial:')
        self.game.mostrar(self.game.tabuleiro)

        totalColides = 0
        movements = 0
        
        inicio = time.time()

        # Execução do Método
        for k in range(int(limit)):
            self.game.move()
            movements = k + 1
            newTotalColides = self.game.amountAtk(self.game.tabuleiro)
            if(newTotalColides == totalColides):
                break
            else:
                totalColides = newTotalColides
                
        fim = time.time()

        print('\nResultado:')
        self.game.mostrar(self.game.tabuleiro)
        print('Total de Colisões: ' + str(self.game.amountAtk(self.game.tabuleiro)))
        print('Total de Movimentos: ' + str(movements))
        print('Tempo Total: ' + str(round(fim - inicio, 4)) + ' milisegundos')

        print('\nQuadro de Movimentações')
        self.game.mostrar(self.game.neighbour())
        print()
        