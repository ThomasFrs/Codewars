# 7kyu
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

def find_next_perfect_square(sq):
  """
  sq: a number that is the square of an integer (perfect square)
  return: -1 if sq is not a perfect square and the square of the square root of sq + 1 if
  sq is a perfect square
  """
  if (sq**0.5)*10 == int(sq**0.5)*10:
    return int(((sq**0.5)+1)**2)
  return -1

def two_to_one(a1, a2):
  """
  a1, a2: string of unsorted letters
  return: sorted string of each letters of a1 and a2
  """
  return "".join(sorted(set(a1 + a2)))


# 6kyu
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

def to_camel_case(text):
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

def roman_numerals_encoder(n):
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
        roman_numerals.append(roman_numerals_encoder(n//roman_steps_list[i]))
      roman_numerals.append(roman_numerals_list[i]*(n//roman_steps_list[i]))
      n = n - roman_steps_list[i]*(n//roman_steps_list[i])
  return "".join(roman_numerals)
  

# 5kyu
def make_readable(seconds):
  """
  seconds: number of seconds to translate into hours, minutes and second
  return: seconds into hours, minutes and seconds in a digital clock format
  """
  second = 0
  minute = 0
  hour = 0
  if seconds <= 359999:
    for i in range(seconds):
        second += 1
        if second >= 60:
          second -= 60
          minute += 1
          if minute >= 60:
            minute -= 60
            hour += 1
    if second < 10:
      second = "0"+str(second)
    if minute < 10:
      minute = "0"+str(minute)
    if hour < 10:
      hour = "0"+str(hour)
    return str("{}:{}:{}".format(hour, minute, second))