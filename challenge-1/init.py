from helpers import display_board, init_interval, find_probability_interval
from random import random


# Task 1
def init_board(width: int, height: int) -> list[list[int]]:
  return [[0 for _ in range(height)] for _ in range(width)]


# Task 2
def init_cells(board: list[list[int]], probabilities: tuple[float]) -> list[list[int]]:
  # take plant probability from probabilities
  plant_probability = probabilities[-1]
  probabilities = probabilities[:-1]

  # init plants on board
  board = [[3 if random() < plant_probability else cell for cell in row] for row in board]

  # init intervals of distribution
  # (0.3, 0.4, 0.3) -> ((0, 0.3), (0.3, 0.7), (0.7, 1.0))
  probability_context = init_interval(probabilities)

  # init cells with animals or leave it blank on board
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 0:
        num = random()
        interval = find_probability_interval(probability_context, num)
        board[i][j] = probability_context.index(interval)

  return board


def init_main() -> list[list[int]]:
  width = int(input('Input width of gaming board: '))
  height = int(input('Input height of gaming board: '))

  board = init_board(width, height)

  display_board(board)

  return board


# Task 1
if __name__ == '__main__':
  init_main()
