
# Imports
from jogo import OitoRainhas
from algoritmos import HillClimbing
from algoritmos import SimulatedAnnealing
from algoritmos import AlgoritmosGeneticos


'''
# Main (Hill Climbing)
problem = OitoRainhas.OitoRainhas()
solver = HillClimbing.HillClimbing(problem)

limit = input("\nHill Climbing\nInforme uma limite: ")
solver.result(limit)



# Main (Simulated Annealing)
problem = OitoRainhas.OitoRainhas()
solver = SimulatedAnnealing.SimulatedAnnealing(problem)

limit = input("\nSimulated Annealing\nInforme uma limite: ")
solver.result(limit)
'''


# Main (Algoritmos Genéticos)
problem = OitoRainhas.OitoRainhas()
solver = AlgoritmosGeneticos.AlgoritmosGeneticos(problem)

#limit = input("\nAlgoritmos Genéticos\nInforme uma limite: ")
limit = 5
solver.result(limit, 10, 0.2, 0.7, 0.1)
