import tkinter


from tkinter import *

from tkinter import ttk

# initializing tkinter instance 
root = Tk()

# creating frame widget
frame_no_2 = ttk.Frame(root, padding=100)
frame_no_2.pack(side="left")

# creating label widget within frame widget
labl = ttk.Label(frame_no_2, text="hello Worls no 2")
labl.pack(side="left")


root.mainloop()


