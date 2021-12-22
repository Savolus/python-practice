from Empty import *
import unittest

class TestEmpty(unittest.TestCase):
  def test_init(self) -> None:
    mocked_init = (1, 2)
    empty = Empty(*mocked_init)
    init = (empty.x, empty.y,)
    self.assertEqual(init, mocked_init)

