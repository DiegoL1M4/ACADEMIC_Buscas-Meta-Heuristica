
# Imports
from jogo import OitoRainhas
from algoritmos import ClimbingHill

# Main
problem = OitoRainhas.OitoRainhas()
print(problem.amountAtk())

solve = ClimbingHill.ClimbingHill(problem)

solve.result()
