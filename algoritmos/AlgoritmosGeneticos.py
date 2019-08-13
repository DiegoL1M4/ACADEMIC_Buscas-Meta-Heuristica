
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
                        break
                    if( evaluations[k][0] > evaluation ):
                        evaluations.insert( k, [evaluation, individual] )
                        break

            # Selecting the best of the current population
            res = evaluations[0][1]
            print(evaluations)
            input()

            # Stop condition
            if( evaluations[0][0] == 0 ):
                break

            # New population
            newPopulation = []

            # Election
            iterations = int(tamPopulation * E)
            for k in range(iterations):
                newPopulation.append(evaluations[k][1])
                #newPopulation.append(self.rodeo(2, population))

            # Reproduction
            iterations = int( (tamPopulation * R) / 2 )
            for k in range(iterations):
                div = random.randrange(1, 7)

                # individual1 = self.rodeo(2, population)
                # individual2 = self.rodeo(2, population)
                
                individual1 = population[random.randrange(0, len(population))]
                individual2 = population[random.randrange(0, len(population))]

                newIndividual = individual1[0:div]
                newIndividual.extend( individual2[div:8] )
                newPopulation.append( newIndividual )

                newIndividual = individual2[0:div]
                newIndividual.extend( individual1[div:8] )
                newPopulation.append( newIndividual )

            # Mutation
            iterations = int(tamPopulation * M)
            for k in range(iterations):
                individual = self.rodeo(3, population)
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
        selected = 0
        for i in range(amount):
            k = random.randrange(0, len(population))
            evaluation = self.game.eval( population[k] )
            if( evaluation < minor ):
                minor = evaluation
                selected = population[k]
        return selected

'''

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
                evaluations.append( self.game.eval(individual) )
            
            # Selecting the best of the current population
            res = population[ evaluations.index( min(evaluations) ) ]
            
            # Stop condition
            if( min(evaluations) == 0 ):
                break
            
            # New population
            newPopulation = []
            join = []

            # Election
            iterations = int(tamPopulation * E)
            for k in range(iterations):
                select1 = random.randrange(0, len(population))
                select2 = random.randrange(0, len(population))
                                
                if(self.game.eval( population[select1] ) < self.game.eval( population[select2] )):
                    newPopulation.append( population[select1] )
                    population.remove( population[select1] )
                else:
                    newPopulation.append( population[select2] )
                    population.remove( population[select2] )
                
            # Reproduction
            iterations = int( (tamPopulation * R) / 2 )
            for k in range(iterations):
                div = random.randrange(0, 8)

                f1 = random.randrange(0, len(newPopulation))
                f2 = random.randrange(0, len(newPopulation))

                newIndividual = newPopulation[f1][0:div]
                newIndividual.extend( newPopulation[f2][div:8] )
                join.append( newIndividual )

                newIndividual = newPopulation[f2][0:div]
                newIndividual.extend( newPopulation[f1][div:8] )
                join.append( newIndividual )

            # Mutation
            iterations = int(tamPopulation * M)
            for k in range(iterations):
                indexRan = random.randrange(0, len(newPopulation))
                copy = newPopulation[indexRan][:]

                selectColumn = random.randrange(0, 8)

                copy[selectColumn] = self.game.getValue()
                join.append(copy)

            
            newPopulation.extend( join )
            population = newPopulation

        # Time
        end = time.time()

        print("\nTempo: " + str(end - start))
        print("Total de execuções: " + str(round + 1))

        return res
'''