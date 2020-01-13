for i in range(10):
  if i == 4:
    break
  print(f'for \'break\' i = {i}')
print('\n\n')

i = 0
for i in range(10):
  if i == 4:
    continue
  print(f'for \'continue\' i = {i}')
print('\n\n')

i = 0
for i in range(10):
  if i == 4:
    break
  print(f'for \'break else\' i = {i}')
else:
  print(f'at exit, i = {i}\n\n')
print('\n\n')

i = 0
for i in range(10):
  if i == 4:
    continue
  print(f'for \'continue else\' i = {i}')
else:
  print(f'at exit, i = {i}')