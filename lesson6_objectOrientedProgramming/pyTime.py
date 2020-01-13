from pyTimeClass import Time

time1 = Time()
time1.set_time(20,10,45)
time1.get_time()
print(Time.__class__)
print(time1.__class__)
print(time1.__doc__)

time1.set_hour(24)



time1.get_time()