from Herbivorous import *
import unittest

class TestHerbivorous(unittest.TestCase):
  def test_init(self) -> None:
    mocked_init = (1, 2)
    herbivorous = Herbivorous(*mocked_init)
    init = (
      herbivorous.x,
      herbivorous.y,
      herbivorous.r_eat,
      herbivorous.state,
    )
    mocked_init = (*mocked_init, 2, None)
    self.assertEqual(init, mocked_init)
