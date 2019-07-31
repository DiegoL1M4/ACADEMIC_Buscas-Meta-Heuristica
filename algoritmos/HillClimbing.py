class HillClimbing(object):

    def __init__(self, game):
        self.game = game

    def result(self, limit):
        print('\nProblema Inicial:')
        self.game.mostrar(self.game.tabuleiro)

        totalColides = 0
        movements = 0
        for k in range(int(limit)):
            self.game.move()
            movements = k + 1
            newTotalColides = self.game.amountAtk(self.game.tabuleiro)
            if(newTotalColides == totalColides):
                break
            else:
                totalColides = newTotalColides

        print('\nResultado:')
        self.game.mostrar(self.game.tabuleiro)
        print('Total de Colisões: ' + str(self.game.amountAtk(self.game.tabuleiro)))
        print('Total de Movimentos: ' + str(movements))

        print('\nQuadro de Movimentações')
        self.game.mostrar(self.game.neighbour())
        print()
        