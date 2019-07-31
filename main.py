
# Imports
from jogo import OitoRainhas
from algoritmos import HillClimbing

# Main
problem = OitoRainhas.OitoRainhas()

solve = HillClimbing.HillClimbing(problem)

limit = input("\nGive a limit: ")
solve.result(limit)
