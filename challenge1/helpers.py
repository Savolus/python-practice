import csv

def pretty_board(board: list[list[int]], sep='\t', square_braces=True) -> str:
  return '\n' \
    .join([
      sep.join([
        f'[{str(cell)}]' if square_braces else str(cell) for cell in row
      ]) for row in board
    ])


def display_board(board: list[list[int]]) -> None:
  print(pretty_board(board))


def save_board(board: list[list[int]], filename='board.csv') -> None:
  f = open(filename, 'w')
  f.write(pretty_board(board, sep=',', square_braces=False))
  f.close()


def read_board(filename='board.csv'):
  with open(filename, 'r') as csv_board:
    board = csv.reader(csv_board, delimiter=',')
    return [[int(cell) for cell in row] for row in board]


def init_interval(probabilities: tuple[float]) -> tuple[tuple[float, float]]:
  return tuple(
    (
      float(sum(probabilities[:i])),
      float(sum(probabilities[:i]) + probabilities[i])
    ) for i in range(len(probabilities))
  )


def find_probability_interval(probability_context: tuple[tuple[float, float]], num: float) -> tuple[float, float]:
  return next(interval for interval in probability_context if interval[0] <= num <= interval[1])
