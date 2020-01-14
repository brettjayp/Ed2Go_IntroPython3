def try_ages():
  alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  for letter in range(len(alphabet)):
    try:
      age = eval(f'10{alphabet[letter]}')
      ten_years = age + 10
      print(f'{alphabet[letter]} : age in 10 years is {ten_years}')
    # except Exception:
    except (NameError, SyntaxError):
      print(f'{alphabet[letter]} : fails')

try_ages()