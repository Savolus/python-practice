from challenge1.init import *

from random import seed
import unittest

class TestInitBoard(unittest.TestCase):
  def test_size(self) -> None:
    width, height = 10, 15
    board = init_board(width, height)

    extracted_width = len(board)
    extracted_height = len(board[0])

    self.assertEqual(
      (width, height),
      (extracted_width, extracted_height)
    )

  def test_content(self) -> None:
    width, height = 2, 3
    board = init_board(width, height)

    mocked_board = [
      [ 0, 0, 0 ],
      [ 0, 0, 0 ],
    ]

    self.assertListEqual(
      board,
      mocked_board
    )

class TestInitCells(unittest.TestCase):
  def test_content(self) -> None:
    width, height = 2, 3
    board = init_board(width, height)

    seed(10)

    p = (0.5, 0.3, 0.4, 0.3)
    board = init_cells(board, p)

    mocked_board = [
      [1, 0, 1],
      [3, 0, 0]
    ]

    self.assertListEqual(
      board,
      mocked_board
    )
