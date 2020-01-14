try:
	john = 1
	age = eval(input('enter age:  '))
	ten_y = age + 10
	print('in 10 y you\'ll be', ten_y)
except NameError:
	print('you must enter a number')
except SyntaxError:
	print('make sure you only enter a number')
print('hava a nice day goodbye')