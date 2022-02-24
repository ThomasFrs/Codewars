# Complete the solution so that the function will break up camel casing,
# using a space between words.

def break_camel_case(s):
  """
  s: string of characters written in camel case
  return: s split between uppercase
  """
  s_characters = ([char for char in str(s)])
  for i in range(len(s_characters) - 1):
    if s_characters[i+1] == s_characters[i+1].upper():
      s_characters[i] = s_characters[i] + " " 
  return "".join(s_characters)

assert break_camel_case("camelCase") == "camel Case", "break_camel_case('camelCase'), 'camel Case'"
assert break_camel_case("breakCamelCase") == "break Camel Case", "break_camel_case('breakCamelCase'), 'break Camel case'"