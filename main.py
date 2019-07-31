
# Imports
from jogo import OitoRainhas
from algoritmos import ClimbingHill

# Main
problem = OitoRainhas.OitoRainhas()

solve = ClimbingHill.ClimbingHill(problem)

limit = input("\nGive a limit: ")
solve.result(limit)
