# Finish the solution so that it returns the sum of all the multiples
# of 3 or 5 below the number passed in.
# Additionally, if the number is negative,
# return 0 (for languages that do have them).

def sum_multiples_three_five(number):
  """
  number: random integer
  return: the sum of all multipliers of 3 and 5 below number
  """
  multipliers = []
  n = 0
  while n < number:
      if n % 3 == 0 or n % 5 == 0:
          multipliers.append(n)
      n += 1
  return sum(multipliers)

assert sum_multiples_three_five(4) == 3, "sum_multiples_three_five(4), 3"
assert sum_multiples_three_five(6) == 8, "sum_multiples_three_five(6), 8"