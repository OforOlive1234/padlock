from tkinter import *
from tkinter.font import Font
import pyautogui
import time
from time import sleep
import keyboard
import threading

class App:

  def __init__(self):
    self.root = Tk()
    self.root.geometry('600x450')
    self.root.title('Clickr')

    self.font = Font(
      family='Arial',
      size=14
    )

    self.root.configure(bg='white')

    self.lbl = Label(self.root, text='Enter an integer (click delay):', font=self.font)
    self.lbl.grid(row=0, column=1)

    self.txt = Entry(self.root, text="Enter a number (1)", width=20)
    self.txt.grid(row=1, column=1, padx=200, pady=20)

    self.btn = Button(self.root, text="Run (F8)", command=self.auto_click, bg='#005500', fg='white', font=self.font)
    self.btn.grid(row=2, column=1)

    if keyboard.is_pressed('F8'):
      self.auto_click()

    self.photo = PhotoImage(file = 'icon.png')
    self.root.iconphoto(False, self.photo)
  
  def auto_click(self):
    run = True
    intervalInt = None

    try:
      intervalInt = int(self.txt.get())
    except:
      pass

    start = time.time()

    while run == True:

      if keyboard.is_pressed('F8'):
        run = False
        break

      if intervalInt != None:
        if time.time() >= (start + intervalInt):
          pyautogui.click()
          start = time.time()
        else:
          pyautogui.click()

if __name__ == '__main__':
  App().root.mainloop()