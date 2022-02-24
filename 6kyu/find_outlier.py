# You are given an array (which will have a length of at least 3,
# but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely
# comprised of even integers except for a single integer N.
# Write a method that takes the array as an argument and
# returns this"outlier" N.

def find_outlier(integers):
  """
  integers: find the outlier in a list of odd or even integers
  return: the outlier in the integers list
  """
  even_numbers = ([elt for elt in integers if elt%2 == 0])
  odd_numbers = ([elt for elt in integers if elt%2 != 0])
  if len(even_numbers)>len(odd_numbers):
    return odd_numbers[0]
  return even_numbers[0]

assert find_outlier([2, 4, 6, 8, 10, 3]) == 3, "find_outlier([2, 4, 6, 8, 10, 3]), 3"
assert find_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160, "find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160"