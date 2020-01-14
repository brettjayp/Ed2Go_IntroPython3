try:
	john = 1
	age = eval(input('enter your age:  '))
	ten_years = age + 10
	print(ten_years)
except (NameError, SyntaxError):
	print('you must enter a number')
print('hava a nice day, goodbye')