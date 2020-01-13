from pyTime import Time

timeOne = Time()

timeOne.print_time()

timeOne.hour = 21
timeOne.minute = 17
timeOne.second = 32

timeOne.print_time()

timeTwo = Time()
timeTwo.set_time(21,18,56)
timeTwo.print_time()

print(Time.__doc__)
print(Time.__class__)
print(timeOne.__class__)