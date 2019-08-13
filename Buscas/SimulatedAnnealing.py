
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

        print("\nTempo: " + str(end - start))
        print("Total de execuções: " + str(round + 1))

        return self.game.positions

    def pertuba(self):
        neighbors = self.game.neighbors()
        k = random.randrange(0, len(neighbors))
        return neighbors[k]
