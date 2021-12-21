from math import isclose

from Visualizer import Visualizer
from Simulator import Simulator


if __name__ == '__main__':
  w = int(input('Input width of gaming board: '))
  h = int(input('Input height of gaming board: '))

  p_3 = float(input('Input probability for plant cells: '))

  if p_3 >= 1:
    raise ValueError('Probability for plants is greater than or equal to 100%')

  p_0 = float(input('Input probability for empty cells: '))
  p_1 = float(input('Input probability for herbivorous cells: '))
  p_2 = float(input('Input probability for carnivores cells: '))

  p = (p_0, p_1, p_2, p_3)

  if not isclose(sum(p[:-1]), 1.0):
    raise ValueError('Probabilities are not distribution')

  i = int(input('Input number of iteration on board: '))

  g_0 = float(input('Input probability for empty cells: '))
  g_3 = float(input('Input probability for plant cells: '))

  g = (g_0, g_3)

  if not isclose(sum(g), 1.0):
    raise ValueError('Probabilities are not distribution')

  visualizer = Visualizer(w, h, i)
  simulator = Simulator(visualizer, p, g)

  for _ in range(i):
    simulator.step()
