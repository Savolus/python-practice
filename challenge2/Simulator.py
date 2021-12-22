from random import choice, random, randrange
from challenge2.Visualizer import Visualizer


class Simulator:
  visualizer: Visualizer
  p: tuple[float, float, float, float]
  g: tuple[float, float]

  def __init__(self, visualizer, p, g) -> None:
    self.visualizer = visualizer
    self.p = p
    self.g = g

    self.fill()
    self.visualizer.save_board()

  def step(self) -> None:
    if self.visualizer.current_i == self.visualizer.i:
      raise IndexError('Out of steps')

    probability_context = self.init_interval(self.g)

    # Task 3
    for i in range(len(self.visualizer.board)):
      for j in range(len(self.visualizer.board[i])):
        is_empty = isinstance(self.visualizer.board[i][j], self.visualizer.entities['empty'])
        is_plant = isinstance(self.visualizer.board[i][j], self.visualizer.entities['plant'])

        if is_empty or is_plant:
          num = random()
          interval = self.find_probability_interval(probability_context, num)
          index = probability_context.index(interval)
          cell_key = 'empty'

          if index == 0:
            cell_key = 'empty'
          else:
            cell_key = 'plant'

          self.visualizer.board[i][j] = self.visualizer.entities[cell_key](i, j)

    # Task 4
    for i in range(len(self.visualizer.board)):
      for j in range(len(self.visualizer.board[i])):
        if isinstance(self.visualizer.board[i][j], self.visualizer.entities['herbivorous']):
          herb = self.visualizer.board[i][j]

          top_cut = 0 if i - herb.r_eat < 0 else i - herb.r_eat
          bottom_cut = len(self.visualizer.board) if i + herb.r_eat + 1 >= len(self.visualizer.board) else i + herb.r_eat + 1
          left_cut = 0 if j - herb.r_eat < 0 else j - herb.r_eat
          right_cut = len(self.visualizer.board[i]) if j + herb.r_eat + 1 >= len(self.visualizer.board[i]) else j + herb.r_eat + 1

          plant_count, herbivorous_count = 0, 0

          for k in range(top_cut, bottom_cut):
            for e in range(left_cut, right_cut):
              if (i, j) != (k, e):
                is_plant = isinstance(self.visualizer.board[k][e], self.visualizer.entities['plant'])
                is_herbivorous = isinstance(self.visualizer.board[k][e], self.visualizer.entities['herbivorous'])

                if is_plant:
                  plant_count += 1
                elif is_herbivorous:
                  is_acted_herb = self.visualizer.board[k][e].state

                  if not is_acted_herb:
                    herbivorous_count += 1

          if herbivorous_count >= 1 and plant_count >= 4:
            plant_count, herbivorous_count = 4, 1

            row_index = randrange(top_cut, bottom_cut)
            cell_index = randrange(left_cut, right_cut)

            while plant_count or herbivorous_count:
              is_plant = isinstance(self.visualizer.board[row_index][cell_index], self.visualizer.entities['plant'])
              is_empty = isinstance(self.visualizer.board[row_index][cell_index], self.visualizer.entities['empty'])

              if is_plant and plant_count:
                self.visualizer.board[row_index][cell_index] = self.visualizer.entities['empty'](row_index, cell_index)
                plant_count -= 1
              elif is_empty and herbivorous_count:
                self.visualizer.board[row_index][cell_index] = self.visualizer.entities['herbivorous'](row_index, cell_index)
                herbivorous_count -= 1
                self.visualizer.board[row_index][cell_index].state = 'spawned'

              row_index = randrange(top_cut, bottom_cut)
              cell_index = randrange(left_cut, right_cut)

            herb.state = 'ate'

    # Task 5
    for i in range(len(self.visualizer.board)):
      for j in range(len(self.visualizer.board[i])):
        if isinstance(self.visualizer.board[i][j], self.visualizer.entities['carnivores']):
          carn = self.visualizer.board[i][j]

          hunt_top_cut = 0 if i - carn.r_eat < 0 else i - carn.r_eat
          hunt_bottom_cut = len(self.visualizer.board) if i + carn.r_eat + 1 >= len(self.visualizer.board) else i + carn.r_eat + 1
          hunt_left_cut = 0 if j - carn.r_eat < 0 else j - carn.r_eat
          hunt_right_cut = len(self.visualizer.board[i]) if j + carn.r_eat + 1 >= len(self.visualizer.board[i]) else j + carn.r_eat + 1

          herbivorous_count, carnivores_count = 0, 0

          for k in range(hunt_top_cut, hunt_bottom_cut):
            for e in range(hunt_left_cut, hunt_right_cut):
              if (i, j) != (k, e):
                is_carnivores = isinstance(self.visualizer.board[k][e], self.visualizer.entities['carnivores'])
                is_herbivorous = isinstance(self.visualizer.board[k][e], self.visualizer.entities['herbivorous'])

                if is_herbivorous:
                  herbivorous_count += 1
                elif is_carnivores:
                  is_acted_carn = self.visualizer.board[k][e].state

                  if not is_acted_carn:
                    carnivores_count += 1

          # eat
          if herbivorous_count >= 1:
            herbivorous_to_eat = 1
            carn.state = 'ate'

            # 2 (2) can eat 2 (1) and make new (2)
            if carnivores_count >= 1 and herbivorous_count >= 2:
              herbivorous_to_eat = 2

            row_index = randrange(hunt_top_cut, hunt_bottom_cut)
            cell_index = randrange(hunt_left_cut, hunt_right_cut)

            while herbivorous_to_eat:
              is_carnivores = isinstance(self.visualizer.board[row_index][cell_index], self.visualizer.entities['carnivores'])
              is_herbivorous = isinstance(self.visualizer.board[row_index][cell_index], self.visualizer.entities['herbivorous'])

              if is_herbivorous and herbivorous_to_eat:
                cell_key = 'carnivores' if herbivorous_to_eat == 2 else 'empty'
                self.visualizer.board[row_index][cell_index] = self.visualizer.entities[cell_key](row_index, cell_index)
                self.visualizer.board[row_index][cell_index].state = 'spawned'
                herbivorous_to_eat -= 1

              row_index = randrange(hunt_top_cut, hunt_bottom_cut)
              cell_index = randrange(hunt_left_cut, hunt_right_cut)

          # move
          if carn.state != 'ate':
            move_top_cut = 0 if i - carn.r_move < 0 else i - carn.r_move
            move_bottom_cut = len(self.visualizer.board) if i + carn.r_move + 1 >= len(self.visualizer.board) else i + carn.r_move + 1
            move_left_cut = 0 if j - carn.r_move < 0 else j - carn.r_move
            move_right_cut = len(self.visualizer.board[i]) if j + carn.r_move + 1 >= len(self.visualizer.board[i]) else j + carn.r_move + 1

            herbivorous = []

            for k in range(move_top_cut, move_bottom_cut):
              for e in range(move_left_cut, move_right_cut):
                if (i, j) != (k, e):
                  if isinstance(self.visualizer.board[k][e], self.visualizer.entities['herbivorous']):
                    herbivorous.append((k, e))

            if len(herbivorous):
              distances = {herb: (((herb[1] - j) ** 2) + ((herb[0] - i) ** 2)) ** 0.5 for herb in herbivorous}
              ordered_distances = dict(sorted(distances.items(), key=lambda item: item[1]))

              for closest in ordered_distances:
                close_top_cut = move_top_cut if closest[0] - carn.r_eat < move_top_cut else closest[0] - carn.r_eat
                close_bottom_cut = move_bottom_cut if closest[0] + carn.r_eat + 1 >= move_bottom_cut else closest[0] + carn.r_eat + 1
                close_left_cut = move_left_cut if closest[1] - carn.r_eat < move_left_cut else closest[1] - carn.r_eat
                close_right_cut = move_right_cut if closest[1] + carn.r_eat + 1 >= move_right_cut else closest[1] + carn.r_eat + 1

                empty_cells = []

                for k in range(close_top_cut, close_bottom_cut):
                  for e in range(close_left_cut, close_right_cut):
                    if closest != (k, e):
                      if isinstance(self.visualizer.board[k][e], self.visualizer.entities['empty']):
                        empty_cells.append((k, e))

                if len(empty_cells):
                  carn.state = 'moved'
                  row_index, cell_index = choice(empty_cells)
                  carn.x = row_index
                  carn.y = cell_index
                  self.visualizer.board[row_index][cell_index] = carn
                  self.visualizer.board[i][j] = self.visualizer.entities['empty'](i, j)

                  break

            carn.turns_without_eat += 1

    self.visualizer.current_i += 1
    self.draw()
    self.clear()

  def clear(self) -> None:
    for i in range(len(self.visualizer.board)):
      for j in range(len(self.visualizer.board[i])):
        is_carnivores = isinstance(self.visualizer.board[i][j], self.visualizer.entities['carnivores'])
        is_herbivorous = isinstance(self.visualizer.board[i][j], self.visualizer.entities['herbivorous'])

        if is_herbivorous or is_carnivores:
          self.visualizer.board[i][j].state = None
        if is_carnivores:
          if self.visualizer.board[i][j].turns_without_eat == 5:
            self.visualizer.board[i][j] = self.visualizer.entities['empty'](i, j)

  def fill(self) -> None:

    # take plant probability from probabilities
    plant_probability = self.p[-1]
    probabilities = self.p[:-1]

    # init plants on board
    self.visualizer.board = [
      [
        self.visualizer.entities['plant'](i, j) \
          if random() < plant_probability
          else self.visualizer.board[i][j]
          for j in range(len(self.visualizer.board[i]))
      ] for i in range(len(self.visualizer.board))
    ]

    # init intervals of distribution
    # (0.3, 0.4, 0.3) -> ((0, 0.3), (0.3, 0.7), (0.7, 1.0))
    probability_context = self.init_interval(probabilities)

    # init cells with animals or leave it blank on board
    for i in range(len(self.visualizer.board)):
      for j in range(len(self.visualizer.board[i])):
        if isinstance(self.visualizer.board[i][j], self.visualizer.entities['empty']):
          num = random()
          interval = self.find_probability_interval(probability_context, num)
          index = probability_context.index(interval)
          entity_key = 'empty'

          if index == 0:
            entity_key = 'empty'
          elif index == 1:
            entity_key = 'herbivorous'
          elif index == 2:
            entity_key = 'carnivores'

          self.visualizer.board[i][j] = self.visualizer.entities[entity_key](i, j)
  
  def draw(self) -> None:
    # self.visualizer.clear()
    pattern = '-' * 8 * self.visualizer.w

    print(pattern)
    print(str(self.visualizer))
    print(pattern)

  def init_interval(self, probabilities: tuple[float, float, float]) -> tuple[tuple[float, float]]:
    return tuple(
      (
        float(sum(probabilities[:i])),
        float(sum(probabilities[:i]) + probabilities[i])
      ) for i in range(len(probabilities))
    )

  def find_probability_interval(self, probability_context: tuple[tuple[float, float]], num: float) -> tuple[float, float]:
    return next(interval for interval in probability_context if interval[0] <= num <= interval[1])
