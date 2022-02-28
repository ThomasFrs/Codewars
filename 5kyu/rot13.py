# ROT13 is a simple letter substitution cipher that replaces a letter
# with the letter 13 letters after it in the alphabet.
# ROT13 is an example of the Caesar cipher.

def rot13(message):
  """
  message: string that can contain any character
  return: message letters encoded 13 letters higher
  """
  alphabet = [char for char in "abcdefghijklmnopqrstuvwxyz"]
  upper_alphabet = [char.upper() for char in alphabet]
  message_chars = [char for char in message]
  encoded_message = []
  for char in message_chars:
    # tests if the character is not a letter
    if ord(char) < 65 or ord(char) > 122:
      encoded_message.append(char)
    # tests if the character is in uppercase
    elif char.upper() == char:
      encoded_message.append(upper_alphabet[(upper_alphabet.index(char) + 13) % 26])
    else:
      encoded_message.append(alphabet[(alphabet.index(char) + 13) % 26])
  return "".join(encoded_message)

assert rot13("test") == "grfg", "rot13('test'), 'grfg'"
assert rot13("Test") == "Grfg", "rot13('Test'), 'Grfg'"