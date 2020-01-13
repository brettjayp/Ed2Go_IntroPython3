class Time:
  '''A class for setting a Time object.
  It will initialize with a constructor that sets an hour, minute, and second (each to 0).
  Functions include set_time() to set the hour, minute, and second, and get_time() to return it.
  There is also set_[hour, minute, second]() and get_[hour, minute, second]() for individual values'''

  def __init__(self):
    self.__hour = 0
    self.__minute = 0
    self.__second = 0

  def get_hour(self):
    print(f'The current hour set is: {self.__hour}')

  def get_minute(self):
    print(f'The current minute set is: {self.__minute}')

  def get_second(self):
    print(f'The current second set is: {self.__second}')

  def set_hour(self, hour):
    if 0 <= hour <= 23:
      self.__hour = hour
    else:
      while 0 > hour or hour > 23:
        hour = eval(input(f'Sorry, cannot set hour to {hour}. It must be a value 0-23. Please try again:   '))
      self.__hour = hour
    print(f'Thank you. You have set the hour to {self.__hour}. The current set time is now {self.__hour}:{self.__minute}:{self.__second}')

  def set_minute(self, minute):
    if 0 <= minute <= 59:
      self.__minute = minute
    else:
      while 0 > minute or minute > 59:
        minute = eval(input(f'Sorry, cannot set minute to {minute}. It must be a value 0-59. Please try again:   '))
      self.__minute = minute
    print(f'Thank you. You have set the minute to {self.__minute}. The current set time is now {self.__hour}:{self.__minute}:{self.__second}')

  def set_second(self, second):
    if 0 <= second <= 59:
      self.__second = second
    else:
      while 0 > second or second > 59:
        second = eval(input(f'Sorry, cannot set second to {second}. It must be a vlaue 0-59. Please try again:   '))
      self.__second = second
    print(f'Thank you. You have set the second to {self.__second}. The current set time is now {self.__hour}:{self.__minute}:{self.__second}')

  def get_time(self):
    print(f'The current set time is {self.__hour}:{self.__minute}:{self.__second}')

  def set_time(self, hour, minute, second):
    if 0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59:
      self.__hour = hour
      self.__minute = minute
      self.__second = second
      print(f'Thank you, you have now set the time to {self.__hour}:{self.__minute}:{self.__second}')
    else:
      self.set_hour(hour)
      self.set_minute(minute)
      self.set_second(second)
  
  def tick(self):
    if self.__second <= 58:
      self.__second = self.__second + 1
      print(f'Tick!\n::{self.__second}')
    elif self.__minute <= 58 and self.__second == 59:
      self.__second = 0
      self.__minute = self.__minute + 1
      print(f'Tick!\n:{self.__minute}:{self.__second}')
    elif self.__hour <= 22 and self.__minute == 59 and self.__second == 59:
      self.__second = 0
      self.__minute = 0
      self.__hour = self.__hour + 1
      print(f'Tick!\n{self.__hour}:{self.__minute}:{self.__second}')
    elif self.__hour == 23 and self.__minute == 59 and self.__second == 59:
      self.__second = 0
      self.__minute = 0
      self.__hour = 0
      print(f'Tick!\nIt\'s a new day:\n{self.__hour}:{self.__minute}:{self.__second}')
    else:
      print(f'Uh-oh, something went wrong.\nThe current time set is {self.__hour}:{self.__minute}:{self.__second}')
