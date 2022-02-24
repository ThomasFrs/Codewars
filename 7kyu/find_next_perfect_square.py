# Complete the findNextSquare method that finds the next integral perfect
# square after the one passed as a parameter.
# Recall that an integral perfect square is an integer n such that
# sqrt(n)is also an integer. 
# If the parameter is itself not a perfect square then -1 should be returned.
# You may assume the parameter is non-negative.

def find_next_perfect_square(sq):
  """
  sq: a number that is the square of an integer (perfect square)
  return: -1 if sq is not a perfect square and the square of the square root of sq + 1 if
  sq is a perfect square
  """
  if (sq**0.5)*10 == int(sq**0.5)*10:
    return int(((sq**0.5)+1)**2)
  return -1

assert find_next_perfect_square(319225) == 320356, "find_next_perfect_square(319225), 320356"
assert find_next_perfect_square(15241383936) == 15241630849, "find_next_perfect_square(15241383936), 15241630849"