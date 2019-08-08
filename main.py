
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
limit = 5000
result = solver.result(limit, 100, 0.4, 0.5, 0.1)

# Contruct the board
for i in range(8):
    for j in range(8):
        if(result[j] == i+1):
            print("  1", end="")
        else:
            print("  0", end="")
    print()
