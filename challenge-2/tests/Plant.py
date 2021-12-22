from Plant import *
import unittest

class TestPlant(unittest.TestCase):
  def test_init(self) -> None:
    mocked_init = (1, 2)
    plant = Plant(*mocked_init)
    init = (plant.x, plant.y,)
    self.assertEqual(init, mocked_init)

