
import random
import time
import math

class AlgoritmosGeneticos(object):

    def __init__(self, game):
        self.game = game

    def result(self, limit, tamPopulation, E, R, M):
        # Time
        start = time.time()

        res = []

        # Create a population
        population = []
        for k in range(tamPopulation):
            population.append( self.game.create() )

        # Iterations with limit
        for round in range(limit):
            # Evaluation
            evaluations = []
            for individual in population:
                evaluation = self.game.eval(individual)
                for k in range( len(evaluations) + 1 ):
                    if( k == len(evaluations) ):
                        evaluations.insert( k, [evaluation, individual] )
                        continue
                    if( evaluations[k][0] < evaluation ):
                        evaluations.insert( k, [evaluation, individual] )
            #print(evaluations)
            #input()

            # Selecting the best of the current population
            res = evaluations[0][1]

            # Stop condition
            if( evaluations[0][0] == 0 ):
                break

            # New population
            newPopulation = []

            # Election
            iterations = int(tamPopulation * E)
            for k in range(iterations):
                newPopulation.append(evaluations[k][1])

            # Reproduction
            iterations = int( (tamPopulation * R) / 2 )
            for k in range(iterations):
                div = random.randrange(0, 8)

                individual1 = self.rodeo(4, population)
                individual2 = self.rodeo(4, population)

                newIndividual = individual1[0:div]
                newIndividual.extend( individual2[div:8] )
                newPopulation.append( newIndividual )

                newIndividual = individual2[0:div]
                newIndividual.extend( individual1[div:8] )
                newPopulation.append( newIndividual )

            # Mutation
            iterations = int(tamPopulation * M)
            for k in range(iterations):
                individual = self.rodeo(4, population)
                copy = individual[:]

                selectColumn = random.randrange(0, 8)

                copy[selectColumn] = self.game.getValue()
                newPopulation.append(copy)

            population = newPopulation

        # Time
        end = time.time()

        print("\nTempo: " + str(end - start))
        print("Total de execuções: " + str(round + 1))

        return res

    def rodeo(self, amount, population):
        minor = float('INF')
        selected = null
        random.shuffle(population)
        for k in range(amount):
            evaluation = self.game.eval( population[k] )
            if( evaluation < minor ):
                minor = evaluation
                selected = population[k]
        return selected
