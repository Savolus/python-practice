from challenge2.Carnivores import *
import unittest

class TestCarnivores(unittest.TestCase):
  def test_init(self) -> None:
    mocked_init = (1, 2)
    carnivores = Carnivores(*mocked_init)
    init = (
      carnivores.x,
      carnivores.y,
      carnivores.r_eat,
      carnivores.r_move,
      carnivores.state,
      carnivores.turns_without_eat
    )
    mocked_init = (*mocked_init, 1, 3, None, 0)
    self.assertEqual(init, mocked_init)

