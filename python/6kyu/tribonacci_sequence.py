# Well met with Fibonacci bigger brother, AKA Tribonacci.
# As the name may already reveal, it works basically like a Fibonacci,
# but summing the last 3 (instead of 2) numbers of the sequence to generate
# the next. 

def tribonacci(signature, n):
  """
  signature: list of 3 integers forming the basis of the tribonacci sequence
  n: numbers to return from the tribonacci sequence
  return: n numbers from the tribonacci sequence beginning with signature numbers
  """
  tribonacci_list = []
  for i in range(len(signature)):
    if i < n:
      tribonacci_list.append(signature[i])
  for j in range(2, n-1):
    tribonacci_list.append(tribonacci_list[-3]+tribonacci_list[-2]+tribonacci_list[-1])
  return tribonacci_list

assert tribonacci([1, 1, 1], 10) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105], "tribonacci([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]"
assert tribonacci([300, 200, 100], 0) == [], "tribonacci([300, 200, 100], 0), []"