windSpeed = eval(input('Please enter the measured wind speed of the hurricane:  '))

if windSpeed >= 156:
    print('That is equivalent to a category 5 hurricane.')
elif windSpeed >= 131 and windSpeed <= 155 :
    print('That is equivalent to a category 4 hurricane.')
elif windSpeed >= 111 and windSpeed <= 130 :
    print('That is equivalent to a category 3 hurricane.')
elif windSpeed >= 96 and windSpeed <= 110 :
    print('That is equivalent to a category 2 hurricane.')
elif windSpeed >= 74 and windSpeed <= 95 :
    print('That is equivalent to a category 1 hurricane.')
else:
    print('That is not strong enough to be classified as a hurricane.')