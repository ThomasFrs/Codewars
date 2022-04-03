# Your task is to make a function that can take any non-negative integer
# as an argument and return it with its digits in descending order.
# Essentially, rearrange the digits to create the highest possible number.

def descending_order(num):
  """
  num: any integer
  return: num sorted in a descending order (highest to lowest)
  """
  list = ([int(i) for i in str(num)])
  list.sort()
  new_list = []
  while len(list) > 0:
    new_list.append(list.pop())
  string_ints = [str(int) for int in new_list]
  string_ints = int("".join(string_ints))
  return string_ints

assert descending_order(15) == 51, "descending_order(15), 51"
assert descending_order(123456789) == 987654321, "descending_order(123456789), 987654321"