from challenge2.Visualizer import *
import unittest

class TestVisualizer(unittest.TestCase):
  def test_init(self) -> None:
    mocked_init = (2, 3, 2)
    visualizer = Visualizer(*mocked_init)
    init = (visualizer.h, visualizer.w, visualizer.i)
    self.assertEqual(init, mocked_init)
