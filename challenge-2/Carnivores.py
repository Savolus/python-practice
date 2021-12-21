from random import randrange, choice

# Хижі
class Carnivores():
  x: int
  y: int
  r_eat: int = 1
  r_move: int = 3
  state: str = None
  turns_without_eat: int = 0

  def __init__(self, x: int, y: int) -> None:
    self.x = x
    self.y = y
