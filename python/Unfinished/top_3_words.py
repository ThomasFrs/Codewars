def top_3_words(text):
  split_characters = [".", "#", "/", "\\", "!"]
  word_list = []
  for word in text.split(" "):
    cleared_word = []
    for char in word:
      if char in split_characters:
        word.split(char)
      else:
        cleared_word.append(char)
    word_list.append("".join(cleared_word))
  return word_list

print(top_3_words("hey mansdf.2..!asfd#slkfj"))
print("you!".split("."))