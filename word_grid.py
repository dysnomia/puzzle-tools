#!/usr/bin/env python
from dict import read_dict
import colorama as color
from sys import stdout

GRID = 'grid.txt'
DICT = 'british.dict'
MIN_LEN = 5

def read_grid(filename):
  with open(filename) as grid:
    return [s.strip().lower() for s in grid]

def solve_grid(grid, words, min_len):
  """Finds horizontal and vertical words in a grid."""
  h = len(grid)
  w = len(grid[0])

  found = []
  marked = [[False] * w for i in range(0, h)]
  for y1 in range(0, h):
    for x1 in range(0, w):
      # Horizontal word
      for x2 in range(x1 + min_len - 1, w):
        word = grid[y1][x1:x2+1]
        if word in words:
          found.append(word)
          for x in range(x1, x2+1):
            marked[y1][x] = True

      # Vertical word
      for y2 in range(y1 + min_len - 1, h):
        word = ''.join(grid[y][x1] for y in range(y1, y2+1))
        if word in words:
          found.append(word)
          for y in range(y1, y2+1):
            marked[y][x1] = True
  return marked, found

def main():
  color.init()

  grid = read_grid(GRID)
  words = read_dict(DICT)
  marked, found = solve_grid(grid, words, MIN_LEN)

  print(found)
  for y, row in enumerate(marked):
    for x, is_word in enumerate(row):
      if is_word:
        stdout.write(color.Fore.RED)
      else:
        stdout.write(color.Fore.WHITE)
      stdout.write(grid[y][x])
    stdout.write('\n')

  color.deinit()

if __name__ == '__main__':
  main()

