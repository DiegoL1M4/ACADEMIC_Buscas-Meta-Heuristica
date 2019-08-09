
# Imports
from jogo import OitoRainhas
from algoritmos import HillClimbing
from algoritmos import SimulatedAnnealing
from algoritmos import AlgoritmosGeneticos

print('\nProblema Inicial:')
problem = OitoRainhas.OitoRainhas()
problem.show(problem.positions)
result = []

#choice = input()
choice = 2

# Main (Hill Climbing)
if(choice == 1):
    solver = HillClimbing.HillClimbing(problem)
    result = solver.result( 50 )

# Main (Simulated Annealing)
elif(choice == 2):
    for k in range(100):
        solver = SimulatedAnnealing.SimulatedAnnealing(problem)
        result = solver.result(5000, 5000, 300, 3, 0.9)
        print( "Total de ataques: " + str(problem.eval(result)) )

# Main (Algoritmos Genéticos)
elif(choice == 3):
    solver = AlgoritmosGeneticos.AlgoritmosGeneticos(problem)
    result = solver.result(5000, 100, 0.4, 0.5, 0.1, [0,0,0,0,1,1,1,1])

print( "Total de ataques: " + str(problem.eval(result)) )

# Contruct the board
for i in range(8):
    for j in range(8):
        if(result[j] == i+1):
            print(" 1", end="")
        else:
            print(" 0", end="")
    print()
