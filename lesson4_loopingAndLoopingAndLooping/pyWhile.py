i = 0

while i < 10:
  print(f'i = {i}')
  i = i + 1

print('i is done')

j = 0

if j:
  while j < 10:
    print(f'j = {j}')
  print('j is done')

print('all done')

# yes no loop
answer = 'y'
num = 0
while answer == 'y':
  print(f'number is {num}')
  num = num + 1
  answer = input('do you want the next number?') 
