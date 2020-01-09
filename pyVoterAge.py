age = eval(input('What is your age?  '))
if age >= 18:
    registered = input('Are you registered? (y/n)  ')

# if age >= 18:
#     if registered == 'y':
#         print('You are ready to vote!')
#     else:
#         print('You are not ready to vote.')
# else:
#     print('You are not old enough yet to vote.')

if age >= 18 and registered == 'y':
    print('You are ready to vote!')
elif age >= 18 and registered == 'y':
    print('You are not ready to vote.')
else:
    print('You are not old enough yet to vote.')