
import random
import time
import math

class AlgoritmosGeneticos(object):

    def __init__(self, game):
        self.game = game

    def result(self, limit, tamPopulation, E, R, M):

        population = []
        evaluations = []

        for k in range(tamPopulation):
            population.append( self.game.randomQueens() )

        

        for k in range(limit):
            # Evaluation
            for individual in population:
                evaluations.append( self.game.amountAtk2(individual) )

            if( min(evaluations) == 0 ):
                return population[ population.index( min(evaluations) ) ]
            # As evaluations servem só pra ter saber se convergiu?

            newPopulation = []

            # Election
            iterations = int(tamPopulation * E)
            indexRan = random.randrange(0, tamPopulation)
            for k in range(iterations):
                if(indexRan + iterations > len(population) - 1):
                    indexRan = (indexRan + iterations) - len(population)
                else:
                    indexRan += iterations
                newPopulation.append( population[indexRan] )

            # Reproduction
            iterations = int(tamPopulation * R)
            mask = [0,1,0,1,0,1,0,1]
            for k in range(iterations):
                f1 = random.randrange(0, len(newPopulation))
                f2 = random.randrange(0, len(newPopulation))
                newIndividual = []
                for k in range(8):
                    if(mask[k] == 0):
                        newIndividual.append(newPopulation[f1][k])
                    else:
                        newIndividual.append(newPopulation[f2][k])
                newPopulation.append( newIndividual )
            #Duvida: uso pra reprodução sempre a lista atualizada da nova população?

            # Mutation
            iterations = int(tamPopulation * M)
            for k in range(iterations):
                indexRan = random.randrange(0, len(newPopulation))
                copy = newPopulation[indexRan][:]

                selectColumn = random.randrange(0, 8)
                newLine = random.randrange(0, 8)

                copy[selectColumn] = newLine
                newPopulation.append(copy)

            population = newPopulation






'''
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

def population(self):
    pass

def selection(self):
    pass

def reproduction(self):
    pass

def mutation(self):
    pass
'''
