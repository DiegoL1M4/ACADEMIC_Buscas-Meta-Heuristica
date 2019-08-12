
# Imports
from jogo import OitoRainhas
from algoritmos import HillClimbing
from algoritmos import SimulatedAnnealing
from algoritmos import AlgoritmosGeneticos

#print('\nProblema Inicial:')
problem = OitoRainhas.OitoRainhas()
#problem.show(problem.positions)
result = []

choice = int(input("\nOpção: "))
rangeInt = int(input("Range: "))

# Main (Hill Climbing)
if(choice == 1):
    print("\nHill Climbing")
    cont = 0
    for k in range(rangeInt):
        problem = OitoRainhas.OitoRainhas()
        solver = HillClimbing.HillClimbing(problem)
        result = solver.result(100)

        if (problem.eval(result) == 0):
            cont += 1
    print( "\nEficiência: " + str( cont ) + '/' + str(rangeInt) )

# Main (Simulated Annealing)
elif(choice == 2):
    print("\nSimulated Annealing")
    cont = 0
    for k in range(rangeInt):
        problem = OitoRainhas.OitoRainhas()
        solver = SimulatedAnnealing.SimulatedAnnealing(problem)
        result = solver.result(500, 5000, 1000, 50, 0.8)

        if (problem.eval(result) == 0):
            cont += 1
    print( "\nEficiência: " + str( cont ) + '/' + str(rangeInt) )

# Main (Algoritmos Genéticos)
elif(choice == 3):
    print("\nAlgoritmos Genéticos")
    cont = 0
    for k in range(rangeInt):
        problem = OitoRainhas.OitoRainhas()
        solver = AlgoritmosGeneticos.AlgoritmosGeneticos(problem)
        result = solver.result(3000, 100, 0.4, 0.2, 0.4)

        if (problem.eval(result) == 0):
            cont += 1
    print( "\nEficiência: " + str( cont ) + '/' + str(rangeInt))

print( "\nTotal de sucessos: " + str(problem.eval(result)) )

# Contruct the board
problem.show(result)
