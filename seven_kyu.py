class Codewars:
  def __init__(self):
    print("Welcome to Codewars 7kyu file")
    
  def descending_order(self, num):
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

  def find_next_perfect_square(self, sq):
    """
    sq: a number that is the square of an integer (perfect square)
    return: -1 if sq is not a perfect square and the square of the square root of sq + 1 if
    sq is a perfect square
    """
    if (sq**0.5)*10 == int(sq**0.5)*10:
      return int(((sq**0.5)+1)**2)
    return -1

  def two_to_one(self, a1, a2):
    """
    a1, a2: string of unsorted letters
    return: sorted string of each letters of a1 and a2
    """
    return "".join(sorted(set(a1 + a2)))

code = Codewars()