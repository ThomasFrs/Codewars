from shutil import move
from sre_parse import REPEAT_CHARS


class Codewars:
  def __init__(self):
    print("Welcome to Codewars 4kyu file")
    
  def snail(self, snail_map):
    """
    snail_map: matrix to browse clockwise as a snail shell
    return: numbers on the path of the snail-browsed matrix
    """
    # chekcs if snail_map is empty
    if snail_map == [[]]:
      return []
    snail_path = []
    side_length = len(snail_map)
    total_movements = 2*len(snail_map) - 1
    repeats = 0
    movements = 0
    while movements < total_movements:
      # horizontal top
      for i in range(repeats, side_length-repeats):
        snail_path.append(snail_map[repeats][i])
      movements += 1
      # vertical right
      for i in range(repeats+1, side_length-repeats):
        snail_path.append(snail_map[i][side_length-repeats-1])
      movements += 1
      # horizontal bottom
      for i in range(repeats+1, side_length-repeats):
        snail_path.append(snail_map[side_length-repeats-1][side_length-i-1])
      movements += 1
      # vertical left
      for i in reversed(range(repeats+1, side_length-repeats-1)):
        snail_path.append(snail_map[i][repeats])
      movements += 1
      repeats += 1
    return snail_path

code = Codewars()