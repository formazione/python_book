from tkinter import *


# This class inherit from Frame
class App(Frame):
  def __init__(self):
    Frame.__init__(self)
    self.option_add("*Font", "arial 20 bold")
    self.pack(expand=YES, fill=BOTH)
    self.master.title("MiniCalculator")
    self.pack_entry() 
    self.bind()

  def pack_entry(self):
    "Display the entry widgets for the digit input"
    self.display = StringVar()
    entry = Entry(self, relief=FLAT, textvariable=self.display, justify='right', bd=15, bg='orange')
    entry.pack(side=TOP)
    entry.focus()

  def bind(self):
    "What happens when you press Enter, Delete or BackSpace"
    self.master.bind(
      "<Return>", lambda e: self.calc(self.display))
    self.master.bind(
      "<Delete>", lambda e: self.display.set(""))
    self.master.bind(
      "<BackSpace>", lambda e: self.display.set(""))

  def calc(self, display):
    "Takes what is in the entry, evaluete it and put the result in the entry"
    try:
        display.set(eval(display.get()))
    except:
        display.set("ERROR")


if __name__ == '__main__':
    App().mainloop()