print('Here\'s a small program to calculate an average.\nIt will request the user to input the quantity of variables to input, and runa for loop to request them before calculating and returning the average\n\n\n')

length = eval(input('How many variables would you like to input to get an average of?'))
agg = 0

for i in range(length):
  agg = agg + eval(input('Enter next input:  '))

avg = agg / length

print(f'\n\nThe average is:  {avg}')