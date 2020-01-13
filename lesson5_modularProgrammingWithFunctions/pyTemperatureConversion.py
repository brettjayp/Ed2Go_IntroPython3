def conversion(celcius):
  fahrenheit = ((9.0/5.0) * celcius) + 32
  return fahrenheit

def convert_to_fahrenheit():
  for i in range(0, 101, 10):
    # print(f'i is at value {i}')
    value = conversion(i)
    print(f'C:F   {i} degrees Celcius converts to {value} degrees Fahrenheit')

convert_to_fahrenheit()