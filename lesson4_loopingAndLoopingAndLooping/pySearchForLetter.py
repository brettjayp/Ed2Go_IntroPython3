phrase = input('Please enter a short phrase:  ').lower()
# phrase = phrase.lower()
letter = input('Please enter a single letter:  ').lower()
# letter = letter.lower()
length = len(phrase)

for i in range(length):
  if phrase[i] == letter:
    print(f'The letter {letter} was found at position {i} in your phrase.\n')
    break
else:
  print(f'The letter {letter} was not found in your phrase.')