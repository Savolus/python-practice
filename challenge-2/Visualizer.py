from os import system

from Empty import Empty
from Herbivorous import Herbivorous
from Carnivores import Carnivores
from Plant import Plant

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

  def __init__(self, w, h, i) -> None:
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
        elif isinstance(cell, self.entities['carnivores']):
          cell_label = 'carnivores'
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
