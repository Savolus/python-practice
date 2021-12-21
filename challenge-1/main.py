from helpers import read_board, display_board, init_interval, find_probability_interval
from random import random, randrange, choice
from math import isclose


# Task 3, 4, 5
def iter_board(board, g) -> list[list[int]]:
  # init function's carnivores life cycle
  # {(0, 1): 1, (2, 4): 6}
  # add -> add point with life level to dict
  # del -> remove point with life level from dict (die)
  iter_board.__dict__.setdefault('carnivores_life_cycle', {})

  # copy board
  matrix = [row[:] for row in board]

  # init intervals of distribution
  # (0.5, 0.5) -> ((0, 0.5), (0.5, 1.0))
  probability_context = init_interval(g)

  # Task 3
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == 0 or matrix[i][j] == 3:
        num = random()
        interval = find_probability_interval(probability_context, num)
        matrix[i][j] = probability_context.index(interval) and 3  # 0 index for 0 and any other index for 3

  # Task 4
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == 1:
        top_cut = 0 if i - 2 < 0 else i - 2
        bottom_cut = len(matrix) if i + 3 >= len(matrix) else i + 3
        left_cut = 0 if j - 2 < 0 else j - 2
        right_cut = len(matrix[i]) if j + 3 >= len(matrix[i]) else j + 3

        plant_count, herbivorous_count = 0, 0

        for k in range(top_cut, bottom_cut):
          for e in range(left_cut, right_cut):
            if (i, j) != (k, e):
              if matrix[k][e] == 3:
                plant_count += 1
              elif matrix[k][e] == 1:
                herbivorous_count += 1

        if herbivorous_count >= 1 and plant_count >= 4:
          plant_count, herbivorous_count = 4, 1

          row_index = randrange(top_cut, bottom_cut)
          cell_index = randrange(left_cut, right_cut)

          while plant_count or herbivorous_count:
            if matrix[row_index][cell_index] == 3 and plant_count:
              matrix[row_index][cell_index] = 0
              plant_count -= 1
            elif matrix[row_index][cell_index] == 0 and herbivorous_count:
              matrix[row_index][cell_index] = 1
              herbivorous_count -= 1

            row_index = randrange(top_cut, bottom_cut)
            cell_index = randrange(left_cut, right_cut)

  # Task 5
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == 2:
        hunt_top_cut = 0 if i - 1 < 0 else i - 1
        hunt_bottom_cut = len(matrix) if i + 2 >= len(matrix) else i + 2
        hunt_left_cut = 0 if j - 1 < 0 else j - 1
        hunt_right_cut = len(matrix[i]) if j + 2 >= len(matrix[i]) else j + 2

        herbivorous_count, carnivores_count = 0, 0

        for k in range(hunt_top_cut, hunt_bottom_cut):
          for e in range(hunt_left_cut, hunt_right_cut):
            if (i, j) != (k, e):
              if matrix[k][e] == 1:
                herbivorous_count += 1
              elif matrix[k][e] == 2:
                carnivores_count += 1

        is_ate = False

        # eat
        if herbivorous_count >= 1:
          herbivorous_to_eat, is_ate = 1, True

          # 2 (2) can eat 2 (1) and make new (2)
          if carnivores_count >= 1 and herbivorous_count >= 2:
            herbivorous_to_eat = 2

          row_index = randrange(hunt_top_cut, hunt_bottom_cut)
          cell_index = randrange(hunt_left_cut, hunt_right_cut)

          while herbivorous_to_eat:
            if matrix[row_index][cell_index] == 1 and herbivorous_to_eat:
              matrix[row_index][cell_index] = 2 if herbivorous_to_eat == 2 else 0
              herbivorous_to_eat -= 1

            row_index = randrange(hunt_top_cut, hunt_bottom_cut)
            cell_index = randrange(hunt_left_cut, hunt_right_cut)

        # move
        if not is_ate:
          move_top_cut = 0 if i - 3 < 0 else i - 3
          move_bottom_cut = len(matrix) if i + 4 >= len(matrix) else i + 4
          move_left_cut = 0 if j - 3 < 0 else j - 3
          move_right_cut = len(matrix[i]) if j + 4 >= len(matrix[i]) else j + 4

          herbivorous = []

          for k in range(move_top_cut, move_bottom_cut):
            for e in range(move_left_cut, move_right_cut):
              if (i, j) != (k, e):
                if matrix[k][e] == 1:
                  herbivorous.append((k, e))

          if len(herbivorous):
            distances = {herb: (((herb[1] - j) ** 2) + ((herb[0] - i) ** 2)) ** 0.5 for herb in herbivorous}
            ordered_distances = dict(sorted(distances.items(), key=lambda item: item[1]))

            for closest in ordered_distances:
              close_top_cut = move_top_cut if closest[0] - 1 < move_top_cut else closest[0] - 1
              close_bottom_cut = move_bottom_cut if closest[0] + 2 >= move_bottom_cut else closest[0] + 2
              close_left_cut = move_left_cut if closest[1] - 1 < move_left_cut else closest[1] - 1
              close_right_cut = move_right_cut if closest[1] + 2 >= move_right_cut else closest[1] + 2

              empty_cells = []

              for k in range(close_top_cut, close_bottom_cut):
                for e in range(close_left_cut, close_right_cut):
                  if closest != (k, e):
                    if matrix[k][e] == 0:
                      empty_cells.append((k, e))

              if len(empty_cells):
                row_index, cell_index = choice(empty_cells)
                life_cycle = iter_board.carnivores_life_cycle.pop((i, j), 0)
                iter_board.carnivores_life_cycle[(row_index, cell_index)] = life_cycle
                matrix[row_index][cell_index] = 2
                matrix[i][j] = 0

                break

        for k in range(hunt_top_cut, hunt_bottom_cut):
          for e in range(hunt_left_cut, hunt_right_cut):
            if matrix[k][e] == 2:
              iter_board.carnivores_life_cycle[(k, e)] = 0 if is_ate else iter_board.carnivores_life_cycle.get((k, e), 0) + 1

              if iter_board.carnivores_life_cycle[(k, e)] == 5:
                del iter_board.carnivores_life_cycle[(k, e)]
                matrix[k][e] = 0

  print(f'\nIteration:')
  display_board(matrix)

  return matrix


if __name__ == '__main__':
  # Task 3
  board = read_board()

  iterations = int(input('Input number of iteration on board: '))

  g_0 = float(input('Input probability for empty cells: '))
  g_3 = float(input('Input probability for plant cells: '))

  g = (g_0, g_3)

  if not isclose(sum(g), 1.0):
    raise ValueError('Probabilities are not distribution')

  for _ in range(iterations):
    board = iter_board(board, g)
