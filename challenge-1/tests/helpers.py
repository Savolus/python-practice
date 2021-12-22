from helpers import *
from init import *

from pathlib import Path
import unittest

class TestPrettyBoard(unittest.TestCase):
  def test_content(self) -> None:
    board = [
      [1, 0, 1],
      [3, 0, 0]
    ]

    prettied_board = pretty_board(board)
    
    mocked_prettied_board = '[1]\t[0]\t[1]\n[3]\t[0]\t[0]'

    self.assertEqual(
      prettied_board,
      mocked_prettied_board
    )

class TestDisplayBoard(unittest.TestCase):
  def test_content(self) -> None:
    board = [
      [1, 0, 1],
      [3, 0, 0]
    ]

    display_board(board)

    mocked_displayed_board = '[1]\t[0]\t[1]\n[3]\t[0]\t[0]'

    self.assertLogs(mocked_displayed_board)

class TestSaveBoard(unittest.TestCase):
  def assertIsFile(self, path):
    if not Path(path).resolve().is_file():
        raise AssertionError("File does not exist: %s" % str(path))

  def test_content(self) -> None:
    board = [
      [1, 0, 1],
      [3, 0, 0]
    ]

    path = 'board.csv'

    save_board(board, path)

    self.assertIsFile(path)

class TestReadBoard(unittest.TestCase):
  def test_content(self) -> None:
    path = 'board.csv'
    board = read_board(path)

    mocked_board = [
      [1, 0, 1],
      [3, 0, 0]
    ]

    self.assertListEqual(
      board,
      mocked_board
    )

class TestInitInterval(unittest.TestCase):
  def test_interval(self) -> None:
    p = (0.3, 0.4, 0.3)

    probability_interval = init_interval(p)

    mocked_probability_interval = (
      (0.0, 0.3),
      (0.3, 0.7),
      (0.7, 1.0),
    )

    self.assertEqual(
      probability_interval,
      mocked_probability_interval
    )

class TestFindProbabilityInterval(unittest.TestCase):
  def test_interval(self) -> None:
    probability_interval = (
      (0.0, 0.3),
      (0.3, 0.7),
      (0.7, 1.0),
    )

    intervel = find_probability_interval(probability_interval, 0.25)

    mocked_intervel = (0.0, 0.3)
    
    self.assertEqual(intervel, mocked_intervel)
