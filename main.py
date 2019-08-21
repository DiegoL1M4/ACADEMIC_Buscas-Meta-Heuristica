
# Imports
from Problemas import OitoRainhas
from Buscas import HillClimbing
from Buscas import SimulatedAnnealing
from Buscas import AlgoritmosGeneticos

#print('\nProblema Inicial:')
problem = OitoRainhas.OitoRainhas()
#problem.show(problem.positions)
result = []

choice = int(input("\nOpção: "))
#rangeInt = int(input("Range: "))
rangeInt = 1

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
        result = solver.result(500, 5000, 500, 50, 0.8)

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
        result = solver.result(500, 500, 0.1, 0.8, 0.1)

        if (problem.eval(result) == 0):
            cont += 1
    print( "\nEficiência: " + str( cont ) + '/' + str(rangeInt))

print( "\nTotal de ataques: " + str(problem.eval(result)) )

# Contruct the board
problem.show(result)
print()
