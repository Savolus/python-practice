from os import system

from challenge2.Empty import Empty
from challenge2.Herbivorous import Herbivorous
from challenge2.Carnivores import Carnivores
from challenge2.Plant import Plant

class Visualizer:
  w: int
  h: int
  i: int
  current_i: int = 0
  board: list[list] = []
  entities = {
    'empty': Empty,
    'herbivorous': Herbivorous,
    'carnivores': Carnivores,
    'plant': Plant,
  }
  labels = {
    'empty': 0,
    'herbivorous': 1,
    'carnivores': 2,
    'plant': 3,
  }
  visual = True

  def __init__(self, h, w, i) -> None:
    self.w = w
    self.h = h
    self.i = i

    self.init_board()

  def set_entities(self, entities) -> None:
    self.entities = entities

  def clear(self) -> None:
    system('clear')

  def __str__(self) -> str:
    output = ''

    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        cell = self.board[i][j]
        cell_label = 'empty'
        l_deco, r_deco = '', ''

        if isinstance(cell, self.entities['empty']):
          cell_label = 'empty'
        elif isinstance(cell, self.entities['herbivorous']):
          cell_label = 'herbivorous'

          if cell.state == 'ate':
            l_deco = '['
            r_deco = ']'
          elif cell.state == 'spawned':
            l_deco = '('
            r_deco = ')'
        elif isinstance(cell, self.entities['carnivores']):
          cell_label = 'carnivores'

          if cell.state == 'ate':
            l_deco = '['
            r_deco = ']'
          elif cell.state == 'spawned':
            l_deco = '('
            r_deco = ')'
          elif cell.state == 'moved':
            l_deco = '{'
            r_deco = '}'
          elif cell.state == 'dead':
            l_deco = '|'
            r_deco = '|*'
        elif isinstance(cell, self.entities['plant']):
          cell_label = 'plant'

        output += l_deco + str(self.labels[cell_label]) + r_deco

        if j != self.w - 1:
          output += '\t'

      output += '\n'

    return output

  def init_board(self) -> None:
    self.board = [
      [
        self.entities['empty'](i, j) \
          for j in range(self.w)
      ] for i in range(self.h)
    ]

  def save_board(self, filename='board.csv') -> None:
    f = open(filename, 'w')
    f.write(str(self).replace('\t', ','))
    f.close()
