def descending_order(num):
    list = ([int(i) for i in str(num)])
    list.sort()
    new_list = []
    while len(list) > 0:
      new_list.append(list.pop())
    string_ints = [str(int) for int in new_list]
    string_ints = "".join(string_ints)
    return string_ints

def find_outlier(integers):
  even_numbers = ([elt for elt in integers if elt%2 == 0])
  odd_numbers = ([elt for elt in integers if elt%2 != 0])
  if len(even_numbers)>len(odd_numbers):
    return odd_numbers[0]
  return even_numbers[0]

def find_next_square(sq):
  if (sq**0.5)*10 == int(sq**0.5)*10:
    return int(((sq**0.5)+1)**2)
  return -1

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

def find_missing_letter(chars):
  characters = ([character.lower() for character in chars])
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  alphabet = ([character for character in str(alphabet)])
  index = alphabet.index(characters[0])
  print(index, characters[0])
  for i in range(index, index + len(chars)):
    if alphabet[i] != characters[i - index]:
      if chars[0] == alphabet[0].lower():
        return alphabet[i]
      return alphabet[i].upper()

def make_readable(seconds):
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

#def tribonacci(signature, n):
  