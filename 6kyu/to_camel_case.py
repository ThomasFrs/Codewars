# Complete the method/function so that it converts dash/underscore delimited
# words into camel casing.
# The first word within the output should be capitalized only if the
# original word was capitalized (known as Upper Camel Case,
# also often referred to as Pascal case). 

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

assert to_camel_case("the_stealth_warrior") == "theStealthWarrior", "to_camel_case('the_stealth_warrior'), 'theStealthWarrior"
assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior'), 'TheStealthWarrior"