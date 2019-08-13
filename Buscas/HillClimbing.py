
import time
import random

class HillClimbing(object):

    def __init__(self, game):
        self.game = game

    def result(self, limit):
        # Time
        start = time.time()

        currentColides = self.game.eval( self.game.positions )

        # Iterations with limit
        for round in range(limit):
            neighbors = self.game.neighbors()

            # Evaluation
            evaluations = []
            for neighbor in neighbors:
                evaluations.append( self.game.eval( neighbor ) )

            # Contruct one list of minors
            minor = min(evaluations)
            minorList = []
            for neighbor in neighbors:
                evaluation = self.game.eval( neighbor )
                if(evaluation == minor):
                    minorList.append( neighbor )

            # Select one
            k = random.randrange(0, len(minorList))
            if(currentColides < minor):
                break

            self.game.positions = minorList[k]
            currentColides = minor

        # Time
        end = time.time()

        print("\nTempo: " + str(end - start))
        print("Total de execuções: " + str(round + 1))

        return self.game.positions
