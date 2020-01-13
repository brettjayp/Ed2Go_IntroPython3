age = 10
if age == 10:
    print ("ten")
print ('How\'s that?')
if age != 10:
    print ('not true')
if age != 9:
    print ('not nine')

print('\nnow for strings:\n')

string = 'C'
print(f'The string is {string}')
stringUpper = 'R'
stringLower = 'e'
if stringLower < stringUpper:
    print(f'The letter {stringLower} is less than the letter {stringUpper}.')
elif stringLower > stringUpper:
    print(f'The letter {stringLower} is greater than the letter {stringUpper}.')
else:
    print(f'The letter {stringLower} is the same as the letter {stringUpper}.')