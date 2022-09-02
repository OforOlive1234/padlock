from tkinter import *
from tkinter import messagebox

root = Tk()

def error():
  messagebox.showinfo('Message', 'Stop gaming in class!')

button = Button(root, text="Play", command=error)
button.pack()


root.geometry('400x150')
root.title('Minecraft')
root.mainloop()