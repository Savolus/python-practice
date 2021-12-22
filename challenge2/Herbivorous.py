class Herbivorous:
  x: int
  y: int
  r_eat: int = 2
  state: str = None

  def __init__(self, x: int, y: int) -> None:
    self.x = x
    self.y = y
