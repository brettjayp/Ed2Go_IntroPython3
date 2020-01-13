# Intro message
print('This is a small example to demonstrate splicing in Python!\nThis is NOT a lesson, just a guided demonstration.\nBlame: brettjayp\n\n')

# First step: Let's make a variable
print('--Let\'s start by creating an example variable. We\'ll name it \'string\', and assign it the following string, \'Fact, bears beats Battlestar Galactica!\'. Then we\'ll print it to the screen.\n')

# # # CODE SNIPPET 01
cs_01 = '>>> string = \'Fact, bears beats Battlestar Galactica!\'\n>>> print(string)\nFact, bears beats Battlestar Galactica!'
# # # END CODE SNIPPET 01
print(cs_01)
print('\n')

# Next step: Splice one character, then two
print('--Great, we\'ve now set up our variable with a string.\nNow let\'s see what happens when we splice one character, then two characaters.\nThis way, we\'ll get to see what goes in then what goes out!\n')

# # # CODE SNIPPET 02
cs_02 = '>>> print (string [3:4])\nt\n>>> print (string [7:9])\nea'
# # # END CODE SNIPPET 02
print(cs_01)
print(cs_02)
print('\n')

# Next step: Use [:x] and [x:] to show open beginning and ending values
print('--Great! As you can see, the values we feed to the splice indicate the cursor position as if you were viewing the text in an editor, and is NOT inclusive!\nNow, we\'ll show you how we can leave the first and last values empty!\n')

# # # CODE SNIPPET 03
cs_03 = '>>> print (string [:9])\nFact, bea\n>>> print (string [9:])\nrs beats Battlestar Galactica!\n>>> print (string [:])\nFact, bears beats Battlestar Galactica!'
# # # END CODE SNIPPET 03
print(cs_01)
print(cs_02)
print(cs_03)
print('\n')

# Next step: Edit a string with splicing
print('--Cool, so leaving either end open means it includes all characters on that end! And it works with both ends open.\nNow, we\'ve got the basics down. Let\'s end with a demonstration that shows another practical use.\nFor this demonstration, we\'re going to feed a splice of our variable \'string\' into a new variable we\'ll create, \'tvShow\'\n')

# # # CODE SNIPPET 04
cs_04 = '>>> tvShow = \'I enjoy watching \' + string [18:]\nprint (tvShow)\nI enjoy watching Battlestar Galactica!'
# # # END CODE SNIPPET 04
print(cs_01)
print(cs_02)
print(cs_03)
print(cs_04)
print('\n')


