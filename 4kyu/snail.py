# Given an n x n array, return the array elements arranged from outermost
# elements to the middle element, traveling clockwise.

def snail(snail_map):
  """
  snail_map: matrix to travel through clockwise as a snail shell
  return: numbers on the path of the snail-traveled matrix
  """
  # checks if snail_map is empty
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

assert snail([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5], "snail([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5]"
assert snail([[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]) == [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10], "snail([[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]), [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]"