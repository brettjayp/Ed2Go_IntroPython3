from tkinter import *
from time import *

class MyFrame(Frame):
  def __init__(self):
    Frame.__init__(self)

    self.myCanvas = Canvas(width=300, height=200, bg='blue')
    self.myCanvas.grid()

    self.myCanvas.create_rectangle(10,10,100,100,fill='red',outline='white',width=5)
    self.myCanvas.update()
    sleep(0.5)
    self.myCanvas.create_oval(10,10,300,200,fill='white',outline='red',width=5)
    self.myCanvas.update()
    sleep(0.5)
    self.myCanvas.create_line(1,1,300,200,fill='green',width=3,arrow='both')
    self.myCanvas.update()
    sleep(0.5)
    self.myCanvas.create_text(10,10,text='Hell, low whirled!',width=70,fill='blue',anchor='nw',justify='center',font=('Times',16))
    # for count in range(10):
    #   increment = 10*count
    #   self.myCanvas.create_rectangle(10 + increment, 10 + increment, 50 + increment, 50 + increment)
    #   self.myCanvas.update()
    #   sleep(0.2)
    # for count in range(10):
    #   increment = 10*count
    #   self.myCanvas.create_rectangle(10 + increment, 10 + increment, 50 + increment, 50 + increment)
    #   self.myCanvas.update()
    #   sleep(0.2)
    #   # Now color over the previous rectangle
    #   self.myCanvas.create_rectangle(10 + increment, 10 + increment, 50 + increment, 50 + increment, outline="white")
    my_rect_id = self.myCanvas.create_rectangle(10, 10, 50, 50)
    self.myCanvas.update()

    for count in range(10):
      increment = 10*count
      self.myCanvas.coords(my_rect_id, 10 + increment, 10 + increment, 50 + increment, 50 + increment)
      self.myCanvas.update()
      sleep(0.25)

# frame01 = Frame()
# frame01.mainloop()

frame02 = MyFrame()
frame02.mainloop()
