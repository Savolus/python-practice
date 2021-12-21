from init import init_cells, init_main
from helpers import save_board
from math import isclose


# Task 2
if __name__ == '__main__':
  board = init_main()

  p_3 = float(input('Input probability for plant cells: '))

  if p_3 >= 1:
    raise ValueError('Probability for plants is greater than or equal to 100%')

  p_0 = float(input('Input probability for empty cells: '))
  p_1 = float(input('Input probability for herbivorous cells: '))
  p_2 = float(input('Input probability for carnivores cells: '))

  p = (p_0, p_1, p_2, p_3)

  if not isclose(sum(p[:-1]), 1.0):
    raise ValueError('Probabilities are not distribution')

  board = init_cells(board, p)

  save_board(board)
