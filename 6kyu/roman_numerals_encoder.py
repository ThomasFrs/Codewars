# Create a function taking a positive integer as its parameter and returning
# a string containing the Roman Numeral representation of that integer.

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

assert roman_numerals_encoder(1889) == 'MDCCCLXXXIX', "roman_numerals_encoder(1889), 'MDCCCLXXXIX'"
assert roman_numerals_encoder(1989) == 'MCMLXXXIX', "roman_numerals_encoder(1989), 'MCMLXXXIX'"