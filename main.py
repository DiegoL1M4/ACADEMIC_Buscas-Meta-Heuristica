
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
choice = 3

# Main (Hill Climbing)
if(choice == 1):
    #solver = HillClimbing.HillClimbing(problem)
    #result = solver.result( 100 )
    cont = 0
    for k in range(100):
        problem = OitoRainhas.OitoRainhas()
        solver = HillClimbing.HillClimbing(problem)
        result = solver.result(100)
        print( "Total de ataques: " + str(problem.eval(result)) )
        if (problem.eval(result) == 0):
            cont += 1
    print( "Total de Acertos: " + str(cont) )

# Main (Simulated Annealing)
elif(choice == 2):
    cont = 0
    for k in range(1000):
        problem = OitoRainhas.OitoRainhas()
        solver = SimulatedAnnealing.SimulatedAnnealing(problem)
        result = solver.result(500, 5000, 500, 50, 0.8)
        print( "Total de ataques: " + str(k) )
        if (problem.eval(result) != 0):
            cont += 1
    print( "Total de falhas: " + str(k+1) )

# Main (Algoritmos Genéticos)
elif(choice == 3):
    cont = 0
    for k in range(10):
        solver = AlgoritmosGeneticos.AlgoritmosGeneticos(problem)
        result = solver.result(3000, 100, 0.5, 0.4, 0.1, [0,0,0,0,1,1,1,1])
        if (problem.eval(result) == 0):
            cont += 1
    print( "Total de ataques: " + str( cont ) )

print( "Total de sucessos: " + str(problem.eval(result)) )

# Contruct the board
for i in range(8):
    for j in range(8):
        if(result[j] == i+1):
            print(" 1", end="")
        else:
            print(" 0", end="")
    print()
