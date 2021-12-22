from random import seed
from challenge2.Visualizer import *
from challenge2.Simulator import *
import unittest

class TestSimulator(unittest.TestCase):
  def test_init(self) -> None:
    mocked_visualizer_init = (2, 3, 2)
    mocked_p = (0.5, 0.3, 0.4, 0.3)
    mocked_g = (0.5, 0.5)
    mocked_init = (mocked_p, mocked_g)
    visualizer = Visualizer(*mocked_visualizer_init)
    simulator = Simulator(
      visualizer,
      mocked_p,
      mocked_g
    )
    init = (simulator.p, simulator.g)
    self.assertEqual(init, mocked_init)

  def test_fill(self) -> None:
    seed(10)

    visualizer = Visualizer(2, 3, 2)
    simulator = Simulator(
      visualizer,
      (0.5, 0.3, 0.4, 0.3),
      (0.5, 0.5)
    )

    mocked_board = '1\t0\t1\n3\t0\t0\n'

    self.assertEqual(
      str(simulator.visualizer),
      mocked_board
    )

  def test_draw(self) -> None:
    seed(10)

    visualizer = Visualizer(2, 3, 2)
    simulator = Simulator(
      visualizer,
      (0.5, 0.3, 0.4, 0.3),
      (0.5, 0.5)
    )

    simulator.draw()

    mocked_board = '1\t0\t1\n3\t0\t0\n'

    self.assertLogs(mocked_board)
