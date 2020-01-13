class Time:
  """A simple class to learn"""

  def __init__(self):
    self.hour = 0
    self.minute = 0
    self.second = 0
  
  def set_time(self, hour=0, minute=0, second=0):
    self.hour = hour
    self.minute = minute
    self.second = second
  
  def print_time(self):
    print(f'The time is {self.hour}:{self.minute}:{self.second}')