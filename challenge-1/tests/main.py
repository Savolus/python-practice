from main import *

from random import seed
import unittest

class TestIterBoard(unittest.TestCase):
  def test_content(self) -> None:
    board = [
      [1, 0, 1],
      [3, 0, 0]
    ]

    g = (0.5, 0.5)

    seed(11)

    board = iter_board(board, g)

    mocked_board = [
      [1, 0, 1],
      [3, 3, 0]
    ]

    self.assertEqual(
      board,
      mocked_board
    )
