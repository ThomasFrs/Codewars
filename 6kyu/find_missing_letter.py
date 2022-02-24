# Write a method that takes an array of consecutive (increasing) letters
# as input and that returns the missing letter in the array.

def find_missing_letter(chars):
  """
  chars: string of characters
  return: missing letter between chars or after
  """
  letters = [char for char in chars][0]
  chars = [char.lower() for char in chars]
  alphabet = [char for char in "abcdefghijklmnopqrstuvwxyz"]
  starting_index = alphabet.index(chars[0])
  for letter in alphabet[starting_index:]:
    if letter not in chars and chars[0].lower() == letters[0]:
      return letter
    if letter not in chars and chars[0].upper() == letters[0]:
      return letter.upper()

assert find_missing_letter(['a','b','c','d','f']) == 'e', "find_missing_letter(['a','b','c','d','f']), 'e'"
assert find_missing_letter(['O','Q','R','S']) == 'P', "find_missing_letter(['O','Q','R','S']), 'P'"