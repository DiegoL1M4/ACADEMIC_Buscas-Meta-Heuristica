
# Imports
from jogo import OitoRainhas
from algoritmos import HillClimbing
from algoritmos import SimulatedAnnealing
from algoritmos import AlgoritmosGeneticos
'''
print('\nProblema Inicial:')
problem = OitoRainhas.OitoRainhas()
problem.show(self.problem.tabuleiro)

choice = input()

if(choice == 1):
    pass
elif(choice == 1):
    pass
elif(choice == 1):
    pass
else:
    print("Fim da Execução")
'''

'''
# Main (Hill Climbing)
problem = OitoRainhas.OitoRainhas()
solver = HillClimbing.HillClimbing(problem)
limit = 5000
result = solver.result(limit)
'''
# Main (Simulated Annealing)
problem = OitoRainhas.OitoRainhas()
solver = SimulatedAnnealing.SimulatedAnnealing(problem)
limit = 5000
result = solver.result(limit, 5000, 2)

'''
# Main (Algoritmos Genéticos)
problem = OitoRainhas.OitoRainhas()
solver = AlgoritmosGeneticos.AlgoritmosGeneticos(problem)
limit = 5000
result = solver.result(limit, 100, 0.4, 0.5, 0.1, [0,0,0,0,1,1,1,1])
'''
# Contruct the board
for i in range(8):
    for j in range(8):
        if(result[j] == i+1):
            print("  1", end="")
        else:
            print("  0", end="")
    print()
