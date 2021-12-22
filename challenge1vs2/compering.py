from challenge2.Simulator import Simulator
from challenge2.Visualizer import Visualizer
from challenge1.helpers import *
from challenge1.init import *
from challenge1.main import *

from random import seed
import unittest

class TestCompering(unittest.TestCase):
  def test_compering(self) -> None:
    w = h = 5
    p = (0.5, 0.3, 0.4, 0.5)
    g = (0.5, 0.5)
    i = 2

    seed(10)

    board_func = init_board(w, h)
    board_func = init_cells(board_func, p)
    
    for _ in range(i):
      board_func = iter_board(board_func, g)

    save_board(board_func, 'board_fun.csv')

    seed(10)

    visualizer = Visualizer(h, w, i)
    simulator = Simulator(visualizer, p, g)

    for _ in range(i):
      simulator.step()

    board_class = [ row.split(',') for row in str(simulator.visualizer).replace('\t', ',').split('\n') ]

    save_board(board_class, 'board_class.csv')

    b1 = read_board('board_fun.csv')
    b2 = read_board('board_class.csv')

    self.assertListEqual(
      b1,
      b2
    )
