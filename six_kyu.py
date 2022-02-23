from array import ArrayType, array


class Codewars:
  def __init__(self):
    print("Welcome to Codewars 6kyu file")

  def find_outlier(self, integers):
    """
    integers: find the outlier in a list of odd or even integers
    return: the outlier in the integers list
    """
    even_numbers = ([elt for elt in integers if elt%2 == 0])
    odd_numbers = ([elt for elt in integers if elt%2 != 0])
    if len(even_numbers)>len(odd_numbers):
      return odd_numbers[0]
    return even_numbers[0]

  def sum_multiples_three_five(self, number):
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

  def to_camel_case(self, text):
    """
    text: string in the format "word-other-another" or "word_other_another"
    return: string the format "wordOtherAnother"
    """
    char_list = ([char for char in str(text)])
    for i in range(len(char_list)):
      if (char_list[i] == "-" or char_list[i] == "_") and i <= len(char_list):
        char_list[i+1] = char_list[i+1].upper()
    for char in char_list:
      if char == "-" or char == "_":
        char_list.remove(char)
    return "".join(char_list)

  def roman_numerals_encoder(self, n):
    """
    n: positive integer
    return: n translated into roman numerals
    """
    roman_numerals_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    roman_steps_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_numerals = []
    if n > 0:
      for i in range(len(roman_numerals_list)):
        if n < roman_steps_list[i]:
          roman_numerals.append(self.roman_numerals_encoder(n//roman_steps_list[i]))
        roman_numerals.append(roman_numerals_list[i]*(n//roman_steps_list[i]))
        n = n - roman_steps_list[i]*(n//roman_steps_list[i])
    return "".join(roman_numerals)

  def break_camel_case(self, s):
    """
    s: string of characters written in camel case
    return: s split between uppercase
    """
    s_characters = ([char for char in str(s)])
    for i in range(len(s_characters) - 1):
      if s_characters[i+1] == s_characters[i+1].upper():
        s_characters[i] = s_characters[i] + " " 
    return "".join(s_characters)

  def tower_build(self, n_floors=1):
    """
    n_floors: number of floors for the tower
    return: tower consisting of "*" from top to bottom layed out as a pyramid
    """
    tower_list = ([" "*(n_floors-i) + "*"*(2*i-1) + " "*(n_floors-i) for i in range(1, n_floors+1)])
    return tower_list

  def array_diff(self, a, b):
    """
    a: array of integers
    b: array of integers to substract to a
    return: the substract of a elements that are present in b
    """
    return ([elt for elt in a if elt not in b])

code = Codewars()
print(code.array_diff([1,2,1, 5],[1, 2, 3]))