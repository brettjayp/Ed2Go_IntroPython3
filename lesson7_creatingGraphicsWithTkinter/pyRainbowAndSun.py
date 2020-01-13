from tkinter import *
from time import *

class MyFrame(Frame):
  def __init__(self):
    Frame.__init__(self)

    # set a canvas with a blue sky background
    self.myCanvas = Canvas(width=600, height=800, bg='blue')
    self.myCanvas.grid()

    # make some grass
    grass = self.myCanvas.create_rectangle(0,500,600,800,fill='green')

    # make a sun
    self.x1 = 50
    self.y1 = 200
    self.x2 = 100
    self.y2 = 250
    sun = self.myCanvas.create_oval(self.x1,self.y1,self.x2,self.y2,fill='yellow',outline='orange',width=3)

    # make rainbow layers
    for color in range(8):
      roygbiv = ['red','orange','yellow','green','blue','indigo','violet', 'blue']
      current_color = roygbiv[color]
      increment = 15 * color
      self.myCanvas.create_arc(150 + increment, 100 + increment, 1050 - increment, 900 - increment, start = 0, extent = 180, fill = f'{current_color}')
    
    self.x3 = 0
    while self.x3 < 1:
      self.x1 = self.x1 + 2
      self.y1 = self.y1 - 1
      self.x2 = self.x2 + 2
      self.y2 = self.y2 - 1
      self.myCanvas.coords(sun,self.x1,self.y1,self.x2,self.y2)
      self.myCanvas.update()
      sleep(0.005)
      if self.x1 == 600:
        self.x3 = self.x3 + 1

# rainbow_red = self.myCanvas.create_arc(150,100,1050,900,start=0,extent=180,fill='red')
# rainbow_orange = self.myCanvas.create_arc(

# a test of the arc method
# arcTest = self.myCanvas.create_arc(50,50,250,150,start=0,extent=45,fill="white")

theFrame = MyFrame()
theFrame.mainloop()